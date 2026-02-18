# STL files overlapping

**Topic ID**: 41653
**Date**: 2025-02-12
**URL**: https://discourse.slicer.org/t/stl-files-overlapping/41653

---

## Post #1 by @Swarna_Yerebairapura (2025-02-12 17:04 UTC)

<p>Hi,<br>
I am unable to overlap two STL files of mandibular canal despite of using Transform module. Is there any alternative feature?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1c4603accd9121b4838b813dd7cb36bb8328c0d.png" data-download-href="/uploads/short-url/yuLNPNtBGhYYCWrbuQ88ndoBeqh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1c4603accd9121b4838b813dd7cb36bb8328c0d_2_690x272.png" alt="image" data-base62-sha1="yuLNPNtBGhYYCWrbuQ88ndoBeqh" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1c4603accd9121b4838b813dd7cb36bb8328c0d_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1c4603accd9121b4838b813dd7cb36bb8328c0d_2_1035x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1c4603accd9121b4838b813dd7cb36bb8328c0d_2_1380x544.png 2x" data-dominant-color="C0C2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1899×749 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Please advise.</p>

---

## Post #2 by @lassoan (2025-02-13 04:10 UTC)

<p>You can use a recent version of Slicer that allows you to adjust the center of rotation in 3D. That should make the alignment much easier.</p>
<aside class="quote quote-modified" data-post="1" data-topic="36974">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">New feature: Interactive transformation + adjustable center of rotation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Any nodes can now be translated, rotated, or scaled by interactive handles.  Editing operations can be constrained to specific axes and center of rotation can be freely chosen. The handles are available both in slice and 3D views. 
Transform nodes can be easily added and visualized for any node in 3D Slicer by right-clicking on the node in the Subject hierarchy visibility column and checking “Interaction”. 

  <a href="https://www.youtube.com/watch?v=ielxgJS-6SI" target="_blank" class="video-thumbnail" rel="noopener">
    [Transform Interaction Handles in 3D Slicer]
  </a>


<a name="visualization-options-1" class="anchor" href="#visualization-options-1"></a>Visualization options
Visualiza…
  </blockquote>
</aside>

<p>Alternatively, you can use landmark registration or various model registration methods. See details on the <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration</a> page.</p>

---
