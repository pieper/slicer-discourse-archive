---
topic_id: 12497
title: "Creating Landmarks On Isosurface"
date: 2020-07-12
url: https://discourse.slicer.org/t/12497
---

# Creating landmarks on isosurface

**Topic ID**: 12497
**Date**: 2020-07-12
**URL**: https://discourse.slicer.org/t/creating-landmarks-on-isosurface/12497

---

## Post #1 by @ramyavij (2020-07-12 21:38 UTC)

<p>Hi,</p>
<p>I am loading DICOM images from CT/MRI. I would like to create the isosurface to obtain the 3D image of the torso surface. On the torso surface, I would like to mark electrode locations.</p>
<p>How can I create the isosurface without segmenting any anatomy inside.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2020-07-13 18:12 UTC)

<p>Hi - you can turn on volume rendering, adjust the shift slider and then fiducials will be placed on the first non-transparent voxel.</p>

---

## Post #3 by @ramyavij (2020-07-14 15:30 UTC)

<p>Thank you very much, Steve. That was very helpful. Can you point me to any tutorial on how to add the fiducials? I need to add more than 100 of them at a time and export their 3D coordinates.</p>

---

## Post #4 by @pieper (2020-07-14 15:47 UTC)

<p>I’m not sure if there’s a tutorial specifically on placing hundreds of fiducials, but the <a href="https://slicermorph.github.io/#two">SlicerMorph</a> tutorials will probably help.</p>

---

## Post #5 by @ramyavij (2020-07-14 16:12 UTC)

<p>Ok, I will check them out. Thank you.</p>

---

## Post #6 by @ramyavij (2020-07-17 16:07 UTC)

<p>Hi Steve, when I tried to add the markup, it doesn’t show up on any of the views. The fiducial list is grayed out. Can you please let me know how to view the added fiducials? Thanks.</p>

---

## Post #7 by @lassoan (2020-07-17 16:17 UTC)

<p>See markups module documentation about how to place markups in recent Slicer Preview Releases (currently recommended version to use): <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html</a></p>

---

## Post #8 by @ramyavij (2020-07-17 16:26 UTC)

<p>Thanks. I am using 4.10. Should I down 4.11 instead?</p>

---

## Post #9 by @lassoan (2020-07-17 16:30 UTC)

<p>Yes, I would recommend 4.11. It has no known major limitations and contains lots of fixes and improvements compared to 4.10.</p>

---

## Post #10 by @ramyavij (2020-07-17 16:34 UTC)

<p>Thank you. I will try it.</p>

---

## Post #11 by @ramyavij (2020-07-21 00:06 UTC)

<p>Hello,</p>
<p>Yes 4.11 worked well for placing fiducials. I was able to use “Persistent” feature to place multiple fiducials on the 3D volume. However, the coordinate of the fiducial changes with rotation. If I rotate the 3D volume and place the same fiducial from a different angle, the coordinates are different. How can that be prevented? Thanks!</p>

---

## Post #12 by @pieper (2020-07-21 00:29 UTC)

<p>Maybe you can post some screenshots to explain what you are seeing.  If you place a fiducial it stays at the same 3D position when you rotate.  New fiducials will be placed base on the first non-transparent data it hits.</p>

---

## Post #14 by @pieper (2020-07-21 12:59 UTC)

<p>I’m still not understanding your process.  Can you reproduce using a volume from the SampleData placing maybe one fiducial and describing your exact steps?</p>

---

## Post #15 by @ramyavij (2020-07-21 16:52 UTC)

<p>I don’t encounter the problem anymore. Thank you for willing to help!</p>

---
