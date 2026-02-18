# Segmentation of Mitral Valve from TEE

**Topic ID**: 19285
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/segmentation-of-mitral-valve-from-tee/19285

---

## Post #1 by @HodaJavadi (2021-08-20 15:36 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Show the multi-plane images to be able to segment the Mitral Valve<br>
Actual behavior: Doesn’t show the multiplane images properly</p>
<p>Super new to Slicer! The TEE echo had done the 3D reconstruction of mitral valve and the volume render is saved. However, when I import the DICOM dataset, it shows each image separately and not coordinated with each other. How can I fix this?</p>

---

## Post #2 by @lassoan (2021-08-20 18:06 UTC)

<p>You can import some 4D TEE volume sequences using <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">SlicerHeart extension</a>. What is the vendor, model, year of your ultrasound system and what transducer do you use?</p>

---
