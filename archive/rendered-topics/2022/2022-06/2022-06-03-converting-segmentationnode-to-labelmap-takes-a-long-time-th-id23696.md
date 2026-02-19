---
topic_id: 23696
title: "Converting Segmentationnode To Labelmap Takes A Long Time Th"
date: 2022-06-03
url: https://discourse.slicer.org/t/23696
---

# Converting SegmentationNode to Labelmap takes a long time through Python

**Topic ID**: 23696
**Date**: 2022-06-03
**URL**: https://discourse.slicer.org/t/converting-segmentationnode-to-labelmap-takes-a-long-time-through-python/23696

---

## Post #1 by @edwardwang1 (2022-06-03 21:03 UTC)

<p>Hello,</p>
<p>I am using Slicer to convert RT structs to binary label maps. I am able to do it via Python, but it takes much longer than using the Segmentations module and doing it by hand (under the representations section). For some files it takes a few minutes, and for some it hangs for hours. I have tested this both via the Jupyter Extension, as well as running a script via the command line.</p>
<p>The line that causes the issue is:<br>
<code>classvtkMRMLSegmentationNode. CreateBinaryLabelmapRepresentation()</code></p>
<p>OS: Windows 10<br>
Slicer versions: 4.11 (Jupyter + python script) and 5.1 (python script only, Jupyter not tested)</p>
<p>I suspect that this issue arises because the Segmentations module is using a different function call, though I have not been able to find more details to support this.</p>
<p>Thanks for your help!<br>
Edward</p>

---

## Post #2 by @mau_igna_06 (2022-06-05 19:17 UTC)

<p>Please read more.about this.class <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<a href="https://apidocs.slicer.org/master/classvtkSegmentation.html" class="onebox" target="_blank" rel="noopener">https://apidocs.slicer.org/master/classvtkSegmentation.html</a></p>
<p>I thimkmit may help</p>

---

## Post #3 by @edwardwang1 (2022-06-06 15:48 UTC)

<p>Hi Mauro,</p>
<p>Thanks for your response. Is there a particular function that you suggest I look at? I’ve double checked that the conversion parameters are the same when running it through Python as well as using the Segmentations module.</p>
<p>I have also tried first converting my planar contours to closed surfaces, then to binary label maps (because it has a much lower estimated cost than planar contour → ribbon model → binary label map), but it is still taking a long time.</p>
<p>Thanks,<br>
Edward</p>

---

## Post #4 by @mau_igna_06 (2022-06-06 17:25 UTC)

<p>I think you should read about this</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules" target="_blank" rel="noopener">SlicerRT/DicomRtImportExport/ConversionRules at master · SlicerRt/SlicerRT</a></h3>

  <p><a href="https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules" target="_blank" rel="noopener">master/DicomRtImportExport/ConversionRules</a></p>

  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #5 by @steffen-o (2022-06-07 07:10 UTC)

<p>I use this code snippet and it works fine:</p>
<blockquote>
<p>segmentationNode = getNode(“Segmentation”)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)</p>
</blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=snippet#export-labelmap-node-from-segmentation-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=snippet#export-labelmap-node-from-segmentation-node</a></p>

---

## Post #6 by @edwardwang1 (2022-06-11 21:18 UTC)

<p>Thanks for the response! Using the code you provided, I was able to narrow down my problem to a few problematic contours/segmentations. Once I get that figured out, I am confident that I will get everything working.</p>

---

## Post #7 by @edwardwang1 (2022-06-13 19:04 UTC)

<p>After playing around with the Segmentation modules some more, I think I’ve discovered the source of my issue. Some of the contours that I exported from our radiation contour planning software are improperly converted to closed surfaces when I import their DICOM into Slicer. Therefore, the conversion of planar contour → closed surface → binary label map doesn’t work.</p>
<p>Using the Segmentation module, I can choose the higher cost option of converting planar contour → ribbon model → binary label map, and this appears to work. Previously when I converted the contours manually in Slicer, I must have chosen this path. So it appears that I can convert everything using the Slicer app, but I would like to do this via a script, as I have a lot patients to convert.</p>
<p>I tried to use the <strong>BatchStructureSetConversion.py</strong> script in the SlicerRT extension and that didn’t work either, I think because it also tries to use closed surface as an intermediate step. Looking at the code, it calls <code>CreateBinaryLabelmapRepresentation()</code>, which is what I did in my original script.</p>
<p>Looking at the Python API for vtkMRMLSegmentationNode and vtkSegmentation, there does not appear to be a way to use a ribbon model as an intermediary. My next step is try and create a C++ extension that can make use of the relevant Conversion Rules in SlicerRT - but before I get to deep in this, I wonder if anyone has any alternate suggestions.</p>

---

## Post #8 by @lassoan (2022-06-13 19:50 UTC)

<p>All features are available via the Python interface, so you don’t need to switch to C++ if you don’t want to. It is possible that in some cases we missed wrapping some structures into Python-compatible types - if you find one then let us know and we’ll fix it.</p>
<p>You can see how conversion is done with custom conversion path in the icdr GUI: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.cxx" class="inline-onebox">Slicer/qMRMLSegmentationConversionParametersWidget.cxx at master · Slicer/Slicer · GitHub</a></p>
<p>There are some <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-all-segments-using-default-path-and-conversion-parameters">related Python code snippets</a> that you may find useful.</p>

---

## Post #9 by @edwardwang1 (2022-06-13 21:26 UTC)

<p>Hi Andras,</p>
<p>Thanks for your response. I took a look at the Python code examples, and it seems like there aren’t any examples using a custom conversion path, just ones that use a custom conversion parameter.</p>
<p>I also took a look at the C++ code that you linked. There is a snippet that I would like to use:</p>
<pre><code class="lang-auto">  vtkSegmentation* segmentation = d-&gt;SegmentationNode-&gt;GetSegmentation();
  vtkSegmentationConverter::ConversionPathAndCostListType pathsCosts;
  segmentation-&gt;GetPossibleConversions(d-&gt;TargetRepresentationName.toUtf8().constData(), pathsCosts);
</code></pre>
<p>but it seems like the method:</p>
<pre><code class="lang-auto">GetPossibleConversions()
</code></pre>
<p>is not available to the Python object of vtkSegmentation (I checked this using the dir() function in Python).</p>
<p>Furthermore, looking at vtkSegmentationConverter, it appears there is no equivalent to: <code>GetBinaryLabelmapRepresentationName ()</code> or<br>
<code>GetSegmentationBinaryLabelmapRepresentationName ()</code><br>
for a Ribbon Model, which is the intermediate representation that I want to use. I would be curious to see if</p>
<pre><code class="lang-auto">segmentation.GetPossibleConversions()
</code></pre>
<p>would include it in one if its paths.</p>
<p>Thanks</p>

---
