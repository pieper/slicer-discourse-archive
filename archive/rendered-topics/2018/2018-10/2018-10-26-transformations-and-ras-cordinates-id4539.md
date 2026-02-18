# Transformations and ras cordinates

**Topic ID**: 4539
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/transformations-and-ras-cordinates/4539

---

## Post #1 by @Melanie (2018-10-26 07:17 UTC)

<p>Hi,<br>
I am tracking movement using 4d ct. When I harden the transform in order to copy the RAS coordinates to clip board, I get different reading to not doing so. Eg: My fiducial marker X would give RAS values after transforming for each frame say, abc, a1b1 ca, etc.  But when I harden one frame, the next frame gives different set of values  , say instead of a1b1 c1 I am expecting it would give a11b11 c11- ( I apply transform again to the subsequent frame because the previous frame is hardened. If not vavule does not change at all) So my question is which one is correct , please. Without hardening I cannot copy my values to clip board, I used to copy each number separately without hardening- but becomes tedious when you exceed some 20 frames. I have no knowledge in python to work this out.</p>
<p>Thanks a lot</p>

---
