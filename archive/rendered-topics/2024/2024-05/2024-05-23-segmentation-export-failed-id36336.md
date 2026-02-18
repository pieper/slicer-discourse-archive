# Segmentation Export Failed

**Topic ID**: 36336
**Date**: 2024-05-23
**URL**: https://discourse.slicer.org/t/segmentation-export-failed/36336

---

## Post #1 by @milly (2024-05-23 00:35 UTC)

<p>Hi guys,</p>
<p>I have segmented a CT using MONAI Label Whole Body Segmentator. I then installed the Quantitative Reporting extension and attempted to save the segmentation as a DICOMSegmentation, but I got the following error: Segmentation object export failed (screenshot provided below) Not sure how to go about resolving this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14251b4d352142096e6cb39759fc16c4539167b4.jpeg" data-download-href="/uploads/short-url/2Sd36kjeqvL65SgN7jBZRmG08oA.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14251b4d352142096e6cb39759fc16c4539167b4_2_690x57.jpeg" alt="error" data-base62-sha1="2Sd36kjeqvL65SgN7jBZRmG08oA" width="690" height="57" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14251b4d352142096e6cb39759fc16c4539167b4_2_690x57.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14251b4d352142096e6cb39759fc16c4539167b4_2_1035x85.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14251b4d352142096e6cb39759fc16c4539167b4_2_1380x114.jpeg 2x" data-dominant-color="DAD3CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×161 70.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-05-23 03:28 UTC)

<p>I’ve improved the instructions for DICOM Segmentation Object export. Please use the latest Slicer Stable Release or latest Slicer Preview Release and follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#dicom-export">these steps</a>.</p>

---
