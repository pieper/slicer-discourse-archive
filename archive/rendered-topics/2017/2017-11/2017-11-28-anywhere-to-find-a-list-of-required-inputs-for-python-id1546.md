# Anywhere to find a list of required inputs for Python?

**Topic ID**: 1546
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/anywhere-to-find-a-list-of-required-inputs-for-python/1546

---

## Post #1 by @gbaltz (2017-11-28 20:23 UTC)

<p>Hello,</p>
<p>I am trying to write a Python script that can automate the export of a .stl model from a segmentation that is imported with the CT DICOM set.</p>
<p>I have pretty much everything by painfully looking through examples online, but I am stuck on how to do the final export.</p>
<p>I think this might be the code to use:</p>
<blockquote>
<p>slicer.modules.models.logic().SaveModel()</p>
</blockquote>
<p>But that code requires two arguments and I have no way of figuring out what they are supposed to be. This is an issue I have run into with many other commands. Is there some database I can access that says what all the arguments for a code are supposed to be?</p>
<p>All i get back in the traceback error is:</p>
<blockquote>
<p>TypeError: SaveModel() takes exactly 2 arguments (0 given)</p>
</blockquote>
<p>Which is next to useless as it doesn’t tell me what the arguments need to be.</p>

---

## Post #2 by @lassoan (2017-11-28 20:45 UTC)

<p>You can use the <code>help</code> command to get documentation on any command. For example, enter this in the Python console:</p>
<pre><code>help(slicer.modules.models.logic().SaveModel)
</code></pre>
<p>You can find full documentation of Slicer’s Python-wrapped C++ API at <a href="http://apidocs.slicer.org">http://apidocs.slicer.org</a>. Models module logic is documented here: <a href="http://apidocs.slicer.org/master/classvtkSlicerModelsLogic.html#ae7123e56a176f06e0eda54403f07f393">http://apidocs.slicer.org/master/classvtkSlicerModelsLogic.html#ae7123e56a176f06e0eda54403f07f393</a></p>

---

## Post #3 by @gbaltz (2017-11-29 21:54 UTC)

<p>Thanks.</p>
<p>I’m having difficulty finding the vtkMRMLModelNode for the model I want to save. Is there a way to list all available?</p>
<p>Also will the SaveModel() save as .stl format?</p>
<p>It’s very confusing to me what stuff I have to use slicer.modules.models for and what stuff I have to use slicer.vtkMRMLModelNode() for</p>

---

## Post #4 by @lassoan (2017-11-30 04:24 UTC)

<p>Get list of all model nodes in the scene: use <code>slicer.util.getNodesByClass</code>. For example:</p>
<pre><code>models=slicer.util.getNodesByClass('vtkMRMLModelNode')
for model in models:   
  if not model.GetHideFromEditors():
    print(model.GetName())
</code></pre>
<p>Save model as STL:</p>
<pre><code>slicer.util.saveNode(modelNode, "c:/tmp/test.stl")
</code></pre>
<aside class="quote no-group" data-username="gbaltz" data-post="3" data-topic="1546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/4491bb/48.png" class="avatar"> gbaltz:</div>
<blockquote>
<p>It’s very confusing to me what stuff I have to use slicer.modules.models for and what stuff I have to use slicer.vtkMRMLModelNode()</p>
</blockquote>
</aside>
<p>Model node only stores the data, so you’ll only find methods in this class that are responsible getting/setting content. Any operation on the data is implemented in Models or other module logic classes or in utility functions.</p>

---

## Post #5 by @gbaltz (2017-11-30 19:14 UTC)

<p>Once again, Thanks so much for your help.</p>
<p>Sorry to be a bother, I hope this is the last I have to ask for help.<br>
So I am trying to automate the step to export all segmentations as model that I can then save using the code you provided above.</p>
<p>So I have these segmentations. The Binary labelmap is currently master:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6749a876415698723b06fce4e02f1d1bfb997e5a.png" data-download-href="/uploads/short-url/eJIZrPh9gJKtmRuKRnx6b5MUhMm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6749a876415698723b06fce4e02f1d1bfb997e5a.png" alt="image" data-base62-sha1="eJIZrPh9gJKtmRuKRnx6b5MUhMm" width="690" height="282" data-dominant-color="ECECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×327 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I have the following code to try to export them to models</p>
<blockquote>
<p>&gt;&gt;&gt;segmentations = slicer.util.getNodesByClass(‘vtkMRMLSegmentationNode’)<br>
&gt;&gt;&gt;modelHierarchyNode = slicer.vtkMRMLModelHierarchyNode()<br>
&gt;&gt;&gt;slicer.mrmlScene.AddNode(modelHierarchyNode)<br>
&gt;&gt;&gt;slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(segmentations[0],slicer.util.getNodesByClass(‘vtkMRMLModelHierarchyNode’)[0])</p>
</blockquote>
<p>After the final line, the console returns “True” but no models appear, just this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c53fe7ca78af2aca52dc99fa584e9fd42f9ee715.png" data-download-href="/uploads/short-url/s8WYF75VQ9pBQs466b8kBpFUFiB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c53fe7ca78af2aca52dc99fa584e9fd42f9ee715.png" alt="image" data-base62-sha1="s8WYF75VQ9pBQs466b8kBpFUFiB" width="690" height="390" data-dominant-color="F0F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×454 9.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i am sure there is one step I am missing…</p>

---

## Post #6 by @gbaltz (2017-12-04 17:29 UTC)

<p>Bump. Please see above. I’ve tried trouble shooting and I’m not sure where I am going wrong.</p>
<p>The ExportAllSegmentsToModelHierarchy() returns “True”, but no models appear under the ModelHierarchy node.</p>

---

## Post #7 by @lassoan (2017-12-04 18:52 UTC)

<p>Thanks for the feedback. You’ve discovered a bug in <code>ExportAllSegmentsToModelHierarchy</code> method that I’ll fix in the nightly build today. Till then, or if you use the latest stable version, you can use <code>ExportSegmentsToModelHierarchy</code> method instead:</p>
<pre><code>seg = getNode('Segmentation')
modelHierarchyNodeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelHierarchyNode')
segmentIds = vtk.vtkStringArray()
seg.GetSegmentation().GetSegmentIDs(segmentIds)
slicer.modules.segmentations.logic().ExportSegmentsToModelHierarchy(seg, segmentIds, modelHierarchyNodeNode)</code></pre>

---
