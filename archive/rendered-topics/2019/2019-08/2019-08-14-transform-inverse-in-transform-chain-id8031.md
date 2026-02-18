# Transform inverse in transform chain

**Topic ID**: 8031
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/transform-inverse-in-transform-chain/8031

---

## Post #1 by @adamrankin (2019-08-14 18:45 UTC)

<p>Hello all,</p>
<p>I am streaming transforms via IGTLink, so the transforms are changing in real-time. I am wondering if it’s possible to parent a transform by another transform, but inverted?</p>
<p>Adam</p>
<p>Edit: using the transform module GUI, I know it can be done in code manually</p>

---

## Post #2 by @lassoan (2019-08-14 19:34 UTC)

<p>There is a transform processor module in SlicerIGT extension that can do this (invert, concatenate, compute relative transforms, constrain rotations, etc.).</p>

---
