---
topic_id: 18335
title: "Programmatically Setting A Transformprocessornode"
date: 2021-06-25
url: https://discourse.slicer.org/t/18335
---

# Programmatically setting a TransformProcessorNode

**Topic ID**: 18335
**Date**: 2021-06-25
**URL**: https://discourse.slicer.org/t/programmatically-setting-a-transformprocessornode/18335

---

## Post #1 by @atracsys-sbt (2021-06-25 09:14 UTC)

<p>Hi,<br>
I’m currently writing a module that handles two tracked markers (one attached to a phantom and one attached to a pointer i.e. a stylus).<br>
In a effort to obtain the pointer coordinates in the referential of the phantom, I would like to use a TransformProcessorNode (which I successfully used in the GUI).<br>
Here is what I wrote:</p>
<pre><code class="lang-auto">transfoProcNode = slicer.vtkMRMLTransformProcessorNode()
transfoProcNode.SetProcessingMode(transfoProcNode.PROCESSING_MODE_COMPUTE_FULL_TRANSFORM)
transfoProcNode.SetAndObserveInputFromTransformNode(pointerTransform)
transfoProcNode.SetAndObserveInputToTransformNode(phantomTransform)
phtToPtrTransfoNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode', 'PointerToPhantom')
transfoProcNode.SetAndObserveOutputTransformNode(phtToPtrTransfoNode)
transfoProcNode.SetUpdateModeToAuto()
pointerModel.SetAndObserveTransformNodeID(phtToPtrTransfoNode.GetID())
</code></pre>
<p>But, looking at the resulting transform ‘PointerToPhantom’ in the Transforms module, it appears as the identity and does not change.<br>
Thank you for any input</p>

---

## Post #2 by @lassoan (2021-06-25 18:09 UTC)

<p>Normally you would just write into the Plus configuration file to send “PointerToPhantom”. Plus toolkit can automatically compute transforms between any coordinate systems, by parsing the name and concatenating and inverting transforms as needed.</p>

---

## Post #3 by @atracsys-sbt (2021-08-23 08:34 UTC)

<p>Despite the proposed solution (deferring the transforms multiplication to Plus) being satisfactory at first, I now also need to have access to both transforms separately for other purposes.<br>
What would be better in terms of performance:</p>
<ul>
<li>keep the actual PointerToPhantom channel from Plus and add two other channels for Pointer and Phantom (which would be kind of redundant)</li>
<li>do what I tried to do in my original post: set a TransformProcessorNode<br>
Thank you for your feedback</li>
</ul>

---

## Post #4 by @lassoan (2021-08-23 16:41 UTC)

<p>Both solutions are fine.</p>
<p>Probably the transform in your script does not update because you did not add the transform processor node to the scene. You can fix it by changing the first line to <code>transfoProcNode = slicer.mrmlScene. AddNewNodeByClass('vtkMRMLTransformProcessorNode')</code>.</p>

---
