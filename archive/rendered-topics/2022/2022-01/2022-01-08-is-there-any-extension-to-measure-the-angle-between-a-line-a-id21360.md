---
topic_id: 21360
title: "Is There Any Extension To Measure The Angle Between A Line A"
date: 2022-01-08
url: https://discourse.slicer.org/t/21360
---

# Is there any extension to measure the angle between a line and a planes directly?

**Topic ID**: 21360
**Date**: 2022-01-08
**URL**: https://discourse.slicer.org/t/is-there-any-extension-to-measure-the-angle-between-a-line-and-a-planes-directly/21360

---

## Post #1 by @zHOU (2022-01-08 16:31 UTC)

<p>Operating system: Mac os<br>
Slicer version: 4.11<br>
Expected behavior: I want to measure the angle between a line and a plane in 3D model<br>
Actual behavior: I have used similar extensions like “Angle planes” or " Q3DC", but none of them solve my problem……<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8fd52c6c224408d4c67d688f06dc22dad9133e2.png" data-download-href="/uploads/short-url/xf7vZ9pZffsXJJ08jYcvWK7rKue.png?dl=1" title="WX20220108-020832@2x" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fd52c6c224408d4c67d688f06dc22dad9133e2_2_690x354.png" alt="WX20220108-020832@2x" data-base62-sha1="xf7vZ9pZffsXJJ08jYcvWK7rKue" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fd52c6c224408d4c67d688f06dc22dad9133e2_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fd52c6c224408d4c67d688f06dc22dad9133e2_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fd52c6c224408d4c67d688f06dc22dad9133e2_2_1380x708.png 2x" data-dominant-color="7A7DA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WX20220108-020832@2x</span><span class="informations">3974×2044 452 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-03-13 05:20 UTC)

<p>There is no extension, but you can compute this with a few lines of Python code (for example: get the normal of the plane and the line and compute the angle between them). There are a number of very similar examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-lines">script repository</a>.</p>

---

## Post #3 by @anasmh101 (2024-11-21 02:45 UTC)

<p>Hello, I tried my best to modify the lines of python code in order to compute angle between plane and a line, but it was not successful, my goal is to calculate the angle between plane established by “mark up module” and a line, but the line is established by identifying two landmark points, without drawing the line by " mark up module", is this possible ? Could you please help me in this matter</p>

---
