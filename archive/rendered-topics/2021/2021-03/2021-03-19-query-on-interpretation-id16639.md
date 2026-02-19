---
topic_id: 16639
title: "Query On Interpretation"
date: 2021-03-19
url: https://discourse.slicer.org/t/16639
---

# Query on interpretation

**Topic ID**: 16639
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/query-on-interpretation/16639

---

## Post #1 by @RadioQuest (2021-03-19 15:07 UTC)

<p>Hi…<br>
I am working on a 2 groups of patients with different therapies in brain cancer. I carried out T2 MRI texture analysis for different ROI. In selected 10 features for heterogeneity (uniformity, TE, entropy, variance, kurtosis, cluster shade, Difference variance, difference entropy, correlation etc), I found only Total Energy ( TE) to be showing significant difference between two groups and no other feature shows significant difference when these groups are compares.<br>
Besides in other larger group I found TE to the only consistent feature found to be correlated with the dose while others do not show this consistent findings.<br>
Can someone help me to interpret these results.<br>
Thanking You.<br>
Kind Regards<br>
RQ</p>

---

## Post #2 by @JoostJM (2021-03-22 16:27 UTC)

<p>It would be interesting to also assess volume and other shape features in this case. TE is known to be heavily dependent on volume.</p>

---

## Post #3 by @RadioQuest (2021-03-22 18:51 UTC)

<p>Thank you for your reply. Its a 2D MRI slice with 2D circular ROI of same fixed diameter. All other factors are  almost matched.I am trying to understand what can TE represent?<br>
In some other areas, other features show difference too but overall TE is the clear winner with maximum association.</p>

---

## Post #4 by @JoostJM (2021-04-12 08:20 UTC)

<p>Total Energy is a <a href="https://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.firstorder.RadiomicsFirstOrder.getTotalEnergyFeatureValue">fairly simple feature</a>. It will be large in larger volumes or in volumes with higher intensity voxels.<br>
So if your ROI is fixed (be sure to check the number of voxels in the diagnostic features though! Same diameter does not mean the same number of voxels if the spacing is different!), The difference is explained by a higher mean or higher number of outliers with a large value.</p>
<p>Why this is the only significant difference between your groups I cannot answer for you, as that requires much more details and research into your specific dataset/study.</p>

---

## Post #5 by @RadioQuest (2021-04-12 09:02 UTC)

<p>Many thanks for your reply. I checked other primary features, they did show the difference.<br>
However still total energy is the only different feature in one group.<br>
Re: Number of voxels, I am not sure about number of voxels , unfortunately I got rid of initial information in the earlier stages of analysis and it is a very large dataset.<br>
Thank you.</p>

---
