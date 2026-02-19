---
topic_id: 18746
title: "How To Change Branch Centerline"
date: 2021-07-15
url: https://discourse.slicer.org/t/18746
---

# How to change branch centerline

**Topic ID**: 18746
**Date**: 2021-07-15
**URL**: https://discourse.slicer.org/t/how-to-change-branch-centerline/18746

---

## Post #1 by @junqiangchen (2021-07-15 10:25 UTC)

<p>hi,i have extract the centerline,but i find centerline bifurcation is not right.just like this,i want modify centerline bifurcation from fig 1 to fig2,is there any function can achieve?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d55c19067784cd5aec4ae4d6297e1032733a64.png" data-download-href="/uploads/short-url/jFkx95tEMwzFrnz0krMpfhhUras.png?dl=1" title="分叉1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d55c19067784cd5aec4ae4d6297e1032733a64_2_602x499.png" alt="分叉1" data-base62-sha1="jFkx95tEMwzFrnz0krMpfhhUras" width="602" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d55c19067784cd5aec4ae4d6297e1032733a64_2_602x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d55c19067784cd5aec4ae4d6297e1032733a64.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d55c19067784cd5aec4ae4d6297e1032733a64.png 2x" data-dominant-color="5D6274"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">分叉1</span><span class="informations">860×714 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e4ee9b1897cab2ecda627dfd061cac56aa318c.png" data-download-href="/uploads/short-url/hftMqCcXY3VdNYHwc15ByXAHkny.png?dl=1" title="分叉2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78e4ee9b1897cab2ecda627dfd061cac56aa318c_2_602x499.png" alt="分叉2" data-base62-sha1="hftMqCcXY3VdNYHwc15ByXAHkny" width="602" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78e4ee9b1897cab2ecda627dfd061cac56aa318c_2_602x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e4ee9b1897cab2ecda627dfd061cac56aa318c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e4ee9b1897cab2ecda627dfd061cac56aa318c.png 2x" data-dominant-color="5E6174"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">分叉2</span><span class="informations">860×714 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-16 22:14 UTC)

<p>The top image is the realistic anatomical centerline (can be obtained using centerline extraction filter). The bottom is geometric centerline (can be obtained using network extraction filter).</p>

---

## Post #3 by @junqiangchen (2021-07-20 06:53 UTC)

<p>thank you for explain the difference between anatomical centerline and geometric centerline.</p>

---

## Post #4 by @lassoan (2021-07-20 12:55 UTC)

<p>Geometric centerline is just a plain skeletonization that returns points that are at equal distance from surface points.</p>
<p>Anatomical centerline provides realistic centerline shape at bifurcations, taking into account flow direction and radius.</p>
<p>You can find details in thesis and papers of Luca Antiga.</p>

---

## Post #5 by @junqiangchen (2021-07-21 04:06 UTC)

<p>thank you lasso,i will read more details between those centerlines</p>

---

## Post #6 by @Wei_Wu (2023-04-18 17:50 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I am a new user of 3D slicer and I love this code very much!<br>
I am using slicer to create centerlines of coronary bifurcation. Now my problem is I can just get the centerlines like figure2, in no way I can get centerlines like figure1, even I tried network or centerline model. That is because of the code updates?<br>
Thank you so much!</p>

---

## Post #7 by @Wei_Wu (2023-04-18 17:55 UTC)

<p>Hi <a class="mention" href="/u/junqiangchen">@junqiangchen</a>, which slicer version were you using to create the centerlines like figure1? Now I can’t create centerline like figure1 but only figures2 using the lastest version.<br>
Thanks!</p>

---
