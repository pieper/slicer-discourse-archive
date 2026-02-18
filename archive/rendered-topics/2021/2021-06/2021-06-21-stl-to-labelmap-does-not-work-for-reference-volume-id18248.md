# stl to labelmap does not work for reference volume

**Topic ID**: 18248
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/stl-to-labelmap-does-not-work-for-reference-volume/18248

---

## Post #1 by @straj (2021-06-21 11:48 UTC)

<p>Hi,</p>
<p>I’m currently trying to convert an stl file to a binary labelmap, which seems to work fine as long as I do not choose a reference volume under ‘advanced’. If i do so, the labelmap which is created has the correct spacing/origin/…, but is completely empty, meaning it only consists of zeros.</p>
<p>Any idea what I’m doing wrong?</p>

---

## Post #2 by @lassoan (2021-06-21 13:32 UTC)

<p>If the output labelmap volume is all empty then it means that the reference volume does not overlap with the segmentation. If you believe that they overlap then save the scene as a .mrb file, upload it somewhere, and post the link here so that we can have a look.</p>

---
