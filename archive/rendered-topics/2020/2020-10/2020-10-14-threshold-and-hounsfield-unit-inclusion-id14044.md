---
topic_id: 14044
title: "Threshold And Hounsfield Unit Inclusion"
date: 2020-10-14
url: https://discourse.slicer.org/t/14044
---

# Threshold and hounsfield unit inclusion

**Topic ID**: 14044
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/threshold-and-hounsfield-unit-inclusion/14044

---

## Post #1 by @S_Jo (2020-10-14 22:51 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.1.1.</p>
<p>Hello,<br>
I am using threshold method to measure ROI.  A question came up if the threshold is set at -30, is -30 included or does the inclusion of values start from -29?</p>

---

## Post #2 by @lassoan (2020-10-14 23:26 UTC)

<p>The threshold range is inclusive on both sides.</p>
<p>Note that 1 HU is such a small difference that it should not matter either way. For example, magnitude of image noise typically tens of HU.</p>

---

## Post #3 by @S_Jo (2020-10-19 01:24 UTC)

<p>Thank you for the information. Knowing the noise level is very helpful.</p>

---
