# Convert 3D Segmentation to contours along different axis

**Topic ID**: 13400
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/convert-3d-segmentation-to-contours-along-different-axis/13400

---

## Post #1 by @evanakm (2020-09-09 13:35 UTC)

<p>If I use SlicerRT to export a segmentation to a Dicom RTSS file using , the 2D contours are all along axial slices. Is there a way to export the contours along a perpendicular direction?</p>

---

## Post #2 by @cpinter (2020-09-09 13:51 UTC)

<p>For that you will need to use a reference volume differently oriented. Looking at the exporter code the transform does not need to be hardened. Just make sure its Z axis points to the direction perpendicular to the contours you want. Please note that this volume will be exported to DICOM as well.</p>

---
