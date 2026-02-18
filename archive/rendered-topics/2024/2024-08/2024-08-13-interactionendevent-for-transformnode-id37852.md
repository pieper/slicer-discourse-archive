# InteractionEndEvent for TransformNode

**Topic ID**: 37852
**Date**: 2024-08-13
**URL**: https://discourse.slicer.org/t/interactionendevent-for-transformnode/37852

---

## Post #1 by @park (2024-08-13 12:10 UTC)

<p>Hello,</p>
<p>I would like to trigger an event when the interaction with the transform node’s handles in Slicer 5.7 ends after modifying the transform (similar to the <code>PointEndInteractionEvent</code> feature in Markups).</p>
<p>So far, I’ve been using the following code:</p>
<pre><code class="lang-auto">transformNode.AddObserver(slicer.vtkMRMLTransducerNode.TransformModifiedEvent, myFunction)
</code></pre>
<p>However, with this approach, the event keeps firing continuously during the transformation, which consumes a lot of computing power.</p>
<p>Is there an existing feature for this, or would I need to implement a custom event? Any advice would be greatly appreciated.</p>

---
