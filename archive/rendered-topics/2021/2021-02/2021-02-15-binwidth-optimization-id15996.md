# Binwidth Optimization

**Topic ID**: 15996
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/binwidth-optimization/15996

---

## Post #1 by @Ceylan (2021-02-15 15:26 UTC)

<p>Hello everyone,</p>
<p>I’m trying to extract the radiomic features from MR images using Pyradiomics extension on 3DSlicer.</p>
<p>I know that the default setting for the binwidth is 25. However, I am not sure which value is more suitable for my studies. How can I optimize this value? Some features cannot be calculated when I use the default value.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @JoostJM (2021-03-09 12:20 UTC)

<ol>
<li>Extract firstorder features for your dataset, with all preprocessing you intend to use.</li>
<li>Look at the value for firstorder - Range; choose a binwidth so, that for the majority of your scans, the binwidth will result in ~10-100 bins. So if your range is, saty [50 - 500], use binwidth 5.</li>
</ol>

---

## Post #3 by @Ceylan (2021-03-21 14:27 UTC)

<p>Thank you for your kind answer.</p>
<p>I want to ask again, just to be sure.</p>
<p>In my FO Range, my minimum number is 1.46 and my maximum number is 7.58. What’s your suggestion for binwidth value?</p>

---

## Post #4 by @JoostJM (2021-03-22 16:25 UTC)

<p>In that case, I would advise a binWidth of about 0.1, this will yield 15 bins for your minimum and 76 for your maximum, both of which are in the range of [10, 100] bins.</p>

---

## Post #5 by @AMM (2024-09-10 11:40 UTC)

<p>What if we have a range of [50 12000] or [10 1000]? We can garantee that both the min and max stand on the [10 100] interval. What should we do in those cases?</p>

---
