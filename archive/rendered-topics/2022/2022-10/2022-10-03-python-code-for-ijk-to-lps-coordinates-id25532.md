# Python code for ijk_to_lps coordinates?

**Topic ID**: 25532
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/python-code-for-ijk-to-lps-coordinates/25532

---

## Post #1 by @dj_96 (2022-10-03 15:59 UTC)

<p>Hi, I have a 3d model in lps that corresponds to a few ct views. I saw that there’s a affine transformation from the image ijk (dicom) to the lps coordinates <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="noopener nofollow ugc">Coordinate systems - Slicer Wiki</a></p>
<p>I’m trying to map the lps coordinate on the model to the ct views(axial, coronal, sagittal), I looked at my sample files manually and it looks like everything matches up if I took from the same orientation on the 3d model(say axial), translate x,y based on the image patient position, and then get the mm distance from pixel spacing to get the same coordinate space in lps. Is there python code that does the affine transformation available somewhere?</p>

---

## Post #2 by @pieper (2022-10-03 16:28 UTC)

<p>There are examples similar to this in the script repository.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates</a></p>

---
