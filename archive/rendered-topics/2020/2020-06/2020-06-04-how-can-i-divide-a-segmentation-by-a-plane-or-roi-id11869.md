---
topic_id: 11869
title: "How Can I Divide A Segmentation By A Plane Or Roi"
date: 2020-06-04
url: https://discourse.slicer.org/t/11869
---

# How can I divide a segmentation by a plane or ROI?

**Topic ID**: 11869
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/how-can-i-divide-a-segmentation-by-a-plane-or-roi/11869

---

## Post #1 by @mikebind (2020-06-04 23:20 UTC)

<p>Hello, I have airway segmentation that I would like to divide into regions (nasopharynx, oropharynx, hypopharynx) based on planes defined by the locations of points I have stored as fiducials.  The airway segmentation is straightforward via thresholding, the fiducial placement is straightforward.  I cannot figure out how to easily combine the two.  If I could define a plane and use it to divide a segment into two segments, that would work.  If I could define a rectangular prism ROI (like is used for CropVolume or Volume Rendering) and crop a segment down to that region, that would also work for me.</p>
<p>I understand that it would be possible for me to generate the ROI’s I want, crop the volume down to that ROI and then segment the cropped volume. However, I want to do this on multiple dynamic volumes (~40 time points each), and the extra processing time generating the cropped volumes seems unnecessary when it feels like I should be able to do the editing on the segmentations instead of the original volumes.</p>
<p>The scissors tool with rectangular selection area also seems close to what I want, but I don’t know how to operate the scissors tool from a python script (i.e. without interactive mouse selection of the area to keep), and as <a class="mention" href="/u/lassoan">@lassoan</a> pointed out in a different post, the scissors tool operates in display coordinates whereas the points I want to use to guide the cutting are in world coordinates.</p>
<p>The Surface Cut tool followed by Keep Selected Islands tool are also close to what I would want, except that again, they are hard to use from a script as they are designed to operate based on interactive mouse input.</p>
<p>If I could create a segment which filled an AnnotationROI, then I could use logical operators to generate what I want.</p>
<p>If there’s really nothing better, I’ll go with the Crop Volume approach, but it seems like Slicer probably has the capabilities I’m looking for, and I’m just not finding or putting them together in the best way.</p>

---

## Post #2 by @pieper (2020-06-04 23:48 UTC)

<p>Sounds like you might be able to use the amazing new Dynamic Modeler module</p>
<aside class="quote quote-modified" data-post="1" data-topic="11759">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-dynamic-modeler-parametric-surface-editing-for-biomedical-applications/11759">New module: Dynamic Modeler - parametric surface editing for biomedical applications</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have added a new module called “Dynamic Modeler” to the latest Slicer preview releases (4.11). This module provides an extensible framework for automatic processing of mesh nodes by executing “Tools” on the input to generate output mesh. 

  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" class="video-thumbnail" rel="noopener">
    [3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications]
  </a>


Output of a tool can be used as input in another tool, which allows specification of complex editing operations. This is similar to “parametric editing” in eng…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-06-05 00:18 UTC)

<p>I agree that this could be a nice application of Dynamic modeler, especially if you want to operate on models. If you prefer to remain in segmentation’s binary labelmap representation then you can use Surface Cut effect from a Python script as shown in its automated test:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/ce48206d642aa19503ba4cea579a6973273e22ad/SegmentEditorSurfaceCut/SegmentEditorSurfaceCut.py#L63-L130" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/ce48206d642aa19503ba4cea579a6973273e22ad/SegmentEditorSurfaceCut/SegmentEditorSurfaceCut.py#L63-L130" target="_blank">lassoan/SlicerSegmentEditorExtraEffects/blob/ce48206d642aa19503ba4cea579a6973273e22ad/SegmentEditorSurfaceCut/SegmentEditorSurfaceCut.py#L63-L130</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="63" style="counter-reset: li-counter 62 ;">
<li>import SampleData</li>
<li>sampleDataLogic = SampleData.SampleDataLogic()</li>
<li>masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()</li>
<li>
</li><li>##################################</li>
<li>self.delayDisplay("Create tumor segmentation")</li>
<li>
</li><li>segmentationNode = slicer.vtkMRMLSegmentationNode()</li>
<li>slicer.mrmlScene.AddNode(segmentationNode)</li>
<li>segmentationNode.CreateDefaultDisplayNodes()</li>
<li>segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</li>
<li>
</li><li>segmentName = "Tumor"</li>
<li>import vtkSegmentationCorePython as vtkSegmentationCore</li>
<li>
</li><li>segment = vtkSegmentationCore.vtkSegment()</li>
<li>segment.SetName(segmentationNode.GetSegmentation().GenerateUniqueSegmentID(segmentName))</li>
<li>segmentationNode.GetSegmentation().AddSegment(segment)</li>
<li>
</li><li>##################################</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/ce48206d642aa19503ba4cea579a6973273e22ad/SegmentEditorSurfaceCut/SegmentEditorSurfaceCut.py#L63-L130" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @mikebind (2020-06-05 00:19 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>  I’ll take a look at that.</p>
<p>So, I would:</p>
<ul>
<li>take my segment, convert it to a model,</li>
<li>cut it with a plane cut and cap surface</li>
<li>convert cut model back to segment?</li>
</ul>
<p>Thanks also <a class="mention" href="/u/lassoan">@lassoan</a>, I will also look at that method as well.</p>

