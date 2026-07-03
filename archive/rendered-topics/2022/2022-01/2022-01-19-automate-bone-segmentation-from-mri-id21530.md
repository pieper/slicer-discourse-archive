---
topic_id: 21530
title: "Automate bone segmentation from MRI"
date: 2022-01-19
url: https://discourse.slicer.org/t/21530
last_bumped: 2026-07-02T09:10:49.308Z
---

# Automate bone segmentation from MRI

**Topic ID**: 21530
**Date**: 2022-01-19
**URL**: https://discourse.slicer.org/t/automate-bone-segmentation-from-mri/21530

---

## Post #1 by @Sezen (2022-01-19 17:14 UTC)

<p>Operating system:Windows 11</p>
<p>I am doing a project on whether it is possible to automate the segmentation of bone from specifically MRI scans however I am new to the software. Can anyone point me in the right direction or at least let me know whether this is possible.</p>
<p>PS. Method must be for MRI not CT as the project is aimed at infants with bone deformities who would like to avoid the ionising X-rays from CT scanning, so please do not suggest using CT.</p>

---

## Post #2 by @Katya_Stansfield (2023-02-02 14:33 UTC)

<p>Hi, I am segmenting the pelvis and femora from MRIs and came across your post. Any luck with your project so far?</p>

---

## Post #3 by @Cedric_Cordey (2023-08-14 09:48 UTC)

<p>Has there been any progress regarding this topic?</p>

---

## Post #4 by @fatemeh (2026-06-30 14:42 UTC)

<p>I came across your post from 2023 about segmenting the pelvis and femora from MRIs. I was wondering how your project turned out and if you had any success with the segmentation process?</p>
<p>The reason I ask is that I am about to start a similar project, but focusing on the pediatric foot and ankle. Since my study involves children, using MRI is essential for us.</p>
<p>I would highly appreciate it if you could share your experience, particularly regarding the accuracy of bone segmentation from MRIs and any specific workflows or tools in 3D Slicer that you found helpful.</p>
<p>Thanks in advance for your time and help!</p>
<p>Best regards,</p>

---

## Post #5 by @Reiniertb (2026-07-01 09:26 UTC)

<p><a class="mention" href="/u/fatemeh">@fatemeh</a> I have published a paper where we accurately and automatically segment the skull and mandible from MRI using CT bone as training labels. If you have both CT and MRI available from a group of patients, you could try something similar as our method: <a href="https://www-mdpi-com.proxy-ub.rug.nl/1943-3883/18/3/40" rel="noopener nofollow ugc">Towards MRI-Only Mandibular Resection Planning: CT-like Bone Segmentation from Routine T1 MRI Images Using Deep Learning</a></p>

---

## Post #6 by @fatemeh (2026-07-02 09:10 UTC)

<p>Thank you for sharing your paper. Your method is very interesting.</p>
<p>Unfortunately, I do not have CT data available, since my study population is pediatric and we need to avoid ionizing radiation. My goal is to segment the foot and ankle bones from MRI, reconstruct 3D bone models, and use them for finite element analysis in Abaqus.</p>
<p>I was wondering whether, based on your experience, an MRI-only workflow could provide sufficiently accurate bone geometries for this type of biomechanical application.</p>
<p>I would also really appreciate any recommendations regarding MRI sequences, segmentation strategies, or 3D Slicer workflows that could improve bone segmentation quality, especially in pediatric foot and ankle cases.</p>
<p>Best regards,</p>

---
