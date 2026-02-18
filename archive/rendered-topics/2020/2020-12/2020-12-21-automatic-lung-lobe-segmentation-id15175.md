# Automatic lung lobe segmentation

**Topic ID**: 15175
**Date**: 2020-12-21
**URL**: https://discourse.slicer.org/t/automatic-lung-lobe-segmentation/15175

---

## Post #1 by @PaoloZaffino (2020-12-21 23:48 UTC)

<p>Hi all,<br>
I have multiple CTs and lung contours.<br>
I would partition the lungs into subvolumes (as in " lobe segmentation", <a href="https://chestimagingplatform.org/" rel="noopener nofollow ugc">Chest Imaging Platform</a>).</p>
<p>The point that I need something completely automatic and runnable via CLI.</p>
<p>Any idea?</p>
<p>Thank you very much.<br>
Best,</p>
<p>Paolo</p>

---

## Post #2 by @rbumm (2020-12-22 11:25 UTC)

<p>Hi Paolo,</p>
<p>As far as I know, completely automatic lung lobe (or even lung segment) segmentation is not yet available in Slicer.<br>
You may want to have a look at the Lung CT Analyzer which includes a semiautomatic lung mask generator.<br>
How detailed would your lung segmentation have to be?</p>
<p>Best regards<br>
rudolf</p>

---

## Post #3 by @PaoloZaffino (2020-12-23 14:42 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,<br>
thanks for replying.<br>
I already have the lung contours, I just need to partition them into subvolumes.<br>
I don’t need super accuracy, I’m more interested in consistency.</p>
<p>Ok, so I can not use slicer…do you know if there are other automatic tools for this task?</p>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #4 by @lassoan (2020-12-23 15:35 UTC)

<p>There can be many solutions. What is the clinical goal? Why do you need completely automatic segmentation? How many cases you need to segment? What are the constraints: how accurate the segmentation should be (how much, what kind of errors are acceptable, where), how robust it should be (what percentage of cases you can accept segmentation to fail on), what is the maximum time allowed for a segmentation, what is the maximum time that an expert can spend with providing inputs and quality-check results?</p>

---

## Post #5 by @PaoloZaffino (2020-12-23 16:19 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I have more or less 400 patients (CTs + lung contours) and I need to split the lungs in different areas.<br>
The ideal thing would be to have accurate partitioning and zero failed cases, but I understand this is not possible. I would pick the best possible solution, than I’ll compute the success ratio and I’ll figure out if it is reasonable.</p>

---

## Post #6 by @lassoan (2020-12-23 16:30 UTC)

<p>My understanding is that CIP’s lobe segmentation requires only a few input points. I guess it should not take more than 1 minute for a trained operator to provide those. Probably another minute of human operator time is needed for quality check of the results. Altogether, 2 minutes per case. For 400 cases it would be about 14 hours of net work (maybe 5-10 hours more the first few dozens of cases will be slower as the operator is still learning). So, overall, for just 400 cases and without very specific constraints, it would be hard to come up with something that works significantly better than the semi-automatic method in CIP. You can probably successfully train a CNN with 400 cases if you need to segment more.</p>

---

## Post #7 by @rbumm (2020-12-23 17:43 UTC)

<p>Do the subvolumes need to be exactly the lung lobes ? If yes, you need manual assistance in the Slicer extensions currently available. Either way you would have to check an automated result, which will not always be perfect because of incomplete  lung fissures. I agree to <a class="mention" href="/u/lassoan">@lassoan</a> that it would probably best to train a person for this purpose and study.</p>

---

## Post #8 by @PaoloZaffino (2020-12-27 17:51 UTC)

<p>Thank you for the suggestions.<br>
I think I’ll segment a single case by using CIP, then I’ll run a sort of single atlas based segmentation to segment the remaining cases…it should be sufficient for what I need.</p>
<p>Thanks a lot!</p>
<p>Paolo</p>

---
