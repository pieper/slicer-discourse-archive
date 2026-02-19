---
topic_id: 10774
title: "Reducing Size Of Segmentation"
date: 2020-03-21
url: https://discourse.slicer.org/t/10774
---

# Reducing size of segmentation

**Topic ID**: 10774
**Date**: 2020-03-21
**URL**: https://discourse.slicer.org/t/reducing-size-of-segmentation/10774

---

## Post #1 by @Aep93 (2020-03-21 23:43 UTC)

<p>Hello all,<br>
I am wondering whether there is a way to reduce the size of my segmentation. I have a segmentation which size is about 3 GB and it needs a lot of time when I want to mesh it in segment-mesher module. I do not want to change the meshing parameters in segment-mesher because I want a mesh with specific options. It would really help me if I can reduce the size of my segmentation which may lead to a faster meshing process.<br>
Thanks</p>

---

## Post #2 by @JanWitowski (2020-03-22 00:47 UTC)

<p>Could you say more about the data you’re working with, type, format etc.? Is just a segmentation file 3GB, is it a .seg.nrrd file?</p>

---

## Post #3 by @Aep93 (2020-03-22 01:07 UTC)

<p>Hello,<br>
Actually what I have is the segmentation file with .seg.nrrd format and I have the main images also with .nrrd format but I prefer to reduce the size of my current segmentation rather than creating a new segmentation again from the images if it is possible.<br>
Thanks</p>

---

## Post #4 by @muratmaga (2020-03-22 06:33 UTC)

<p>I think you can use the <strong>Specify Geometry</strong> option to reduce the detail of your segmentation.<br>
Choose your segmentation, and hit the specify the oversampling (&lt;1). You should be able to see the resolution of your segmentation being reduced accordingly.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aea7217dbdb15b94837f9884165c81470ec63ea.png" alt="image" data-base62-sha1="hxmy27PmxwPHNqYdbYoVvoRyDV0" width="627" height="83"></p>

---

## Post #5 by @Aep93 (2020-03-23 19:09 UTC)

<p>Thank you very much for your answer.</p>

---
