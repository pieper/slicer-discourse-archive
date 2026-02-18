# Capability to add a simple circular ROI to quantify fat fraction.

**Topic ID**: 37427
**Date**: 2024-07-17
**URL**: https://discourse.slicer.org/t/capability-to-add-a-simple-circular-roi-to-quantify-fat-fraction/37427

---

## Post #1 by @achery (2024-07-17 11:05 UTC)

<p>Hello,<br>
I’m try to create a circulate ROI in order to quantify the fat fraction on Philips MRI files but I can’t get circular ROI and Segmentation seems very cumbersome compared to what other viewers can offer. Is there any method you may know that would help me ?<br>
Thanks for your help,<br>
Best regards,<br>
Alex</p>

---

## Post #2 by @lassoan (2024-07-17 11:29 UTC)

<p>Other viewers are simpler because they are limited to work with 2D regions in 2D images. Slicer works in 3D, with arbitrary shaped regions, which generally works better, because humans are 3D and organs/body regions are usually not rectangular out circular.</p>
<p>We could simulate the simple 2D software behavior by writing a short Python code snippet that automatically creates a segment from the ROI, runs segment statistics, and adds the segmentation result to the ROI.</p>
<p>However, we can probably do much better. For example, you can automatically segment the 3D region you want to quantify (MONAIAuto3DSeg, TotalSegmentator, etc) then get statistics for each slice. This way you could do the analysis fully automatically. Our we could just specify a3D region manually, using points, lines, curves, etc. and then compute all measurements and generate a report (e.g., at lines to a CSV file) by a single click.</p>
<p>What is your full workflow? Do you need to make a single 2D measurement for each patient or you measure in multiple slices? What do you measure - visceral fat, fat in liver, …? How do you choose the location and size of the ROI?</p>

---
