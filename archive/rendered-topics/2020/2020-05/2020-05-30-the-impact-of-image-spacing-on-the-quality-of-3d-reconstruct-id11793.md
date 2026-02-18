# The impact of image spacing on the quality of 3D reconstruction

**Topic ID**: 11793
**Date**: 2020-05-30
**URL**: https://discourse.slicer.org/t/the-impact-of-image-spacing-on-the-quality-of-3d-reconstruction/11793

---

## Post #1 by @loubna (2020-05-30 07:23 UTC)

<p>Hi;<br>
I understand that this can be a very basic VTK image processing question. But, I would know what is the imapct of SetSpacing values in 3D image using vtkImageData on the quality of reconstructed model. The default values are (1.0,1.0,1.0), in Other examples, they set the spacing to (0.5,0.5,0.5) or use specific formula to compute the spacing. What is the impact on  reconstructed surfaces? the wrong values can deform the quality of the reconstructed model?.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-05-31 01:08 UTC)

<p>For visualization, you normally use the native spacing of an image (as it was acquired by the imaging device). For segmentation or analysis it often makes sense to resample voxel arrays to be isotropic; and if you want to represent features that are smaller then the voxel spacing (such as segmenting a thin membrane) then you may need to oversample the image by up to a factor of 2-4x.</p>

---
