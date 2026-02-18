# Reset Slice view after Maximum intensity projection or Thick slab reconstruction

**Topic ID**: 15224
**Date**: 2020-12-25
**URL**: https://discourse.slicer.org/t/reset-slice-view-after-maximum-intensity-projection-or-thick-slab-reconstruction/15224

---

## Post #1 by @manjula (2020-12-25 13:12 UTC)

<p>is there a way to reset the slice view back without restarting after using MIP or thick slab reconstruction?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d4f07387807a2ec27f024acc8831d4c95b2a29.jpeg" alt="image_00031" data-base62-sha1="tWg0IyjSiGMsX5fAinYdMkdjbIt" width="482" height="400"></p>
<p>After this I am restarting Slicer if i need to change the projecton. Is there a way to reset to previous state ? Closing the scene does not correct/reset it.</p>

---

## Post #2 by @lassoan (2020-12-25 19:50 UTC)

<p>You can set SlabNumberOfSlices back to 1.</p>
<p>For reference, <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections">here</a> is the code for setting number of slices in a slab.</p>

---
