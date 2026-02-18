# Resize 3d volume

**Topic ID**: 11767
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/resize-3d-volume/11767

---

## Post #1 by @1116 (2020-05-29 02:55 UTC)

<p>If i want to resize 3d volume 256 x 256 x 26  to  184 x 220 x 26 , is it right to use  Resample Sacalar/Vector/DWI Volume module?<br>
The Original volumes spacing is 1.25 x 1.25 x 4</p>
<p>The reason to resize 3d volume is that I’m going to extract the axial slices of volume to set of png file and use it for 2D CNN.</p>

---

## Post #2 by @pieper (2020-05-29 17:13 UTC)

<p>Yes, that should work.</p>

---

## Post #3 by @lassoan (2020-05-30 00:02 UTC)

<p>Note that your CNN uses numpy arrays as inputs, so there is no need to force your data into compressed 8-bit (or even worse, 24-bit) png images. Instead, you can get numpy array directly from your volume using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume"><code>slicer.util.arrayFromVolume</code></a> and save it to a npy file that you can directly use in your CNN.</p>

---
