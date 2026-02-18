# How to segment the brain with midsagittal plane to two parts? EMSegmenter modul is missing

**Topic ID**: 17394
**Date**: 2021-04-30
**URL**: https://discourse.slicer.org/t/how-to-segment-the-brain-with-midsagittal-plane-to-two-parts-emsegmenter-modul-is-missing/17394

---

## Post #1 by @bencenemeth (2021-04-30 14:27 UTC)

<p>Operating system: Ubuntu Linux 18.04<br>
Slicer version: 4.11.<br>
Expected behavior: EMSegmenter<br>
Actual behavior: EMSegmenter missing</p>
<p>I want to segment bad quality MR perfusion maps with coregistration the Freesurfer t1 masks on it.<br>
Additionaly, I need the equation of the midsagittal plane - between the two hemispheres for my calculations.</p>
<p>EMSegmenter cannot be found in the modul browser of Slicer 4.11. Is that obsolete? Or can it be somehow installed and access the left and right hemisphere mask? Do you have any other suggestion to get the midsagittal plane? ( I am planning to implement convex_hull for hemispheres then 3D support vector maschine for the medial borders).</p>

---

## Post #2 by @pieper (2021-04-30 17:48 UTC)

<p>Unfortunately the EMSegmenter is no longer maintained and there’s not a logical replacement for it at present.</p>
<p>If you need to manually place the plane, the new plane markup option in the nightly preview builds of Slicer might work.</p>
<p>I believe currently we only have the AC/PC alignment option.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html</a></p>

---

## Post #3 by @lassoan (2021-04-30 22:59 UTC)

<p>ACPC module computes the midsagittal plane. Specify midsagittal points in the “Midline” input and compute the transform. First column of the transformation matrix is the plane normal, last column is the position.</p>

---
