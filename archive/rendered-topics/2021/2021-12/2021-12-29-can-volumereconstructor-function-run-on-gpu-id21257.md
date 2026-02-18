# Can VolumeReconstructor function run on GPU?

**Topic ID**: 21257
**Date**: 2021-12-29
**URL**: https://discourse.slicer.org/t/can-volumereconstructor-function-run-on-gpu/21257

---

## Post #1 by @Junshi_Peng (2021-12-29 08:48 UTC)

<p>I’m tring to reconstruct volume from a set of ultrasound images, and I am trying to get the output with less time cost. I have switched the interpolate method into NEAREST_NEIGHBOR and turn off the hole filling, but it still needs about two minutes to get output from a 400 frames series. Is VolumeReconstructor of PLUS running on CPU? And how can I switch it to GPU? Great thank!</p>

---

## Post #2 by @lassoan (2023-03-21 01:55 UTC)

<p>Volume Reconstructor can insert slices in real-time, unless you choose very high resolution so that the image no longer fits into your physical memory. Speed can be slightly further improved by enabling OpenCL support when building Plus or SlicerIGT, but this option is not enabled in the official builds.</p>

---
