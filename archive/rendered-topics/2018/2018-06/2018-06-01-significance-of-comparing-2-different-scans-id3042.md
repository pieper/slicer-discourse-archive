---
topic_id: 3042
title: "Significance Of Comparing 2 Different Scans"
date: 2018-06-01
url: https://discourse.slicer.org/t/3042
---

# Significance of comparing 2 different scans

**Topic ID**: 3042
**Date**: 2018-06-01
**URL**: https://discourse.slicer.org/t/significance-of-comparing-2-different-scans/3042

---

## Post #1 by @teresababy (2018-06-01 13:53 UTC)

<p>I have an MRI of my head that was taken on a 1.5 T scanner a few years back and an MRI that was taken at 3 T last year. I want to compare the two scans to look at differences in the sinuses, the ventricles, and the temporal lobe. When I say differences, I mean atrophy or growth.</p>
<p>First, I am not sure what tests to run to find differences. I am familiar with Siena/Viena but that is it.</p>
<p>Next, are the scans comparable? There are about 20 different scans that either vary in acquisition plane, Phase echo, or frequency. Some are dwi, others are gre, some are pre others are post - there are a lot of acronyms that get overwhelming, but long story short all the scans differ on one of the 3 categories. Would comparing them be significant?</p>
<p>Finally, is sliver capable of doing statistical analysis, and what tests would you run?</p>

---

## Post #2 by @lassoan (2018-06-02 16:11 UTC)

<p>You can segment structures of interest using Segment Editor module and compute properties (volume surface, etc) using Segment Statistics module.</p>
<p>To avoid manual segmentation, you may use registration to transfer segmentation from one data set to the other (it should work particularly well for images of the same patient, acquired with the same imaging modality).</p>
<p>Slicer may be able to do some statistical tests using Python packages but I think most people just exports data in csv format and do their analysis in their usual statistical package.</p>

---
