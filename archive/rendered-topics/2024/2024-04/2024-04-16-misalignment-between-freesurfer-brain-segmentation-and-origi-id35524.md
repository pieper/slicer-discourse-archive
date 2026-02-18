# Misalignment between Freesurfer brain segmentation and original T1 images

**Topic ID**: 35524
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/misalignment-between-freesurfer-brain-segmentation-and-original-t1-images/35524

---

## Post #1 by @pablomac7 (2024-04-16 12:03 UTC)

<p>Slicer version: 5.6.1</p>
<p>Hello,</p>
<p>I am having problems when exporting a brain segmentation as a .seg.nrrd file, previously imported into 3D Slicer from Freesurfer. When I import the segmentation and the original MRI images into 3D slicer using FreeSurfer Importer, the alignment between both looks correct. However, when I try to export the segmentation as a .seg.nrrd file, the dimensions of the file (256,256,256) do not match those of the original MRI (192,240,256). I think this 256^3 cube is the default output format in Freesurfer, but I was wondering if it was possible to export the aligned segmentation directly from 3D slicer, as Slicer seems to align it perfectly. I read in another post that it is possible to do so by selecting the original images as the reference volume, but the exported .seg.nrrd file still contains a matrix with 256^3 shape. I would be super grateful for any pointers.</p>
<p>Best,</p>
<p>Pablo</p>

---

## Post #2 by @lassoan (2024-04-16 12:08 UTC)

<p>3D Slicer uses the same geometry (origin, spacing, axis directions, extents) for segmentation as the source volume. Therefore, if your input volume was 256 x 256 x 256 size then the segmentation will use that size by default. If for some reason the geometry does not match (e.g., becasue you selected a different image first, you chose the option to crop to minimum necessary size on save, you created a segmentation in an older Slicer version where we cropped to minimum necessary size by default, etc.) then you can very easily change it using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">Specify geometry</a> feature.</p>

---

## Post #3 by @pablomac7 (2024-04-16 12:20 UTC)

<p>Dear Andras,</p>
<p>Thank you so much for your answer, this is exactly what I needed. I hope this information will be useful to others as well.</p>
<p>Best,</p>
<p>Pablo</p>

---
