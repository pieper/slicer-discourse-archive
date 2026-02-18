# Toggling Parallel Projection programmatically not updating the 3D viewer

**Topic ID**: 40548
**Date**: 2024-12-06
**URL**: https://discourse.slicer.org/t/toggling-parallel-projection-programmatically-not-updating-the-3d-viewer/40548

---

## Post #1 by @smrolfe (2024-12-06 21:34 UTC)

<p>When I set the parallel projection parameter of the 3D view in the Python Console, the camera updates, but the parallel projection button in the 3D viewer does not. If it’s toggled off using the button and turned on programmatically, it reverts back to off after scene interaction.</p>
<p>I tried calling <code>slicer.app.processEvents()</code> and triggering different events, but I don’t seem to be able to get this setting to update.</p>
<p>This can be replicated with the code below.</p>
<pre><code class="lang-auto">viewNode1 = slicer.mrmlScene.GetFirstNodeByName("View1")
camera1 = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode1)
camera1.SetParallelProjection(0)
camera1.SetParallelProjection(1)
</code></pre>

---

## Post #2 by @lassoan (2024-12-06 22:14 UTC)

<p><del>Camera parameters must be changed at MRML level (in the camera node). If you modify anything directly at lower level in VTK then the change will not be effective and will be undone when the camera node is modified. If this is not described in the camera node documentation then it would be great if you could submit a pull request that adds it. Thank you!</del></p>
<p>I’ve had another look and that you used the camera node method, so the update should work well. I’ll debug this.</p>

---
