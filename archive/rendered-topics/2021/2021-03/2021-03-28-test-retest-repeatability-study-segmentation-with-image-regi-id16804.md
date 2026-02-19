---
topic_id: 16804
title: "Test Retest Repeatability Study Segmentation With Image Regi"
date: 2021-03-28
url: https://discourse.slicer.org/t/16804
---

# Test-retest repeatability study: segmentation with image registration or not?

**Topic ID**: 16804
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/test-retest-repeatability-study-segmentation-with-image-registration-or-not/16804

---

## Post #1 by @GMA (2021-03-28 18:50 UTC)

<p>I’m using 3DSlicer to do a repeatability study where I make ADC measurements over two scans which are acquired with the usual “coffee-break” approach, the patient is scanned twice in the same hour. I was reading some literature and I see that in some repeatability studies Authors did an affine registration before doing the actual segmentation.<br>
Isn’t this kind of approach giving ultimately a biased measure of test-retest (specifically a lower value of the coefficient of repeatability)? I thought that the objective of test-retest was to try to obtain a repeatability index that was relative to each measurement.<br>
What are your thoughts about it?</p>
<p>Thank you!</p>
<p>GMA</p>

---

## Post #2 by @pieper (2021-03-28 21:11 UTC)

<p>You might want to register them so you can use the same segmentation on both (so you are consistent in defining boundaries), but you would not want to resample the ADC.  Instead apply the transform to the segmentation.  Probably supersample the segmentation to minimize resampling artifact.  Probably best would be to perform segmentation on both scans and compare the original and transformed segmentation in both directions.</p>

---
