---
topic_id: 22448
title: "Median And Iqr Values Please Help"
date: 2022-03-11
url: https://discourse.slicer.org/t/22448
---

# Median and IQR values please help

**Topic ID**: 22448
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/median-and-iqr-values-please-help/22448

---

## Post #1 by @Saffana (2022-03-11 09:52 UTC)

<p>Hello</p>
<p>I am segmenting the lungs and I am looking for median and IQR in the results</p>
<p>the software provides mean and SD for the values of segmented lungs</p>
<p>Can you help me please?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2022-03-11 19:27 UTC)

<p>You can get a the median of any scalar volume within a segmented region using the Segment Statistics module.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>
<p>Standard deviation is provided but not IQR, which you could calculate yourself by accessing the volume and mask as numpy arrays and using scipy to compute.</p>
<p><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.iqr.html#:~:text=The%20interquartile%20range%20(IQR)%20is,ranges%20than%20the%20actual%20IQR" class="inline-onebox">scipy.stats.iqr — SciPy v1.8.0 Manual</a>.</p>
<p>It’s also possible to make an IQR plugin to Segment Statistics if you end up using it a lot.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#information-for-developers" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#information-for-developers</a></p>

---
