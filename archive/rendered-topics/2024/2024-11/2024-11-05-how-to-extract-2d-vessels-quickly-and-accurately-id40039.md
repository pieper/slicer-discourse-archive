# How to extract 2D vessels quickly and accurately?

**Topic ID**: 40039
**Date**: 2024-11-05
**URL**: https://discourse.slicer.org/t/how-to-extract-2d-vessels-quickly-and-accurately/40039

---

## Post #1 by @jsalas424 (2024-11-05 17:40 UTC)

<p>Hello,</p>
<p>I’m trying to segment out the left anterior descending coronary artery from a contrast enhanced XR image. The goal is to calculate the surface area of the vessel, and then compare this longitudinally within patients are multiple timepoints to see any changes in coronary lumen.</p>
<p>This functionality is well documented for 3D scans, but I can’t figure this out in 2D. Similar to the youtube walkthrough, I attempted to use the Segment Editor and Local Thresholding, but the next step is the “Show 3D” and clean up the segmentation there, but that’s not available for 2D slices.</p>
<p>I’ve also tried the VMTK module " Guided Artery Segmentation". I started with adding a curve in markups as so:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7badbbe29b0c96df245b1f03c94cf2fad603610c.jpeg" data-download-href="/uploads/short-url/hE6X1OLbQi3vG6SkipZEP6tFKwc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7badbbe29b0c96df245b1f03c94cf2fad603610c_2_690x470.jpeg" alt="image" data-base62-sha1="hE6X1OLbQi3vG6SkipZEP6tFKwc" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7badbbe29b0c96df245b1f03c94cf2fad603610c_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7badbbe29b0c96df245b1f03c94cf2fad603610c_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7badbbe29b0c96df245b1f03c94cf2fad603610c_2_1380x940.jpeg 2x" data-dominant-color="4D4A4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1310 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I run the segmentation, here’s my result which I don’t know how to use:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4ff724159006e5814ae235e300453c0afef2fa6f.jpeg" data-download-href="/uploads/short-url/bppdsYZZ4zoOYdds64HM25EMkpN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4ff724159006e5814ae235e300453c0afef2fa6f_2_690x475.jpeg" alt="image" data-base62-sha1="bppdsYZZ4zoOYdds64HM25EMkpN" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4ff724159006e5814ae235e300453c0afef2fa6f_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4ff724159006e5814ae235e300453c0afef2fa6f_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4ff724159006e5814ae235e300453c0afef2fa6f_2_1380x950.jpeg 2x" data-dominant-color="4C4C49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1323 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I uploaded the DICOM I’m trying to process here: <a href="https://file.io/6c408TBokUNg" rel="noopener nofollow ugc">https://file.io/6c408TBokUNg</a></p>
<p>Thank you!</p>
<div class="youtube-onebox lazy-video-container" data-video-id="caEuwJ7pCWs" data-video-title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=caEuwJ7pCWs" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/caEuwJ7pCWs/maxresdefault.jpg" title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" width="690" height="388">
  </a>
</div>
<aside class="quote quote-modified" data-post="1" data-topic="12571">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/ebca7d/60.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-extract-3d-vessels-segmentation-quickly-and-accurately/12571">How to extract 3D vessels segmentation quickly and accurately?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi,All! 
I need to extract 3D vessels segmentation from 3d TOF MRA,I want to do that more quickly and accurately .Now I use threshold and islands in segment editor to that and my segmentation as follow.But is there a better way to do? <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c729ddb784a40d1e2340eeb0e8fd1649cc73b8.png" data-download-href="/uploads/short-url/iw4izFO8WhHWEupTlFDIcjJo2Ny.png?dl=1" title="QQ图片20200716175054" rel="noopener nofollow ugc">[QQ图片20200716175054]</a>
  </blockquote>
</aside>


---

## Post #2 by @chir.set (2024-11-05 18:50 UTC)

<p>This is a 2D image from a coronary angiogram. Slicer works with 3D volumes. Consider working with CT coroscans if you want to segment anything in Slicer.</p>

---

## Post #3 by @jsalas424 (2024-11-05 18:53 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="40039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>CT coroscans</p>
</blockquote>
</aside>
<p>Is this to say that dealing with 2D images is not possible in Slicer?</p>

---

## Post #4 by @chir.set (2024-11-05 20:16 UTC)

<aside class="quote no-group" data-username="jsalas424" data-post="3" data-topic="40039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> jsalas424:</div>
<blockquote>
<p>Is this to say that dealing with 2D images is not possible in Slicer?</p>
</blockquote>
</aside>
<p>Yes, not possible. You would be investing time worthlessly, even if you get to some kind of promising output.</p>
<p>There’s a project called SAM - ‘Segment anything model’,  that works on 2D images. You may investigate there.</p>

---
