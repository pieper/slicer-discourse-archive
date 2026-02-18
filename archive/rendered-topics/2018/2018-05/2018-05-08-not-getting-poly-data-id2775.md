# Not getting poly data

**Topic ID**: 2775
**Date**: 2018-05-08
**URL**: https://discourse.slicer.org/t/not-getting-poly-data/2775

---

## Post #1 by @anandmulay3 (2018-05-08 13:38 UTC)

<pre><code>[success, loadedVolumeNode] = slicer.util.loadVolume('\Sft.nrrd', returnNode=True)
#Segmentation
masterVolumeNode = getNode('Sft')

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("bone")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","300")
effect.setParameter("MaximumThreshold","5695")
effect.self().onApply()

# Smoothing
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 3)
effect.self().onApply()

modelNode = getNode('Sft') 
points = arrayFromModelPoints(modelNode)
</code></pre>
<p>please check above code everything works fine except last line .<br>
Traceback:<br>
‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘GetPolyData’</p>
<p>do i need any additional code, so that i can get polydata from my node or from these segmentation process.</p>

---

## Post #2 by @lassoan (2018-05-09 03:52 UTC)

<aside class="quote no-group quote-modified" data-username="anandmulay3" data-post="1" data-topic="2775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>modelNode = getNode(‘Sft’)</p>
</blockquote>
</aside>
<p>This method will return your input volume node, the same way as this method call returns your input volume node at the beginning of your script. You can get surface mesh from your segmentation as shown in this example: <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9#file-extractskin-py-L37-L41" class="inline-onebox">This example demonstrates how to extract skin surface from an MRI image using thresholding and smoothing effect of Segment Editor · GitHub</a></p>

---

## Post #3 by @anandmulay3 (2018-05-09 14:03 UTC)

<p>using above method to create surfacemesh i’m still not able to get polydata<br>
i have tried setting <code>modelNode = getNode(sementID)</code></p>
<p>still am i missing any code?</p>

---

## Post #4 by @lassoan (2018-05-09 15:07 UTC)

<p><code>getNode</code> expects a node name or node ID. Passing a segment ID (an internal ID within a segmentation node) will not work. Follow the example that I referenced above more closely. It should be something like this:</p>
<pre><code>segmentationNode.CreateClosedSurfaceRepresentation()
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)</code></pre>

---

## Post #5 by @anandmulay3 (2018-05-10 06:52 UTC)

<p>yeah, i did the same thing and then i tried to getNode like this</p>
<pre><code>modelNode = getNode(addedSegmentID)
    Traceback (most recent call last):
      File "&lt;console&gt;", line 1, in &lt;module&gt;
      File "C:\Program Files\Slicer 4.9.0-2018-05-07\bin\Python\slicer\util.py", line 631, in getNode
        raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (type(pattern) == str) else ""))
    MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'bone'
</code></pre>
<p>and this error comes up , in data still i cant find out the mode hierarchy;only my volume node under that segmentation and a single segment…</p>

---

## Post #6 by @lassoan (2018-05-10 14:57 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="5" data-topic="2775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>modelNode = getNode(addedSegmentID)</p>
</blockquote>
</aside>
<p>This should return an error and it does, so everything works as expected. If you need a vtkPolyData of a segment, then please see my post above that shows how <code>surfaceMesh</code> variable is set.</p>

---
