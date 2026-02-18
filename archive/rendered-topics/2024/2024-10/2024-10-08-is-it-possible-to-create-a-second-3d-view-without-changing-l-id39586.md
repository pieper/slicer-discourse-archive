# Is it possible to create a second 3D view without changing layout?

**Topic ID**: 39586
**Date**: 2024-10-08
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-second-3d-view-without-changing-layout/39586

---

## Post #1 by @mau_igna_06 (2024-10-08 17:37 UTC)

<p>Hi, <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/ee133884bc126d4d593612bd90211fe2e3165625/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L155-L179" rel="noopener nofollow ugc">my custom layout</a> has 2 threeDViews.</p>
<p>This layout is available in the layout menu after Slicer starts up but, apparently, I cannot access the second threeDView until the custom layout has not been set once.<br>
This is a problem because I want to automatically create some nodes that should only be visible in the 2nd threeDView and I can’t because an error tells me the 2nd threeDView is <code>NoneType</code></p>
<p>Hope you can help</p>

---

## Post #2 by @lassoan (2024-10-08 22:34 UTC)

<p>You can set the view node IDs in the display node before those views are created.</p>

---
