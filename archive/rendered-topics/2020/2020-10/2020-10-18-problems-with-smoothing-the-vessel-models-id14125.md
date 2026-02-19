---
topic_id: 14125
title: "Problems With Smoothing The Vessel Models"
date: 2020-10-18
url: https://discourse.slicer.org/t/14125
---

# Problems with smoothing the vessel models

**Topic ID**: 14125
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/problems-with-smoothing-the-vessel-models/14125

---

## Post #1 by @Andreas (2020-10-18 21:12 UTC)

<p>Hello everyone,</p>
<p>I sometimes have vessel models that are very difficult to flatten (see pictures). Is there any way I can tweak the smoothing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c4baee64f8f9c3cc5e16d6fef09cad92b4e8751.jpeg" data-download-href="/uploads/short-url/aSWraH4NUqONGT2HJYAoEkBx5Pr.jpeg?dl=1" title="Bild_2020-10-18_195222 (5)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c4baee64f8f9c3cc5e16d6fef09cad92b4e8751_2_627x499.jpeg" alt="Bild_2020-10-18_195222 (5)" data-base62-sha1="aSWraH4NUqONGT2HJYAoEkBx5Pr" width="627" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c4baee64f8f9c3cc5e16d6fef09cad92b4e8751_2_627x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c4baee64f8f9c3cc5e16d6fef09cad92b4e8751_2_940x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c4baee64f8f9c3cc5e16d6fef09cad92b4e8751.jpeg 2x" data-dominant-color="515468"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bild_2020-10-18_195222 (5)</span><span class="informations">1131×901 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is another problem:<br>
When I have smoothed the vessel and then want to create the hollow body, an opening (hole) is created at the tip of the aneurysm and the shape is greatly changed, that is, it flattens out. How can that be avoided?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a394eb6707a79f5bfb26de1383329710fd12beed.jpeg" data-download-href="/uploads/short-url/nl6SX2MsL2Es2hkxUXxuXkAsYi1.jpeg?dl=1" title="Screenshot (4)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a394eb6707a79f5bfb26de1383329710fd12beed_2_463x500.jpeg" alt="Screenshot (4)" data-base62-sha1="nl6SX2MsL2Es2hkxUXxuXkAsYi1" width="463" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a394eb6707a79f5bfb26de1383329710fd12beed_2_463x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a394eb6707a79f5bfb26de1383329710fd12beed_2_694x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a394eb6707a79f5bfb26de1383329710fd12beed_2_926x1000.jpeg 2x" data-dominant-color="9B94C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (4)</span><span class="informations">1712×1848 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff2af641092e829ea496048abe8642823c965dd9.png" data-download-href="/uploads/short-url/ApjND1xKOP75BhGHgh1HZGxwIQ1.png?dl=1" title="Screenshot_1 (4)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff2af641092e829ea496048abe8642823c965dd9_2_463x500.png" alt="Screenshot_1 (4)" data-base62-sha1="ApjND1xKOP75BhGHgh1HZGxwIQ1" width="463" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff2af641092e829ea496048abe8642823c965dd9_2_463x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff2af641092e829ea496048abe8642823c965dd9_2_694x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff2af641092e829ea496048abe8642823c965dd9_2_926x1000.png 2x" data-dominant-color="9B94C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1 (4)</span><span class="informations">1712×1848 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>best regards</p>

---

## Post #2 by @lassoan (2020-10-20 03:52 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="14125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I sometimes have vessel models that are very difficult to flatten (see pictures). Is there any way I can tweak the smoothing?</p>
</blockquote>
</aside>
<p>You can represent vessel with finer resolution by cropping and oversampling the image before segmentation, using Crop volume module (use spacing scale of 0.5 or less).</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="14125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>There is another problem:<br>
When I have smoothed the vessel and then want to create the hollow body, an opening (hole) is created at the tip of the aneurysm and the shape is greatly changed, that is, it flattens out. How can that be avoided?</p>
</blockquote>
</aside>
<p>Both the flattening and the whole are because there is no space in the segmentation’s binary labelmap for the growth of the aneurysm. The easiest is to leave some space around the vasculature before segmentation, when you crop the input volume. If you already segmented the image then you can adjust the segmentation’s extent by creating a ROI node that encloses the region you need and then use it as “Source geometry” in the “Segmentation geometry” window (that you can bring up by clicking the button next to the master volume selector in Segmentation module).</p>

---
