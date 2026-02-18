# How to display the OBB of a nrrd file in 3d slicer?

**Topic ID**: 37891
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/how-to-display-the-obb-of-a-nrrd-file-in-3d-slicer/37891

---

## Post #1 by @hk_y (2024-08-14 16:08 UTC)

<p>Operating system: mac<br>
Slicer version: 5.2.1<br>
Expected behavior: I have an NRRD file and I can calculate its OBB and RAS diameter using Segment Statistics, but I want to display its bounding box. How can I do that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d450f57d1791e9dc47fdf604a1d6b0c8516a06ef.png" data-download-href="/uploads/short-url/uieG0aGB7nJpTjWb9isiyNHsguX.png?dl=1" title="截屏2024-08-15 上午12.11.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d450f57d1791e9dc47fdf604a1d6b0c8516a06ef_2_574x500.png" alt="截屏2024-08-15 上午12.11.29" data-base62-sha1="uieG0aGB7nJpTjWb9isiyNHsguX" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d450f57d1791e9dc47fdf604a1d6b0c8516a06ef_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d450f57d1791e9dc47fdf604a1d6b0c8516a06ef_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d450f57d1791e9dc47fdf604a1d6b0c8516a06ef.png 2x" data-dominant-color="E5E5F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2024-08-15 上午12.11.29</span><span class="informations">928×808 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-08-15 09:44 UTC)

<p>See code snippet that you can copy-paste into the Slicer Python console in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">script repository</a>.</p>

---

## Post #3 by @hk_y (2024-08-15 13:07 UTC)

<p>Thank you so much！ Can you give me the code snippet that could display the AABB (axis-aligned bounding box) of the label. Thanks.</p>

---

## Post #4 by @lassoan (2024-08-15 13:27 UTC)

<p>The topic of getting axis-aligned bounding boxes is discussed here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="27795">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caetox/48/17513_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/get-axis-aligned-bounding-boxes-for-segments/27795">Get axis-aligned bounding boxes for segments</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I created a segmentation with some segments and want to get an axis-aligned bounding box for each segment. As far as i know, with the segment statistics module we can compute oriented bounding boxes, but i couldn’t find an option to get axis-aligned bounding boxes. I tried to get the segments as numpy arrays and use numpy functions to find the required values as suggested <a href="https://discourse.slicer.org/t/python-script-to-get-axis-aligned-bounding-box/26227/5">here</a>. But since i rotated the segments before, the segments do not match with the original scalar volume anymore. Do I need t…
  </blockquote>
</aside>


---
