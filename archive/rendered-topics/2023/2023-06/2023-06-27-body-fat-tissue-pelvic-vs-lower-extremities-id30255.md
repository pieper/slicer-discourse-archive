# Body Fat Tissue_Pelvic VS Lower Extremities

**Topic ID**: 30255
**Date**: 2023-06-27
**URL**: https://discourse.slicer.org/t/body-fat-tissue-pelvic-vs-lower-extremities/30255

---

## Post #1 by @Spiros_Karkavitsas (2023-06-27 12:40 UTC)

<p>Hello</p>
<p>I am using MONAI for segmenting the body fat tissue in MR images from two different anatomical regions.Lower extremities and Pelvic region.</p>
<p>I used two separate models for each region using MONAI. For the pelvic region is fine. The problem is for the lower exremities.More specifically, as you can see from the image below, in some cases, the automatic segmentation captures both legs (axial plane) and in other treatments only capturres one out of two.</p>
<p>I have not yet used enough patients for training the algorithm , but I do not know if that is the issue or not.</p>
<p>Thank you for reading this message and if someone has an idea on it , looking forward to it.</p>
<p>Best<br>
Spiros<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f4a3eec1bd7380a07ad49dfd98ef2413451def.jpeg" data-download-href="/uploads/short-url/kGkTvxHBTNaN2MUbFtWf4SEivUP.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90f4a3eec1bd7380a07ad49dfd98ef2413451def_2_690x400.jpeg" alt="Screenshot_1" data-base62-sha1="kGkTvxHBTNaN2MUbFtWf4SEivUP" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90f4a3eec1bd7380a07ad49dfd98ef2413451def_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f4a3eec1bd7380a07ad49dfd98ef2413451def.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f4a3eec1bd7380a07ad49dfd98ef2413451def.jpeg 2x" data-dominant-color="696860"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1013×588 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Spiros_Karkavitsas (2023-06-27 21:18 UTC)

<p>Okay, apparently if I use only one label in my model (eg  body fat) in the case for the lower extremities, MONAI detects only one thigh. In the case where slices of a volume captures the upper region or the start of the pelvic then, the it captures both thighs because the thigh volume share common voxels there. In that case, MONAI considers both thighs as one volume rather than two different objects.</p>
<p>I will consider training the dataset using two labels like right/ left thigh.</p>

---
