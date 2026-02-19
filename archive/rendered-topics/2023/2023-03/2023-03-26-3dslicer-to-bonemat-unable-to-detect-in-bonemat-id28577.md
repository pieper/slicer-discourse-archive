---
topic_id: 28577
title: "3Dslicer To Bonemat Unable To Detect In Bonemat"
date: 2023-03-26
url: https://discourse.slicer.org/t/28577
---

# 3DSlicer to Bonemat, unable to detect in Bonemat

**Topic ID**: 28577
**Date**: 2023-03-26
**URL**: https://discourse.slicer.org/t/3dslicer-to-bonemat-unable-to-detect-in-bonemat/28577

---

## Post #1 by @tjjay17 (2023-03-26 02:53 UTC)

<p>Hi,<br>
Extremely new to the domain, so please excuse me if I’m confused on things.</p>
<p>I had a 3DSlicer segmentation of a vertebra given in STL format, which I took and cleaned up in ANSYS Spaceclaim. I then meshed it in ANSYS workbench, and exported the mesh to Bonemat in order to map the material properties.</p>
<p>However, when I import the mesh and CT Scan (Dicom) into Bonemat, Bonemat is unable to detect the mesh on the CT Scan as it does with the sample data.</p>
<p>If anyone has went through the Bonemat workflow, would appreciate some assistance</p>

---

## Post #2 by @lassoan (2023-03-26 03:30 UTC)

<p>I don’t know what Spaceclaim and Ansys workbench does to the branch, so it is hard to tell what is the root cause of the different behavior.</p>
<p>Can you share a sample data set that works and the sample data set that does not work? (use publicly available data set)</p>
<p>Do you use <a href="https://github.com/elisepegg/py_bonemat_abaqus">py_bonemat_abaqus</a>?</p>

---
