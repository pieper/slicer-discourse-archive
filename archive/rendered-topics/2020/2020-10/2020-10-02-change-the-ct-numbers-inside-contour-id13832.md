# Change the CT numbers inside contour

**Topic ID**: 13832
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/change-the-ct-numbers-inside-contour/13832

---

## Post #1 by @ToufikDZ (2020-10-02 21:39 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.0</p>
<p>Hello,<br>
I’m using slicer to change the ct numbers inside a contour. Please, I need your help to set the ct numbers (HU) inside a contour to 0 and outside it to -1000. How can I do that with 3d slicer please?</p>

---

## Post #2 by @lassoan (2020-10-03 02:46 UTC)

<p>You can use Mask volume effect for this (available in Segment Editor module after installing SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @ToufikDZ (2020-10-03 04:01 UTC)

<p>Thank you very much, it worked!</p>

---
