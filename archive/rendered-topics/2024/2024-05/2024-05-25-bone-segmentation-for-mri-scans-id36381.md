---
topic_id: 36381
title: "Bone Segmentation For Mri Scans"
date: 2024-05-25
url: https://discourse.slicer.org/t/36381
---

# Bone Segmentation for MRI scans

**Topic ID**: 36381
**Date**: 2024-05-25
**URL**: https://discourse.slicer.org/t/bone-segmentation-for-mri-scans/36381

---

## Post #1 by @BDA (2024-05-25 00:03 UTC)

<p>Operating system: windows<br>
Slicer version: 5.6.2<br>
Expected behavior: creating 3D bone models from MR images<br>
Actual behavior:<br>
I want to create 3D bone models from MRI scans…I have MR images of the shoulder and knee region in DICOM format, but I couldnt make any segmentation of the humerus, tibia and femur bones with the “threshold” button as in CT and create an image in a three-dimensional window. How can I segment these bones in MR images? I would appreciate your help.</p>

---

## Post #2 by @muratmaga (2024-05-26 05:00 UTC)

<p>MR is not a good modality to visualize bones. They usually appear dark (since they don’t have a lot of water). For good visualization/segmentation of bones, you need CT scans.</p>

---

## Post #3 by @BDA (2024-05-26 14:57 UTC)

<p>I have seen articles where three-dimensional segmentation of bones was done with 3D Slicer from radial MR images and typical MR images. But I think special shooting is required for this. I wondered if it could be done with normal standard typical MR images in the 3D slicer program.</p>

---

## Post #4 by @BDA (2024-05-28 11:03 UTC)

<p>I have seen some articles suc as “Segmentation of the proximal femur in radial MR scans using a random forest classifier and deformable model registration”, “A 3D active model framework for segmentation of proximal femur in MR images”  I wondered if it could be done with standard typical MR images in the 3D slicer program.</p>

---

## Post #5 by @ThomasVanParys (2024-05-29 11:56 UTC)

<p>For your research, I would personally recommend obtaining CT scans for bones, which will yield a better threshold. It can be done ([<a href="https://web.stanford.edu/class/ee368/Project_Autumn_1516/Reports/Migimatsu.pdf" rel="noopener nofollow ugc">https://web.stanford.edu/class/ee368/Project_Autumn_1516/Reports/Migimatsu.pdf</a>]), but MRI is primarily for soft tissue and fluid analysis.</p>

---
