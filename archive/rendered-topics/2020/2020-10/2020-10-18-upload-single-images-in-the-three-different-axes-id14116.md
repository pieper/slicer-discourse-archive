# Upload single images in the three different axes

**Topic ID**: 14116
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/upload-single-images-in-the-three-different-axes/14116

---

## Post #1 by @gnigni (2020-10-18 15:05 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11<br>
Expected behavior: i’d like to be able  to upload and assign images to different axes<br>
Actual behavior: all images are assigned automatically to axis</p>
<p>I have a sets of magnetic resonance images of an ankle, in the sagittal and coronal planes and I would like to load them into the red and green quadrants, for example. The images are single jpgs no DICOM.<br>
When I use the “load data” function and select the images folder, the sagittal and coronal images are loaded into the same square, red quadrand - axial. I tried to create sub folders, but in this case slicer 3d loads the sagittal and coronal projections in two different volumes.</p>
<p>I’d like to be able  to upload and assign images to different axes, can you help me?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2020-10-18 19:29 UTC)

<p>You can add a transform to each volume that positions, rotates, and scales them appropriately. If you don’t know the transformation parameters then you can try and guess it. However, I would recommend to get get higher quality, more reliable data. Where this data set came from?</p>

---
