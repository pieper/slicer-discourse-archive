# How to use registration for CT scans to create 3D models?

**Topic ID**: 35548
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/how-to-use-registration-for-ct-scans-to-create-3d-models/35548

---

## Post #1 by @ylee (2024-04-17 02:40 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 5.4.0</p>
<p>Hi all, I am trying to use registration for CT scans of the nasal airway to create 3D models, using one scan as the posterior portion of the airway and another scan as the anterior portion to demonstrate airflow changes following different surgeries. I have already performed segmentation and created 3D models of the respective areas but am trying to use registration to align them and create one 3D model end product. I have not found any success so far and would like to see if anyone can provide any help with this. I would greatly appreciate any suggestions you have!</p>

---

## Post #2 by @lassoan (2024-04-17 02:50 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">Automatic image registration</a> using Elastix or ANTs should work well. You can then apply and harden the computed transform on the segmentation.</p>

---

## Post #3 by @ylee (2024-04-18 17:44 UTC)

<p>That did the job, thank you so much!</p>

---
