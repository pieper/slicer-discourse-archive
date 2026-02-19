---
topic_id: 10278
title: "Apply Transformation"
date: 2020-02-15
url: https://discourse.slicer.org/t/10278
---

# Apply transformation

**Topic ID**: 10278
**Date**: 2020-02-15
**URL**: https://discourse.slicer.org/t/apply-transformation/10278

---

## Post #1 by @Adam1122 (2020-02-15 16:10 UTC)

<p>Hello all,</p>
<p>I want to apply the saved transformation (a transformation matrix 4x4 acquired by registration of an anatomical and a diffusion image) on my input anatomical mask and change a final FOV by specifying a diffusion reference image (its voxels size). It means to apply the same command as the command ApplyXFM in FSL FLIRT. Does this option exist also in 3D Slicer?</p>
<p>Thanks a lot<br>
Regards<br>
Adam</p>

---

## Post #2 by @timeanddoctor (2020-02-16 04:19 UTC)

<p>yes, see an example</p><aside class="quote" data-post="1" data-topic="6964">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-i-read-and-modify-a-transform-matrix-with-python/6964">Can I read and modify a transform matrix with python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    can I read and modify a transform matrix with python directly(not the GUI of transform) in slicer. 
for example: 
Read 
display (transformMatrix) 
I will get a 4*4matrix: 
[ [  1  0  0  52.64097] 
[ 0  1 0 -46.12696] 
[ 0   0   1  -0.48185] 
[  0.   0.   0.  1.  ]] 
Modify 
transformMatrix=np.array[ 
[  0.92979  -0.26946  -0.25075  52.64097] 
[  0.03835   0.74845  -0.66209 -46.12696] 
[  0.36608   0.60599   0.70623  -0.48185] 
[  0.        0.        0.        1.     ]]
  </blockquote>
</aside>


---

## Post #3 by @manjula (2020-02-16 09:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/creates-cylinder-in-center-of-a-segment-for-volume-calculation/10194/4">Creates Cylinder in Center of a segment for volume calculation</a></div>
<blockquote>
<p>You can find examples of how to set transforms in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" rel="noopener nofollow ugc">Transforms module documentation </a> and in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">script repository</a>.</p>
</blockquote>
</aside>
<p>I had the similar problem and this was Prof Lasso solution.</p>

---

## Post #4 by @Adam1122 (2020-02-16 10:56 UTC)

<p>Yes, it´s working. Thanks a lot for your advice.</p>

---
