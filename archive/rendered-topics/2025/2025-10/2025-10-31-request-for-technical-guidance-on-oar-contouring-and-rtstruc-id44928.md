---
topic_id: 44928
title: "Request For Technical Guidance On Oar Contouring And Rtstruc"
date: 2025-10-31
url: https://discourse.slicer.org/t/44928
---

# Request for Technical Guidance on OAR Contouring and RTSTRUCT Export Using 3D Slicer

**Topic ID**: 44928
**Date**: 2025-10-31
**URL**: https://discourse.slicer.org/t/request-for-technical-guidance-on-oar-contouring-and-rtstruct-export-using-3d-slicer/44928

---

## Post #1 by @RAJVEER_RUPEN (2025-10-31 14:50 UTC)

<p>Respected Team,<br>
I am Dr. [Your Full Name], BHMS, currently learning and developing skills in OAR (Organs at Risk) contouring using 3D Slicer.<br>
My goal is to understand the complete technical workflow for accurate delineation and DICOM RTSTRUCT export suitable for radiotherapy planning systems.<br>
At present, I am working in a self-learning and research capacity (non-clinical), and in the future I plan to establish an outsourcing OAR contouring support service using 3D Slicer.<br>
I would be grateful if you could kindly guide me or share any resources on the following points:<br>
Recommended modules or extensions for automatic or semi-automatic OAR segmentation.<br>
Correct process for RTSTRUCT export, including how to ensure proper metadata, geometry matching, and DICOM compatibility with planning systems (e.g., Monaco, RayStation).<br>
Any best-practice advice for maintaining data integrity and structure naming conventions for radiotherapy workflows.<br>
Thank you for your valuable time and for providing this excellent open-source platform to the medical imaging community.<br>
With regards,<br>
Dr. RUPEN RAJVIR<br>
BHMS<br>
Email: <em>(removed for privacy)</em><br>
City: Rajkot Gujarat</p>

---

## Post #2 by @cpinter (2025-11-04 14:05 UTC)

<p>I think the reason you’re not getting answers is that your question is extremely broad. Moreover, dozens, if not hundreds of topics on this forum have discussed these already.</p>
<p>I suggest reading about segmentation first: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<p>This page has a list of extensions, including some that provide deep learning based automatic organ segmentation.</p>
<p>RTSS export works from the Data module. See details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">documentation</a>, but also there are forum topics about this such as <a href="https://discourse.slicer.org/t/export-segmentation-in-dicom-rt-format/16805">this one</a>.</p>
<p>Try these out; we will be happy to answer specific questions afterwards.</p>

---
