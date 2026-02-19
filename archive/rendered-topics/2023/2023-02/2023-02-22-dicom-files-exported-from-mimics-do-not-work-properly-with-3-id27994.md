---
topic_id: 27994
title: "Dicom Files Exported From Mimics Do Not Work Properly With 3"
date: 2023-02-22
url: https://discourse.slicer.org/t/27994
---

# Dicom files exported from mimics do not work properly with 3Dslicer

**Topic ID**: 27994
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/dicom-files-exported-from-mimics-do-not-work-properly-with-3dslicer/27994

---

## Post #1 by @spiderman (2023-02-22 22:30 UTC)

<p>Operating system:win10 Windows Feature Experience Pack 120.2212.4190.0<br>
Slicer version:5.2.1、5.3.0</p>
<p>I first trimmed the dicom file with mimics24 and exported a new dicom file, which can be opened and used in both mimics and MITK.<br>
However, in 3Dslicer it is not normal, although there is no problem with the threshold selection, but when I click “Apply”, some of the thresholds are missing and cannot be selected, and it also shows weird in volumetric rendering</p>
<p>I also researched this issue, I deliberately applied all the thresholds, and it was clear that the thresholds outside the green box were like lost</p>
<p>By the way, how do I change my avatar in the forum?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/938a4ce37bc234027af574c3ad8bb297468fcb92.jpeg" data-download-href="/uploads/short-url/l3cuHRkNZftW9BaHvSziL78nScG.jpeg?dl=1" title="2a51d28ae54b10f961fa62a7b325f7e0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938a4ce37bc234027af574c3ad8bb297468fcb92_2_690x310.jpeg" alt="2a51d28ae54b10f961fa62a7b325f7e0" data-base62-sha1="l3cuHRkNZftW9BaHvSziL78nScG" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938a4ce37bc234027af574c3ad8bb297468fcb92_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938a4ce37bc234027af574c3ad8bb297468fcb92_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938a4ce37bc234027af574c3ad8bb297468fcb92_2_1380x620.jpeg 2x" data-dominant-color="686C6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2a51d28ae54b10f961fa62a7b325f7e0</span><span class="informations">1920×864 79.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dacaaa1c69de508e5d5d3e6fdeebad006ad0d34.jpeg" data-download-href="/uploads/short-url/1WY8TqIDpDeDgaYcBRO1RAmHLpy.jpeg?dl=1" title="4b57326996595dc462323e7973ba323e" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dacaaa1c69de508e5d5d3e6fdeebad006ad0d34_2_690x388.jpeg" alt="4b57326996595dc462323e7973ba323e" data-base62-sha1="1WY8TqIDpDeDgaYcBRO1RAmHLpy" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dacaaa1c69de508e5d5d3e6fdeebad006ad0d34_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dacaaa1c69de508e5d5d3e6fdeebad006ad0d34_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dacaaa1c69de508e5d5d3e6fdeebad006ad0d34_2_1380x776.jpeg 2x" data-dominant-color="7E7F84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4b57326996595dc462323e7973ba323e</span><span class="informations">2560×1441 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d904129142a1bb3b11925f94ae189684a138232.jpeg" data-download-href="/uploads/short-url/hUMKme5T8Zyswovf6rq4cw1kj1U.jpeg?dl=1" title="75a1e53d558c55c59729a251b3a086dd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d904129142a1bb3b11925f94ae189684a138232_2_690x388.jpeg" alt="75a1e53d558c55c59729a251b3a086dd" data-base62-sha1="hUMKme5T8Zyswovf6rq4cw1kj1U" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d904129142a1bb3b11925f94ae189684a138232_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d904129142a1bb3b11925f94ae189684a138232_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d904129142a1bb3b11925f94ae189684a138232_2_1380x776.jpeg 2x" data-dominant-color="7E7F7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">75a1e53d558c55c59729a251b3a086dd</span><span class="informations">1920×1081 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
