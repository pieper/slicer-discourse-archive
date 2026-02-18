# Is there a feature to make an entity that suits concave surfaces?

**Topic ID**: 30104
**Date**: 2023-06-18
**URL**: https://discourse.slicer.org/t/is-there-a-feature-to-make-an-entity-that-suits-concave-surfaces/30104

---

## Post #1 by @telomere (2023-06-18 14:32 UTC)

<p>Hello.<br>
After I load a keyhole model, I want to make a key that exactly suits the keyhole.<br>
Is there any feature for this?<br>
Select the inner surfaces of the keyhole and use “some features” and the result is the key.<br>
What would be “some feaures”?<br>
For an easier example, I want to invert?(or reverse?) the surface of a bowl and the result would be a dome-shaped material or a half-sphere material.</p>
<p>Any ideas? Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-06-18 14:35 UTC)

<p>You can create an inverse of a 3D shape (for example, to create a mold) using Segment Editor’s Logical operators effect.</p>
<p>If you have an internal holes then you can extract one or more using the Island effect. If the holes are not completely closed (leak into each other or the outer space) then you can use Wrap Solidify effect (provided by SurfaceWrapSolidify extension).</p>

---

## Post #3 by @mau_igna_06 (2023-06-18 20:47 UTC)

<p>Please explore the use of the CombineModels module in the Sandbox extension. Probably you need to use difference operation:</p>
<p>e.g.<br>
<code>CylinderModel - KeyholeModel = KeyModel</code></p>
<p>Hope it helps</p>

---
