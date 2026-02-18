# Model Plane Cutting

**Topic ID**: 30556
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/model-plane-cutting/30556

---

## Post #1 by @Muhammed_Fatih_Talu (2023-07-12 15:48 UTC)

<p>How can I set the InputPlane parameter to RED plane?<br>
Because I want it to do the cutting on the RED plane.</p>
<pre><code class="lang-auto">dynamicModelerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")                
dynamicModelerNode.SetToolName("Plane cut")                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputModel", InputModelNode.GetID())                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", "Red")
dynamicModelerNode.SetNodeReferenceID("PlaneCut.OutputPositiveModel", InputModelNode.GetID())
slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(dynamicModelerNode)

</code></pre>

---

## Post #2 by @Sunderlandkyl (2023-07-12 15:54 UTC)

<p>You need to specify the “Red” slice node ID.</p>
<p>Ex.</p>
<pre><code class="lang-python">redSliceNode = slicer.util.getFirstNodeByClassByName("vtkMRMLSliceNode", "Red")
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", redSliceNode.GetID())
</code></pre>

---

## Post #3 by @Muhammed_Fatih_Talu (2023-07-12 18:04 UTC)

<p>Thank you for quick reply</p>
<p>But there is no Red slice node.<br>
So i can not use getnode.<br>
i need to set the plane node parameter of the dynamic model object as RED.<br>
Thanks</p>

---

## Post #4 by @Sunderlandkyl (2023-07-12 18:19 UTC)

<p>If there isn’t a Red slice node, then you can’t set it as an input. It also wouldn’t appear in any view layouts.</p>
<p>There should always be a red slice node in the scene if you are running a Slicer GUI.</p>

---

## Post #5 by @Muhammed_Fatih_Talu (2023-07-12 18:31 UTC)

<p>I have tried:</p>
<pre><code class="lang-auto">redSliceNode = slicer.util.getNodesByClass('vtkMRMLSliceNode','Red')
dynamicModelerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")                
dynamicModelerNode.SetToolName("Plane cut")                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputModel", InputBeyinModelNode.GetID())                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", redSliceNode.GetID())
dynamicModelerNode.SetNodeReferenceID("PlaneCut.OutputPositiveModel", InputBeyinModelNode.GetID())
slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(dynamicModelerNode)
</code></pre>
<p>but, the error:</p>
<pre><code class="lang-auto">dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", redSliceNode.GetID())
AttributeError: 'list' object has no attribute 'GetID'
</code></pre>

---

## Post #6 by @Sunderlandkyl (2023-07-12 18:37 UTC)

<p>‘getNodesByClass’ returns a list of all "vtkMRMLSliceNodes in the scene ([Red, Green, Yellow]).</p>
<p>getFirstNodeByClassByName returns only a single node with the specified class name and node name.</p>

---

## Post #7 by @Muhammed_Fatih_Talu (2023-07-12 18:55 UTC)

<p>After loading model file, the Red, Green and Yellow slices remain beyond the model.<br>
I guess that’s why the Red slice plane cut isn’t doing any work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0437ccf9c8a9ab353b128bac8170acbb1000a4e.png" data-download-href="/uploads/short-url/vZVxM6ZCfpaZxcKRbnoZlrpfcaW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0437ccf9c8a9ab353b128bac8170acbb1000a4e_2_345x210.png" alt="image" data-base62-sha1="vZVxM6ZCfpaZxcKRbnoZlrpfcaW" width="345" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0437ccf9c8a9ab353b128bac8170acbb1000a4e_2_345x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0437ccf9c8a9ab353b128bac8170acbb1000a4e_2_517x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0437ccf9c8a9ab353b128bac8170acbb1000a4e_2_690x420.png 2x" data-dominant-color="9A9A9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×443 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2023-07-12 19:16 UTC)

<p>It is all good then. If you only work with models (no image) then probably you want to use markup plane nodes for cutting.</p>

---

## Post #9 by @Muhammed_Fatih_Talu (2023-07-12 19:20 UTC)

<p>I solved the problem.<br>
Thanks Sunderland and Lasso<br>
The solution is as below:</p>
<pre><code class="lang-auto">pointCoordinates = slicer.util.arrayFromModelPoints(InputBeyinModelNode)
import numpy as np
position = np.average(pointCoordinates, axis=0)

# Center slice views and cameras on this position                
for sliceNode in slicer.util.getNodesByClass('vtkMRMLSliceNode'):
    sliceNode.JumpSliceByCentering(*position)
for camera in slicer.util.getNodesByClass('vtkMRMLCameraNode'):
    camera.SetFocalPoint(position)              
    
# red slicedan kes
redSliceNode = slicer.util.getFirstNodeByClassByName("vtkMRMLSliceNode", "Red")

dynamicModelerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")                
dynamicModelerNode.SetToolName("Plane cut")                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputModel", InputBeyinModelNode.GetID())                
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", redSliceNode.GetID())
dynamicModelerNode.SetNodeReferenceID("PlaneCut.OutputPositiveModel", OutputBeyinModelNode.GetID())
slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(dynamicModelerNode)
</code></pre>

---
