---
topic_id: 21233
title: "Behind The Scene Calculation For Ice"
date: 2021-12-27
url: https://discourse.slicer.org/t/21233
---

# Behind-the-scene Calculation for ICE

**Topic ID**: 21233
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/behind-the-scene-calculation-for-ice/21233

---

## Post #1 by @Wong_Yun_Ming (2021-12-27 11:46 UTC)

<p>Hi, I am trying to compute ICE on my own as I did not use Slicer to perform deformable registration on my images. May I know the way ICE is computed in Slicer, so that I can reproduce the results using my own code?</p>

---

## Post #2 by @lassoan (2021-12-27 11:59 UTC)

<p>ICE acronym has several very different meanings in medical imaging. Do you mean inverse consistency error?</p>
<p>Are you already using a the Transform module or a Slicer extension (e.g., RegistrationQA) to compute it and interested n how they work?</p>
<p>What is your overall goal? Comparison of registration algorithms? What is the target organ? What registration software are you comparing?</p>

---

## Post #3 by @Wong_Yun_Ming (2021-12-27 13:01 UTC)

<p>Hi, yes I was referring to inverse consistency error.</p>
<p>I did the registration on Velocity software and I could not find a way to evaluate the ICE for certain ROIs using the deformation vector field obtained from Velocity.</p>
<p>I am not comparing registration algorithms, instead I would like to check whether ICE correlates with some other metrics for deformation accuracy evaluation (eg. DICE) for prostate cancer patients.</p>

---
