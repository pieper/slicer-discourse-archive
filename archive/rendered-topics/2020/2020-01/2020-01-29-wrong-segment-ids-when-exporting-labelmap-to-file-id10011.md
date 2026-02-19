---
topic_id: 10011
title: "Wrong Segment Ids When Exporting Labelmap To File"
date: 2020-01-29
url: https://discourse.slicer.org/t/10011
---

# Wrong segment IDs when exporting labelmap to file

**Topic ID**: 10011
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/wrong-segment-ids-when-exporting-labelmap-to-file/10011

---

## Post #1 by @Mostafa_Darwiche (2020-01-29 23:58 UTC)

<p>Hello,</p>
<p>I am developing a scriptedLoadableModules and I am currently facing a small issue. So,</p>
<ol>
<li>I’am loading a segmentation and labelmap in which, for the sake of simplicity, I have three segmented regions (IDs: 3, 6 and 48)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d907404dcb9b438ffcaf5c9fff244b61dca8352.png" data-download-href="/uploads/short-url/mtSs34xU6UuEtDNl6RSXftb2PhE.png?dl=1" title="screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d907404dcb9b438ffcaf5c9fff244b61dca8352_2_517x233.png" alt="screenshot_1" data-base62-sha1="mtSs34xU6UuEtDNl6RSXftb2PhE" width="517" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d907404dcb9b438ffcaf5c9fff244b61dca8352_2_517x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d907404dcb9b438ffcaf5c9fff244b61dca8352_2_775x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d907404dcb9b438ffcaf5c9fff244b61dca8352.png 2x" data-dominant-color="B0B0BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_1</span><span class="informations">1000×452 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Next, let’s say I select region 48, and click “Remove”. (it will be removed)</li>
<li>I have the following code, taken from the documentation, to save the current/modified labelmap (so without the region 48):</li>
</ol>
<blockquote>
<p>name = “current_results.nii.gz”<br>
filePath = slicer.app.temporaryPath + ‘/’ + name<br>
localLabelmap = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)    slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(self.segmentationVolumeNode, localLabelmap)<br>
slicer.util.saveNode(localLabelmap, filePath)</p>
</blockquote>
<ol start="4">
<li>When I load current_results.nii.gz, I see two regions, which is good, but their IDs are 1 and 2. I see the same IDs when I open the image in ITKsnap. So, clearly the IDs are not being saved based on existing ones.</li>
</ol>
<p>In logs file, I see the following:</p>
<blockquote>
<p>[ERROR][VTK] 30.01.2020 00:20:20 [vtkLookupTable (00000255CE57F650)] (D:\D\S\Slicer-4100-build\VTK\Common\Core\vtkLookupTable.cxx:143) - Bad table range: [0, -1]<br>
[ERROR][VTK] 30.01.2020 00:20:20 [vtkMRMLLabelMapVolumeDisplayNode (00000255D3176EE0)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:150) - GetOutputImageData: Lookup table exists but empty!<br>
[ERROR][VTK] 30.01.2020 00:20:20 [vtkLookupTable (00000255CE57FB90)] (D:\D\S\Slicer-4100-build\VTK\Common\Core\vtkLookupTable.cxx:143) - Bad table range: [0, -1]<br>
[ERROR][VTK] 30.01.2020 00:20:20 [vtkMRMLLabelMapVolumeDisplayNode (00000255D3176EE0)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:150) - GetOutputImageData: Lookup table exists but empty!<br>
[WARNING][VTK] 30.01.2020 00:20:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Generic Warning: In D:\D\S\Slicer-4100\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nii.gz</p>
</blockquote>
<p>I have no clue what those errors mean! I would really appreciate your help in telling me what am I doing wrong. How can I do the export keeping the same IDs as when loading?</p>
<p>Just so you know, I also tried (unsuccessfully) to do the export using this line of code:</p>
<blockquote>
<p>slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(self.segmentationVolumeNode, localLabelmap, self.labelmapVolumeNode)</p>
</blockquote>

---

## Post #2 by @lassoan (2020-01-30 03:05 UTC)

<p>Slicer keeps track of meaning of each label by using <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">custom metadata fields in the file header</a>.</p>
<p>In recent Slicer preview versions, original label values are preserved if you load a nrrd or nifti file as segmentation and save that segmentation in nrrd file.</p>
<p>Segments are relabeled if you export the segmentation to labelmap node, so if you want to preserve the original label values then avoid this operation.</p>

---

## Post #3 by @Mostafa_Darwiche (2020-01-30 09:34 UTC)

<p>Thanks for your input.</p>
<p>But, then how can I save the image with changes done through slicer? (Of course while keeping the original labels)</p>

---

## Post #4 by @lassoan (2020-01-30 14:54 UTC)

