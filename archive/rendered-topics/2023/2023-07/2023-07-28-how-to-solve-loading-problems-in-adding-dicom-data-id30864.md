---
topic_id: 30864
title: "How To Solve Loading Problems In Adding Dicom Data"
date: 2023-07-28
url: https://discourse.slicer.org/t/30864
---

# How to solve loading problems in adding DICOM data

**Topic ID**: 30864
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/how-to-solve-loading-problems-in-adding-dicom-data/30864

---

## Post #1 by @yumin (2023-07-28 19:34 UTC)

<p>Hi everyone! I am new to 3D slicer, and I encountered some problems in loading the data. I wonder do I need to fix the code (which I don’t know how…). It would be great if someone can help! Many thanks!</p>
<p>Could not load: 100: MED PT 2-15KG as a Scalar Volume<br>
Could not load: 100: MED PT 2-15KG - acquisitionNumber 0 as a Scalar Volume<br>
Could not load: 100: MED PT 2-15KG - acquisitionNumber 1 as a Scalar Volume<br>
Could not load: 201: ST PLAIN, iDose (3) as a Scalar Volume<br>
Could not load: 202: BONE PLAIN, iDose (3) as a Scalar Volume<br>
Could not load: 301: Exam Summary as a Scalar Volume<br>
Could not load: 301: Exam Summary - acquisitionNumber 0 as a Scalar Volume<br>
Could not load: 301: Exam Summary - acquisitionNumber 1 as a Scalar Volume<br>
Could not load: 301: Exam Summary - acquisitionNumber as a Scalar Volume<br>
Could not load: 301: Exam Summary - imageType DERIVED-SECONDARY-EXECUTED_SURVIEW-- as a Scalar Volume<br>
Could not load: 301: Exam Summary - imageType DERIVED-SECONDARY-PATIENT_INFO-- as a Scalar Volume<br>
Could not load: 301: Exam Summary - imageType DERIVED-SECONDARY-DOSE_INFO-- as a Scalar Volume<br>
Could not load: 301: Exam Summary - imageType DERIVED-SECONDARY-RESULTS-- as a Scalar Volume</p>

---

## Post #2 by @pieper (2023-07-28 19:35 UTC)

<p>The info here should help you get started: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="inline-onebox">DICOM — 3D Slicer documentation</a></p>

---

## Post #3 by @lassoan (2023-07-28 19:37 UTC)

<p>Series numbers &gt;= 100 are all reprocessed images, reports, etc., which may not be loadable as images. Do you expect to have images in them? If not then you can safely ignore these series.</p>

---
