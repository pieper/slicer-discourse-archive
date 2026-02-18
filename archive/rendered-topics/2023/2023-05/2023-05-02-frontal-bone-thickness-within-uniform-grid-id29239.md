# Frontal bone thickness within uniform grid

**Topic ID**: 29239
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/frontal-bone-thickness-within-uniform-grid/29239

---

## Post #1 by @damiazlkflee (2023-05-02 07:41 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.1<br>
Expected behavior: Calculating thickness within each grid of a uniform grid.<br>
Actual behavior: None</p>
<p>Hi. I segmented a frontal bone. I want to put a uniform grid with 20 roi on the bone surface and calculate the thickness in each of 20 roi. then, I want to colour the grid to show the thickness distribution across the bone surface. Can I do that using 3D Slicer?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c43edd48fdb71df983bcd454e79d5cd8900097bf.png" alt="image" data-base62-sha1="s04gM0ocvMkOiijDCMHlrV4dUg7" width="390" height="219"></p>

---

## Post #2 by @lassoan (2023-05-10 04:42 UTC)

<p>You can use VMTK extension’s Extract centerline module for computing thickness, as it can compute not only a centerline but a medial surface and associated radius value.</p>
<p>You get the radius for the entire medial surface, you are not limited to some lower-resolution grid, but if you need these bins then you can compute statistics for each box: get the point position of each model point, determine which box it corresponds to, and add the radius value to that bin.</p>

---
