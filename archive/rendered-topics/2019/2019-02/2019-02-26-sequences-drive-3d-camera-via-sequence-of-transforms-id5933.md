# [Sequences] Drive 3D camera via sequence of transforms

**Topic ID**: 5933
**Date**: 2019-02-26
**URL**: https://discourse.slicer.org/t/sequences-drive-3d-camera-via-sequence-of-transforms/5933

---

## Post #1 by @adamrankin (2019-02-26 16:39 UTC)

<p>Is it currently possible to drive the 3D view camera by a sequence of transforms? I know you can record the camera and play it back, but I am unable to find a way to convert transforms to camera.</p>

---

## Post #2 by @lassoan (2019-02-26 16:56 UTC)

<p>Camera nodes are transformable nodes, so you can apply a transform to a camera for <strong>relative positioning</strong>.</p>
<p>You can use Viewpoint module (in SlicerIGT extension) for <strong>absolute camera positioning</strong>:</p>
<ul>
<li>bullseye view mode is for driving a camera using a transform (using position only, or also with 2/3 DOF orientation)</li>
<li>auto-center view mode adjust the camera automatically to keep a node in the field of view (even if that node is moved/transformed)</li>
</ul>

---
