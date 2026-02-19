---
topic_id: 11485
title: "Crop Volume Wrong Result"
date: 2020-05-10
url: https://discourse.slicer.org/t/11485
---

# Crop volume wrong result

**Topic ID**: 11485
**Date**: 2020-05-10
**URL**: https://discourse.slicer.org/t/crop-volume-wrong-result/11485

---

## Post #1 by @giovform (2020-05-10 22:14 UTC)

<p>Hello, I am using the Crop Volume programmatically to crop with a ROI around a segmentation node (the segmentation node is used for a Mask). In some cases it works, and in others it results in a misalignment like this one bellow:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9ce6bb8747174ab71f5ac6f4d1b528650203e02.png" alt="error" data-base62-sha1="qvIAmAx3yPaMtbMWu8nfGvaXDHk" width="417" height="367"></p>
<p>The segmentation on the original volume is fine (it all encompasses some data) but this resulting cropped volume has lost a piece at the bottom (Out of Frame). What could be causing this misalignment on the final crop result?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2020-05-10 22:40 UTC)

<p>Hi -</p>
<p>For questions like this is always helps to create a small set of steps so others can reproduce the result that seems wrong (e.g. a small snippet of python code they can paste into slicer like the ones in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>).  Sometimes the process of creating such a reproducible example can actually lead you to the solution on your own - it’s worked for me more that once!</p>

---

## Post #3 by @lassoan (2020-05-11 00:14 UTC)

<p>We have been testing rasterization for rounding errors quite thoroughly, so I would be surprised if there were issues. Cross-sectional images may be misleading, especially if spacing is anisotropic, interpolated display is disabled, or you are viewing oblique slices.</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> wrote above, we need to reproduce this case on our own computer to tell if the behavior is correct. An easy way to reproduce is to share the scene (.mrb) file.</p>

---

## Post #4 by @giovform (2020-05-11 00:17 UTC)

<p>Changing the Crop Volume Technique to “Voxel Based” solved the problem. I will try to make a working example soon.</p>

---
