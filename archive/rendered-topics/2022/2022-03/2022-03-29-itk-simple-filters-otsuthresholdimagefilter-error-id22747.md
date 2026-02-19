---
topic_id: 22747
title: "Itk Simple Filters Otsuthresholdimagefilter Error"
date: 2022-03-29
url: https://discourse.slicer.org/t/22747
---

# ITK Simple Filters - OtsuThresholdImageFilter Error

**Topic ID**: 22747
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/itk-simple-filters-otsuthresholdimagefilter-error/22747

---

## Post #1 by @Michele_Bailo (2022-03-29 13:09 UTC)

<p>Hi there,</p>
<p>Operating system:window10<br>
Slicer version: 4.13.0-2021-12-22 r30513 / 0a65de7</p>
<p>I’m trying to perform an Otsu thresholding inside a tumor mask (LabelMap 0/1) using the OtsuThresholdImageFilter in ITK Simple Filters, but it keeps ending in this error.</p>
<p><em>Exception thrown in SimpleITK OtsuThresholdImageFilter_Execute: D:\D\P\Slicer-0-build\SimpleITK\Code\Common\include\sitkProcessObject.h:354:</em><br>
<em>sitk::ERROR: Failure to convert SimpleITK image of dimension: 3 and pixel type: “16-bit signed integer” to ITK image of dimension: 3 and pixel type: “8-bit unsigned integer”!</em></p>
<p>I also tried to change the pixel type of the original scalar volume in different types using ResampleImageFilter function, but it doesn’t work either.<br>
Am I doing something wrong or it is a bug?</p>
<p>thank you very much</p>
<p>M<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36f4473fc2a0dc5fee2b241301302766299676e.jpeg" data-download-href="/uploads/short-url/rSTuKKbAYa7WFEpQpI7ffba9Rqm.jpeg?dl=1" title="Screen Shot 2022-03-29 at 14.56.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36f4473fc2a0dc5fee2b241301302766299676e_2_690x403.jpeg" alt="Screen Shot 2022-03-29 at 14.56.24" data-base62-sha1="rSTuKKbAYa7WFEpQpI7ffba9Rqm" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36f4473fc2a0dc5fee2b241301302766299676e_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36f4473fc2a0dc5fee2b241301302766299676e_2_1035x604.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36f4473fc2a0dc5fee2b241301302766299676e_2_1380x806.jpeg 2x" data-dominant-color="6B6B6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-03-29 at 14.56.24</span><span class="informations">1920×1124 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-03-29 13:35 UTC)

<p>You can try Cast Scalar Volume instead.</p>

---

## Post #3 by @mau_igna_06 (2022-03-29 13:40 UTC)

<p>I think you could also prefix the <a href="https://simpleitk.org/doxygen/v2_1/html/classitk_1_1simple_1_1CastImageFilter.html" class="inline-onebox">SimpleITK: itk::simple::CastImageFilter Class Reference</a> to your pipeline</p>

---
