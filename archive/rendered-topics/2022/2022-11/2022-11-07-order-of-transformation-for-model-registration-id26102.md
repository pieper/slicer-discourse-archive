# Order of transformation for model registration

**Topic ID**: 26102
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/order-of-transformation-for-model-registration/26102

---

## Post #1 by @jegberink (2022-11-07 07:31 UTC)

<p>Hello everyone,</p>
<p>I cant seem to find a definitive answer on this. I’m using ALPACA through Slicermorph to register 2 models to eachother. My question is regarding the resulting transformation. Is there and order of translation and rotation ALPACA uses, or is this irrelevant?</p>
<p>Thank you kindly.</p>

---

## Post #2 by @jegberink (2022-11-08 10:08 UTC)

<p>To elaborate. within the single transformation that happens for alpaca, does it matter if the order is XYZ, or ZYX, or any other combination.</p>
<p>I know that with multiple transformation rotations the rotation order matters, but is this also within a single transformation like you get from model registration?</p>

---

## Post #3 by @lassoan (2022-12-01 07:48 UTC)

<p>Euler angles is a very poor representation of orientation (gimbal lock issue, many variants in axis ordering, no 1-to-1 mapping between angle values and orientation, etc.), therefore we avoid this parametrization.</p>
<p>Probably Alpaca uses a simple 4x4 homogeneous transformation matrix representation for 3D translation and rotation.</p>

---
