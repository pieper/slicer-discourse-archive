---
topic_id: 37421
title: "Creating Multiple Transform Handles For A Modelnode In Slice"
date: 2024-07-17
url: https://discourse.slicer.org/t/37421
---

# Creating Multiple Transform Handles for a ModelNode in Slicer 5.7

**Topic ID**: 37421
**Date**: 2024-07-17
**URL**: https://discourse.slicer.org/t/creating-multiple-transform-handles-for-a-modelnode-in-slicer-5-7/37421

---

## Post #1 by @park (2024-07-17 08:40 UTC)

<p>Hello,</p>
<p>Is it possible to create two Transform handles for one model?<br>
I have tried to make it work with the video using the code below, but only one handle works while the other does not function properly.</p>
<p>Am I missing something? Any advice would be greatly appreciated.</p>
<pre><code class="lang-auto">scanNode = slicer.util.getNode("scan")
lowerNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', 'lower')
upperNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', 'upper')

def applyUpper(*_unused):
    scanNode.SetAndObserveTransformNodeID(None)
    
    lowerNode.SetAndObserveTransformNodeID(upperNode.GetID())
    scanNode.SetAndObserveTransformNodeID(lowerNode.GetID())

def applyLower(*_unused):
    scanNode.SetAndObserveTransformNodeID(None)
    
    upperNode.SetAndObserveTransformNodeID(lowerNode.GetID())
    scanNode.SetAndObserveTransformNodeID(upperNode.GetID())

lowerNode.CreateDefaultDisplayNodes()
lowerNode.SetCenterOfTransformation(0,0,-12)
lowerNode.GetDisplayNode().SetEditorVisibility(True)
lowerNode.AddObserver(slicer.vtkMRMLTransformNode.TransformModifiedEvent, applyLower)

upperNode.CreateDefaultDisplayNodes()
upperNode.SetCenterOfTransformation(0,0,2)
upperNode.GetDisplayNode().SetEditorVisibility(True)
upperNode.AddObserver(slicer.vtkMRMLTransformNode.TransformModifiedEvent, applyUpper)
</code></pre>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b7c209cf30ed33aee6a56f6cc6cebd98634ba4d.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03765fea40a85339ddec50528382ec144b355b33.png">
  </div><p></p>
<p>P.S. The Transform handle added in Slicer 5.7 is fantastic.</p>

---
