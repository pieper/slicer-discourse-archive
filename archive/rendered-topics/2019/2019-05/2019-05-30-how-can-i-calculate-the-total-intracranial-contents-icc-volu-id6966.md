---
topic_id: 6966
title: "How Can I Calculate The Total Intracranial Contents Icc Volu"
date: 2019-05-30
url: https://discourse.slicer.org/t/6966
---

# How can I calculate the total intracranial contents (ICC) volume using 3D slicer modules?

**Topic ID**: 6966
**Date**: 2019-05-30
**URL**: https://discourse.slicer.org/t/how-can-i-calculate-the-total-intracranial-contents-icc-volume-using-3d-slicer-modules/6966

---

## Post #1 by @otanit (2019-05-30 03:31 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.10.1<br>
Expected behavior: Caluculate the total intracranial contents (ICC) volume using 3D slicer modules.<br>
Actual behavior: I can’t calculate it in 3D slicer.</p>
<p>I would like to know how to calculate the ICC volume using 3D slicer modules.<br>
I could  calculate it in 3D slicer version 2.6.<br>
However, I can’t find the module for calculating ICC volume after version 3.<br>
I appreciate any advice for it.</p>

---

## Post #2 by @pieper (2019-05-30 15:49 UTC)

<p>Do you remember what tool you used in slicer2?</p>

---

## Post #3 by @muratmaga (2019-05-30 16:24 UTC)

<p>Is ICC volume same as ICV (intracranial volume)? If it is, I think osteotomy planner does it from a segmented skull.</p>

---

## Post #4 by @lassoan (2019-05-30 17:57 UTC)

<p>In general, you segment object of interests using Segment Editor module, then compute their volume using Segment Statistics module.</p>

---

## Post #5 by @otanit (2019-06-01 01:36 UTC)

<p>I 'm sorry, I can’t recall the module.</p>

---

## Post #6 by @otanit (2019-06-01 01:48 UTC)

<p>The segmented voxel volumes of gray and white matter and cerebrospinal fluid were summed to yield the total intracranial contents (ICC).<br>
I can measure ROI volumes using Segment Editor and Segment Statistics modules.<br>
However, I think I may have to use other module or icons in order to calculate the ICC volume.<br>
I could calculate the ICC volumes when I use Slicer 2.6, but I have already updated the Slicer version, and now I can’t use Slicer 2.6.<br>
I would like to know how to calculate ICC in Slicer 4.10.1.<br>
I appreciate your time and kind advice.</p>

---

## Post #7 by @rkikinis (2019-06-01 07:56 UTC)

<p>Hi,</p>
<p>If you have a segmentation of GM, WM and CSF, then you can use segment statistics to get the individual volumes and add them up.</p>
<p>One other solution would be to use the Swiss skull stripper extension to define the ICC.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper</a></p>
<p>Note that you have to install some data (as described in the manual above) before running the module.</p>
<p>Best<br>
Ron</p>

---

## Post #8 by @otanit (2019-06-01 14:55 UTC)

<p>Dear Ron,</p>
<p>I appreciate your kind advice.<br>
I will use Swiss Skull Stripper following the manual you informed me.<br>
Thanks a lot.</p>
<p>Best<br>
Toshiyuki</p>

---
