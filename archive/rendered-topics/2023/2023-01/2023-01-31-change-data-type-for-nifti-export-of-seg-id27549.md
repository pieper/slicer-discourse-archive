# Change data type for nifti export of SEG

**Topic ID**: 27549
**Date**: 2023-01-31
**URL**: https://discourse.slicer.org/t/change-data-type-for-nifti-export-of-seg/27549

---

## Post #1 by @alireza (2023-01-31 03:11 UTC)

<p>Hi, thanks in advance</p>
<ol>
<li>Is nifti export of Segmentations in 3D Slicer, Nifti2? or Nifti1?</li>
<li>Seems like 3D Slicer uses <code>signed short</code> (16 bit) for data type of the exported nifti. Is it possible to force it to use <code>unsigned char</code> ? (2bits)</li>
</ol>
<p>PS: ITK-SNAP seems to have default data type for seg export in nifti of <code>2-Byte Unsigned Integer</code></p>

---

## Post #2 by @pieper (2023-01-31 11:05 UTC)

<p>Slicer uses ITK to save nifti and it should be nifti 1 (with 32 bit floats in the header field) but there may be options in the ITK code to export either.</p>
<p>You can change the datatype of your MRML Volume using the Cast Scalar Volume module and the nifti file should match the datatype you convert to.</p>

---
