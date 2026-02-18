# Loading VivoQuant .rmha images into slicer (some rough code provided)

**Topic ID**: 35169
**Date**: 2024-03-29
**URL**: https://discourse.slicer.org/t/loading-vivoquant-rmha-images-into-slicer-some-rough-code-provided/35169

---

## Post #1 by @EgorZindy (2024-03-29 17:33 UTC)

<p>Hello,</p>
<p>I adapted some nifty <a href="https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/72671/Brook_J_160002821_BCI_final_Edited.pdf?sequence=3" rel="noopener nofollow ugc">matlab code</a> to read .rmha images into 3d slicer. As I understand, these are VivoQuant labelled ROI images.</p>
<p>The original code was written by Joseph Dalton Brook, which he made available in his Ph.D Thesis. Thanks mate! Full disclosure, ChatGPT did the grunt work as I don’t speak matlab very well. I’m amazed the code works at all but here we are. <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p>And the metadata I was able to extract for one of our .rmha files:</p>
<pre><code class="lang-auto">print(dic)
{'ObjectType': 'ROI', 'NDims': 3, 'BinaryData': True, 'BinaryDataByteOrderMSB': False, 'CompressedData': 'RLE', 'TransformMatrix': [-1, 0, 0, 0, -1, 0, 0, 0, -1], 'Offset': [0, 0, 0], 'CenterOfRotation': [0, 0, 0], 'AnatomicalOrientation': 'LPS', 'ElementSpacing': [0.020446, 0.020446, 0.020446], 'DimSize': [490, 490, 587], 'ElementType': &lt;class 'numpy.uint8'&gt;, 'ROI[1]': 'Vis:red:1:0:127:255', 'ROI[2]': 'Upper_Bone:magenta:1:0:127:255', 'ROI[3]': 'Lower_Bone:green:1:0:127:255', 'ROI[4]': 'Implant:blue:1:0:127:255', 'PatientsName': '', 'PatientID': '', 'StudyDescription': '', 'StudyDate': '', 'StudyTime': '', 'SeriesDescription': '', 'SeriesDate': '', 'SeriesTime': '', 'ReferenceUID': '', 'ElementDataFile': 'LOCAL'}
</code></pre>
<p>The 3D slicer extension is very basic and simply loads the rmha file as a volume. It works, but there are a few things I still need to look at:</p>
<ul>
<li>
<p>I haven’t used the named colours provided in the metadata to the different labels yet, but I’m pretty sure I can use the <a href="https://pypi.org/project/webcolors/" rel="noopener nofollow ugc">webcolors module</a> for that. I’ll have a look at how other modules might apply a discrete look-up table to the volumetric data but any guidance here will be welcome.</p>
</li>
<li>
<p>I’m also discovering that whereas the original image (mha or mhd) may well have an origin offset, the rmha’s offset is always 0. So I still need to think about what to do. Do I check if in the rmha file’s directory, there’s a mha/mhd file from which I can copy the offset?</p>
</li>
<li>
<p>I’ve been reading up on past discussions on the volume orientation issues <a href="https://discourse.slicer.org/t/bug-when-reading-mha-file-with-anatomicalorientation/7038">here</a> and <a href="https://discourse.itk.org/t/read-mha-metadata/2007" rel="noopener nofollow ugc">here</a>… I’m still digesting the info but I understand this is something I need to take into account to match the orientation of the rmha to that of the mha / mhd supporting volume. I have a <code>'TransformMatrix': [-1, 0, 0, 0, -1, 0, 0, 0, -1]</code> and a <code>'AnatomicalOrientation': 'LPS'</code>.</p>
</li>
</ul>
<p>So that’s where I’m at, and I have some very rough code I can share if anyone is interested:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/zindy/SlicerSandbox/tree/master/ImportRMHA">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/zindy/SlicerSandbox/tree/master/ImportRMHA" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/zindy/SlicerSandbox/tree/master/ImportRMHA" target="_blank" rel="noopener nofollow ugc">SlicerSandbox/ImportRMHA at master · zindy/SlicerSandbox</a></h3>


  <p><span class="label1">Collection of utilities that are not polished implementations but can be useful to users - zindy/SlicerSandbox</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ll check some other extensions for code I can borrow and if I make any progress I’ll report back! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Kind regards,<br>
Egor</p>

---

## Post #2 by @lassoan (2024-03-30 21:24 UTC)

<p>Nice work thank you for your contribution!</p>
<p>Is .rmha file a standard .mha file with some additional custom fields? In that case, you may use the ITK reader for loading the image data itself and you don’t need to worry about image orientation. You may be able to get custom fields from the ITK reader as well.</p>
<p>It would be important to provide at least one pair of image and corresponding segmentation for testing.</p>
<p>Webcolors would probably work but the safest would be to check the .rmha specification for a complete list of colors (and maybe their RGB value).</p>

