---
topic_id: 41164
title: "Importing 2D Time Series"
date: 2025-01-20
url: https://discourse.slicer.org/t/41164
---

# Importing 2D-time series 

**Topic ID**: 41164
**Date**: 2025-01-20
**URL**: https://discourse.slicer.org/t/importing-2d-time-series/41164

---

## Post #1 by @dehnjo54 (2025-01-20 13:47 UTC)

<p>Hello,<br>
I am new to 3D Slicer and want to work on Segmentation of 2D-time-Series. I have multiple Dicom Studies where the same slice is captured in CT at multiple (&gt;100) time steps, varying from 60s to 3s per step. When I import the Dicom files into Slicer, the order of  the time steps is completely random and i cannot scroll through time steps but through dimension z in steps of 1 mm. I have played with various settings in the Dicom Setup and used different plugins (scalar, volume, multivolume) but I cannot get the import to work correctly. The only workaround I found is to export the slices in .tiff and import as data, but I would like to keep the Dicom file format. All other Dicom viewer i tried are automatically importing the files in the right order.<br>
I am working with Slicer 5.7.0 on Linux and Mac.</p>
<p>I would appreciate any help and tips to get a correct import of the files.<br>
Thanks in advance and greeting!</p>
<p>edit: I get this warning when importing the Dicom files<br>
9: Key Images [Scalar Volume]: Image slices are not equally spaced (0 spacing was expected, 39.9219 spacing was found between files /home/…/…/…/CT000371 and …/…/…/…/CT000341).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.</p>

---

## Post #2 by @lassoan (2025-01-20 14:03 UTC)

<p>Slicer attempts to reconstruct 3D volumes from the set of slices dispersed in space, time, and other parameywr spaces, while most other viewers just regurgitate slices in the order they were acquired. We have tested this time sequence imoort with dozens of scanners and imaging protocols but there are of course it is always possible to come up with new, unexpected ways of organizing data.</p>
<p>The easiest would be if you could share an anonymized data set and we could test and tune the DICOM import plugins with it.</p>

---
