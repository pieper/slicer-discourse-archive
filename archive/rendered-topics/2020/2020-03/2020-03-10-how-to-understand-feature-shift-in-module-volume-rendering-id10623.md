---
topic_id: 10623
title: "How To Understand Feature Shift In Module Volume Rendering"
date: 2020-03-10
url: https://discourse.slicer.org/t/10623
---

# How to understand feature "Shift" in module "Volume Rendering"?

**Topic ID**: 10623
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/how-to-understand-feature-shift-in-module-volume-rendering/10623

---

## Post #1 by @Illusion (2020-03-10 20:05 UTC)

<p>Hello,</p>
<p>There are two questions that I was not able to figure out. Please help me. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<ol>
<li>I was trying to get the 3D coords of the skin-surface of the back surface from a vertebral MR, to get the posterior-anterior axis given the inferior-superior axis and left-right axis.</li>
</ol>
<p>Is there a module to help do that?</p>
<ol start="2">
<li>When showing the volume rendering, the feature “Shift” (as shown in the screenshot below) changed the valid volume.  How should I understand the disappeared volume when Shift is enlarged? And how the extra pure-black volume was added when Shift is reduced?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef89238a0acce95f5b184b615da408a696031f97.jpeg" data-download-href="/uploads/short-url/yb1VUlW1MW4J8UEhCqAS21XALVt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef89238a0acce95f5b184b615da408a696031f97_2_690x430.jpeg" alt="image" data-base62-sha1="yb1VUlW1MW4J8UEhCqAS21XALVt" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef89238a0acce95f5b184b615da408a696031f97_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef89238a0acce95f5b184b615da408a696031f97_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef89238a0acce95f5b184b615da408a696031f97_2_1380x860.jpeg 2x" data-dominant-color="ADADC9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1549×966 386 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20cf1b168de42c6d737937482c4ad4eea7777264.jpeg" data-download-href="/uploads/short-url/4Gf04ESaLJ7dShEPP30Z8OtK56Y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20cf1b168de42c6d737937482c4ad4eea7777264_2_690x412.jpeg" alt="image" data-base62-sha1="4Gf04ESaLJ7dShEPP30Z8OtK56Y" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20cf1b168de42c6d737937482c4ad4eea7777264_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20cf1b168de42c6d737937482c4ad4eea7777264_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20cf1b168de42c6d737937482c4ad4eea7777264_2_1380x824.jpeg 2x" data-dominant-color="9A9AAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1501×898 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-03-11 12:42 UTC)

<p>It is equivalent with adding/subtracting a constant to voxel values.</p>
<p>What it actually does it shifts volume rendering transfer functions, which you can find in the “Advanced” section.</p>

---

## Post #3 by @Illusion (2020-03-11 19:52 UTC)

<p>Hi Iassoan,</p>
<p>Thank you for your reply!<br>
It seems that the “Advanced” section is kind of advanced for me. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>Could you please post some link or tutorial, or even source code about how the feature “Shift” is applied on voxel processing mathematically?</p>
<p>Thank you in advance!</p>

---

## Post #4 by @lassoan (2020-03-12 22:24 UTC)

<p>Shift is equivalent to adding/subtracting a constant value from the voxel values. You can read more about volume rendering in the <a href="https://vtk.org/vtk-textbook/">VTK Textbook</a>.</p>

---
