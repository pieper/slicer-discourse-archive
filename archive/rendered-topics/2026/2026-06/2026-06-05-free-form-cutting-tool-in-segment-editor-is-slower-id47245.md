---
topic_id: 47245
title: "Free form cutting tool in segment editor is slower. "
date: 2026-06-05
url: https://discourse.slicer.org/t/47245
last_bumped: 2026-06-16T05:28:39.075Z
---

# Free form cutting tool in segment editor is slower. 

**Topic ID**: 47245
**Date**: 2026-06-05
**URL**: https://discourse.slicer.org/t/free-form-cutting-tool-in-segment-editor-is-slower/47245

---

## Post #1 by @Chayce_Ross (2026-06-05 12:25 UTC)

<p>Recently the UI updated for the cutting tool in the segment editor to include new options like rectangle or circular cutting tools. These are much faster than the free form tool was/is. However, I feel like the performance has regressed on the free form tool with free form cuts often causing a crash on large segmentations (e.g. bone thresholded segmentations for Head and Neck CT).</p>

---

## Post #2 by @lassoan (2026-06-16 05:28 UTC)

<p>There were no recent changes in the Scissors tool, but if you can give step-by-step instructions for reproducing any problem then let us know.</p>
<p>After segmenting using Thresholding, it is always recommended to use the Smoothing effect to remove surface noise, which slows down editing operations. You can also temporarily disable “Show 3D” or surface smoothing to make updates appear faster, or in Experimental menu of Show 3D button, enable “Use Surface nets”.</p>

---
