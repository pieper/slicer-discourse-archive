---
topic_id: 8836
title: "To Do Metric Test For Imported Nrrd Images"
date: 2019-10-18
url: https://discourse.slicer.org/t/8836
---

# To do metric test for imported .nrrd images

**Topic ID**: 8836
**Date**: 2019-10-18
**URL**: https://discourse.slicer.org/t/to-do-metric-test-for-imported-nrrd-images/8836

---

## Post #1 by @HariES (2019-10-18 17:16 UTC)

<p>The loaded .nrrd files not appeared in the moving and fixed image list for metric test module. How to get those in the list.</p>

---

## Post #2 by @lassoan (2019-10-18 17:50 UTC)

<p>Which exact module you are trying to use (name of extension and module name)?<br>
Is there a chance that the nrrd file contains tensor or vector data (time sequence, color, diffusion image…)?</p>

---

## Post #3 by @HariES (2019-10-19 08:34 UTC)

<p>It is loaded as FSPGR Bravo 1.4mm-as DWI Volume. Is there any problem if it contains vector data.</p>

---

## Post #4 by @HariES (2019-10-19 16:14 UTC)

<p>Registration–Metric Test</p>

---

## Post #5 by @HariES (2019-10-22 09:10 UTC)

<p>I have converted Fiesta and SPGR images using DWIconvert into .nrrd files and it is stored as DWI file. I applied Transforms and it has stored as new transform and new displacement file.  Once I open to do metric test in General registration I could see only displacement file which is stored in convert section of Transform module. I cannot see any of nrrd original file in the list of moving and fixed image.   How to do metric test for these images.</p>

---

## Post #6 by @lassoan (2019-10-22 13:25 UTC)

<aside class="quote no-group" data-username="HariES" data-post="3" data-topic="8836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>Is there any problem if it contains vector data.</p>
</blockquote>
</aside>
<p>Yes, it is. Metric test module only accepts scalar images, not vector or tensor images. You can use “Vector to scalar volume” to choose a scalar component of a vector or tensor image and analyze the metric on that image.</p>
<p>What is your overall goal? What information do you expect from metric test will give you?</p>

---

## Post #7 by @HariES (2019-10-23 02:04 UTC)

<p>I would like to see metric scoring with and without applying scaling factor in transform to study the mri images.</p>

---

## Post #8 by @HariES (2019-10-23 02:28 UTC)

<p>While converting I did not select any of Advanced Conversion Parameters to give scalar image. Any how the image is not having vector quantity since image is not dwi or dti image.</p>

---

## Post #9 by @lassoan (2019-10-23 04:40 UTC)

<aside class="quote no-group" data-username="HariES" data-post="7" data-topic="8836" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>I would like to see metric scoring with and without applying scaling factor in transform to study the mri images.</p>
</blockquote>
</aside>
<p>Scoring of what metric? What scaling factor: spatial or intensity?</p>
<aside class="quote no-group" data-username="HariES" data-post="8" data-topic="8836" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>While converting I did not select any of Advanced Conversion Parameters to give scalar image. Any how the image is not having vector quantity since image is not dwi or dti image.</p>
</blockquote>
</aside>
<p>There are no “Advanced Conversion Parameters” in “Vector to Scalar Volume” module. Which module did you use?<br>
Is your input volume type scalar or vector (Volumes module / Volume information / Volume type)?</p>

---
