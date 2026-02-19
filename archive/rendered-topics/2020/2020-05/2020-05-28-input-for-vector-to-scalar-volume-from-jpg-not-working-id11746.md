---
topic_id: 11746
title: "Input For Vector To Scalar Volume From Jpg Not Working"
date: 2020-05-28
url: https://discourse.slicer.org/t/11746
---

# Input for vector to scalar volume from jpg not working

**Topic ID**: 11746
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/input-for-vector-to-scalar-volume-from-jpg-not-working/11746

---

## Post #1 by @Pietro_Ibba (2020-05-28 13:43 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am sorry if this question was already posted.</p>
<p>I am trying to reconstruct a 3D model from an MRI series of jpg images, I am following the tutorial for the import of png images, so first after importing I set the image spacing and origin in the “volumes” module. Then when I try to input the vector volume in the “vector to scalar conveter” module, I cannot select the previously imported volume.</p>
<p>Am I doing something wrong?</p>

---

## Post #2 by @lassoan (2020-05-28 13:47 UTC)

<p>Maybe it is already a single-component (grayscale) volume. Can you check what value do you see in Volumes module / Volume information / Number of scalars? If you see 1 there then “Volume type” should be “Scalar” and you don’t need “Vector to scalar converter”. If you see 3 or 4 then you should see that “Volume type” is “Vector” and so the volume shows up in need “Vector to scalar converter” module’s input selector.</p>

---

## Post #3 by @Pietro_Ibba (2020-05-28 14:23 UTC)

<p>Hi Andras, thank you for your reply, it was indeed already a greyscale volume!</p>

---
