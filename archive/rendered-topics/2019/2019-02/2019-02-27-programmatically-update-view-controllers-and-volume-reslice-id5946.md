# Programmatically update View Controllers and Volume Reslice Driver?

**Topic ID**: 5946
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/programmatically-update-view-controllers-and-volume-reslice-driver/5946

---

## Post #1 by @dsikka (2019-02-27 18:31 UTC)

<p>Hi,</p>
<p>Is there a way to programmatically update the axial view of the Red Slice (as we can do using the View Controllers module)? Also, is there a way to progammatically update the Driver and Mode of the Red Slicer as well (as we can do using the Volume Reslice Driver)?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-02-28 16:24 UTC)

<p>Yes, see these examples: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View</a></p>
<p>Also you can look at the corresponding code in the reslice driver, and it should be easily scriptable.</p>

---
