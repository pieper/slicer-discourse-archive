---
topic_id: 25760
title: "Which Difference Between Direction Matrices In Vtkimagedata"
date: 2022-10-18
url: https://discourse.slicer.org/t/25760
---

# Which difference between Direction Matrices in vtkImageData and vtkMRMLScalarVolumeNode?

**Topic ID**: 25760
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/which-difference-between-direction-matrices-in-vtkimagedata-and-vtkmrmlscalarvolumenode/25760

---

## Post #1 by @Cailen (2022-10-18 15:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb414f92f347eed88eef91d6d0bce554358e9f4f.png" data-download-href="/uploads/short-url/t04QY0RdKeepUIhZDvK4btDUCZx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb414f92f347eed88eef91d6d0bce554358e9f4f_2_302x500.png" alt="image" data-base62-sha1="t04QY0RdKeepUIhZDvK4btDUCZx" width="302" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb414f92f347eed88eef91d6d0bce554358e9f4f_2_302x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb414f92f347eed88eef91d6d0bce554358e9f4f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb414f92f347eed88eef91d6d0bce554358e9f4f.png 2x" data-dominant-color="F3F3F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">348×576 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This behavior spoils the display of the results of my algorithms, because only from the VTK it is not clear where to get the same matrix as in the slicer</p>

---

## Post #2 by @lassoan (2022-10-18 16:07 UTC)

<p>vtkImageData did not store image directions for many years, so we had to store image geometry (origin, spacing, and axis directions) in the MRML node, and removed it from vtkImageData (vtkImageData origin is always set to 0,0,0 and direction is set to identity). Therefore, right now, you must get the image geometry information from the MRML node.</p>
<p>In the not too distant future (maybe within a year) we’ll update Slicer to store image geometry in the vtkImageData, which will make things simpler.</p>

---
