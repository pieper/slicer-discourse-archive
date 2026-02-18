# image overlay of a cbct image and a corresponding DICOM structure 

**Topic ID**: 30375
**Date**: 2023-07-03
**URL**: https://discourse.slicer.org/t/image-overlay-of-a-cbct-image-and-a-corresponding-dicom-structure/30375

---

## Post #1 by @take5 (2023-07-03 16:00 UTC)

<p>Greetings, I am new to 3D Slicer and would like to know if my thought is correct.<br>
I have created a cone-beam CT image by using Plastimatch fdk with a matrix size and a voxel size that are different  from its corresponding DICOM CT image set. Surprizingly, 3D Slicer has shown a cooordinate-matched image overlaid result when I import the cbct.mha and add a DICOM strcture. So I guess this automatic adjustment is a functionality of the 3D Slicer. Is this correct?</p>

---

## Post #2 by @pieper (2023-07-03 17:12 UTC)

<p>Yes, Slicer uses the <a href="https://www.slicer.org/wiki/Coordinate_systems">image geometries</a> to display the data in a patient-centric coordinate system.</p>

---

## Post #3 by @take5 (2023-07-03 23:32 UTC)

<p>Dear Steve Pieper,<br>
Thanks for your reply. I have read the linked image geometries page.<br>
Now I understand that 3D Slicer image transformation makes it possible to overlay multiple image objects having diferent matrix sizes and different voxel spacings.<br>
I like it a lot.</p>

---
