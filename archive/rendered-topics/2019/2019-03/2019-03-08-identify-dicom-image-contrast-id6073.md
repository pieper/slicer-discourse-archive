# Identify Dicom image contrast

**Topic ID**: 6073
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/identify-dicom-image-contrast/6073

---

## Post #1 by @prorai (2019-03-08 13:13 UTC)

<p>How can i identify the level of contrast in Dicom file by just reading it using python file</p>

---

## Post #2 by @lassoan (2020-01-26 16:01 UTC)

<p>If you already loaded the DICOM file into the scene (this is most likely the case if you are converting DICOM images to nrrd files or numpy arrays for deep learning training) then you can get window/level from the volume’s display node.</p>
<p>If you only imported the data set into Slicer’s DICOM database but not loaded it then you can look up the filenames corresponding to a series and then use pydicom to retrieve DICOM fields related to intensity scaling. DICOM uses rescale/slope values and various look-up tables to specify “contrast”. Depending on what kind of images you acquired, using what scanner, and what imaging protocol, you need to use different fields.</p>

---
