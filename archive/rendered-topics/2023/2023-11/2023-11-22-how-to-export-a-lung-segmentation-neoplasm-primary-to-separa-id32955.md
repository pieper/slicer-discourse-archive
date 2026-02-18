# How to export a lung segmentation neoplasm primary to separately image files

**Topic ID**: 32955
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/how-to-export-a-lung-segmentation-neoplasm-primary-to-separately-image-files/32955

---

## Post #1 by @Felix_Mauricio_Varga (2023-11-22 12:22 UTC)

<p>Hi, I need to view-export only lung tumor slides to images, so how to export a neoplasm  lung segmentation to separately image files for example png.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-11-22 12:28 UTC)

<p>For presentation purposes, you can use Screen Capture module.</p>
<p>For computation you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">get the segmentation as a numpy array</a> and extract the slices of the source volume where there are segment voxels.</p>
<p>If you want to do this to generate training data for an AI model then you may consider extracting 3D regions instead of 2D slices, as putting together a 3D segmentation from independently segmented 2D slices typically leads to very poor results (too much variation between neighbor slices).</p>

---
