---
topic_id: 5775
title: "Mirroring In 3D Slicer"
date: 2019-02-14
url: https://discourse.slicer.org/t/5775
---

# Mirroring in 3D slicer

**Topic ID**: 5775
**Date**: 2019-02-14
**URL**: https://discourse.slicer.org/t/mirroring-in-3d-slicer/5775

---

## Post #1 by @ntinos (2019-02-14 05:06 UTC)

<p>Hello 3D slicer users!<br>
I am working on a university project and I need to mirror the right side of a skull on the midsagittal plane, so as to create a new skull from 2 right sides. Can this be done with 3D slicer or should I use a different software?</p>

---

## Post #2 by @muratmaga (2019-02-14 06:26 UTC)

<p>It takes a few steps but it is entirely doable. Using MRHead as an example</p>
<ol>
<li>Crop the volume along the midsagittal plane (Crop Volume)</li>
<li>Clone this volume (Data Module)</li>
<li>Use ConstantImagePad filter from SimpleFilters to pad both images to the original size dimensions (since cropped images now have roughly the half size) as two new volumes.</li>
<li>Create a new linear transform and change the sign of of the upper left corner from 1 to -1.</li>
<li>Apply this transform to one of the volumes created in step 3 and harden the transform. You should now have a mirrored whole head, but in two volumes</li>
<li>Use AddScalarVolume to a merge two volumes into one volume</li>
</ol>

---

## Post #3 by @ntinos (2019-02-16 04:59 UTC)

<p>Thanks a lot! Appreciate your help!</p>

---
