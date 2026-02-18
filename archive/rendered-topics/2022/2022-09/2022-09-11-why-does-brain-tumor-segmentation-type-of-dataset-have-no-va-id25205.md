# Why does Brain Tumor Segmentation type of dataset have no values in the array

**Topic ID**: 25205
**Date**: 2022-09-11
**URL**: https://discourse.slicer.org/t/why-does-brain-tumor-segmentation-type-of-dataset-have-no-values-in-the-array/25205

---

## Post #1 by @luna1 (2022-09-11 18:49 UTC)

<p>i have been trying to work with BRATS dataset like this one <a href="https://www.kaggle.com/datasets/andrewmvd/brain-tumor-segmentation-in-mri-brats-2015" class="inline-onebox" rel="noopener nofollow ugc">Brain Tumor Segmentation | Kaggle</a> but when i try to load it in 3d slicer then type this command in the python interpretor it tells me that the array only contains 0<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30363168c31089f025fba4f9bb73540a14a12f8.jpeg" data-download-href="/uploads/short-url/wofDPVoxGwss35Xuh79w2lDNpZ6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30363168c31089f025fba4f9bb73540a14a12f8_2_690x351.jpeg" alt="image" data-base62-sha1="wofDPVoxGwss35Xuh79w2lDNpZ6" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30363168c31089f025fba4f9bb73540a14a12f8_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30363168c31089f025fba4f9bb73540a14a12f8_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30363168c31089f025fba4f9bb73540a14a12f8_2_1380x702.jpeg 2x" data-dominant-color="2D2D2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1744×889 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-09-11 19:25 UTC)

<p>The BraTS data is skull stripped, so the entire background is zeros.  When you print a numpy array you only see the start and end of the arrays, so probably all you are seeing is background.  You can use other numpy operations, like <code>nnn.mean()</code> or <code>nnn.max()</code> to confirm there are values.</p>

---
