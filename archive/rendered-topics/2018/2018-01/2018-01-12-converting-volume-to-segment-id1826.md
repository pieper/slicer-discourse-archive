# Converting volume to segment?

**Topic ID**: 1826
**Date**: 2018-01-12
**URL**: https://discourse.slicer.org/t/converting-volume-to-segment/1826

---

## Post #1 by @tnguyen (2018-01-12 19:31 UTC)

<p>Hi everyone,</p>
<p>I am new to Slicer and I have a quick question,<br>
I used the Editor module to carve out a volume and make a model with that volume (resulting in a nrrd and mrml files). I thought this was a segment and attempted to use some of Slicer quantitation functions for segments, however, Slicer doesn’t recognize it as a segment. I guess my question is how do I make a segment after having a volume/model?<br>
Thank you</p>

---

## Post #2 by @lassoan (2018-01-12 19:50 UTC)

<p>Use Segment Editor module instead of the legacy Editor module. To carve out parts from a volume, you can use Mask volume effect (it is available in the SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @tnguyen (2018-01-12 20:28 UTC)

<p>Thanks so much for replying!<br>
I will use the Segment Editor to make segment, is there a way to salvage the volume I already have by changing it to segment somehow?</p>

---

## Post #4 by @HarishRRao (2018-01-12 22:38 UTC)

<p>I think you could use the <strong>Export/import models and labelmaps</strong> section in the <strong>Segmentations</strong> module to convert a model into a segment again. I have posted a screenshot when I tried this feature:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ede57fbe5326bda9776a6b81e4784cd5a0ba3e8.png" alt="image" data-base62-sha1="8Y9YhBkj6zgcrrbD8J0gAxrWEqY" width="577" height="232"></p>

---

## Post #5 by @tnguyen (2018-01-13 01:46 UTC)

<p>It works!! Thanks so much everyone for helping me!</p>

---