---

## Post #5 by @mikebind (2020-06-05 17:15 UTC)

<p>Having looked at the two approaches, I think both are promising.  I now understand the SurfaceCut tool much better than I did before.  I initially assumed it had to do with cutting based on an existing model surface, or something like that.  I now understand that you are interactively creating a model surface by placing points which should be on the surface of that model, and then using that surface to generate a segmentation.  So, my thought after looking at the self test code for the SurfaceCut tool was to supply the 8 corners of the rectangular ROI I want to use to bound the airway segment volumes, and mask the intensity range to represent air, and fill inside.  This would work perfectly if the SurfaceCut tool did not round the edges of the surface it generates.  If I place 8 corners, the rounding means that voxels outside the box defined by those corners end up included inside the generated surface, when for my application they should be excluded because they are properly part of the next airway segment.</p>
<p>Is there any way to use the SurfaceCut machinery but use flat faces instead of smooth rounded surfaces?  For my purposes the convex hull of the supplied points would be fine, I don’t need any concavity (which I see the curved surface doesn’t allow either). If not, I think I’ll have to go with the Dynamic Modeler approach.</p>

---

## Post #6 by @lassoan (2020-06-05 17:32 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="5" data-topic="11869">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Is there any way to use the SurfaceCut machinery but use flat faces instead of smooth rounded surfaces?</p>
</blockquote>
</aside>
<p>You can change <code>True</code> to <code>False</code> in this line to turn off smoothing:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py#L420">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py#L420" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py#L420" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py#L420</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="410" style="counter-reset: li-counter 409 ;">
          <li>    if not self.segmentMarkupNode or not self.segmentModel:</li>
          <li>      return</li>
          <li>    smoothing = self.scriptedEffect.integerParameter("SmoothModel") != 0</li>
          <li>    self.logic.updateModelFromMarkup(self.segmentMarkupNode, self.segmentModel, smoothing)</li>
          <li></li>
          <li>  def interactionNodeModified(self, interactionNode):</li>
          <li>    # Override default behavior: keep the effect active if markup placement mode is activated</li>
          <li>    pass</li>
          <li></li>
          <li>  def getNumberOfDefinedControlPoints(self):</li>
          <li class="selected">    count = 0</li>
          <li>    if self.segmentMarkupNode:</li>
          <li>      count = self.segmentMarkupNode.GetNumberOfDefinedControlPoints()</li>
          <li>    return count</li>
          <li></li>
          <li>class SurfaceCutLogic:</li>
          <li></li>
          <li>  def __init__(self, scriptedEffect):</li>
          <li>    self.scriptedEffect = scriptedEffect</li>
          <li></li>
          <li>  def setUpModelDisplayNode(self, modelDisplayNode):</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you added a checkbox on the GUI to enable/disable smoothing and send a pull request then we would be happy to merge it.</p>

---

## Post #7 by @mikebind (2020-06-05 17:33 UTC)

<p>Great!  I’ll work on doing that.  I appreciate all the support!  Thanks!</p>

---

## Post #8 by @mikebind (2020-06-05 22:42 UTC)

<p>Created pull request: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/pull/33" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/pull/33</a></p>
<p>This is my first attempt making a pull request for a real github project. Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the encouragement to figure out the last few steps to contribute back to the Slicer community.</p>

---
