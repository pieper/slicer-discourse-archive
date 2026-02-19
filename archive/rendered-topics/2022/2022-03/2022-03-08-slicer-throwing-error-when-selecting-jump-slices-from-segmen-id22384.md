---
topic_id: 22384
title: "Slicer Throwing Error When Selecting Jump Slices From Segmen"
date: 2022-03-08
url: https://discourse.slicer.org/t/22384
---

# Slicer throwing error when selecting jump slices from segment table view

**Topic ID**: 22384
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/slicer-throwing-error-when-selecting-jump-slices-from-segment-table-view/22384

---

## Post #1 by @Dwij_Mistry (2022-03-08 20:03 UTC)

<p>Slicer is throwing this error when selecting “Jump Slices” option from Segment editor widget → Segment list table → Right click on segment → select Jump slices.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3741859b664ee8a2249870a8e435e13ae574206.png" alt="erroe" data-base62-sha1="pBwcof9RgbFlHvs3pLA4LBCS4xE" width="690" height="298"></p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://b48QEHksFW86iP05RkQfsFzkeVF.mp4">
  </div><p></p>
<p>Slicer version: 4.13.0-2022-02-17<br>
Operating system: Windows 10</p>

---

## Post #2 by @lassoan (2022-03-11 20:35 UTC)

<p>Thanks for reporting, I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/86c9a550df82d42d3e6452daa3c5d94ca35b17bc">fix</a>, it’ll be available in the Slicer Preview Release from tomorrow.</p>

---
