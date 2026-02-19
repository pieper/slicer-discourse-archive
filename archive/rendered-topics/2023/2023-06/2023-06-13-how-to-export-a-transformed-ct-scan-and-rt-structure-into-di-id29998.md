---
topic_id: 29998
title: "How To Export A Transformed Ct Scan And Rt Structure Into Di"
date: 2023-06-13
url: https://discourse.slicer.org/t/29998
---

# How to export a transformed CT scan and RT structure into DICOM format

**Topic ID**: 29998
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/how-to-export-a-transformed-ct-scan-and-rt-structure-into-dicom-format/29998

---

## Post #1 by @Tiberiu (2023-06-13 02:53 UTC)

<p>Version: 5.2.2<br>
OS      : MacOS</p>
<p>I read a scan and RT structures in dicom format in Slicer and successfully applied a rotation. I would like to export this into a new scan and structures in dicom format. Is that possible? I could not find in the drop-down menu this option.</p>

---

## Post #2 by @Tiberiu (2023-06-13 06:18 UTC)

<p>On further thought, it doesn’t have to be DICOM format. I’m only interested in the underlying rotated HU array with its corresponding extents. So any format (binary) that allows me to load it into a numpy array would suffice.</p>

---

## Post #3 by @volkodavmyx (2023-06-16 10:43 UTC)

<p>You need to go to the DATA module, select your series, right-click and then “Export to DICOM”<br>
If you want to export in RT struct - you must install SlicerRT extension.</p>

---
