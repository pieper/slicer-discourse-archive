---
topic_id: 7623
title: "Segmentation Extract Skin Py"
date: 2019-07-17
url: https://discourse.slicer.org/t/7623
---

# Segmentation (Extract Skin Py)

**Topic ID**: 7623
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/segmentation-extract-skin-py/7623

---

## Post #1 by @ThomPote (2019-07-17 10:38 UTC)

<p>Hi,</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for your previously answers</p>
<p>I’m always in troubles with <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="noopener nofollow ugc">ExtractSkin</a></p>
<p>I tryed to import my own CT scan but it doesn’t work as your example datas</p>
<p>Further I will need to load DICOM.</p>
<blockquote>
<p>masterVolumeNode = slicer.util.loadVolume(‘/…/myCT.nrrd’, returnNode=True)<br>
masterVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkmasterVolumeNode”)</p>
<p><span class="hashtag-raw">#Create</span> segmentation<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)<br>
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“bone”)</p>
<p><span class="hashtag-raw">#Create</span> segment editor to get access to effects<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
</blockquote>
<p>Occuring errors for all effects on apply line</p>
<blockquote>
<p><span class="hashtag-raw">#Thresholding</span><br>
modifierLabelmap.GetImageToWorldMatrix(originalImageToWorldMatrix)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetImageToWorldMatrix’</p>
</blockquote>
<blockquote>
<p><a class="hashtag-cooked" href="/tag/smoothing" data-type="tag" data-slug="smoothing" data-id="475"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>smoothing</span></a><br>
modifierLabelmap.DeepCopy(smoothingFilter.GetOutput())<br>
AttributeError: ‘NoneType’ object has no attribute ‘DeepCopy’</p>
</blockquote>

---

## Post #2 by @lassoan (2019-07-17 14:27 UTC)

<aside class="quote no-group" data-username="ThomPote" data-post="1" data-topic="7623">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thompote/48/2256_2.png" class="avatar"> ThomPote:</div>
<blockquote>
<p>masterVolumeNode = slicer.util.loadVolume(’/…/myCT.nrrd’, returnNode=True)<br>
masterVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkmasterVolumeNode”)</p>
</blockquote>
</aside>
<p>Here you load a volume into <code>masterVolumeNode</code> then immediately overwrite it with an empty volume, which breaks everything else.</p>

---

## Post #3 by @ThomPote (2019-10-04 08:24 UTC)

<p>Ok thanks a lot !</p>
<p>Another bug, I tried to test différent <strong>parameters combinations</strong> like this :</p>
<p>THRESHOLD_LIST = [item,item]<br>
SMOOTH_SIZE = [item,item]<br>
MARGIN_SIZE = [item,item]</p>
<p>for t in THRESHOLD_LIST<br>
…for m in MARGIN_SIZE:<br>
…for s in SMOOTH_SIZE:<br>
…# Thresholding effect<br>
…# Margin effect effect<br>
…# Smoothing effect<br>
…# Test</p>
<p>To obtain results like this :<br>
Threshold, Margin size, Smoothing, Result<br>
t,m,s, resultat1<br>
t,m,s, resultat2<br>
t,m,s, resultat3 …</p>
<p>But computer is overheating !!! it’s very very very long, any idea ?</p>

---

## Post #4 by @lassoan (2019-10-04 11:26 UTC)

<p>Probably you try to store results of tens or hundreds of iterations in the scene. During this you run out of physical memory and everything slows down due to starting swapping data between RAM and physical disk. To avoid this, at the end of each iteration, write the results to file then delete the result nodes (or reuse them in the next iteration).</p>

---

## Post #5 by @ThomPote (2019-10-05 11:09 UTC)

<p>Ok not so much iterations in my case, I need your help.<br>
I tryed it without saving any results, just for testing iteration process.<br>
First iteration takes 18 seconds, the second 1min14 ! and after I stop it before overheating</p>
<pre><code>def run(self, inputVolume):
"""

SEUIL = [0.97,0.90]
SMOO_SIZE = [3,7]
SMOO_METHOD = "MEDIAN"
MARGIN_SIZE = [3]
MARGIN_METHOD = "Shrink"
SEUIL_ISLAND_SIZE = 500
masterVolumeNode = inputVolume

for iSEUIL in SEUIL:
  for iMARGIN_SIZE in MARGIN_SIZE:
    for iSMOO_SIZE in SMOO_SIZE:

      # Create segmentation
      segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
      segmentationNode.CreateDefaultDisplayNodes() # only needed for display
      segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
      addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")
      # Create segment editor to get access to effects
      segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
      segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
      segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
      segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
      segmentEditorWidget.setSegmentationNode(segmentationNode)
      segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
      
      # UH Range
      rangeUH = masterVolumeNode.GetImageData().GetScalarRange()

      # Thresholding
      segmentEditorWidget.setActiveEffectByName("Threshold")
      effect = segmentEditorWidget.activeEffect()
      effect.setParameter("MinimumThreshold",rangeUH[1]*iSEUIL)
      effect.setParameter("MaximumThreshold",rangeUH[1])
      effect.self().onApply()

      # Margin
      segmentEditorWidget.setActiveEffectByName("Margin")
      effect = segmentEditorWidget.activeEffect()
      effect.setParameter("Operation", MARGIN_METHOD)
      effect.setParameter("MarginSize", iMARGIN_SIZE)
      effect.self().onApply()

      # Smoothing
      segmentEditorWidget.setActiveEffectByName("Smoothing")
      effect = segmentEditorWidget.activeEffect()
      effect.setParameter("SmoothingMethod", SMOO_METHOD)
      effect.setParameter("KernelSizeMm", iSMOO_SIZE)
      effect.self().onApply()

      # Islands
      segmentEditorWidget.setActiveEffectByName("Islands")
      effect = segmentEditorWidget.activeEffect()
      effect.setParameter("Minimumsize", SEUIL_ISLAND_SIZE)
      effect.setParameter("Operation", "SPLIT_ISLANDS_TO_SEGMENTS")
      effect.self().onApply()
     
      # Measures
      # [...]

      # Clean up
      segmentEditorWidget = None
      slicer.mrmlScene.RemoveNode(segmentEditorNode)
      slicer.mrmlScene.RemoveNode(segmentationNode)

      qt.QMessageBox.information(slicer.util.mainWindow(), 'Slicer Python - Result', str)</code></pre>

---

## Post #6 by @lassoan (2019-10-05 12:31 UTC)

<p>This confirms that the problem is that you run out of RAM.</p>
<p>Your script still does not free up memory because you need to delete display nodes and all filters. It could be simpler to get it right, if you create nodes and filters once and then update them in each iteration.</p>

---
