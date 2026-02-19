---
topic_id: 11639
title: "Vtk To Dicom Using 3D Slicer Or Python Shell"
date: 2020-05-20
url: https://discourse.slicer.org/t/11639
---

# VTK to DICOM using 3D slicer or python shell

**Topic ID**: 11639
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/vtk-to-dicom-using-3d-slicer-or-python-shell/11639

---

## Post #1 by @EkaitzEsteban87 (2020-05-20 14:13 UTC)

<p>Hello,</p>
<p>I have a question about VTK to DICOM conversion. I have an surface mesh VTK file which can be read perfectly in paraview. I want to convert this VTK to DICOM using 3D Slicer. Is there any possibility to make this conversion using the 3Dslicer python shell…? If not, which are the steps for the conversion?</p>
<p>best regards,<br>
Ekaitz.</p>

---

## Post #2 by @lassoan (2020-05-20 15:51 UTC)

<p>Yes, you can do this in Slicer using Python scripting. What DICOM object would you like to create? CT image, RT structure set, DICOM segmentation object? What is your clinical application?</p>

---

## Post #3 by @EkaitzEsteban87 (2020-06-16 20:03 UTC)

<p>Dear Lasso,</p>
<p>Thank you for your fast reply. I guess that it is a DICOM segmentation object. It is not a clinical application… The most nearest example can be a bone that I want to check inside it.</p>
<p>Best regards,<br>
Ekaitz.</p>

---

## Post #4 by @lassoan (2020-06-16 20:28 UTC)

<p>If it is not a clinical application then I would not recommend using DICOM, but any of the common mesh file formats.</p>

---

## Post #5 by @Karthik (2022-04-01 07:02 UTC)

<p>Hi lassoan, I have vtkImageData that I would like to convert to DICOM. I would like to create a CT image from it.</p>
<p>What possible ways are there to do that? Are there any libraries available in python for the same?<br>
Thanks for the help.</p>

---
