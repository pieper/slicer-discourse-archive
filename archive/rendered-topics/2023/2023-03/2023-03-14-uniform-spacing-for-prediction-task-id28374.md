---
topic_id: 28374
title: "Uniform Spacing For Prediction Task"
date: 2023-03-14
url: https://discourse.slicer.org/t/28374
---

# Uniform spacing for prediction task

**Topic ID**: 28374
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/uniform-spacing-for-prediction-task/28374

---

## Post #1 by @Nima_Yousefi (2023-03-14 13:31 UTC)

<p>Hi,<br>
In case of prediction and feature extraction,<br>
is it necessary to have uniform spacing for ct images by doing resampling?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I would appreciate if you share your opinions with me.</p>
<p>Best regard</p>

---

## Post #2 by @lassoan (2023-03-14 14:20 UTC)

<p>Yes, generally for any 3D processing or analysis you can avoid some problems if you resample the image to have isotropic resolution. Resampling is a lossy operation, so try to keep the current resolution along axes (e.g, if you have a 0.8x0.8x3mm spacing then resample to 0.8x0.8x0.8 instead of 1.0x1.0x1.0).</p>

---

## Post #3 by @Nima_Yousefi (2023-03-14 17:31 UTC)

<p>Thank you. How about filtering such as wavelet or LoG?</p>

---

## Post #4 by @lassoan (2023-03-14 18:57 UTC)

<p>Noise filtering or other arbitrary enhancement or feature extraction filters are probably unnecessary and may even lead to worse end results.</p>

---
