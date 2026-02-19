---
topic_id: 18172
title: "Blurry Image When Uploading Dicom Files Into Slicer"
date: 2021-06-16
url: https://discourse.slicer.org/t/18172
---

# Blurry Image When Uploading DICOM files into Slicer

**Topic ID**: 18172
**Date**: 2021-06-16
**URL**: https://discourse.slicer.org/t/blurry-image-when-uploading-dicom-files-into-slicer/18172

---

## Post #1 by @joannecallow (2021-06-16 20:22 UTC)

<p>Operating system: macOS Catalina 10.15.1<br>
Slicer version: 4.11<br>
Expected behavior: Images upload clear<br>
Actual behavior: Images upload blurry and two errors showed up (when looking at the slices individually they are clear, but when uploading all together it looks like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f580b8e0f471e53307936cbf5ef816e47b6b8b9a.png" data-download-href="/uploads/short-url/z1OLvwddSvMCu0hYxcbb5mwxLVo.png?dl=1" title="Screen Shot 2021-06-16 at 12.26.17 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f580b8e0f471e53307936cbf5ef816e47b6b8b9a_2_690x375.png" alt="Screen Shot 2021-06-16 at 12.26.17 PM" data-base62-sha1="z1OLvwddSvMCu0hYxcbb5mwxLVo" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f580b8e0f471e53307936cbf5ef816e47b6b8b9a_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f580b8e0f471e53307936cbf5ef816e47b6b8b9a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f580b8e0f471e53307936cbf5ef816e47b6b8b9a.png 2x" data-dominant-color="5F605A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-16 at 12.26.17 PM</span><span class="informations">944×514 82.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/468929a4c484de40ff9f3944a1278335829afcf5.png" data-download-href="/uploads/short-url/a3Zi8Kar5O4OSfHQ68y2Kgb9cbP.png?dl=1" title="Screen Shot 2021-06-16 at 12.25.27 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/468929a4c484de40ff9f3944a1278335829afcf5.png" alt="Screen Shot 2021-06-16 at 12.25.27 PM" data-base62-sha1="a3Zi8Kar5O4OSfHQ68y2Kgb9cbP" width="690" height="60" data-dominant-color="353535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-16 at 12.25.27 PM</span><span class="informations">1267×111 12.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b85bc8118563fcc486569d96a382e583fbb5b92.png" data-download-href="/uploads/short-url/jUgTCNrugi4hRfKXGe79fppBPKq.png?dl=1" title="Screen Shot 2021-06-16 at 12.25.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b85bc8118563fcc486569d96a382e583fbb5b92_2_690x66.png" alt="Screen Shot 2021-06-16 at 12.25.41 PM" data-base62-sha1="jUgTCNrugi4hRfKXGe79fppBPKq" width="690" height="66" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b85bc8118563fcc486569d96a382e583fbb5b92_2_690x66.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b85bc8118563fcc486569d96a382e583fbb5b92_2_1035x99.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b85bc8118563fcc486569d96a382e583fbb5b92.png 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-16 at 12.25.41 PM</span><span class="informations">1275×122 7.85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried enabling acquisition geometry regularization, but it didn’t change anything.</p>

---

## Post #2 by @lassoan (2021-06-16 20:30 UTC)

<p>Most probably you have 3 series, each is high-resolution only along one image axis. See this topic for more details:</p>
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

## Post #3 by @joannecallow (2021-06-16 20:59 UTC)

<p>I went onto the View Controllers Module and found that there are many series options and when I switch to a different series the image appears clear. I am not sure what I am doing though or what these series are. Could you try to explain what is happening?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8883aabe133e6df733ab8973bc5b07478a27bcb8.png" data-download-href="/uploads/short-url/jtF1VJpNAELtko1PtOIiXJkNAlW.png?dl=1" title="Screen Shot 2021-06-16 at 12.39.56 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8883aabe133e6df733ab8973bc5b07478a27bcb8_2_690x364.png" alt="Screen Shot 2021-06-16 at 12.39.56 PM" data-base62-sha1="jtF1VJpNAELtko1PtOIiXJkNAlW" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8883aabe133e6df733ab8973bc5b07478a27bcb8_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8883aabe133e6df733ab8973bc5b07478a27bcb8_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8883aabe133e6df733ab8973bc5b07478a27bcb8.png 2x" data-dominant-color="3F3F3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-16 at 12.39.56 PM</span><span class="informations">1248×659 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-06-16 21:08 UTC)

<p>In an imaging study, usually many series are acquired and even more can be created by reconstructing the same acquired data in many different ways. Use those sequences that work the best for you.</p>

---

## Post #5 by @joannecallow (2021-06-17 22:03 UTC)

<p>Thanks Andras. I have a follow up question. Would I be able to make 3D measurements using three different series of images (one for each orientation)? Or do I need to somehow align the series first? If so, what is the best way to do this?</p>

---

## Post #6 by @lassoan (2021-06-17 22:44 UTC)

<p>First you need to verify that there is no significant displacement between these images. If they are well aligned (which is probably the case) then you can make measurements on any combination of them. You just need to be aware that accuracy of your measurements may be limited to the slice spacing (which may be a magnitude larger then pixel spacing within the slice).</p>

---
