---
topic_id: 1799
title: "Problem Loading Mri Scan Only One View Axial Is Clear The Ot"
date: 2018-01-09
url: https://discourse.slicer.org/t/1799
---

# Problem loading MRI scan. Only one view, axial, is clear, the other two are blurry

**Topic ID**: 1799
**Date**: 2018-01-09
**URL**: https://discourse.slicer.org/t/problem-loading-mri-scan-only-one-view-axial-is-clear-the-other-two-are-blurry/1799

---

## Post #1 by @olivya_caballero (2018-01-09 22:00 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.0<br>
Expected behavior: All three views are clear<br>
Actual behavior: Only axial is clear and the other views are a bit titled and blurry. Unable to get a good 3d model out of this data. I’ve attached images for reference.</p>

---

## Post #2 by @olivya_caballero (2018-01-09 22:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbccc6ccaced7b521e6aa95376455fe181c55c92.jpeg" data-download-href="/uploads/short-url/qNm1a0h9n2NgALQMc95CZbIDZxU.jpg?dl=1" title="Screenshot (123)_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbccc6ccaced7b521e6aa95376455fe181c55c92_2_690x407.jpg" alt="Screenshot (123)_LI" data-base62-sha1="qNm1a0h9n2NgALQMc95CZbIDZxU" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbccc6ccaced7b521e6aa95376455fe181c55c92_2_690x407.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbccc6ccaced7b521e6aa95376455fe181c55c92_2_1035x610.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbccc6ccaced7b521e6aa95376455fe181c55c92_2_1380x814.jpg 2x" data-dominant-color="F2ECED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (123)_LI</span><span class="informations">1575×930 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/016d291a69da3ca5e52513ceb97b77e4251d451b.jpeg" data-download-href="/uploads/short-url/cClSvAHVfpYpvX4KyPAIOCezEL.jpg?dl=1" title="Screenshot (124)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/016d291a69da3ca5e52513ceb97b77e4251d451b_2_690x373.jpg" alt="Screenshot (124)" data-base62-sha1="cClSvAHVfpYpvX4KyPAIOCezEL" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/016d291a69da3ca5e52513ceb97b77e4251d451b_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/016d291a69da3ca5e52513ceb97b77e4251d451b_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/016d291a69da3ca5e52513ceb97b77e4251d451b_2_1380x746.jpg 2x" data-dominant-color="88888F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (124)</span><span class="informations">1919×1040 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2018-01-11 04:28 UTC)

<p>Volumes are often high-resolution only in a certain plane and low-resolution in others to reduce acquisition time (or in case of CT, also to reduce X-ray dose).</p>
<p>You can still use this volume, but for certain operations, such as segmentation, you may want to resample the volume to have uniform resolution along all axes, using Crop volume module, Isotropic spacing option. I would recommend to choose spacing value between the highest and lowest spacing; for example: if you have 0.2 x 0.2 x 5 mm spacing then you may resample it to 1 x 1 x 1 mm.</p>

---

## Post #4 by @francesca_flore (2022-05-16 10:05 UTC)

<p>Is there any tutorial for segmentation of volumes with just high-resolution in a certain plane? Thanks.</p>

---

## Post #5 by @rbumm (2022-05-17 12:16 UTC)

<p>Should be upvoted and pinned <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2022-05-17 13:46 UTC)

<aside class="quote no-group" data-username="francesca_flore" data-post="4" data-topic="1799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/francesca_flore/48/15307_2.png" class="avatar"> francesca_flore:</div>
<blockquote>
<p>Is there any tutorial for segmentation of volumes with just high-resolution in a certain plane?</p>
</blockquote>
</aside>
<p>There is no simple solution. See this discussion for details:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---

## Post #7 by @mohamad_saidi (2024-06-19 17:33 UTC)

<p>i cant seem to change the the spacing value in my case , why is that  ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf0ca2ba279f5cdad783e939479a6a4b6420d476.png" data-download-href="/uploads/short-url/rg6gEz3QGSZ9AFKvceoYfgOshtI.png?dl=1" title="Capture d’écran (77)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf0ca2ba279f5cdad783e939479a6a4b6420d476_2_690x388.png" alt="Capture d’écran (77)" data-base62-sha1="rg6gEz3QGSZ9AFKvceoYfgOshtI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf0ca2ba279f5cdad783e939479a6a4b6420d476_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf0ca2ba279f5cdad783e939479a6a4b6420d476_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf0ca2ba279f5cdad783e939479a6a4b6420d476_2_1380x776.png 2x" data-dominant-color="96959B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran (77)</span><span class="informations">1920×1080 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2024-06-19 23:39 UTC)

<p>You can change the output volume spacing by adjusting the <code>spacing scale</code> value.</p>

---
