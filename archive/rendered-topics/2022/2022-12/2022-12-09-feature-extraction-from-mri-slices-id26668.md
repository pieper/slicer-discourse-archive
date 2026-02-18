# Feature extraction from MRI slices

**Topic ID**: 26668
**Date**: 2022-12-09
**URL**: https://discourse.slicer.org/t/feature-extraction-from-mri-slices/26668

---

## Post #1 by @Saadia_Azeroual (2022-12-09 20:36 UTC)

<p>Hello Pyradiomics community,<br>
I am a little bit confused because I am new in radiomics.<br>
I have 3 MRI slices with 3 corresponding masks, and I want to know if I should extract radiomic features from each slice and calculate the mean ? or it is okay to have features for each slice?</p>
<p>I’m eagerly awaiting your response. Many thanks.</p>

---

## Post #2 by @lassoan (2022-12-10 15:12 UTC)

<p>Normally you use a 2D region in 2D images and 3D region in 3D images. Are the 3 slices coming from a single volume? If yes, then it would be probably more appropriate to compute features in a 3D region.</p>

---

## Post #3 by @Saadia_Azeroual (2022-12-11 14:48 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> for your reply !</p>

---
