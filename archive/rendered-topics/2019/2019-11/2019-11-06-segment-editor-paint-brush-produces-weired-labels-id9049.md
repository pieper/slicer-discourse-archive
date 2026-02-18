# Segment Editor paint brush produces weired labels

**Topic ID**: 9049
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/segment-editor-paint-brush-produces-weired-labels/9049

---

## Post #1 by @Dmitriy_Desser (2019-11-06 19:47 UTC)

<p>Hi guys,</p>
<p>I am doing some segmentation on MRI data (nii.gz) I am trying to label a very small stucture. After zooming in and trying to paint with the smalles size of the brush it produces a very strange square labels.</p>
<p>Here is a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c88b2b6d102d9310056c1ea85040f9f14b590afa.jpeg" data-download-href="/uploads/short-url/sC5F958ICsLxFXAWsLgVEbfZCxY.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c88b2b6d102d9310056c1ea85040f9f14b590afa_2_623x500.jpeg" alt="PNG" data-base62-sha1="sC5F958ICsLxFXAWsLgVEbfZCxY" width="623" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c88b2b6d102d9310056c1ea85040f9f14b590afa_2_623x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c88b2b6d102d9310056c1ea85040f9f14b590afa_2_934x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c88b2b6d102d9310056c1ea85040f9f14b590afa_2_1246x1000.jpeg 2x" data-dominant-color="A6A7A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1276×1023 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you maybe have an idea what could be the reason for this problem?<br>
(3dslicer version: 4.10.1 r27931, Windows 7 Professional)</p>
<p>ITK SNAP is working fine on the same image…</p>
<p>Best,</p>
<p>Dima</p>

---

## Post #2 by @pieper (2019-11-06 21:19 UTC)

<p>Maybe you need to rotate, as discussed in this post:</p><aside class="quote quote-modified" data-post="3" data-topic="9041">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problem-uploading-mri-ima-files-correctly/9041/3">Problem uploading MRI (IMA files) correctly </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Also it looks like your images were acquired obliquely, so you may want to rotate the view to volume plane. 
[image]
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-11-06 23:27 UTC)

<p>If you switch to the latest stable release of Slicer (currently 4.10.2) then you’ll get a warning icon displayed when the slice view is not aligned with any of the volume axes. You can align slice views by clicking that icon:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82277b318bc980ebf0ca92eb1340eb033d8011ae.png" alt="image" data-base62-sha1="izoESjOLcVCDysjL8Ul3sjoLDZA" width="643" height="387"></p>

---
