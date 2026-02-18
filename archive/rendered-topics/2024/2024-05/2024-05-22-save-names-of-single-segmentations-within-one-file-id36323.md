# Save names of single segmentations within one file

**Topic ID**: 36323
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/save-names-of-single-segmentations-within-one-file/36323

---

## Post #1 by @hfri (2024-05-22 13:21 UTC)

<p>When I export multiple segmentations within one .nii file, and reopen it, the initial names of the segments are lost. Is there any way to save the names of the segments? Thanks</p>

---

## Post #2 by @cpinter (2024-05-22 13:31 UTC)

<p>The Slicer-native format for saving segmentations is <code>.seg.nrrd</code>. It is expected to suffer data loss when exporting to other formats.</p>

---

## Post #3 by @lassoan (2024-05-22 13:33 UTC)

<p>First of all, I would not recommend using NIFTI files, ever. They have some advantages compared to general-purpose file formats if you store brain MRI images (they can store some MR imaging specific fields), but they are really bad for any other purpose. It is an unnecessarily complex yet extremely limited file format. For example, it has two ways to store image orientation (which can make interpretation if NIFTI images ambiguous), but it cannot store simple extra metadata like segment names.</p>
<p>I would recommend to use NRRD file format to store the segmentations. It is a very simple file format yet it allows saving custom information, such as segment names and colors.</p>
<p>If you want to create segmentations with archival quality (so that you can use it several years later, or the segmentations can be used in multiple projects) then you can use standard terminology (double-click on the colored box next to the segment name). When you want to use the segmentation for training a network, you can use slicerio Python package to specify what label value should be used for what segment as shown in this <a href="https://github.com/lassoan/slicerio?tab=readme-ov-file#extract-segments-by-name">example</a>.</p>

---

## Post #4 by @hfri (2024-05-22 16:31 UTC)

<p>Makes sense, thanks a lot!</p>

---
