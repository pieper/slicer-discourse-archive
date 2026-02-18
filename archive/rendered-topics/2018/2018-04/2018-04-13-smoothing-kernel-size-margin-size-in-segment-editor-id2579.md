# Smoothing kernel size, Margin size in Segment editor

**Topic ID**: 2579
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/smoothing-kernel-size-margin-size-in-segment-editor/2579

---

## Post #1 by @MancaZerovnik (2018-04-13 07:44 UTC)

<p>I am doing segmentation of volume with Segment editor.<br>
I can’t use margin tool. Beside margin size input I get warning “margin too small” but I can’t make it big enough, because the limit of the input field is 9999.000mm. Why is that?</p>
<p>I have the similar problem with a kernel size in Smoothing tool, where I can’t set kernel that would be bigger than 1x1x1 voxel (because of limitations in the input field - 10000.000mm).</p>
<p>Is there any solution to overcome those limitations?</p>

---

## Post #2 by @lassoan (2018-04-13 12:44 UTC)

<p>What is the image spacing of your volume?</p>

---

## Post #3 by @MancaZerovnik (2018-04-16 07:56 UTC)

<p>224980.1875mm on all axis,</p>

---

## Post #4 by @lassoan (2018-04-17 03:12 UTC)

<p>I’ve updated Segment Editor effects so that you can set up to 100x larger values than the image spacing. The fix is available in the nightly build that you download tomorrow or later.</p>

---
