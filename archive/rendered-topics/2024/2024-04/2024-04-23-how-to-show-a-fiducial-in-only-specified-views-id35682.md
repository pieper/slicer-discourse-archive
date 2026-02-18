# How to show a fiducial in only specified views?

**Topic ID**: 35682
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/how-to-show-a-fiducial-in-only-specified-views/35682

---

## Post #1 by @koeglfryderyk (2024-04-23 14:56 UTC)

<p>I have a vtkMRMLMarkupsFiducialNode and want to show it only a few views, e.g. Red+, Green+ and Yellow+.</p>
<p>How can I do that?</p>

---

## Post #2 by @koeglfryderyk (2024-04-23 14:58 UTC)

<p>First get the slice nodes of all the views and then set the view node IDs of the display node of the vtkMRMLMarkupsFiducialNode</p>
<pre><code class="lang-auto">sliceNodeRed_plus = slicer.app.layoutManager().sliceWidget("Red+").mrmlSliceNode()
sliceNodeGreen_plus = slicer.app.layoutManager().sliceWidget("Green+").mrmlSliceNode()
sliceNodeYellow_plus = slicer.app.layoutManager().sliceWidget("Yellow+").mrmlSliceNode()

my_fiducial_node.GetDisplayNode().SetViewNodeIDs([sliceNodeRed_plus.GetID(), sliceNodeGreen_plus.GetID(), sliceNodeYellow_plus.GetID()])
</code></pre>

---
