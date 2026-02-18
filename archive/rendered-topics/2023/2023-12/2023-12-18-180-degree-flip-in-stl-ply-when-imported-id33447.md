# 180 degree Flip in STL/PLY when imported

**Topic ID**: 33447
**Date**: 2023-12-18
**URL**: https://discourse.slicer.org/t/180-degree-flip-in-stl-ply-when-imported/33447

---

## Post #1 by @Vignesh_Chakravarthy (2023-12-18 20:27 UTC)

<p>Hi,<br>
I am using Slicer 5.2.2. I have saved lesions and prostate from Ultrasound as landmarks in slicer. Then, imported landmarks into MATLAB for non-rigid registration. I converted them to ply/stl from pointcloud after transformation and when I imported them back to slicer it is flipped 180 degree.<br>
Please let me know how to avoid this angle flip.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ee22a8887cb986dbe989274618f80a300bc0e5.png" data-download-href="/uploads/short-url/yNUe8x6UQSEOCaGx5jyHXI8kp7L.png?dl=1" title="STL flip" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ee22a8887cb986dbe989274618f80a300bc0e5_2_384x500.png" alt="STL flip" data-base62-sha1="yNUe8x6UQSEOCaGx5jyHXI8kp7L" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ee22a8887cb986dbe989274618f80a300bc0e5_2_384x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ee22a8887cb986dbe989274618f80a300bc0e5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ee22a8887cb986dbe989274618f80a300bc0e5.png 2x" data-dominant-color="9293B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">STL flip</span><span class="informations">504×656 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Vignesh</p>

---

## Post #2 by @pieper (2023-12-18 22:30 UTC)

<p>You can search for LPS / RAS and will get lots of information about how to keep track of the relationship between images and meshes in different programs.</p>
<p>E.g. <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="inline-onebox">Coordinate systems — 3D Slicer documentation</a></p>

---

## Post #3 by @Vignesh_Chakravarthy (2023-12-19 18:33 UTC)

<p>Hi,</p>
<p>I used transform technique in Slicer (Inferior - Superior - 180 deg) to align the imported PLY files with the existing Ultrasound prostate model. Thanks for letting me know about the coordinate systems.</p>
<p>Best,<br>
Vignesh</p>

---
