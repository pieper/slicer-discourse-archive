# Quantitative analysis of a lung SPECT

**Topic ID**: 15976
**Date**: 2021-02-13
**URL**: https://discourse.slicer.org/t/quantitative-analysis-of-a-lung-spect/15976

---

## Post #1 by @fbaerenfaenger (2021-02-13 18:01 UTC)

<p>Is it possible to contour the different lobes of the lung in a CT and then transfer the contours to a SPECT for quantitative evaluation?</p>

---

## Post #2 by @lassoan (2021-02-13 18:14 UTC)

<p>Yes, if the SPECT and CT are aligned then you can segment one image and use those segments to quantify the other image (for example, using Segment Statistics module).</p>

---

## Post #3 by @fbaerenfaenger (2021-02-13 18:26 UTC)

<p>Thanks a lot for your answer!<br>
Then I will start to get into it.</p>

---
