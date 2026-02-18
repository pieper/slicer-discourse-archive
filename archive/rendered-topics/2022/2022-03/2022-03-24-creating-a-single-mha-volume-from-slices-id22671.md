# Creating a single .mha volume from slices

**Topic ID**: 22671
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/creating-a-single-mha-volume-from-slices/22671

---

## Post #1 by @Fabyan (2022-03-24 15:30 UTC)

<p>Hi, I want to know if it is possible to compose multiple .mha slices into a single .mha volume by layering them on top of each other? I have seen ways to split a single .mha volume into multiple slices but not the other way around. Also I want to note that I would like to be able to do this through code, and the mha slices I have are taken separately if that changes anything. thanks</p>

---

## Post #2 by @lassoan (2022-03-26 03:43 UTC)

<p>Would you like to just stack the slices on top of each other (all slices are parallel, spacing between slices is the same) then you can create a short script that iterates through the input images, gets the pixels as a numpy array and copies into a 3D numpy array. You can find examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>
<p>If the slice position and orientation vary randomly (e.g., freehand tracked ultrasound) then you can use SlicerIGSIO extension’s Volume Reconstruction module.</p>

---

## Post #3 by @Fabyan (2022-03-26 04:05 UTC)

<p>Hi, Thank you. The MRI slices are alternating between two different orientations so I was thinking of just creating a volume for each orientation because I want to simply display these slices in the Slice Widgets. I will look into the volume reconstruction module though just in case.</p>

---

## Post #4 by @lassoan (2022-03-26 04:28 UTC)

<p>If you have two image stacks then it is easier to just copy the pixel data using numpy arrays.</p>
<p>Note that all these problems would be solved if you loaded these slices from DICOM, as the DICOM importer automatically groups the images by orientation and sorts by position. You would just double-click on the study and you would get your volumes loaded.</p>

---
