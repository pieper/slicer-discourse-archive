---
topic_id: 37130
title: "Resample A Series Of Radial Images Into 3D Cartesian Volume"
date: 2024-07-01
url: https://discourse.slicer.org/t/37130
---

# resample a series of radial images into 3D cartesian volume

**Topic ID**: 37130
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/resample-a-series-of-radial-images-into-3d-cartesian-volume/37130

---

## Post #1 by @heatherdrury (2024-07-01 19:25 UTC)

<p>Operating system: Win 10<br>
Slicer version: 5.6.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, i’m new to slicer but i did read the documentation and tried to find a similar topic. I have a set of images from a rotational scan of an object (heart) that i’d like to resample into a 3D volume. Restated I exported 103 640x480 jpegs from a rotational scan. I’d like to load these into 3D slicer and use a module (“resample scalar volume”, “slicer morph”, ??) to resample into cartesian space. Not sure this is possible and I may need to write some numpy code but just wanted to check to see if this is something that has been done before. thank you!</p>

---

## Post #2 by @pieper (2024-07-01 20:18 UTC)

<p>It sounds like you have projection images, so you need something like RTK.  This thread should help: <a href="https://discourse.slicer.org/t/dsa-3d-reconstruction/31549" class="inline-onebox">DSA 3D reconstruction</a></p>

---

## Post #3 by @heatherdrury (2024-07-02 20:53 UTC)

<p>Yup, that’s perfect. Thanks for the reply!</p>

---
