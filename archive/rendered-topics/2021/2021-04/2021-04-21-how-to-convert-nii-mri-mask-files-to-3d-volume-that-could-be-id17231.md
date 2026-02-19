---
topic_id: 17231
title: "How To Convert Nii Mri Mask Files To 3D Volume That Could Be"
date: 2021-04-21
url: https://discourse.slicer.org/t/17231
---

# How to convert .nii MRI mask files to 3D volume that could be meshed with 3D element types later?

**Topic ID**: 17231
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/how-to-convert-nii-mri-mask-files-to-3d-volume-that-could-be-meshed-with-3d-element-types-later/17231

---

## Post #1 by @Mohsen (2021-04-21 16:49 UTC)

<p>Hello,</p>
<p>I am trying to convert a .nii MRI mask (binary 3D mask) file to a 3D volume mesh or any 3D volume format, so I could mesh the model with 3D element types and do Finite Element Analysis.</p>
<p>I would appreciate it if anyone could help me with that.</p>
<p>Thanks,<br>
Mohsen</p>

---

## Post #2 by @lassoan (2021-04-25 15:52 UTC)

<p>You can load the nii file as a segmentation and then use SegmentMesher extension to create a volumetric mesh.</p>
<p>If you want to use a different mesher software then probably you want to export the segmentation as a surface mesh (ply, obj, stl, vtk,…), as most volumetric meshers require this format as input.</p>

---

## Post #3 by @Mohsen (2021-04-30 00:18 UTC)

<p>Thank you so much for your help!</p>

---
