# Setting or Trimming Slice Range for DICOM Images

**Topic ID**: 40715
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/setting-or-trimming-slice-range-for-dicom-images/40715

---

## Post #1 by @Kowsar_Sheikhi (2024-12-16 14:29 UTC)

<p>Hi!</p>
<p>Would it be possible to define a specific range of slices for the DICOM images imported into 3D Slicer? Or perhaps trim the range of interest?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-12-16 19:26 UTC)

<p>Try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html">CropVolume</a> module to trim away unwanted parts of the image.</p>

---
