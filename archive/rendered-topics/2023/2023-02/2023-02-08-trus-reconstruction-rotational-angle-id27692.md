---
topic_id: 27692
title: "Trus Reconstruction Rotational Angle"
date: 2023-02-08
url: https://discourse.slicer.org/t/27692
---

# TRUS Reconstruction + Rotational Angle

**Topic ID**: 27692
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/trus-reconstruction-rotational-angle/27692

---

## Post #1 by @Michael_Gorin_M.D (2023-02-08 00:16 UTC)

<p>I have a series of images obtained with a linear side-fire transrectal ultrasound probe (I.e sagital images). The series of images was obtained by simply rotating the probe within the rectum. I know the angle of rotation of the probe for each slice. There is no other tracker on the probe. Any thoughts on how I can reconstruct the ultrasound in the axial view incorporating the probe’s rotational angle?</p>
<p>Thank you everyone!</p>

---

## Post #2 by @ungi (2023-02-08 17:48 UTC)

<p>Hi, it’s possible with a custom python script in Slicer.<br>
How are your images saved? Can you already load them in Slicer? Do they appear as a volume or individual 2D images? For volume reconstruction, it’s best to convert the images to a Slicer Sequence.<br>
How are you angles saved? You need to import that data and create a Sequence of Slicer transforms from it. Besides the angle, you need a few more parameters to accurately create transforms. If the image units are in pixels than the scaling from pixels to millimeters. And the diameter of the ultrasound probe, so we know how far do we need to push the images away from the rotation center.<br>
A lot of these can be figured out by a bit experimentation if you are familiar with Slicer python scripting.</p>

---
