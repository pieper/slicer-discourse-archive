# PETCT（Import image）

**Topic ID**: 17503
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/petct-import-image/17503

---

## Post #1 by @lcj (2021-05-07 10:58 UTC)

<p>Hi ,<br>
I use the 4.11 version of 3DSlicer and have read the official documents. I want to know if I can import the CT image first, and then import the PET image for fusion instead of importing the .mrb file when doing PETCTFusion. If so, is there a tutorial?<br>
Looking forward to your reply。</p>

---

## Post #2 by @pieper (2021-05-07 14:00 UTC)

<p>Unfortunately there’s no tutorial as far as I know.  Best suggestion is to install the PETDICOM extension and use the DICOM module to load both PET and CT.  From there you can use the standard viewing, segmentation, and quantification tools.</p>

---
