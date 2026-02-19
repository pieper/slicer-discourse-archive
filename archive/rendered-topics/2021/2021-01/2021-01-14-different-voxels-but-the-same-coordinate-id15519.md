---
topic_id: 15519
title: "Different Voxels But The Same Coordinate"
date: 2021-01-14
url: https://discourse.slicer.org/t/15519
---

# Different voxels, but the same coordinate?

**Topic ID**: 15519
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/different-voxels-but-the-same-coordinate/15519

---

## Post #1 by @Yasuhiro_TAKEDA (2021-01-14 07:44 UTC)

<p>Hi</p>
<p>There are two MRI images, and the pointers in these two images indicate two different voxels which is adjacent. However, data probe shows the same coordinate, (115,134,63), and the same intensity, 2870.</p>
<p>When importing dicom images, 3D slicer perform automatic resample?<br>
I would like to have native images without resample. How could I do that?</p>
<p>Sorry for my poor english writing.<br>
Thank you in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33d52a224e53af396ff476f0384b29f12d8b93f8.png" data-download-href="/uploads/short-url/7ox3lCA80RVdO5LpTCfOoKqG25G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d52a224e53af396ff476f0384b29f12d8b93f8_2_690x328.png" alt="image" data-base62-sha1="7ox3lCA80RVdO5LpTCfOoKqG25G" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d52a224e53af396ff476f0384b29f12d8b93f8_2_690x328.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d52a224e53af396ff476f0384b29f12d8b93f8_2_1035x492.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33d52a224e53af396ff476f0384b29f12d8b93f8_2_1380x656.png 2x" data-dominant-color="F2F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2020×963 96.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26ad3cbeb779cc88afbfbbae8fbb53c8872cf89e.png" data-download-href="/uploads/short-url/5w9iMUYsTbPgoiu1VD0VQE7zChg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ad3cbeb779cc88afbfbbae8fbb53c8872cf89e_2_690x335.png" alt="image" data-base62-sha1="5w9iMUYsTbPgoiu1VD0VQE7zChg" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ad3cbeb779cc88afbfbbae8fbb53c8872cf89e_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ad3cbeb779cc88afbfbbae8fbb53c8872cf89e_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ad3cbeb779cc88afbfbbae8fbb53c8872cf89e_2_1380x670.png 2x" data-dominant-color="F2F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2003×974 91.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-01-14 20:16 UTC)

<p>Yes, by default Slicer does linear interpolation.  You can turn this off for a volume <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">with the slice view interpolate button</a>.</p>

---

## Post #3 by @lassoan (2021-01-14 20:39 UTC)

<p>Also note that the segmentation node’s internal binary labelmap representation does not have to have the same geometry (origin, spacing, axis directions) as the current master volume (one voxel of the master volume does not have to correspond to one voxel in the segmentation). Segmentation’s binary labelmap representation is initialized by default using the master volume that you select first, but you can later change it as needed.</p>

---

## Post #4 by @Yasuhiro_TAKEDA (2021-01-15 00:47 UTC)

<p>Thank you for your all kindness!</p>
<p>Why does 3D slicer recommend to keep interpolation enabled?</p>
<p>I am interested in Radiomics extension of 3D slicer, that is a method in the medical field that extracts a large number of features from using data-characterisation algorithms. Like, the quantification of tumor malignancy from medical images.</p>
<p>Radiomics is sensitive to data handling. Therefore, interpolation should be cared because interpolation may change the texture of medical image, or change the intensity at each voxels. If the texture or intensity of medical image change, the features from Radiomics also change.</p>
<p>Do you think that interpolation method should be off when using Radiomics extension?</p>
<p>Thank you,</p>

---

## Post #5 by @pieper (2021-01-15 01:29 UTC)

<p>Hi - The interpolation is only in the display pipeline so it will not impact your radiomics calculations.  We have it on by default to avoid aliasing artifacts.</p>

---

## Post #6 by @Yasuhiro_TAKEDA (2021-01-15 01:33 UTC)

<p>Thank you so much!!!</p>

---

## Post #7 by @Yasuhiro_TAKEDA (2021-01-15 01:47 UTC)

<p>Sorry, one extra question.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d16d8ffb14e0722ca178019e8c51182e33fb5720.jpeg" data-download-href="/uploads/short-url/tSGwICr1MTYiWT58JCYv20DRE76.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d16d8ffb14e0722ca178019e8c51182e33fb5720_2_678x499.jpeg" alt="1" data-base62-sha1="tSGwICr1MTYiWT58JCYv20DRE76" width="678" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d16d8ffb14e0722ca178019e8c51182e33fb5720_2_678x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d16d8ffb14e0722ca178019e8c51182e33fb5720_2_1017x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d16d8ffb14e0722ca178019e8c51182e33fb5720_2_1356x998.jpeg 2x" data-dominant-color="43444E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2304×1697 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58ec919460204373b8cd4f31685c8ca2abd03196.jpeg" data-download-href="/uploads/short-url/cGERx3sDZgF0f29HosS8dDM9LnM.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ec919460204373b8cd4f31685c8ca2abd03196_2_674x500.jpeg" alt="2" data-base62-sha1="cGERx3sDZgF0f29HosS8dDM9LnM" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ec919460204373b8cd4f31685c8ca2abd03196_2_674x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ec919460204373b8cd4f31685c8ca2abd03196_2_1011x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58ec919460204373b8cd4f31685c8ca2abd03196_2_1348x1000.jpeg 2x" data-dominant-color="44454F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2304×1709 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When using paint function of segment editor, it sometimes doesn’t work well. Please refer to the two pictures I have attached. （Selected the paint function and left-clicked once on the image. Then, striped-pattern of ROI appeared.)<br>
Does this phenomenon relate to interpolate function?</p>

---

## Post #8 by @lassoan (2021-01-15 01:53 UTC)

<p>This is expected when you paint on oblique slices. See detailed explanation here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>

---

## Post #9 by @Yasuhiro_TAKEDA (2021-01-15 01:58 UTC)

<p>Thank you for teaching me a lot of things!!</p>

---
