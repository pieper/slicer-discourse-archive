# Why does the shape of the image change?

**Topic ID**: 4192
**Date**: 2018-09-26
**URL**: https://discourse.slicer.org/t/why-does-the-shape-of-the-image-change/4192

---

## Post #1 by @zgk110 (2018-09-26 11:05 UTC)

<p>Hi, I read a MRI series image by Simpleitk and the shape of it is (168L, 640L, 640L).<br>
However, when i use the 3D slicer to read the same image, the shape of the image is changed to (24L, 640L, 640L), meanwhile, I find that the image read by the Simpleitk just have many same slices (7 times repeated for each slice ).<br>
I don’t know whether the 3D slicer does some pre-processing to merge the repeated slices to one or some else operations, so can anyone give any advice?</p>

---

## Post #2 by @lassoan (2018-09-26 14:23 UTC)

<p>Slicer’s DICOM reader uses the same reader as ITK (SimpleITK) at the lowest level, but it does a lot of additional pre-processing (determine how to group and order slices) and post-processing (apply necessary warping to correct any geometrical issues).</p>

---
