---
topic_id: 220
title: "Robustness Of Fill Between Slices Effect"
date: 2017-04-28
url: https://discourse.slicer.org/t/220
---

# Robustness of "Fill between slices" effect

**Topic ID**: 220
**Date**: 2017-04-28
**URL**: https://discourse.slicer.org/t/robustness-of-fill-between-slices-effect/220

---

## Post #1 by @Fernando (2017-04-28 13:27 UTC)

<p>Hi all,</p>
<p>I’m applying the “Fill between slices” effect to two very similar images and I get the desired result in only one of them. Can someone take a look and let me know if you have any ideas to solve this? I expect two connected components and not three.</p>
<p>I tried (outside Slicer) all different combinations of the boolean parameters of <code>itkMorphologicalContourInterpolator</code> and got no improvements.</p>
<p>Link to the scene containing the two images and a segmentation with the contours before and after interpolation: <a href="https://www.dropbox.com/s/auhvg2epq9efdhk/2017-04-28-Scene-fill-between-slices.mrb?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - File Deleted - Simplify your life</a></p>
<p>Thanks for looking into this. If you think this should be posted in ITK instead of here, please let me know.</p>
<p>Here’s what the scene looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/022d52b57e7b72656f26406a4cb0bcf7a7cfa5c6.png" data-download-href="/uploads/short-url/jg3Fy3LN0UbUKK6HRY5I6gE15c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022d52b57e7b72656f26406a4cb0bcf7a7cfa5c6_2_613x500.png" alt="image" data-base62-sha1="jg3Fy3LN0UbUKK6HRY5I6gE15c" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022d52b57e7b72656f26406a4cb0bcf7a7cfa5c6_2_613x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022d52b57e7b72656f26406a4cb0bcf7a7cfa5c6_2_919x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022d52b57e7b72656f26406a4cb0bcf7a7cfa5c6_2_1226x1000.png 2x" data-dominant-color="2F3139"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1299×1058 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Fernando</p>

---

## Post #3 by @lassoan (2017-04-29 04:33 UTC)

<p>The interpolation algorithm assumes smoothly changing shape between segmented slices. If anywhere the interpolated contours are not accurate, all you have to do is segment some more slices. The interpolation will be updated automatically.</p>

---

## Post #4 by @thewtex (2017-04-29 13:09 UTC)

<p>As Andras noted, another manual segmentation on the region where it is failing will improve the result.</p>
<p>It fails because there is an assumption that the segmented contours will overlap – it looks like they are not quite overlapping in that case.</p>

---

## Post #5 by @dzenanz (2017-04-29 17:48 UTC)

<p>The contours must have some overlap to be considered the same object. The<br>
lack of overlap distinguishes different objects e.g. parallel blood vessels.</p>

---
