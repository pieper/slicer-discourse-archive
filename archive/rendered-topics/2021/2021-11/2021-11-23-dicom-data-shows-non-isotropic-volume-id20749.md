# dicom data shows non isotropic volume

**Topic ID**: 20749
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/dicom-data-shows-non-isotropic-volume/20749

---

## Post #1 by @SONALIGHAICHOUDHURY (2021-11-23 13:36 UTC)

<p>Operating system: carestream, my cs3D imaging system shows non isotropic volume of dicom data imported from new tom slicer. why? i am unable to use my cs software for analysis.</p>

---

## Post #2 by @lassoan (2021-11-23 18:32 UTC)

<p>Non-isotropic data (different spacing along different axis) is very common in medical imaging. It is very surprising that a medical imaging software refuses to work with such data.</p>
<p>However, if Carestream3D software is really so limited then you can work around its problems in Slicer, by resampling the image in Slicer before exporting it to DICOM. You can use Crop volume module with the “Isotropic spacing” option enabled to resample the volume to be isotropic.</p>

---
