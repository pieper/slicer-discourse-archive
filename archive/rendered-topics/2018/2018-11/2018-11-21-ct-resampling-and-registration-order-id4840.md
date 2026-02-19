---
topic_id: 4840
title: "Ct Resampling And Registration Order"
date: 2018-11-21
url: https://discourse.slicer.org/t/4840
---

# CT Resampling and Registration order

**Topic ID**: 4840
**Date**: 2018-11-21
**URL**: https://discourse.slicer.org/t/ct-resampling-and-registration-order/4840

---

## Post #1 by @ZA_S (2018-11-21 19:09 UTC)

<p>Hello guys,</p>
<p>I have non-contrast 3D CT images. I would like to resample them to 1mm and perform registration. In what order it should be;  resampling then registration, or firstly registration then resampling?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-11-21 19:16 UTC)

<p>I don’t think it will affect the registration if you resample the images before. During registration, linear interpolation is used for point sampling. If you use a different interpolator (bspline, sinc, …) for the 1mm resampling then the sampled values will be slightly different, but it is unlikely to affect the registration result.</p>
<p>Of course, once registration is completed, apply the computed transform and resample to 1mm in one step (to minimize sampling artifacts). You can use Crop volume module for this.</p>

---

## Post #3 by @ZA_S (2018-11-23 11:19 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>.  I am very appreciate for your help.</p>

---
