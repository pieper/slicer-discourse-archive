# Filtering to improve level tracing

**Topic ID**: 34577
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/filtering-to-improve-level-tracing/34577

---

## Post #1 by @khaledmatloub (2024-02-27 21:08 UTC)

<p>Hello,</p>
<p>I was trying to implement a filter but I can’t quite get the result that I’m looking for.</p>
<p>My goal is to implement this so that it can improve the Level Tracing effect in Segment Editor and get better segmentation results.</p>
<p>Thank you in advance !</p>

---

## Post #2 by @lassoan (2024-02-27 21:21 UTC)

<p>To get started, you don’t need any Python scripting, but you can use Thresholding and Mask volume effect to replace very dark and very bright values.</p>
<p>However, I don’t see how that would help with segmenting something, because clipping the intensity range just removes details in very bright and very dark regions, which should not matter anyway (because you are interested in the boundary of an object that will not be outside the clipping thresholds). Moreover, “Level Tracing” effect has questionable value anyway, as it performs only 2D segmentation, so you would need to manually iterate through a large number of slices to segment anything with it.</p>
<p>I would recommend to experiment further with existing segmentation tools (e.g., “Grow from seeds” effect with a reduced “Editable intensity range”) to segment 30-50 images manually, then use those to train a neural network (MONAI Auto3DSeg, nn-UNet, etc.) to make all further segmentations fully automatic.</p>

---
