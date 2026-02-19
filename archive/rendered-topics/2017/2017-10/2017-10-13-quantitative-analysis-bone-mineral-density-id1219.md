---
topic_id: 1219
title: "Quantitative Analysis Bone Mineral Density"
date: 2017-10-13
url: https://discourse.slicer.org/t/1219
---

# Quantitative analysis: Bone Mineral Density

**Topic ID**: 1219
**Date**: 2017-10-13
**URL**: https://discourse.slicer.org/t/quantitative-analysis-bone-mineral-density/1219

---

## Post #1 by @blaked93 (2017-10-13 17:22 UTC)

<p>Hello,</p>
<p>Is it possible to measure BMD using slicer? I’ve been unsuccessful thus far.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-10-13 21:17 UTC)

<p>If you segment the bone using Segment Editor module then you can use Segment Statistics module to compute average density values in each segmentes region. Do you know how to get bone mineral density value from Hounsfield unit? Is that linear relationship? If the relationship is non-linear then you probably have to convert to bone mineral density first and then compute statistics.</p>

---

## Post #3 by @ElaniaDiBart (2023-11-15 06:06 UTC)

<p>Hi!<br>
I’m doing something similar.<br>
The relationship between density and HU is linear. Then i calculate the apparent density and finally the elastic modulus.<br>
Do you have any suggestion for doing it on 3d slicer?</p>

---

## Post #4 by @manjula (2023-11-16 19:03 UTC)

<ol>
<li>Do the scan of the standard phantoms (calibration rods ) using calibrated CT</li>
<li>Do your sample scans using the same CT</li>
<li>calculated the HU values using the segment stattistics module after segmenting the ROI</li>
<li>Using the HU values of the phantoms calculate the linear regressiion formula</li>
<li>using the above formula you can come at the BMD of a ROI</li>
</ol>

---

## Post #5 by @Joseph_L (2023-12-05 00:04 UTC)

<p>Is it possible to expand more on this?</p>
<p>I have a phantom with 2 values. I assume I have to segment out the two phantoms individually, then use the segment statistics module to determine HU for each phantom. Then using these two values I can determine the linear regression formula. What are the x and y values use to calculate regression? I assume one of them is HU?</p>

---

## Post #6 by @ElaniaDiBart (2024-01-25 01:27 UTC)

<p>I don’t have the phantoms so my CT is not calibrated. i think i need the density of each segment and the mean HU. i can easily compute the HU using segment statistic but do you have any suggestion for the density?<br>
Thank you</p>

---
