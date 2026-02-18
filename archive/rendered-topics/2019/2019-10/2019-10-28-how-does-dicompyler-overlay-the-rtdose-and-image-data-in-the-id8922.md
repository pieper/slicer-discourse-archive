# How does dicompyler overlay the RTDOSE and Image data in the correct position?

**Topic ID**: 8922
**Date**: 2019-10-28
**URL**: https://discourse.slicer.org/t/how-does-dicompyler-overlay-the-rtdose-and-image-data-in-the-correct-position/8922

---

## Post #1 by @Iman_Shokatian (2019-10-28 11:39 UTC)

<p>Hello,</p>
<p>I’m currently an MS student in Medical Physics and I have a great need to be able to overlay an isodose distribution from an RTDOSE file onto a CT image from a .dcm file set.</p>
<p>I’ve managed to extract the image and the dose pixel arrays myself using pydicom and dicom_numpy, but the two arrays are not the same size! So, if I overlay the two together, the dose will not be in the correct position based on what the Elekta Gamma Plan software exported it as.</p>
<p>I’ve played around with slicerrt and it obviously is able to do this even though the arrays are not the same size. However, I think I cannot export the numerical data when using slicerrt…I can only scroll through and view it as an image. What section of the code has the algorithm for overlaying the RTDOSE to an image?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-10-28 11:46 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-does-3d-slicer-overlay-the-rtdose-and-image-data-in-the-correct-position/8924">How does 3D Slicer overlay the RTDOSE and Image data in the correct position?</a></p>

---

## Post #3 by @lassoan (2019-10-28 11:46 UTC)



---
