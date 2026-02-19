---
topic_id: 13475
title: "Correction Of Mri Image Distortion"
date: 2020-09-14
url: https://discourse.slicer.org/t/13475
---

# Correction of MRI image distortion

**Topic ID**: 13475
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/correction-of-mri-image-distortion/13475

---

## Post #1 by @aseman (2020-09-14 04:41 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D Slicer experts and all<br>
I have 2 images( CT and MRI). We calculated the displacement (distortion) of each point in MRI relative to CT image(Slicer B splin Tranform). Now, I have a question. How can I apply a matrix on my MRI image to correct these distortions, to different points of the MRI image be without distortion? (As CT image).<br>
Thanks a lot</p>

---

## Post #2 by @wpgao (2020-09-14 15:52 UTC)

<p>You can use the transform module. The transformation type is grid transform, whose parameter is the displacement matrix. Then this transform is applied to your MR image.</p>

---
