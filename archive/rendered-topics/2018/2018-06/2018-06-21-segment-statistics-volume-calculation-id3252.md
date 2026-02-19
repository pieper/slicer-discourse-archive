---
topic_id: 3252
title: "Segment Statistics Volume Calculation"
date: 2018-06-21
url: https://discourse.slicer.org/t/3252
---

# Segment Statistics Volume Calculation

**Topic ID**: 3252
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/segment-statistics-volume-calculation/3252

---

## Post #1 by @sboebin (2018-06-21 00:12 UTC)

<p>Hello, I am new to Slicer and have a few questions about the Segment Statistics Module, particularly how it calculates volume. I am currently segmenting muscle groups, subcutaneous and intramuscular fat within a single slice from MR Images of the thigh. I have read that the Labelmap Statistics calculates volume as the product of the pixel spacing (mm3) and the pixel count. I am curious if Slicer is using the actual pixel dimensions given in the DICOM header combined with the slice thickness or not. I cannot find anything on this from the user manual, so I am looking here for help.</p>
<p>Also for the output of segmentation, is it normalized to total volume? Or is it an absolute volume?</p>
<p>I have attached a photo that I hope will better illustrate the issue I am having.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a2143311ed9f7482d5702ed5c497856da9354f1.png" data-download-href="/uploads/short-url/3J9G55380aa7Wy54GDX1RWInctP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2143311ed9f7482d5702ed5c497856da9354f1_2_690x468.png" alt="image" data-base62-sha1="3J9G55380aa7Wy54GDX1RWInctP" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2143311ed9f7482d5702ed5c497856da9354f1_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2143311ed9f7482d5702ed5c497856da9354f1_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a2143311ed9f7482d5702ed5c497856da9354f1.png 2x" data-dominant-color="959696"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1277×867 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-06-21 00:17 UTC)

<aside class="quote no-group" data-username="sboebin" data-post="1" data-topic="3252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f0a364/48.png" class="avatar"> sboebin:</div>
<blockquote>
<p>I am curious if Slicer is using the actual pixel dimensions given in the DICOM header combined with the slice thickness or not.</p>
</blockquote>
</aside>
<p>Yes, of course, the volume computation is correct, it takes into account pixel size, slice spacing, axis directions, etc.</p>
<aside class="quote no-group" data-username="sboebin" data-post="1" data-topic="3252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f0a364/48.png" class="avatar"> sboebin:</div>
<blockquote>
<p>Also for the output of segmentation, is it normalized to total volume? Or is it an absolute volume?</p>
</blockquote>
</aside>
<p>It is an absolute volume, not relative or normalized.</p>

---

## Post #3 by @lassoan (2018-06-21 00:19 UTC)

<p>Of course, if you segment a single slice then you will have the volume of a single slice. You can get a full 3D segmentation by using for example “Fill between slices” or “Grow from seeds” effect.</p>

---

## Post #4 by @sboebin (2018-06-21 14:28 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="3252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<blockquote>
<p>I am curious if Slicer is using the actual pixel dimensions given in the DICOM header combined with the slice thickness or not.</p>
</blockquote>
<p>Yes, of course, the volume computation is correct, it takes into account pixel size, slice spacing, axis directions, etc.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f04057e1809652b88d3bf2a269c8769ee113a2c3.png" alt="" data-base62-sha1="yhmrLbAqD2d9F614In3Wgv7ndYL" width="20" height="20" role="presentation"> sboebin:</p>
<blockquote>
<p>Also for the output of segmentation, is it normalized to total volume? Or is it an absolute volume?</p>
</blockquote>
<p>It is an absolute volume, not relative or normalized.</p>
</blockquote>
</aside>
<p>Thank you very much for your response, it was most helpful.  I do have an additional question regarding what specific DICOM tags are used for volume calculations (as most DICOM headers contain both nominal pixel size and actual).</p>

---

## Post #5 by @lassoan (2018-06-21 15:33 UTC)

<p>I don’t know what you mean by nominal pixel size. DICOM contains physical pixel size and physical slice position and orientation (PixelSpacing, ImagePositionPatient, ImageOrientationPatient tags) - these define the actual physical geometry and we use these. We are aware that there are other fields (such as slice thickness) that must not be used for geometry computation and we do not use them.</p>

---

## Post #6 by @Ash_Alarfaj (2018-06-26 15:28 UTC)

<p>I’ve done for many slices by threshold effect because it allow me to correct the mislabel while the grow from seeds effect or fill between slices effects don’t allow me to correct.</p>

---

## Post #7 by @Ash_Alarfaj (2018-06-26 15:43 UTC)

<p>Hi Iassoan<br>
It is same my question the pixel size in slicer match the real one in acquired image? because I am trying to measure (cross sectional area,mm2) from pixels number.  so pixel dimension not always 1x1x1mm?<br>
Sincerely</p>

---

## Post #8 by @lassoan (2018-06-26 17:19 UTC)

<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="6" data-topic="3252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>grow from seeds effect or fill between slices effects don’t allow me to correct</p>
</blockquote>
</aside>
<p>Both Grow from seeds and Fill between slices effect allow dynamic updates (if you change seeds or slice intersections, the full 3D segmentation is recomputed immediately).</p>
<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="7" data-topic="3252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>my question the pixel size in slicer match the real one in acquired image</p>
</blockquote>
</aside>
<p>You can find the voxel size in Volumes module / Volume information section / Image spacing field.</p>

---

## Post #9 by @Ennio_Russo_Clarisci (2022-07-04 07:59 UTC)

<p>Dear Andras Lasso,</p>
<p>when calculating the mean, median, max, min HU value of a segment, does Slicer 3d consider also the surface of that segment?</p>
<p>Thnak you in adavance<br>
Ennio</p>

---
