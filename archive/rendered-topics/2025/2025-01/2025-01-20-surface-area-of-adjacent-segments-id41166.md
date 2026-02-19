---
topic_id: 41166
title: "Surface Area Of Adjacent Segments"
date: 2025-01-20
url: https://discourse.slicer.org/t/41166
---

# Surface area of adjacent segments

**Topic ID**: 41166
**Date**: 2025-01-20
**URL**: https://discourse.slicer.org/t/surface-area-of-adjacent-segments/41166

---

## Post #1 by @amreen_spsingh (2025-01-20 14:03 UTC)

<p>I am currently working on paranasal sinuses which may be filled with polypoidal mucosa in the diseased state. So I have created two separate segmentations inside the sinuses… One containing air (green) and the other containing the polypoidal tissue(yellow). I want the total surface area of the sinus… When I apply segment statistics, the output gives the surface area of the two segments. How do I remove the common surface area shared by the two segments ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f6971adb24d3a8a8b7ed1515df6b1ed202f8d55.jpeg" data-download-href="/uploads/short-url/2cl4DWfgb8FHYBlosUtJlUl2etn.jpeg?dl=1" title="1000169901" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f6971adb24d3a8a8b7ed1515df6b1ed202f8d55_2_375x500.jpeg" alt="1000169901" data-base62-sha1="2cl4DWfgb8FHYBlosUtJlUl2etn" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f6971adb24d3a8a8b7ed1515df6b1ed202f8d55_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f6971adb24d3a8a8b7ed1515df6b1ed202f8d55_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f6971adb24d3a8a8b7ed1515df6b1ed202f8d55_2_750x1000.jpeg 2x" data-dominant-color="707895"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000169901</span><span class="informations">1920×2560 419 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-01-20 14:04 UTC)

<p>You can get the outer surface area of multiple segments by combining them into one segment.</p>

---
