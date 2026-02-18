# Module to flip through connected components

**Topic ID**: 34871
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/module-to-flip-through-connected-components/34871

---

## Post #1 by @rkraaijveld (2024-03-13 17:02 UTC)

<p>Hi!</p>
<p>I want to make a module where I first input a mask and get the connected components (with Islands for example). I then somehow want to flip through the islands using Previous/Next buttons and give each connected component a score/label.</p>
<p>I was wondering if anyone has some advice on the flipping-through-connected-components part? I see that SegmentationReview has code for scoring, which I could use, but I am unsure how to do the first part.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2024-03-17 03:01 UTC)

<p>You can split islands to segments in Segment Editor’s Islands effects, and then write a few-line Python script that adjusts the visibility of segments.</p>

---
