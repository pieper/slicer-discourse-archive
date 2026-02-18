# Spin 3D view in certain axis

**Topic ID**: 17536
**Date**: 2021-05-09
**URL**: https://discourse.slicer.org/t/spin-3d-view-in-certain-axis/17536

---

## Post #1 by @park (2021-05-09 18:20 UTC)

<p>Hi all</p>
<p>I would like to make some video which rotate the 3D view with certain axis</p>
<p>I know there is a module “Screen Capture” however this module only support<br>
Yaw and pitch direction rotation</p>
<p>Is there any way to make 3D view spin in certain vector direction (ex [0,0,1]) ?</p>
<p>Thank you<br>
TY Park</p>

---

## Post #2 by @lassoan (2021-05-09 19:55 UTC)

<p>Rotation in screen capture module specifies rotation axes relative to the current camera orientation. You can choose between the two meaningful rotation axes (vertical and horizontal - yaw and pitch). Roll would not be useful, as it would not reveal anything of the scene content (it would just rotate around the camera’s “up” vector).</p>
<p>You can make more complex camera animations by using Endoscopy module. You may also find <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator">Animator module</a> (in SlicerMorph extension) useful. For completely custom camera or node movements, you can apply a transform or node you want to move and adjust the transformation matrix in a Python script.</p>

---
