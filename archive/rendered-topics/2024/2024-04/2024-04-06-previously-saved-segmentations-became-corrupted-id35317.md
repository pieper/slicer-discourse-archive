# Previously saved segmentations became corrupted

**Topic ID**: 35317
**Date**: 2024-04-06
**URL**: https://discourse.slicer.org/t/previously-saved-segmentations-became-corrupted/35317

---

## Post #1 by @Reza (2024-04-06 02:32 UTC)

<p>Hi,</p>
<p>When I try to load previously saved segmentations (saved 1-2 years ago in nifti format) in 3D-Slicer, the segmentation appears corrupted. What can I do to make them right again? More importantly, what should I do to prevent this from happening in the future?</p>
<p>Thank you all in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/807594679cf7e7cf7c7348bdfb5f36d0b0483727.jpeg" data-download-href="/uploads/short-url/ikp1PGJTOCSohwskXkhk0iHqk99.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/807594679cf7e7cf7c7348bdfb5f36d0b0483727_2_230x500.jpeg" alt="image" data-base62-sha1="ikp1PGJTOCSohwskXkhk0iHqk99" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/807594679cf7e7cf7c7348bdfb5f36d0b0483727_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/807594679cf7e7cf7c7348bdfb5f36d0b0483727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/807594679cf7e7cf7c7348bdfb5f36d0b0483727.jpeg 2x" data-dominant-color="6B6F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">239×519 27.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-04-06 04:12 UTC)

<p>The segmentation looks good. What you see is that the slice view orientation is not aligned with the segmentation axes. Since the discrete values in a labelmap cannot be interpolated for rendering it is normal to see this kind of banding. You can safely ignore it, but if you don’t want to see it at all then snap the slice view orientation to the segmentation axes (e.g., select the segmentation in Segment Editor module and click the warning icon).</p>

---

## Post #3 by @Reza (2024-04-06 16:15 UTC)

<p>Thank you for your response. The problem that I am facing is not because of displacement of the labels on the original image. As you can see the sharp edges and clear cuts, some parts of segmentations and even original image are missing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7ec6b8acb6a79e09e438e5b77c47775cc52778.jpeg" data-download-href="/uploads/short-url/xsrlo1xas15z3Yb4sjczaDXjqZi.jpeg?dl=1" title="IMG_5087" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7ec6b8acb6a79e09e438e5b77c47775cc52778_2_230x500.jpeg" alt="IMG_5087" data-base62-sha1="xsrlo1xas15z3Yb4sjczaDXjqZi" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7ec6b8acb6a79e09e438e5b77c47775cc52778_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7ec6b8acb6a79e09e438e5b77c47775cc52778_2_345x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7ec6b8acb6a79e09e438e5b77c47775cc52778_2_460x1000.jpeg 2x" data-dominant-color="161413"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_5087</span><span class="informations">1179×2556 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b46326657c0b7459e55c9f8743ba3f769de533.jpeg" alt="IMG_5085" data-base62-sha1="7noPoIs3WXhdsoPeiEPbHgKton9" width="193" height="147"></p>

---

## Post #4 by @pieper (2024-04-06 16:21 UTC)

<p>These links might help:</p>
<p><a href="https://discourse.slicer.org/t/segmenting-in-a-rotated-volume/29147">https://discourse.slicer.org/t/segmenting-in-a-rotated-volume/29147</a></p>
<p><a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---
