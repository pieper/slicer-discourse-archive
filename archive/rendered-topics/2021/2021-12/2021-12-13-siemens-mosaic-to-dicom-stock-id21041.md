# Siemens mosaic to DICOM stock

**Topic ID**: 21041
**Date**: 2021-12-13
**URL**: https://discourse.slicer.org/t/siemens-mosaic-to-dicom-stock/21041

---

## Post #1 by @Pawel_Ozga (2021-12-13 22:45 UTC)

<p>Hi,</p>
<p>I’m sorry if I’m writing this question in the wrong place but I don’t know where to ask.<br>
I have an exam made on siemens MR and the DTI sequence is stored as a mosaic. Is there any way to convert the exam so that DTI is saved DICOM stock?</p>

---

## Post #2 by @pieper (2021-12-13 23:05 UTC)

<p><a href="http://dmri.slicer.org/">SlicerDMRI</a> is suggested for DTI processing.  You can use either DWIConvert or dcm2niix to convert the dicom to nrrd for processing.  Most Siemens mosaic formats are supported.</p>

---

## Post #3 by @Pawel_Ozga (2021-12-14 08:55 UTC)

<p>I’ll try, thank you Pieper</p>

---
