---
topic_id: 16696
title: "Display Of Two Dimensional Image In Ras Space Under Transfor"
date: 2021-03-22
url: https://discourse.slicer.org/t/16696
---

# Display of two-dimensional image in RAS space under transform matrix

**Topic ID**: 16696
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/display-of-two-dimensional-image-in-ras-space-under-transform-matrix/16696

---

## Post #1 by @Natsu-666 (2021-03-22 15:02 UTC)

<p>Operating system:Win10<br>
Slicer version:4.11.20200930<br>
Hi！I want to translate and rotate the two-dimensional  image which under a transform matrix in RAS space,just like other model.But in fact as show in the figure.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50265a7cbea13b7038781b58b6197c6a4839761c.png" data-download-href="/uploads/short-url/br2mUzXxS2Ptm5vKV3jrTyQAoHO.png?dl=1" title="微信截图_20210322171920" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50265a7cbea13b7038781b58b6197c6a4839761c_2_690x347.png" alt="微信截图_20210322171920" data-base62-sha1="br2mUzXxS2Ptm5vKV3jrTyQAoHO" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50265a7cbea13b7038781b58b6197c6a4839761c_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50265a7cbea13b7038781b58b6197c6a4839761c_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50265a7cbea13b7038781b58b6197c6a4839761c.png 2x" data-dominant-color="1E1F20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信截图_20210322171920</span><span class="informations">1361×685 39.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The image can no display like that<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ccef504d877a65d68e174f8bc3997e8869b0a0.png" data-download-href="/uploads/short-url/lNJE4vhMNWs8uqjCzFzik2wQFMY.png?dl=1" title="123" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ccef504d877a65d68e174f8bc3997e8869b0a0_2_690x413.png" alt="123" data-base62-sha1="lNJE4vhMNWs8uqjCzFzik2wQFMY" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ccef504d877a65d68e174f8bc3997e8869b0a0_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ccef504d877a65d68e174f8bc3997e8869b0a0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ccef504d877a65d68e174f8bc3997e8869b0a0.png 2x" data-dominant-color="8B92BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">123</span><span class="informations">887×531 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to know how to do?Thanks!</p>

---

## Post #2 by @lassoan (2021-03-23 05:51 UTC)

<p>You did it right, but probably you want to move the slice view along with the image slice. You can use “Volume reslice driver” module for this (in SlicerIGT extension).</p>

---
