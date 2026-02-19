---
topic_id: 12034
title: "Issue With Mean Diffusivity Scalar Measurement"
date: 2020-06-15
url: https://discourse.slicer.org/t/12034
---

# Issue with Mean diffusivity scalar measurement

**Topic ID**: 12034
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/issue-with-mean-diffusivity-scalar-measurement/12034

---

## Post #1 by @KatS (2020-06-15 14:16 UTC)

<p>Dear all,<br>
I’m facing issues when trying to create a Mean Diffusivity output from my DTI data.<br>
I’m using Slicer 4.10.1 and the DMRI Extension and imported my data (acquired at 3T, Siemens Skyra, 41 gradient directions) using DWIConvert. Then I followed the DTI tutorial by Sonia Pujol and was able to create a brain mask and to estimate a tensor that looked ok. However, I have problems to calculate a Mean Diffusivity map from my data. I used Diffusion --&gt; Quantify --&gt; Diffusion Tensor Scalar Maps as described, but the MD map I get has some “blank” spaces/missing values (several pixels are displayed like the background so that it looks as if the map has holes).<br>
When calculating trace or FA, the maps look fine and don’t show any missing values.<br>
How can I fix this?<br>
Thanks a lot for your help!</p>

---
