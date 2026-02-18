# Is output curve from Curved Planar Reformat available?

**Topic ID**: 37318
**Date**: 2024-07-11
**URL**: https://discourse.slicer.org/t/is-output-curve-from-curved-planar-reformat-available/37318

---

## Post #1 by @Hwi_Kwon (2024-07-11 03:33 UTC)

<p>I am using curved planar reformation to verify if the centerline I am labeling accurately follows the coronary artery.<br>
I would like to know if it is possible to visualize the output curve (straightened line) after applying the curved planar reformation.<br>
This would help me identify the specific areas where I need to modify the curve to ensure it passes through the center of the artery correctly.</p>
<p>Any assistance would be greatly appreciated. Thank you in advance.</p>

---

## Post #2 by @lassoan (2024-07-11 04:38 UTC)

<p>Yes, sure, you can apply the computed straightening transform to any data - image, model, segmentation, curve, … including the input curve.</p>

---

## Post #3 by @Hwi_Kwon (2024-07-11 04:49 UTC)

<p>After applying the curved planar reformation, the results look align well with my expectations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4931b0f47e28707d06dc4bd98c47c1387590160.jpeg" data-download-href="/uploads/short-url/ukwozaZw6tmP1i4nYIKwbCdG932.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4931b0f47e28707d06dc4bd98c47c1387590160_2_690x433.jpeg" alt="image" data-base62-sha1="ukwozaZw6tmP1i4nYIKwbCdG932" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4931b0f47e28707d06dc4bd98c47c1387590160_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4931b0f47e28707d06dc4bd98c47c1387590160_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4931b0f47e28707d06dc4bd98c47c1387590160_2_1380x866.jpeg 2x" data-dominant-color="3B3B46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1949×1225 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I attempt to apply a straightening transform to the centerline, the output does not seem to accurately reflect the intended transformation. I’m wondering if there might be an issue with my approach or if I’m missing a crucial step in the process.![image|690x433]</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3632d47963548eb0482ca6618d7e4d25cc127f.jpeg" data-download-href="/uploads/short-url/qziVCvbiBbtpF1VqmPloQdHxOQn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3632d47963548eb0482ca6618d7e4d25cc127f_2_690x433.jpeg" alt="image" data-base62-sha1="qziVCvbiBbtpF1VqmPloQdHxOQn" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3632d47963548eb0482ca6618d7e4d25cc127f_2_690x433.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3632d47963548eb0482ca6618d7e4d25cc127f_2_1035x649.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba3632d47963548eb0482ca6618d7e4d25cc127f_2_1380x866.jpeg 2x" data-dominant-color="3C3B46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1949×1225 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I followed the tutorial from <a href="https://www.youtube.com/watch?v=WJQexDTiRRc" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=WJQexDTiRRc</a></p>

---
