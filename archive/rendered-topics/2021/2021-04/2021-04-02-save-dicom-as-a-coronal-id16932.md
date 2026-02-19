---
topic_id: 16932
title: "Save Dicom As A Coronal"
date: 2021-04-02
url: https://discourse.slicer.org/t/16932
---

# Save DICOM as a coronal

**Topic ID**: 16932
**Date**: 2021-04-02
**URL**: https://discourse.slicer.org/t/save-dicom-as-a-coronal/16932

---

## Post #1 by @Rouba1987 (2021-04-02 19:46 UTC)

<p>Hi,</p>
<p>I am trying to save a DICOM dataset (MRI) in slicer however it is changing the orientation from coronal to axial in the DICOM header. I need to import these scans into software to register to another MRI and its causing a lot of issues.</p>
<p>Does anyone know how to fix the DICOM header??</p>

---

## Post #2 by @lassoan (2021-04-02 19:53 UTC)

<p>DICOM exporter organizes volumes into slices so that the slices are split along the third volume axis. Since all processing and visualization should happen in physical space, it should not matter which axis is chosen.</p>
<p>However, if you work with software that can only work with specific axis directions then you can specify the desired volume geometry and resample the image before exporting. For example, you can use “Resample scalar/vector/DWI volume” module and specify axis directions in Manual output parameters / Direction matrix.</p>

---
