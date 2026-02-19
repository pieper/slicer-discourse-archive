---
topic_id: 28804
title: "How Can I Fill A Hollow Area Present In A Femur Head"
date: 2023-04-07
url: https://discourse.slicer.org/t/28804
---

# How can I fill a hollow area present in a femur head?

**Topic ID**: 28804
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/how-can-i-fill-a-hollow-area-present-in-a-femur-head/28804

---

## Post #1 by @JESUS (2023-04-07 22:08 UTC)

<p>Hello my name is Jesus, I am doing a project in which I must do a 3D modeling, using DCOM images. But I have a small problem, some areas present in the head of the femur are not completely filled, and I do not know what I could do to fill that area. Attached image of how I have the model for now<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54569c4fe5aaedccfc5f2cd2a4518de188191d8a.jpeg" data-download-href="/uploads/short-url/c25FwWmaYR4Kvp9zHTESBLKy6Ce.jpeg?dl=1" title="2023-04-07-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54569c4fe5aaedccfc5f2cd2a4518de188191d8a_2_690x452.jpeg" alt="2023-04-07-Scene" data-base62-sha1="c25FwWmaYR4Kvp9zHTESBLKy6Ce" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54569c4fe5aaedccfc5f2cd2a4518de188191d8a_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54569c4fe5aaedccfc5f2cd2a4518de188191d8a_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54569c4fe5aaedccfc5f2cd2a4518de188191d8a.jpeg 2x" data-dominant-color="797B75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-07-Scene</span><span class="informations">1355×889 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-07 22:09 UTC)

<p>This is very typical for femur CT images and the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSoldify extension</a> is developed for solving this.</p>

---