<p>If you want to preserve label values then load the files as segmentation and save the file as segmentation. Slicer saves segmentation in a .nrrd file, which can be loaded by any other imaging software (they will not use the additional information in the custom fields,  such as segment name and color, but that should not matter).</p>
<p>Note that you need to use a recent Slicer preview release. Slicer-4.10 always saved segmentation as a 4D volume and so label values were not preserved, but recent Slicer Preview releases will keep the segmentation in a 3D volume (and the original label values) if you don’t have overlapping segments.</p>
<p>Can you write a bit about your workflow? What do you do with the modified segmentation file? How do you currently know which label value correspond to which segment?</p>

---

## Post #5 by @Mostafa_Darwiche (2020-01-30 17:27 UTC)

<ul>
<li>So when you say “<em>If you want to preserve label values then load the files as segmentation and save the file as segmentation</em>”, how can do the save through Python? Can you show me an example please !</li>
<li>I will try, then, to use version 4.11 to see if it works! I will let you know.</li>
<li>Briefly, I have an application with some sort of catalogs/atlases of different organs (brain, heart, …), for which I know (using my automatic segmentation method) how to segment all regions when a new image is given. However, it is possible that my catalogs are not complete (some regions are missing) or not accurate, that’s why I am using Slicer (SegmentationEditor) to improve or perform a segmentation for a new region. Therefore, I need to extract/export/save the image after modification in slicer, so I can update my catalog. If label values have changed (which is my problem right now), then I’ll lose track on my side. Hope it’s clear!</li>
</ul>

---

## Post #6 by @lassoan (2020-01-30 19:26 UTC)

<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="5" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>So when you say “ <em>If you want to preserve label values then load the files as segmentation and save the file as segmentation</em> ”, how can do the save through Python? Can you show me an example please !</p>
</blockquote>
</aside>
<p>You can use <code>slicer.util.saveNode()</code> to save the segmentation node to file.</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="5" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>I have an application with some sort of catalogs/atlases of different organs (brain, heart, …), for which I know (using my automatic segmentation method) how to segment all regions when a new image is given</p>
</blockquote>
</aside>
<p>I see. Probably you then have metadata files somewhere that store which label correspond to which segment, which is a reasonable solution, as it is very simple. Is that the case? Is there a standard format you follow?</p>
<p>In Slicer .seg.nrrd file format, we store this metadata in the same file as the image data, which is very robust, but it may be slightly inconvenient to read/write nrrd header to access this data. It is also important to note that Slicer uses standard terminologies (DICOM, and soon TA2) to identify segment contents to make the content really portable (avoid all issues around spelling, names in different languages, etc.).</p>
<p>In scope of <a href="https://www.openanatomy.org/">OpenAnatomy</a> project, we are working on additional export options (such as glTF+json) to create portable and interoperable atlases.</p>

---

## Post #7 by @Mostafa_Darwiche (2020-01-31 00:28 UTC)

<p>So here are my findings:</p>
<ol>
<li>I tried version 4.11, saving segmentation to nii file, and I got exactly the same behavior, original labels were lost. Code used:</li>
</ol>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="1" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>localLabelmap = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’) slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(self.segmentationVolumeNode, localLabelmap)<br>
slicer.util.saveNode(localLabelmap, filePath)</p>
</blockquote>
</aside>
<ol start="2">
<li>Next, I tried saving with the same way to nrrd file (both versions 4.10 and 4.11). The header files did not have information about original labels.</li>
<li>Then, I changed the way I am saving the node using this code:</li>
</ol>
<blockquote>
<p>myStorageNode = self.segmentationVolumeNode.CreateDefaultStorageNode()<br>
myStorageNode.SetFileName(filePath)<br>
myStorageNode.WriteData(self.segmentationVolumeNode)</p>
</blockquote>
<p>3.a. If I save to .nii file, labels are lost.<br>
3.b. While saving to nrrd,  I get the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2c5194e72a6b0d8cc988d5b6c5f026297c99ad.png" data-download-href="/uploads/short-url/zYPh2ErWdgDlHV1bdm3r1A2KaDz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2c5194e72a6b0d8cc988d5b6c5f026297c99ad.png" alt="image" data-base62-sha1="zYPh2ErWdgDlHV1bdm3r1A2KaDz" width="517" height="308" data-dominant-color="F3F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×639 23.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Which is exactly what I am looking for. The original IDs are stored in metadata. The problem, however, is that the pixels are not labeled with those IDs. In fact, I only have two IDs in the whole image, 0 and 1. All segments are labeled 1 and the rest is 0. I reproduced this in ITK-Snap.</p>
<p>Basically, I still have the problem! I will try DICOM and see.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I see. Probably you then have metadata files somewhere that store which label correspond to which segment, which is a reasonable solution, as it is very simple. Is that the case? Is there a standard format you follow?</p>
</blockquote>
</aside>
<p>I am using a graph-based approach to store segments information, where I have there IDs and additional features such spacial relationships and many others…</p>
<p>Thanks for sharing OpenAnatomy! It is similar to what I am working on.</p>

---

## Post #8 by @lassoan (2020-01-31 01:26 UTC)

