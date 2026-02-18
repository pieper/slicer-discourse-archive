# Issue with coordinate system mismatch

**Topic ID**: 11622
**Date**: 2020-05-19
**URL**: https://discourse.slicer.org/t/issue-with-coordinate-system-mismatch/11622

---

## Post #1 by @KatS (2020-05-19 14:13 UTC)

<p>Dear Slicer community,</p>
<p>I’m having issues when trying to register small animal brains (scanned on a 9.4T Bruker system, exported as DICOM using ParaVision) to each other which are likely due to a coordinate system mismatch.<br>
The data I have are similar to the ones presented in case#41 in the Registration case library. Similar to the case, my images load with axial and coronal views switched. I was able to fix this by editing the space field information in a .nhdr as explained in the User FAQs. However, the orientation of the image in the sagittal plane is still incorrect: the head looks to the top instead of to the left and the superior side is oriented to the left side of the panel.<br>
I could not correct this by editing the .nhdr file and wasn’t able to reorient the image using the Transforms module (I could bring the sagittal view in the correct orientation though, but not without messing up the axial and coronal view).<br>
Does anyone have experience with the coordinate system used by Bruker and knows how I can reorient the files so that they match the RAS-system?</p>
<p>Thank you a lot!<br>
Katie</p>

---

## Post #2 by @lassoan (2020-05-19 23:47 UTC)

<p>I don’t have experience with that specific device, but you can solve all these kind of issues without manually editing the nhdr file and just applying a linear transform. Each one of the first 3 columns specify direction of the image axes. You can change position of the <code>1.0</code> value and invert the sign as needed. You can also use rotation sliders to find a good orientation of the data (rotate with 0, 90, or 180 deg angles).</p>

---
