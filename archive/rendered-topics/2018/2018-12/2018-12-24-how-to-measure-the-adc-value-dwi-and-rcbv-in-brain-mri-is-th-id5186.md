# How to measure the ADC value(DWI) and rCBV in brain MRI？（is there a guideline?）

**Topic ID**: 5186
**Date**: 2018-12-24
**URL**: https://discourse.slicer.org/t/how-to-measure-the-adc-value-dwi-and-rcbv-in-brain-mri-is-there-a-guideline/5186

---

## Post #1 by @scu_why (2018-12-24 21:46 UTC)

<p>Operating system:WIN10<br>
Slicer version:4.11<br>
Expected behavior:Draw the same small ROI in DWI and CBV image, then measure the ADC value(DWI) and rCBV in brain MRI,all utilize the DWI and PWI(CBV) image(DICOM) of multimodality MRI.<br>
Actual behavior: I didn"t find the way or extension to achieve that. can i do it in 3Dslicer ? or maybe other application should work. the final goal is to make the DWI and CBV image registration， then measure the ADC and rCBV in the same small ROI</p>

---

## Post #2 by @pieper (2018-12-29 19:00 UTC)

<p>If you have the rCBV and ADC images then you should be able to apply the same ROI (segmentation).  Have a look at the Segment Editor and the Segment Statistics modules as a starting point.  As a start you need to load your data through the DICOM module.</p>

---
