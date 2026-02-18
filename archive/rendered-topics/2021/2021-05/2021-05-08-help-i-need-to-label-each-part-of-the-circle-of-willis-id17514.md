# Help! I need to label each part of the Circle of Willis

**Topic ID**: 17514
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/help-i-need-to-label-each-part-of-the-circle-of-willis/17514

---

## Post #1 by @sannpeterson (2021-05-08 00:09 UTC)

<p>Hi, I’m new to 3D Slicer and would love to get some help on how to manually label vessels in the Circle of Willis.</p>
<p>So far I’ve been able to create segmentations from MRA images, no problem. Then (following a tutorial) I export that as a labelmap -&gt;load the -label.nrrd file → open Editor module → create a merge label map →  ThresholdEffect set min/max to 1, Apply → PaintEffect, check “Paint Over”, “Threshold Paint” -&gt;draw over ROI</p>
<p>This is where I get lost because the tutorial says to click Apply after painting over each vessel to reset the label but I don’t see that option. The sphere brush also doesn’t work. If I left click using the sphere brush it continuously paints even when I’m not pressing the mouse button.</p>
<p>Any suggestions would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2021-05-21 17:52 UTC)

<p>Editor module was deprecated several years ago. Where did you find this tutorial?</p>
<p>You can now use the Segment Editor module instead. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point.</p>

---
