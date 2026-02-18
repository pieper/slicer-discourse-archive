# Transform a labelmap with a transorm and save it

**Topic ID**: 25640
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/transform-a-labelmap-with-a-transorm-and-save-it/25640

---

## Post #1 by @S_Arbabi (2022-10-11 09:19 UTC)

<p>Hi,</p>
<p>I have a labelmap and I’m transforming it using a transform node:</p>
<p><code>lblmap_node.SetAndObserveTransformNodeID(transform_node.GetID())</code></p>
<p>but then when I save this labelmap_node and open it later it seems like it hasn’t been transformed:</p>
<p><code>slicer.util.saveNode(lblmap_node, path)</code></p>
<p>I’ve seen threads here about hardening the transform, or exporting the node in the world coordinate system. I finally extract the segmentation out of labelmap, apply the transform of segmentation node and convert it into labelmap again:</p>
<pre><code class="lang-auto">segmentation_node.SetAndObserveTransformNodeID(transform_node.GetID())
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, segmentationLblmap,  reference_volume_node)
</code></pre>
<p>It works but weiredly it cuts an area of labelmap shown in the image bellow:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e69ac6006acc47e277ae70e7c2619ed1aff27521.png" alt="image" data-base62-sha1="wU1pXMo947KRxFMudhJ04WM1nkR" width="287" height="270"><br>
instead of being like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3eca50e87e13378f996cc329fa27d84cb60cda6.png" alt="image" data-base62-sha1="yNR285UVpcAqC6HWBaRdh0BUXie" width="280" height="264"></p>
<p>Am I missing something here? I appreciate any suggestions.</p>
<p>Best,<br>
Saeed</p>

---

## Post #2 by @S_Arbabi (2022-10-12 08:02 UTC)

<p>I found the solution to this using transformableNode.HardenTransform().<br>
But my question is why the shape changes after hardenning the transform? in my case the shape of fixed image is 135x300x177 and shape of moving labelmap before transfer is 135x300x189, but after setAndObserveTransform and hardening transform its shape is 141x308x192. which is something I don’t understand!!</p>

---

## Post #3 by @S_Arbabi (2022-10-12 12:17 UTC)

<p>Resample Scalar Volume worked.<br>
<a href="https://discourse.slicer.org/t/resample-scalar-volumes-scripting-in-python/19736/11">https://discourse.slicer.org/t/resample-scalar-volumes-scripting-in-python/19736/11?u=s_arbabi</a></p>

---
