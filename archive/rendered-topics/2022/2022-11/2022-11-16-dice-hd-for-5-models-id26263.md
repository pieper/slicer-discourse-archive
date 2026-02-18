# DICE + HD for 5 models

**Topic ID**: 26263
**Date**: 2022-11-16
**URL**: https://discourse.slicer.org/t/dice-hd-for-5-models/26263

---

## Post #1 by @SlicerBP (2022-11-16 16:50 UTC)

<p>Dear Community,</p>
<p>how can I calculate the HD and DICE for 5 segmented models. As a comparison, the average model of all 5 models should be used as a basis.</p>
<p>Thank you very much!<br>
BP</p>

---

## Post #2 by @lassoan (2022-12-01 07:14 UTC)

<p>You can use Segment Comparison module of SlicerRT extension.</p>

---

## Post #3 by @SlicerBP (2022-12-04 15:50 UTC)

<p>Thanks, but this only works if you want to compare 2 models. As soon as you want to compare more than 2 models</p>
<p>Best regards<br>
BP</p>

---

## Post #4 by @gcsharp (2022-12-05 18:23 UTC)

<p>Why not take the average (or median, or max) of all pair-wise results?</p>

---

## Post #5 by @SlicerBP (2022-12-07 17:07 UTC)

<p>Thank you! That’s a good idea. I did that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> But the question is, what could be applied as ground truth. There is the method according to RCA, however I would like to set a simpler solution.</p>
<p>You can’t form a median between segmentations, can you? A function with the logical operation “median” does not exist or?</p>

---

## Post #6 by @gcsharp (2022-12-07 21:11 UTC)

<p>There are a few ways to do it.  The easiest is majority voting.  So if a voxel is inside 3 of 5 segmentations, it is part of the consensus.  I think you would need to use python for this.</p>

---
