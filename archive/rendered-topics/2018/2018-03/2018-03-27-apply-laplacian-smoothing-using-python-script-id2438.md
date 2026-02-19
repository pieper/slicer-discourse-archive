---
topic_id: 2438
title: "Apply Laplacian Smoothing Using Python Script"
date: 2018-03-27
url: https://discourse.slicer.org/t/2438
---

# Apply Laplacian smoothing using Python script

**Topic ID**: 2438
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/apply-laplacian-smoothing-using-python-script/2438

---

## Post #1 by @anandmulay3 (2018-03-27 14:17 UTC)

<p>how can i set smoothing effect to laplacian filter type in scriptable module script ??</p>

---

## Post #2 by @lassoan (2018-03-27 14:28 UTC)

<p>Segment editor smoothing effect uses <a href="https://www.vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html">vtkWindowedSincPolyDataFilter</a>, which works better than <a href="https://www.vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html">Laplacian filter</a>. The main problem with Laplacian filter is that it reduces segment volume.</p>
<p>See this example how to apply Smoothing effect from Python script:</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a></h4>
<h5>ExtractSkin.py</h5>
<pre><code class="Python">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")
</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Change <code>SmoothingMethod</code> from <code>MEDIAN</code> to <code>JOINT_TAUBIN</code> to use vtkWindowedSincPolyDataFilter instead of median filter.</p>

---

## Post #3 by @anandmulay3 (2018-03-28 06:48 UTC)

<p>Ahh… I’m already using this one…<br>
Alright so this is the best smoothing technique …<br>
Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Can i repeat same code of segmentation to add multiple segment in same model .</p>

---

## Post #4 by @lassoan (2018-03-28 10:55 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="3" data-topic="2438">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>Can i repeat same code of segmentation to add multiple segment in same model</p>
</blockquote>
</aside>
<p>To fuse segments, you can use Logical operators effect.</p>
<p>You can merge segments (boundaries between them is kept) if you use the direct file export tool that has been added recently to the nightly build - see <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428" class="inline-onebox">Save segmentation directly to STL or OBJ files</a></p>
<p>You can merge models one by one using Merge Models module.</p>

---

## Post #5 by @anandmulay3 (2018-03-29 13:38 UTC)

<p>thanks it works and gives nice output , but how can i do this by adding code into this script ?? <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a></p>
<p>and thanks for the support <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @lassoan (2018-03-29 15:40 UTC)

<p>Could you describe what you would like to do? Develop a new interactive Slicer module that does this? Or apply this processing in a batch mode on a large number of images?</p>
<p>You may find this tutorial useful: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial</a></p>

---

## Post #7 by @anandmulay3 (2018-04-02 06:12 UTC)

<p>I’m trying to make a batch file which will process the fbx file with different segmentation part in a single file.<br>
i’m already using your script to make segmentation and save output in fbx using fbx exporter, but now im using latest nightly build so i want use the export segmentation feature using script.</p>
<p>thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @lassoan (2018-04-04 05:54 UTC)

<p>You can use <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a9578121589a3b5e20a05aa8dce33c642">slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles(…)</a> method.</p>

---

## Post #9 by @anandmulay3 (2018-04-04 07:50 UTC)

<p>Thanks Its working perfectly… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #10 by @Saima (2021-08-23 05:57 UTC)

<p>Hi Andras,<br>
Is the sinc filter in model maker the same as the segment editor?</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #11 by @lassoan (2021-08-23 12:04 UTC)

<p>There are a few differences.</p>
<p>Segment Editor performs the same joint smoothing algorithm as Model maker, but then converts back the result into binary labelmap representation, so that it can be appropriately visualized and further edited. In contrast, Model maker creates a model that is not editable anymore.</p>
<p>Segment Editor performs a slight additional anti-aliasing filtering during generation of the closed surface representation.</p>
<p>Segment Editor can handle overlapping segments, while the Model maker cannot</p>

---
