# How to visualize 2d xray and 3d model overlapped

**Topic ID**: 13142
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/how-to-visualize-2d-xray-and-3d-model-overlapped/13142

---

## Post #1 by @Henry_Cope (2020-08-24 16:06 UTC)

<p>Hi all,<br>
Is it possible to visualize a 2D Xray in the same space as a 3D volume inside the 3D only viewer? I realize that from the start, it’s obvious that 2D will not appear in 3D. But is there any way to include it as a plane with depth 1 pixel or however many are need to be drawn in the 3D viewer? I’m trying to visually align blood vessels to see how good/bad the original CT volume segmentation is compared to a contrast injected XRay. Ideally, I could visualize the 2D XRay as the background and then rotate the 3D volume above it until it is aligned</p>

---

## Post #2 by @lassoan (2020-08-24 16:20 UTC)

<p>Yes, this is perfectly doable. Click the “eye” icon in <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controls</a> to show the slice in 3D.</p>
<p>It is up to you to set up the camera to match the X-ray projection. It is quite simple:</p>
<ul>
<li>camera position is the X-ray generator position</li>
<li>camera focal point is the image centerpoint position</li>
<li>camera up vector is one of the image axis</li>
<li>camera view angle is computed from source-to-image distance (distance between camera position and centerpoint) and image size</li>
</ul>

---

## Post #3 by @Henry_Cope (2020-08-24 16:21 UTC)

<p>Thank you Mr. Lasso, that did the trick</p>

---
