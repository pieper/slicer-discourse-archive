# Unit correct for my DICOM Data

**Topic ID**: 13153
**Date**: 2020-08-25
**URL**: https://discourse.slicer.org/t/unit-correct-for-my-dicom-data/13153

---

## Post #1 by @Jini (2020-08-25 09:48 UTC)

<p>Where can you calibrate or set the unit of the 3D slicer. By the segmentation and volume it shows me in mm, is this unit correct?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-08-25 12:13 UTC)

<p>Yes, if the dicom data follows the standard then Slicer will show the units correctly in millimeters.  If the units are not correct for some reason you can change them in the Volumes module.</p>

---

## Post #3 by @Jini (2020-08-25 16:29 UTC)

<p>How do I know if the unit is properly adjusted? does I have to calculate something from dicom data?</p>

---

## Post #4 by @pieper (2020-08-25 16:32 UTC)

<p>If you know the actual size of something in the images you can use a ruler or line markup in slicer to measure it and compare.  Do you have some reason to think your dicom data is invalid?</p>

---

## Post #5 by @Jini (2020-08-26 11:47 UTC)

<p>the middle ear is very small and I can’t imagine that the deflection is in mm. I don’t know how to set it automatically without measuring it manually with a ruler. Do I have to take data from the DICOM for the setting?<br>
I have to be able to calculate it somehow back to check whether the unit can be correct?</p>
<p>Thanks</p>

---
