---
topic_id: 36539
title: "Compute Co Occurrence Matrix From Dicom"
date: 2024-06-01
url: https://discourse.slicer.org/t/36539
---

# Compute co-occurrence matrix from DICOM

**Topic ID**: 36539
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/compute-co-occurrence-matrix-from-dicom/36539

---

## Post #1 by @sajad_amiri (2024-06-01 12:05 UTC)

<p>Hello friends, I want to know how we can extract the matrices themselves from our DICOM. for example, I want to have a Co-occurrence matrix . to produce new features from this matrix. how can I extract the matrix?</p>

---

## Post #2 by @cpinter (2024-06-03 11:48 UTC)

<p>To clarify: do you want to get matrices that are stored in DICOM tags?</p>
<p>If you use C++ there are examples for this in the SlicerRT extension code. Otherwise I think you can use pydicom.</p>

---

## Post #3 by @sajad_amiri (2024-06-03 11:55 UTC)

<p>yes. I want matrices, I do not have experience with c++ . I will try pydicom . thanks too much</p>
<p>‫‪Csaba Pinter via 3D Slicer Community‬‏ &lt;‪<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>‬‏&gt; در تاریخ دوشنبه ۳ ژوئن ۲۰۲۴ ساعت ۴:۴۸ نوشت:‬</p>

---
