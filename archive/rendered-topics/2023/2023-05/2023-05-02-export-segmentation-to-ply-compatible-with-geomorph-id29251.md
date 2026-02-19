---
topic_id: 29251
title: "Export Segmentation To Ply Compatible With Geomorph"
date: 2023-05-02
url: https://discourse.slicer.org/t/29251
---

# Export segmentation to PLY compatible with geomorph

**Topic ID**: 29251
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/export-segmentation-to-ply-compatible-with-geomorph/29251

---

## Post #1 by @thelobsternods (2023-05-02 18:33 UTC)

<p>I have been using 3D Slicer to segment bones out of scans. So far we have been saving these as STL files for 3D printing. However we would like to begin 3D geometric morphometrics using geomorph in R. This requires PLY files that are are in ASCII format. I tried saving these surfaces as PLY files through the save menus but this apparently saves them into a different “binary little endian format” (based on the error I am getting in geomorph).</p>
<p>How can I save PLY files in ASCII format in 3D slicer? If there are any specific tutorials or threads to point me to that already help users wishing to export surfaces for use with geomorph, please feel free to bring those to my attention.</p>
<p>Thanks, Sarah</p>
<p>Operating system: PC<br>
Slicer version: 5.2.2<br>
Expected behavior: PLY file in ASCII format<br>
Actual behavior: PLY file is in binary little endian format</p>

---

## Post #2 by @lassoan (2023-05-02 18:34 UTC)

<p>You can save as ASCII by disabling the compression option when saving/exporting the model.</p>

---
