# NRRD or SEG.NRRD 

**Topic ID**: 17757
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/nrrd-or-seg-nrrd/17757

---

## Post #1 by @GuoFeng_Lv (2021-05-24 12:27 UTC)

<p>I used 3dslicer to annotate some data. When exporting, there are two formats, seg.nrrd and nrrd. I want to know the difference between the two. If you use python’s simpleITK to read, will the result be different?</p>

---

## Post #2 by @lassoan (2021-05-26 04:48 UTC)

<p>There is no difference between the contents of the two files. Composite file extensions are used by Slicer as hints for deciding on how the file should be interpreted by default.</p>
<p>For example, voxels of a volume can be interpreted as grayscale values (Volume), label values (Segmentation), displacement values (Transform), etc. The composite file extension <code>.seg.nrrd</code> indicates that by default the file should be offered to be loaded as segmentation (“Segmentation” is the default selection in “Description” column in “Add data” dialog).</p>

---
