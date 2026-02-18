# Ignore nodes when placing fiducial?

**Topic ID**: 17014
**Date**: 2021-04-09
**URL**: https://discourse.slicer.org/t/ignore-nodes-when-placing-fiducial/17014

---

## Post #1 by @hherhold (2021-04-09 15:44 UTC)

<p>Normally when you interactively place a fiducial in the 3D view, the cursor/placement fiducial jumps to the intersection point closest to the camera of whatever is visible. For example, let’s say I have a body with a skeleton. I have a segment for the skin and a segment for the bones. If I turn the opacity down for the skin so I can see the bones, then I try to place a fiducial/markup point on the bones, it will jump to the skin as it’s the point nearest to the camera that’s visible.</p>
<p>Is it possible to force placement to a single segment only, such that it will ignore all other segments? That is, for the above example, can I force intersection tests to only be on the bones and ignore the skin?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-04-14 05:27 UTC)

<p>You cannot exclude individual segments from picking in 3D views, but you can exclude model nodes. After exporting your segmentation to model nodes (and hiding the segmentation) turn off <code>Selectable</code> property for the skin model by this command:</p>
<pre><code class="lang-python">getNode('skin').SetSelectable(False)
</code></pre>

---

## Post #3 by @hherhold (2021-04-14 11:04 UTC)

<p>Oh, excellent - that’s perfect.</p>
<p>Thanks!</p>

---
