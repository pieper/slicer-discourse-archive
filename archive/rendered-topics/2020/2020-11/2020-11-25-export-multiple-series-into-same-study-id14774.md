# Export multiple series into same study

**Topic ID**: 14774
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/export-multiple-series-into-same-study/14774

---

## Post #1 by @marianaslicer (2020-11-25 11:50 UTC)

<p>Thank you for your help.</p>
<p>For each volume of the 4D CT data I used the Gaussian Blur Image Filter extension and added noise. Now I want to export each manipulated image into DICOM files with the same study and different series. However, when I try to export the files are created several studies. Am I doing anything wrong? Thank you again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd454593a3bf567f7d736eb0630e53df41f86e78.png" data-download-href="/uploads/short-url/r0mEFLM4IKPixFVqAhtVBHx1nE4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd454593a3bf567f7d736eb0630e53df41f86e78_2_666x500.png" alt="image" data-base62-sha1="r0mEFLM4IKPixFVqAhtVBHx1nE4" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd454593a3bf567f7d736eb0630e53df41f86e78_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd454593a3bf567f7d736eb0630e53df41f86e78_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd454593a3bf567f7d736eb0630e53df41f86e78.png 2x" data-dominant-color="C3D7E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×960 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-25 20:33 UTC)

<p>If you don’t specify study, series, and frame of reference UIDs then new ones will be generated on each export. If you want to export multiple series into the same study then specify the same StudyInstanceUID and FrameOfReferenceInstanceUID and a unique SeriesInstanceUID. We’ll make this more intuitive in the future.</p>

---
