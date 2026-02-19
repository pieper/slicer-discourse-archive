---
topic_id: 16660
title: "Total Energy Of Image"
date: 2021-03-20
url: https://discourse.slicer.org/t/16660
---

# Total energy of image

**Topic ID**: 16660
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/total-energy-of-image/16660

---

## Post #1 by @RadioQuest (2021-03-20 19:28 UTC)

<p>Hi…<br>
I am working on a 2 groups of patients with different therapies in brain cancer. I carried out T2 MRI texture analysis for different ROI. In selected 10 features for heterogeneity (uniformity, TE, entropy, variance, kurtosis, cluster shade, Difference variance, difference entropy, correlation etc), I found only Total Energy ( TE) to be showing significant difference between two groups and no other feature shows significant difference when these groups are compares.<br>
Besides in other larger group I found TE to the only consistent feature found to be correlated with the dose while others do not show this consistent findings.<br>
Can someone help me to interpret these results.</p>
<p>Is this significant or by chance? What total energy represents?<br>
Thanking You.<br>
Kind Regards<br>
RQ</p>

---

## Post #2 by @JoostJM (2021-04-12 08:16 UTC)

<p>My suggestion would be to calculate the shape features and analyze those.<br>
Total Energy is heavily influenced by the volume of the ROI (see the feature formula in the pyradiomics documentation for the reason why), so it is possible you are seeing the effect of Volume.</p>
<p>Without more details on your studie I can’t provide a more precise answer. However, this is what Radiomics is about. Extracting features is just the first step. Analyzing the correlation and determining the reason behind any found correlation is the real work.</p>

---
