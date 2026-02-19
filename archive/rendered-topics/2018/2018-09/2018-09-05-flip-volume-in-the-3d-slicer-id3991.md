---
topic_id: 3991
title: "Flip Volume In The 3D Slicer"
date: 2018-09-05
url: https://discourse.slicer.org/t/3991
---

# Flip volume in the 3d slicer

**Topic ID**: 3991
**Date**: 2018-09-05
**URL**: https://discourse.slicer.org/t/flip-volume-in-the-3d-slicer/3991

---

## Post #1 by @sepideh (2018-09-05 14:25 UTC)

<p>Operating system:windows<br>
Slicer version:4.5.0-1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>To whom it may concerns,</p>
<p>I need to do a 3d/3d registration using 3d slicer. I have two volumes which one of them is completely flipped from another one. That is why i am going to flip one volume and get the same coordinate for both volumes and afterward applying the 3d/3d registration. Can you please kindly tell me how to apply flipping on a volume in 3d slicer, i can not find any tutorial for that. In addition, do you know how to change the center of rotation in the 3d slicer? because if i can change the center of rotation then i can fix that to the center of my volume and then flip the volume manually easily by rotating around the center of volume.</p>
<p>Thanks in advance<br>
Best regards<br>
Sepideh</p>

---

## Post #2 by @lassoan (2018-09-05 14:57 UTC)

<p>You can achieve all these by applying linear transforms in Transforms module.</p>
<p>For example, you can flip around an axis by applying a 4x4 matrix where one element in the diagonal is set to -1 instead of 1. After this, it is recommended to resample the volume using any of the image resampling modules, as applying such a transforms makes volume IJK to RAS coordinate system left-handed, while it is expected to be right-handed.</p>
<p>You can rotate around an arbitrary center by creating a chain of transforms, where the first transform is a translation, second is rotation, and third transform is inverse of the first translation. There is no simpler interface for implementing rotation around arbitrary point, as it is much more accurate, simpler, and faster to align objects based on landmark matching (using <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT extension’s Fiducial registration wizard</a>; or using Landmark registration Slicer core module).</p>

---

## Post #3 by @cpinter (2018-09-05 15:00 UTC)

<p>Also, please use a recent 4.9.0 nightly version instead of the 3 year old 4.5. Since then an interactive transform editing tool has been added among countless other improvements.</p>
<p>From your description it is not clear to me whether you want to flip or rotate. Flipping is only needed if the handedness of the volume coordinate systems are different. This shouldn’t be the case, and if it is, then it should probably be fixed at the time of export.</p>

---

## Post #4 by @sepideh (2018-09-07 10:08 UTC)

<p>Thank you very much for your answer. I am working on that based on your comments…</p>

---

## Post #5 by @sepideh (2018-09-07 10:10 UTC)

<p>Thanks a lot for your answer. I will try the mentioned version of 3d slicer and also playing around the export format.</p>

---

## Post #6 by @alexk (2019-11-23 22:15 UTC)

<p>Hello,<br>
I have the same problem.<br>
Do you have a tutorial to create an arbitrary rotation point and to create the different possible transformations ?<br>
Alex</p>

---
