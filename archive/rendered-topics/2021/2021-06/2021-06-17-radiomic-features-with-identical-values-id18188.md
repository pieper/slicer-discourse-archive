---
topic_id: 18188
title: "Radiomic Features With Identical Values"
date: 2021-06-17
url: https://discourse.slicer.org/t/18188
---

# Radiomic features with identical values

**Topic ID**: 18188
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/radiomic-features-with-identical-values/18188

---

## Post #1 by @Gergely_Orsi (2021-06-17 14:38 UTC)

<p>Dear Community Members,</p>
<p>I do not have too much prior experience with pyradiomics, so sorry for the dull question.</p>
<p>I have several features with identical values and I’d like to know if it’s ok, or not.</p>
<p>Examples:<br>
In Gray Level Size Zone Matrix (GLSZM) Features:<br>
Small Area Low Gray Level Emphasis (SALGLE) is equal with Small Area High Gray Level Emphasis (SAHGLE) and with Zone Entropy (ZE).</p>
<p>original_glrlm_ShortRunHighGrayLevelEmphasis and original_glrlm_ShortRunLowGrayLevelEmphasis	 and original_glszm_GrayLevelNonUniformity are also equal.</p>
<p>Is this normal?</p>
<p>Thank you,</p>
<p>Gergő</p>

---

## Post #2 by @Gergely_Orsi (2021-07-25 06:12 UTC)

<p>Up!</p>
<p>Any help would be appreciated.</p>
<p>Thank you,</p>
<p>Gergő</p>

---

## Post #3 by @JoostJM (2022-01-21 10:11 UTC)

<p>I’m not sure, please take a look at the diagnostic features. Is there adequate range of gray values in your image? are you using a corresponding bin width (about 1/10 to 1/100th of the firstorder range)?</p>

---

## Post #4 by @Gergely_Orsi (2022-01-21 10:21 UTC)

<p>Dear Joost Van Griethuysen,</p>
<p>Thank you for the reply. I’ve postes some 6 months ago so I have to take a closer look on Monday to answer all your questions.</p>
<p>But again, thank you for the reply.</p>
<p>Gergő</p>

---
