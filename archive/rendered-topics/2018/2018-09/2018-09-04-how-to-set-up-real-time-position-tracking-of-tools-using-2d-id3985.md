# How to set up real-time position tracking of tools using 2D barcodes

**Topic ID**: 3985
**Date**: 2018-09-04
**URL**: https://discourse.slicer.org/t/how-to-set-up-real-time-position-tracking-of-tools-using-2d-barcodes/3985

---

## Post #1 by @kamrul079 (2018-09-04 14:37 UTC)

<p>I had used the same steps to calibrate the camera using the printed out markers and add connection with OpenIGTLinkIF successfully. After that, I did not find any direction that what should I need to do to track an object in real time. What are the steps? How to create let’s say this water glass model and then track in real time?</p>

---

## Post #2 by @lassoan (2018-09-04 15:36 UTC)

<p>If you go to Transforms module, you should see transforms showing up as soon as you put markers in the camera’s field of view. If you use the demo configuration file then you have to have at least a reference marker and some tool markers in the field of view simultaneously.</p>
<p>If you have the transforms then you need to calibrate your tools and set up visualization as explained in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>

---

## Post #3 by @kamrul079 (2018-09-04 16:22 UTC)

<p>Don’t I need the pivot calibration?</p>

---

## Post #4 by @lassoan (2018-09-04 18:38 UTC)

<p>You need to calibrate your tools, i.e., determine transform between coordinate system of the tool’s model and coordinate system of the attached barcode. For pointer-like tools, you can compute this transform using pivot calibration.</p>

---
