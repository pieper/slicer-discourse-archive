---
topic_id: 20955
title: "Volume Rendering And Multiplanar Reconstruction"
date: 2021-12-07
url: https://discourse.slicer.org/t/20955
---

# Volume rendering and multiplanar reconstruction

**Topic ID**: 20955
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/volume-rendering-and-multiplanar-reconstruction/20955

---

## Post #1 by @Luna (2021-12-07 21:42 UTC)

<p>I am viewing my dicom files in 3D slicer and I notice that the images are stretched out in yz and xz plane, so in all the planes except the original image plane which is xy plane. I tried fiji imageJ as well but my images weren’t stretched here.<br>
The values in the dicom header for slice thickness and pixel spacing are correct. I have a voxel size of 0.4x0.4x0.4 mm^3, so slice thickness is 0.4 and pixel spacing is [0.4 0.4] in my dicom header. What could have gone wrong? Are there any other attributes that I have to fill in?</p>

---

## Post #2 by @mikebind (2021-12-08 23:00 UTC)

<p>Are you creating the DICOM headers yourself?  Slicer does not use the “Slice Thickness” to set the slice spacing, see discussion here:</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="453">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/slicer-loads-wrong-image-spacing/453/4">Slicer loads wrong image spacing</a></div>
<blockquote>
<p>The out of plane spacing is defined by the distance between the ImagePositionPatient of adjacent slices, not by the SliceThickness, which can be different for a variety of reasons.</p>
</blockquote>
</aside>

---

## Post #4 by @Luna (2021-12-09 13:45 UTC)

<p>I created the dicom headers myself.<br>
I see I defined my ImagePositionPatient incorrectly. Problem is fixed now, thanks a lot!</p>

---
