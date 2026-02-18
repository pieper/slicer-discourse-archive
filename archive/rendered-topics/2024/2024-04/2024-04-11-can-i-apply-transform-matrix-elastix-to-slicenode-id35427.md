# Can I apply transform matrix(Elastix) to slicenode?

**Topic ID**: 35427
**Date**: 2024-04-11
**URL**: https://discourse.slicer.org/t/can-i-apply-transform-matrix-elastix-to-slicenode/35427

---

## Post #1 by @matrosica0808 (2024-04-11 07:31 UTC)

<p>Instead of applying the Transform matrix to the Volume, I want to apply it to the SliceNode.</p>
<p>There is a problem with image warping when applied to Volume.<br>
I want to apply it to the slicenode of the axial coronal and sagittal view.</p>

---

## Post #2 by @lassoan (2024-04-11 15:21 UTC)

<p>The transform is actually already applied to the slice plane (we don’t actually transform the entire volume to display a slice of it).</p>

---
