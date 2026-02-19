---
topic_id: 10743
title: "Dwi Data Denoising"
date: 2020-03-19
url: https://discourse.slicer.org/t/10743
---

# DWI data denoising

**Topic ID**: 10743
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/dwi-data-denoising/10743

---

## Post #1 by @Adam1122 (2020-03-19 10:55 UTC)

<p>Hello all, does the current Slicer version enable to apply denoising on the DWI data? I haven´t found any DWI denoising filter. In Slicer 3.6 there were implemented 3 DWI filters ( Joint Rician, Rician and Unbiased NLM). Eventually, do slicer extensions include these filters?</p>
<p>Thanks lot<br>
Adam</p>

---

## Post #2 by @pieper (2020-03-19 14:38 UTC)

<p>I don’t know for sure - you can look through SlicerDMRI.  <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> do you know?</p>

---

## Post #3 by @zhangfanmark (2020-03-20 13:14 UTC)

<p>Hi <a class="mention" href="/u/adam1122">@Adam1122</a>,</p>
<p>There is no such functionality in SlicerDMRI now. You may want to take a look at dipy for DWI denoising.</p>
<p>Regards,<br>
Fan</p>

---

## Post #4 by @lassoan (2020-03-21 13:54 UTC)

<p>I’m just curious, was there any specific reason to remove these modules? (were there compatibility issues with recent ITK or Slicer changes?)</p>

---
