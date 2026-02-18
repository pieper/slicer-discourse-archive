# How to save dicom files optimized by 3D Slicer

**Topic ID**: 30861
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/how-to-save-dicom-files-optimized-by-3d-slicer/30861

---

## Post #1 by @nikanika (2023-07-28 17:30 UTC)

<p>We found that the edge of the dicom file in 3d slcier is smoother than that of other software such as itk, and we learned that this is because 3d slcier has interpolated it. We want to export the processed image. But it seems that the exported file is no different from the original file.</p>
<p>Is there any senior who can guide us how to export the processed file successfully?</p>

---

## Post #2 by @lassoan (2023-07-28 20:26 UTC)

<p>Interpolation that is used during image display does not change the image content, it is just used for resampling the input image at the display’s resolution on-the-fly. If you want to change the image content then you can resample it, for example using <code>Resample Scalar Volume</code> module.</p>
<p>Note that ITK is a toolkit, not an application. It cannot do any visualization, just processing. There are various tools that can display images that are loaded and processed by ITK, but each work completely differently. Do you mean ITK-Snap? It does not use interpolation by default but you can enable in lienar interpolation in Tools / Preferences / Slice views / Display.</p>

---
