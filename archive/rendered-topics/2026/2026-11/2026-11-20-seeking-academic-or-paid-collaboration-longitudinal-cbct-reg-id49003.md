---
topic_id: 49003
title: "Seeking Academic or Paid Collaboration – Longitudinal CBCT Registration and Volumetric Bone Healing Analysis"
date: 2026-11-20
url: https://discourse.slicer.org/t/49003
last_bumped: 2026-11-26T05:27:53.078Z
---

# Seeking Academic or Paid Collaboration – Longitudinal CBCT Registration and Volumetric Bone Healing Analysis

**Topic ID**: 49003
**Date**: 2026-11-20
**URL**: https://discourse.slicer.org/t/seeking-academic-or-paid-collaboration-longitudinal-cbct-registration-and-volumetric-bone-healing-analysis/49003

---

## Post #1 by @Amila (2026-11-20 18:57 UTC)

<p>Hello everyone,</p>
<p>I am a PhD candidate and researcher in Oral Surgery at the University of Sarajevo, Bosnia and Herzegovina.</p>
<p>I am currently conducting a clinical study investigating bone regeneration following mandibular third molar extraction, comparing two platelet-rich fibrin (PRF) protocols with a control group.</p>
<p>The study includes approximately <strong>59 paired CBCT datasets</strong>, acquired immediately after surgery (T0) and three months postoperatively (T1).</p>
<p><strong>Research objective</strong></p>
<p>Our goal is to develop a reliable and reproducible workflow for:</p>
<ul>
<li>
<p>Rigid registration of T0 and T1 CBCT scans.</p>
</li>
<li>
<p>Segmentation of the original extraction socket at T0.</p>
</li>
<li>
<p>Quantification of radiographically mineralized tissue within the original socket volume at T1.</p>
</li>
<li>
<p>Volumetric analysis and assessment of measurement reproducibility.</p>
</li>
</ul>
<p><strong>Current challenge</strong></p>
<p>I have been working with 3D Slicer and have attempted rigid registration using BRAINSFit and Elastix, but have encountered difficulties achieving satisfactory alignment.</p>
<p>Although the scans were acquired using the same CBCT system, the relatively limited field of view and differences in patient positioning may be contributing to the problem.</p>
<p>I have also explored registration masks based on stable mandibular structures, but have not yet established a sufficiently accurate and reproducible workflow.</p>
<p><strong>Collaboration opportunity</strong></p>
<p>I am looking for a researcher or medical image analysis specialist with experience in longitudinal CT/CBCT registration, preferably in dental or maxillofacial imaging.</p>
<p>I would particularly appreciate support with developing and validating the registration and volumetric analysis methodology.</p>
<p><strong>I am primarily interested in academic collaboration, but I am also open to paid consultation or technical collaboration.</strong></p>
<p>Ideally, I would like to work alongside an experienced specialist, understand the methodology, and learn how to perform the analysis independently.</p>
<p>We could initially evaluate one or two de-identified paired datasets to assess feasibility and determine the most appropriate approach.</p>
<p>If anyone is interested in collaborating, or could recommend a researcher or research group with relevant expertise, I would be very grateful.</p>
<p>Thank you for your time and consideration!</p>

---

## Post #2 by @MasatoshiOBA (2026-11-23 13:06 UTC)

<p>One possible approach would be to use surface-based registration rather than direct CBCT image registration.</p>
<p>In our previous study (Am J Sports Med. 2022;50:1272–1280, <a href="https://doi.org/10.1177/03635465221074338" rel="noopener nofollow ugc">https://doi.org/10.1177/03635465221074338</a>), we registered preoperative, planned (virtual postoperative), and actual postoperative bone models to quantify surgical changes.</p>
<p>Our workflow was as follows:</p>
<ol>
<li>
<p>Segment the bone from each CT scan and export the models as STL files.</p>
</li>
<li>
<p>Import the models into CloudCompare and perform rigid ICP registration.</p>
</li>
<li>
<p>Export the resulting 4×4 transformation matrices, apply them to the corresponding original CT volumes in 3D Slicer, and use “Harden transform” before further analysis.</p>
</li>
</ol>
<p>We chose CloudCompare mainly because it allowed us to explicitly control ICP registration parameters, handle models with large numbers of points, and save the transformation matrices for reproducibility.</p>
<p>For your study, you might consider segmenting relatively unchanged portions of the mandible in both scans and using these surfaces for registration, rather than attempting to register the entire CBCT volumes directly.</p>
<p>Nowadays, much of this workflow may also be possible entirely within 3D Slicer, but CloudCompare remains a useful option when detailed control over ICP parameters is needed.</p>
<p>I hope this helps!</p>

---

## Post #3 by @Amila (2026-11-26 05:27 UTC)

<p>Thank you so much for the advice, I will try this approach as well, hope it works!</p>
<p>Best wishes,</p>
<p>Amila.</p>

---
