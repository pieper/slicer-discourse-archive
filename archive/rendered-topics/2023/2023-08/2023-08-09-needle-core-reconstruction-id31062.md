---
topic_id: 31062
title: "Needle Core Reconstruction"
date: 2023-08-09
url: https://discourse.slicer.org/t/31062
---

# Needle Core Reconstruction

**Topic ID**: 31062
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/needle-core-reconstruction/31062

---

## Post #1 by @Basil_Kaufmann (2023-08-09 11:30 UTC)

<p>Hi all,</p>
<p>I’m trying to reconstruct biopsy needle cores in segmentation editor. The underlying data is a VTP file. It shows me the segmentation of the core and prostate per slice, but I’m not able to connect them to make a 3d volume (see attached image).</p>
<p>Is there any solution for this problem?</p>
<p>Many thanks in advance.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33563b7c1fd07acb5e0d4ae8fda8871c12f8e218.png" alt="image" data-base62-sha1="7k96nQxtSrQpjVEK9qpe6ypeNwQ" width="489" height="338"></p>

---

## Post #2 by @lassoan (2023-08-09 11:41 UTC)

<p>If you load these contours as a segmentation in “parallel contours” representation then conversion to a 3D “closed surface” representation is done automatically.</p>
<p>If you have control over how the .vtp files are generated then I would recommend to save it directly as a segmentation file: a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html#segmentation-surface-file-format-seg-vtm">multiblock (.vtm) file with the required metadata fields</a>.</p>
<p>If you need to use the .vtk files without changing them then you can write an importer script that constructs the segmentation node from the contours, similarly as it is done in <a href="https://github.com/PerkLab/SlicerSandbox/blob/e163d61c5babc25f53badb87f64cf4d123243c36/ImportOsirixROI/ImportOsirixROI.py#L348-L382">this importer</a>.</p>

---
