---
topic_id: 47275
title: "Segmenting individual lobes in an abnormal brain (with hydrocephalus)"
date: 2026-06-08
url: https://discourse.slicer.org/t/47275
last_bumped: 2026-06-08T20:35:50.202Z
---

# Segmenting individual lobes in an abnormal brain (with hydrocephalus)

**Topic ID**: 47275
**Date**: 2026-06-08
**URL**: https://discourse.slicer.org/t/segmenting-individual-lobes-in-an-abnormal-brain-with-hydrocephalus/47275

---

## Post #1 by @Preetham_Dange (2026-06-08 10:28 UTC)

<p>Hello everyone,</p>
<p>I am currently working on hydrocephalus . I need do segment the lobes of the brain in MRI of children with hydrocephalus . I saw a few extensions on 3D slicer and some sites like VolBrain but they are only able to segment in near normal appearing brain. I am ok with semi automatic segmentation also but I would prefer if I can do it in approx 20-30 minutes per scan. Does anyone have any suggestions ?</p>
<p>Thanks in advance</p>
<p>Regards,</p>
<p>Preetham S.D.</p>
<p>Fellow in pediatric neurosurgery, Amrita institute, Kochi,India</p>

---

## Post #2 by @ThomasVanParys (2026-06-08 10:39 UTC)

<p>Hello. Do you need the true anatomical lobes (as meshes) or regional volumes (i.e., as a value)? If ventricular enlargement isn’t too severe I would try TotalSegmentator or NNInteractive (<a href="https://github.com/coendevente/SlicerNNInteractive" class="inline-onebox" rel="noopener nofollow ugc">GitHub - coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation with nnInteractive. · GitHub</a>). There are also other MONAI/n-Unet based methods.</p>

---

## Post #3 by @Preetham_Dange (2026-06-08 11:12 UTC)

<p>Thanks for replying Thomas</p>
<p>No I don’t need true anatomical lobes . If I can segment cerebrum, deep nuclei, brainstem and cerebellum. It would be fine</p>

---

## Post #4 by @Preetham_Dange (2026-06-08 11:14 UTC)

<p>I tried both of them . The hydrocephalus I’m working on are quite severe so it didn’t work. Also I am working on CISS/Fiesta sequences .</p>

---

## Post #5 by @ThomasVanParys (2026-06-08 12:44 UTC)

<p>Ah, I see. Most brain segmentation packages are not trained on CISS/FIESTA sequences, so that may be a challenge. I would suggest deformable registration of one known segmented volume to your target followed by manual correction:</p>
<ol>
<li>Obtain a (‘normal’) pediatric template with lobar labels.</li>
<li>Register using ANTs.</li>
<li>Import labels into 3D Slicer.</li>
<li>Manually correct the boundaries.<br>
Even when the registration is imperfect, correcting the propagated lobe map may be much faster than drawing the lobes from scratch… I have not done this, so this method may not work well, just a suggestion…</li>
</ol>

---

## Post #6 by @Preetham_Dange (2026-06-08 15:38 UTC)

<p>Thanks for the advice Thomas. I will try it once and let you know how it goes</p>

---

## Post #7 by @Esteban_Barreiro (2026-06-08 20:35 UTC)

<p>Hi! Did you try: <a href="https://github.com/HOA-2/SlicerNeuroSegmentation" rel="noopener nofollow ugc">GitHub - HOA-2/SlicerNeuroSegmentation: NeuroSegmentation extension for 3D Slicer · GitHub</a></p>
<p>Or maybe: <a href="https://github.com/ErenArkun/SlicerBrainParcellation275" rel="noopener nofollow ugc">GitHub - ErenArkun/SlicerBrainParcellation275: This repository provides a method for segmenting and labeling brain structures from MRI images into 275 regions. The segmentation process divides the brain into distinct parcels, and after segmentation, the volume of each parcel is calculated and presented in mm³. · GitHub</a></p>

---
