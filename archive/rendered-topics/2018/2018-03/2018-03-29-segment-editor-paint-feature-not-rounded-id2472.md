# Segment Editor Paint Feature Not Rounded

**Topic ID**: 2472
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/segment-editor-paint-feature-not-rounded/2472

---

## Post #1 by @Rachel_Wathen (2018-03-29 20:31 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1<br>
Problem: I am trying to edit an MRI using the segment editor and the paint feature in the editor. But when I go to paint instead of getting a rounded area filled in I get rectangular markings painted instead. This is a problem since it doesn’t fill in exactly where the paint feature shows its going to (it shows a circle that will be painted in but then once I’m done painting I get jagged segments). I have tried to use a spherical brush, different files, uninstalled and redownloaded SLICER several times with the same results. Does anyone know how to fix this problem?</p>

---

## Post #2 by @lassoan (2018-03-30 01:45 UTC)

<p>Probably your image axes are not aligned with slice view axes. Apply “rotate to volume plane” as described here: <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/3">Segmentation Editor - How to disable painting on adjacent slices?</a></p>

---
