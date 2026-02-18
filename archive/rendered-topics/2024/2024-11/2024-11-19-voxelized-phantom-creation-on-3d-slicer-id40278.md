# Voxelized phantom creation on 3D slicer

**Topic ID**: 40278
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/voxelized-phantom-creation-on-3d-slicer/40278

---

## Post #1 by @imbeatriz (2024-11-19 22:10 UTC)

<p>Hello everyone,</p>
<p>I am currently working on constructing a patient-specific phantom for <a href="https://opengate.readthedocs.io/en/latest/introduction.html" rel="noopener nofollow ugc">GATE simulations</a>. I’ve uploaded a CT image and segmented the regions of interest using the TotalSegmentator module. The resulting segmentations were saved as STL files. However, I would prefer to convert these segmentations into a voxelized format, such as interfile, analyse, dicom or metaimage format, as these are more compatible and easier to use in GATE for my simulations.</p>
<p>Could anyone guide me on how to achieve this conversion using 3D Slicer?</p>
<p>Your help would be greatly appreciated!</p>
<p>Best regards,<br>
Beatriz</p>

---

## Post #2 by @pieper (2024-11-19 22:41 UTC)

<p>If you convert the segmentation to a labelmap (right click on Segmentation in Data module and pick export to binary labelmap) then  you can save in metaimage format directly (right click on labelmap and pick export to file and pick mha or mhd format).</p>

---

## Post #3 by @imbeatriz (2024-11-20 18:29 UTC)

<p>Thank you for explaining!</p>

---

## Post #4 by @lassoan (2024-11-20 21:16 UTC)

<p>Also note that if the source representation is “binary labelmap” (this is usually the case) and you save the segmentation then it is already saved in “voxelized” format in NRRD file format.</p>
<p>NRRD file format is very similar to MHA (metaimage) and NIFTI, but we prefer NRRD because MHA does not have a standard way of specifying image dimensions and image orientation; and NIFTI has ambiguities in image orientation specification and cannot store arbitrary additional metadata.</p>

---
