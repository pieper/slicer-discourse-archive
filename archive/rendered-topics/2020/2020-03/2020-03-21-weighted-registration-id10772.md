---
topic_id: 10772
title: "Weighted Registration"
date: 2020-03-21
url: https://discourse.slicer.org/t/10772
---

# Weighted registration

**Topic ID**: 10772
**Date**: 2020-03-21
**URL**: https://discourse.slicer.org/t/weighted-registration/10772

---

## Post #1 by @endlessric23 (2020-03-21 14:48 UTC)

<p>Dear Slicer’s users:<br>
I am doing the image registration in CT image.<br>
And I wonder is there a feature weighted registration tool ?(When I register the abdomen image,I know the spine is the important feature. How to put more emphasis on spine?)</p>

---

## Post #2 by @lassoan (2020-03-21 15:11 UTC)

<p>There is no fractional weighting, as you would not want to compromise accurate registration in the region of interest to improve registration in non-essential regions. Instead, you normally crop to the region of interest in both fixed and moving image (using Crop volume module) and register these cropped images. The computed transformation can be applied to the original (non-cropped) volumes.</p>

---
