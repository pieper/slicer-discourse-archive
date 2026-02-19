---
topic_id: 14474
title: "Different Between Crop Volume And Segmentation Geometry"
date: 2020-11-07
url: https://discourse.slicer.org/t/14474
---

# Different between Crop Volume and Segmentation geometry

**Topic ID**: 14474
**Date**: 2020-11-07
**URL**: https://discourse.slicer.org/t/different-between-crop-volume-and-segmentation-geometry/14474

---

## Post #1 by @Andreas (2020-11-07 16:15 UTC)

<p>Hello all,</p>
<p>what is the difference between the two modules: Crop Volume and Segmentation geometry. (see image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9619d9751c17d7b4f8bc14d67245747ae52719f.jpeg" data-download-href="/uploads/short-url/zA81TxTBGPZlhcKBHyEzOGxJiVx.jpeg?dl=1" title="Different between Crop Volume and Segmentation geometry" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9619d9751c17d7b4f8bc14d67245747ae52719f_2_690x325.jpeg" alt="Different between Crop Volume and Segmentation geometry" data-base62-sha1="zA81TxTBGPZlhcKBHyEzOGxJiVx" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9619d9751c17d7b4f8bc14d67245747ae52719f_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9619d9751c17d7b4f8bc14d67245747ae52719f_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9619d9751c17d7b4f8bc14d67245747ae52719f.jpeg 2x" data-dominant-color="F3F4F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Different between Crop Volume and Segmentation geometry</span><span class="informations">1271×599 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Both can be used to adjust the spacing. What exactly is the difference?</p>
<p>best regards</p>

---

## Post #2 by @lassoan (2020-11-10 21:03 UTC)

<p>Crop volume crops and resamples <em>volume nodes</em>. Segmentation geometry feature is for resampling <em>segmentation nodes</em>.</p>

---

## Post #3 by @bserrano (2022-09-08 13:28 UTC)

<p>Hi,</p>
<p>I am struggling with those two modules as well. Which one is better to achieve maximum accuracy when segmenting (using threshold, local threshold…). Changing segmentation geometry to 1.1 takes much longer than segmenting a cropped volume with 0.9. Why is that?</p>

---

## Post #4 by @lassoan (2022-09-10 12:13 UTC)

<p>Crop volume has not much to do with image segmentation. You can use it to prepare your image for segmentation: reduce the image size to the region of interest (to reduce memory need and computation time during segmentation) and make it possible to segment smaller details (by making image spacing isotropic and slightly smaller than the original image).</p>
<p>You can then segment the image using Segment Editor.</p>
<p>Metrics on the segmentation can be computed using Segment Statistics, or specialized modules such as Segment Geometry, Vessel Modelling Toolkit (VMTK), etc.</p>

---

## Post #5 by @bserrano (2022-09-12 11:23 UTC)

<p>OK, thank you. I understand the purpose of crop volume but what is the point of defining a new geometry when segmenting? I understand that the image is not modified when doing an oversampling factor &gt; 1, so how does the segment change?</p>

---
