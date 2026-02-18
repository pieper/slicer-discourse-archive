# Simple solution for MRI navigation

**Topic ID**: 10316
**Date**: 2020-02-17
**URL**: https://discourse.slicer.org/t/simple-solution-for-mri-navigation/10316

---

## Post #1 by @qeee (2020-02-17 18:54 UTC)

<p>hi guys, I am looking for a simple solution for MRI navigation, I need a pointer which shows location on MRI for example if I point on patella it shows me MRI transverse slice of patella, is it so difficult and do I need extensions like slicerIGT, plus toolkit etc, or is there any more simple solution? I just need a navigation in one simple transverse plane which shows me direct location on MRI slice. Is there any solution yet developed? thank you for your answer</p>

---

## Post #2 by @lassoan (2020-02-17 18:58 UTC)

<p>It is really simple to do using Plus and SlicerIGT. You don’t even need to write a single line of script, just set up the scene using the GUI. Since everything is saved in the scene (your hardware configuration, calibration, all visualization settings), you can just load the scene and your navigation system is ready to go.</p>
<p>Note that unlike commercial navigation systems, SlicerIGT can use almost any tracking and imaging device, so you need to do some extra work to define your hardware configuration and calibrate your system, but you only need to do this once.</p>

---
