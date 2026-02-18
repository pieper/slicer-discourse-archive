# Segmentation operation failed: Minimum 2 visible segments (or specification of editable area or intensity range)

**Topic ID**: 35547
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/segmentation-operation-failed-minimum-2-visible-segments-or-specification-of-editable-area-or-intensity-range/35547

---

## Post #1 by @Basel04 (2024-04-17 02:40 UTC)

<p>Hello,</p>
<p>I am currently experiencing an issue while performing object segmentation using the latest version of 3D Slicer. Occasionally, I encounter the following error message: “Segmentation operation failed: Minimum 2 visible segments (or specification of editable area or intensity range).” Despite adhering to the same procedures as in previous successful attempts and having at least two visible segments, the error persists. I would appreciate any explanations or potential solutions to address this problem.</p>
<p>Regards,<br>
Dr. Basel</p>

---

## Post #2 by @lassoan (2024-04-17 02:52 UTC)

<p>As far as I remember this issue has been solved. Please test the latest Slicer Preview Release and let us know if it does not work as you expect.</p>

---

## Post #3 by @dmm (2024-08-01 13:02 UTC)

<p>Hi, same issue here, or I don’t understand what “visible segments” are. Currently using 5.6.2 r32448.</p>

---

## Post #4 by @lassoan (2024-08-02 10:11 UTC)

<p>You need to have two segments that are visible (eye icon is open). Maybe they have to be non-empty, too.</p>

---
