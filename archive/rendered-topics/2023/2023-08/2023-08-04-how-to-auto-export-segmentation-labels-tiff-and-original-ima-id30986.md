# How to auto export Segmentation-Labels.tiff and Original images from .mrb file?

**Topic ID**: 30986
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/how-to-auto-export-segmentation-labels-tiff-and-original-images-from-mrb-file/30986

---

## Post #1 by @Jeff_Boker (2023-08-04 19:13 UTC)

<p>I have several .mrb files which contain images and segmentation annotations. I currently manually open the .mrb file in 3D slicer and then go to “Data” → “Export visible segments to binary labelmap” → “Save” and then select “Tiff” for the export format for the segmentations. However since there are so many .mrb files, I was wondering if there is an automatic way of exporting all the data quicker.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-08-05 10:35 UTC)

<p>You can write a Python script to automate this. Probably all the necessary steps are described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> but if there is anything specific that you cannot find then you can ask here.</p>

---
