---
topic_id: 30152
title: "How To Create A Plane Which Is Parallel To Other Specific Pl"
date: 2023-06-20
url: https://discourse.slicer.org/t/30152
---

# How to create a plane which is parallel to other specific plane in Slicer 3D

**Topic ID**: 30152
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/how-to-create-a-plane-which-is-parallel-to-other-specific-plane-in-slicer-3d/30152

---

## Post #1 by @viet_duc_Vu (2023-06-20 15:16 UTC)

<p>I am wanting to create a plane which is parallel to other plane on the model. Do you know any function to do that in slicer3D<br>
Thanks</p>

---

## Post #2 by @lassoan (2023-06-20 15:17 UTC)

<p>In recent Slicer versions, if you place a plane on a model in the 3D view, the plane will be parallel to the surface at the chosen position.</p>

---

## Post #3 by @viet_duc_Vu (2023-07-01 13:09 UTC)

<p>Hi Iassoan. Thank you for your reply. What I mean is that in case I had a pointed plane on the model ( For example, Frankfort Horizontal Plane) and I am wanting to create a other plane which goes 2 specific points and be parallel to the previous pointed plane. How can do it on Slicer 3D<br>
Thank you</p>

---

## Post #4 by @lassoan (2023-07-02 11:59 UTC)

<p>In this case you can write a few lines of Python script to compute the new plane’s position and normal.</p>
<p>Note that it is mathematically impossible to make a plane that is already constrained by two points to be parallel with another plane (unless the line connecting the two points are already parallel with the other plane).</p>

---

## Post #5 by @viet_duc_Vu (2023-07-02 12:04 UTC)

<p>Thank you for your reply.<br>
I made a mistake in the previous comment: I need to create a plane which comes through a point and parallel to another plane.<br>
So could you please show me the script for that cause I am not familiar with Python<br>
Thank you</p>

---

## Post #6 by @lassoan (2023-07-02 12:44 UTC)

<p>In this case you can get the position of the point using <code>GetNthControlPointPositionWorld()</code> method and set as the plane position by calling <code>SetCenter()</code> method. See many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">script repository</a>.</p>

---

## Post #7 by @viet_duc_Vu (2023-07-02 12:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="30152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In this case you can write a few lines of Python script to compute the new plane’s position and normal.</p>
</blockquote>
</aside>
<p>Could you please take an example ?. I would highly appreciate.</p>

---

## Post #8 by @lassoan (2023-07-02 15:24 UTC)

<p>If you don’t find the examples in the script repository sufficient, then probably you need help with all the subsequent analysis steps. Could you describe your overall clinical goal and the complete analysis that you would like to perform?</p>

---

## Post #9 by @viet_duc_Vu (2023-07-03 13:52 UTC)

<p>My clinical goal is to define and form a plane that passes through the point Cor and be parallel to the existed plane formed by the 3 points as shown in the figure.<br>
Through building this plane I also need to find the intersection point of this plane with ramus model as shown in the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cf312481f203b590195f34d66b32e4f8063f6f0.jpeg" data-download-href="/uploads/short-url/1QyvtM4cXWfHBoQPX2AZc6EBfna.jpeg?dl=1" title="Ảnh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cf312481f203b590195f34d66b32e4f8063f6f0_2_643x499.jpeg" alt="Ảnh" data-base62-sha1="1QyvtM4cXWfHBoQPX2AZc6EBfna" width="643" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cf312481f203b590195f34d66b32e4f8063f6f0_2_643x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cf312481f203b590195f34d66b32e4f8063f6f0_2_964x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cf312481f203b590195f34d66b32e4f8063f6f0.jpeg 2x" data-dominant-color="134F47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ảnh</span><span class="informations">1159×901 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
