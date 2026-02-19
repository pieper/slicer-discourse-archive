---
topic_id: 24953
title: "Total Radioactivity Within Voi"
date: 2022-08-27
url: https://discourse.slicer.org/t/24953
---

# Total radioactivity within VOI

**Topic ID**: 24953
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/total-radioactivity-within-voi/24953

---

## Post #1 by @samcyc (2022-08-27 21:37 UTC)

<p>Hello all,</p>
<p>I come to you for a question which I can’t find the answer on the forum or on internet.</p>
<p>I want to know the total radioactivity within a volume of interest. All quantitative tools I found for 3D slicer (PET-IndiC, Quantitative Indices, Quantitative Indices Tools, Label Statistics) do not seem to provide this information. Is there a solution ?</p>
<p>Thank you very much for your attention !</p>

---

## Post #2 by @3sa5c64x (2023-04-20 06:25 UTC)

<p>Hi, did you mean SUBbw (g/mL)?</p>
<ol>
<li>install PETDICOM Extension, IndiC and restart</li>
<li>add segments</li>
<li>go to quantification model, segment statistics</li>
<li>select segmentation and statistics options</li>
<li>click apply</li>
</ol>

---