<aside class="quote no-group quote-modified" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<ol>
<li>I tried version 4.11, saving segmentation to nii file, and I got exactly the same behavior, original labels were lost. Code used:</li>
</ol>
<p><img src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/40/5685_2.png" alt="" width="20" height="20" role="presentation"> Mostafa_Darwiche:</p>
<blockquote>
<p>localLabelmap = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’) slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(self.segmentationVolumeNode, localLabelmap)<br>
slicer.util.saveNode(localLabelmap, filePath)</p>
</blockquote>
</blockquote>
</aside>
<p><code>ExportAllSegmentsToLabelmapNode</code> assign lables from 0 to (n-1). Same as when you export to labelmap using GUI. If you want to preserve original label values then don’t use this method.</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>Next, I tried saving with the same way to nrrd file (both versions 4.10 and 4.11). The header files did not have information about original labels.</p>
</blockquote>
</aside>
<p>Since you have called <code>ExportAllSegmentsToLabelmapNode</code> before, it does not matter what file format you saved into after that.</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>If I save to .nii file, labels are lost.</p>
</blockquote>
</aside>
<p>It is very hard to save custom fields to nifti file header, therefore we do not support writing segmentation to nifti file.</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>Next, I tried saving with the same way to nrrd file (both versions 4.10 and 4.11). The header files did not have information about original labels.</p>
</blockquote>
</aside>
<p>Slicer is developed rapidly. The 4.11 version that you tried may be several months old, which is <em>old</em>. Try with the most recent preview release and you’ll find that original label values are preserved in the file.</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>Which is exactly what I am looking for. The original IDs are stored in metadata. The problem, however, is that the pixels are not labeled with those IDs. In fact, I only have two IDs in the whole image, 0 and 1. All segments are labeled 1 and the rest is 0. I reproduced this in ITK-Snap.</p>
</blockquote>
</aside>
<p>This is a 4D volume (dimension: 4). Earlier Slicer versions always created 4D volume (each segment is stored as a separate 3D volume). This is what you see in the file header above.</p>
<p>Users had difficulty using this file format with third-party software that could only handle 3D volumes (and it also consumed more memory than it was necessary), so we recently changed Slicer so that it can store non-overlapping segments in a single 3D volume. We still support 4D segmentation volumes and use it when segments overlap (we use multiple “layers” of 3D volumes).</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>I will try DICOM and see.</p>
</blockquote>
</aside>
<p>For clinical applications, DICOM is very good (and unavoidable anyway). If you install Quantitative Reporting extension then you can export segmentation to DICOM segmentation object (you can also export to DICOM RT structure set but that’s a terrible format, so I would not recommend to use that). You can set standard terminology by double-clicking the color swatch in segment list. Slicer is shipped with 2 terminologies (both are based on DICOM SNOMED CT terms, one contains a large list, the other contains only those terms that are listed in 3D Slicer’s GenericAnatomyColors colormap; but you can add your own terminology list).</p>
<aside class="quote no-group" data-username="Mostafa_Darwiche" data-post="7" data-topic="10011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mostafa_darwiche/48/5685_2.png" class="avatar"> Mostafa_Darwiche:</div>
<blockquote>
<p>I am using a graph-based approach to store segments information, where I have there IDs and additional features such spacial relationships and many others…</p>
<p>Thanks for sharing OpenAnatomy! It is similar to what I am working on.</p>
</blockquote>
</aside>
<p>Great! Make sure you coordinate with them to avoid parallel efforts.</p>
<p>They are working closely with leading anatomist groups worldwide (for example, they are going to release TA2 soon), collaborating with several groups who produce atlases, building tools to organize terminologies, creating graphs/hierarchies to organize them, provide various filtering, searching, tagging mechanisms in web and desktop applications (including authoring and export tools in Slicer), etc.</p>
<p>I’m sure they would be happy to hear about your efforts and there would be lots of collaboration opportunities.</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> do you have anything to add?</p>

---

## Post #9 by @Mostafa_Darwiche (2020-02-08 12:39 UTC)

<p>Just so we can close this thread, the easiest solution that worked for me was to parse manually the nrrd file and generate my expected nii one. In a nutshell:</p>
<ol>
<li>I am saving the segmentation into nrrd using:</li>
</ol>
<blockquote>
<p>myStorageNode = self.segmentationVolumeNode.CreateDefaultStorageNode()<br>
myStorageNode.SetFileName(filePath)<br>
myStorageNode.WriteData(self.segmentationVolumeNode)</p>
</blockquote>
<ol start="2">
<li>I parse the nrrd and convert to nii (using pynrrd and nibabel). I count on nrrd metadata to get the original labels and set them in my nii.</li>
</ol>
<p>This is the cheapest solution for me so far and it does the job. However, soon I’ll be shifting to a newer version of slicer and adding more functionalities especially supporting DICOM format.</p>
<p>Thank you.</p>

---