---

## Post #3 by @EgorZindy (2024-03-30 23:44 UTC)

<p>Dear Andras,</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is .rmha file a standard .mha file with some additional custom fields?</p>
</blockquote>
</aside>
<p>I don’t think the metadata is all that different from that of a .mhd or .mha file (when looking at <a href="https://github.com/Kitware/VTK/blob/master/IO/Image/vtkMetaImageReader.cxx" rel="noopener nofollow ugc">vtkMetaImageReader.cxx</a> versus the one in the dictionary I provided, but the RLE compression of the data is something unique to the .rmha files and not handled by the VTK reader.</p>
<p>All in all, there isn’t a lot of information available on the .rmha format. It’s mentioned in a couple of place <a href="http://vivoquant.com/files/manual/2022/vqmanual_operators_3droitool.html#load-an-roi-from-disk" rel="noopener nofollow ugc">in the VivoQuant manual</a> and referred to as “VQ 3D ROI (.rmha)”.</p>
<p>The only source code I was able to track down was that of Joseph Dalton Brook in his Ph.D Thesis (page 133 onwards and RLE decompression code on page 197).</p>
<p>I’ll check with my colleagues if we can make a set of microct images available (.mhd or .mha and the vivoquant .rmha corresponding file). I’ll also check if the colours in webcolors module match the ones in VivoQuant while I’m at it.</p>
<p>Cheers,<br>
Egor</p>

---

## Post #4 by @jamesobutler (2024-03-31 01:06 UTC)

<p>It seems that .rmha is probably a MetaImage volume with their custom tags for ROIs which Slicer calls segmentations. It is similar to .seg.nrrd which is a NRRD volume with some custom tags for a Slicer segmentation object. So a file reader for rmha should probably be implemented similar to the seg.nrrd file reader.</p>

---

## Post #5 by @EgorZindy (2024-03-31 21:43 UTC)

<p>Hey <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="35169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>with their custom tags for ROIs which Slicer calls segmentations</p>
</blockquote>
</aside>
<p>thanks for the clarification. Yes, segmentations!</p>
<p>The closest extension I found (in Python) that does something similar to what I want is <a href="https://github.com/zindy/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py" rel="noopener nofollow ugc">ImportOsirixROI</a>  (Import Osirix ROI: Load Osirix ROI files as segmentation).</p>
<p>I will write a new extension based on it and see where it takes me.</p>
<p>Just wanted to add, I’m not disregarding your advice about the .seg.nrrd files, but so far I only found <a href="https://github.com/lassoan/slicerio/" rel="noopener nofollow ugc">slicerio</a> which doesn’t seem to be a loader the way ImportOsirixROI is.</p>
<p>Cheers,<br>
Egor</p>

---

## Post #6 by @EgorZindy (2024-04-01 08:36 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> I see why you suggested looking at .seg.nrrd, the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file" rel="noopener nofollow ugc">documentation on this topic</a> is quite thorough.</p>
<blockquote>
<p>3D volumes in NRRD (.nrrd or .nhdr) and Nifti (.nii or .nii.gz) file formats can be directly loaded as segmentation:</p>
<ul>
<li>Drag-and-drop the volume file to the application window (or use menu: <code>File</code> / <code>Add Data</code>, then select the file)</li>
<li>In <code>Description</code> column choose <code>Segmentation</code></li>
<li>Optional: if a color table (specifying name and color for each label value) is available then load that first into the application and then select it as <code>Color node</code> in the <code>Options</code> section. Specification of the color table file format is available <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-file-format-txt-ctbl" rel="noopener nofollow ugc">here</a>.</li>
<li>Click <code>OK</code></li>
</ul>
<p>Tip: To avoid the need to always manually select <code>Segmentation</code>, save the <code>.nrrd</code> file using the <code>.seg.nrrd</code> file extension. It makes Slicer load the image as a segmentation by default.</p>
</blockquote>
<p>And further down, I see</p>
<blockquote>
<p>Other image file formats can be loaded as <em>labelmap volume</em> and then converted to segmentation</p>
</blockquote>
<p>OK, so the rmha files are in fact labelmap volumes, with some specific metadata to indicate names and colours. Sorry, I’m still wrapping my head around specific terminologies and corresponding code! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>
<p>Cheers,<br>
Egor</p>

---

## Post #7 by @lassoan (2024-04-01 17:44 UTC)

<p>Yes, the rmha reader should work similarly to the .seg.nrrd reader in the sense that it should read labelmap volume files into a segmentation node, because you can attach more metadata (segment bames and colors), visualize it more nicely, and directly edit it in Segment Editor. Implementation can be importing the labelmap node into a segmentation after the reading is completed. You can create a color node to specify segment names and colors and use that during labelmap to segmentation import; or you can import without a color node and fix up segment names and colors after the import.</p>

---
