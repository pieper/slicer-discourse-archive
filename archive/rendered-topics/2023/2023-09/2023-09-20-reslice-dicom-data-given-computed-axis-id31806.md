# Reslice dicom data given computed axis

**Topic ID**: 31806
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/reslice-dicom-data-given-computed-axis/31806

---

## Post #1 by @winnfr (2023-09-20 15:42 UTC)

<p>Hello,</p>
<p>I think this question has been asked many times but I can’t find a post answering it.<br>
Here’s my workflow:</p>
<ul>
<li>I use slicer to segment an organ from CT Scan</li>
<li>then export the STL</li>
<li>this STL is processed by a programm of mine. It gives me 3 vectors as usual reference frame to display this organ.</li>
</ul>
<p>Here I don’t know what to do. The slices of the CT scan are not perpendicular to the computed frame.<br>
I’d like to resample, rotate and translate the initial CT scan or compute a new CT Scan so that the slice are perpendicular of my frame.<br>
What module can I use to archieve that?<br>
Thanks</p>

---

## Post #2 by @pieper (2023-09-20 20:53 UTC)

<p>If you know these vectors you can create a matrix to transform the CT and the segmentation for display.  If you want you can resample the data <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html">through this transform</a>.</p>

---

## Post #3 by @winnfr (2023-09-21 13:01 UTC)

<p>thanks for your reply.<br>
It’s seems to be what I’m looking for but is there another tutorial or explanation how to use it. I’m bit lost…</p>

---
