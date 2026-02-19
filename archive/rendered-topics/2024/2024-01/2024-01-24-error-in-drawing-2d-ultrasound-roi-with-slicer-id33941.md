---
topic_id: 33941
title: "Error In Drawing 2D Ultrasound Roi With Slicer"
date: 2024-01-24
url: https://discourse.slicer.org/t/33941
---

# Error in drawing 2D ultrasound ROi with slicer

**Topic ID**: 33941
**Date**: 2024-01-24
**URL**: https://discourse.slicer.org/t/error-in-drawing-2d-ultrasound-roi-with-slicer/33941

---

## Post #1 by @Nancy (2024-01-24 01:50 UTC)

<p>When I finished sketching the ROI of an ultrasound image and then opened another patient’s image to prepare for sketching, I found that the ROI that had just been sketched appeared on another patient’s image. Where is the problem? Please help take a look, thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745601981454ecf81ff8d89c06e7f41b290ae048.jpeg" data-download-href="/uploads/short-url/gB9EydzbXsBOsNIfqKquRakciFO.jpeg?dl=1" title="屏幕截图 2024-01-24 094925" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745601981454ecf81ff8d89c06e7f41b290ae048_2_690x406.jpeg" alt="屏幕截图 2024-01-24 094925" data-base62-sha1="gB9EydzbXsBOsNIfqKquRakciFO" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745601981454ecf81ff8d89c06e7f41b290ae048_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745601981454ecf81ff8d89c06e7f41b290ae048_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745601981454ecf81ff8d89c06e7f41b290ae048.jpeg 2x" data-dominant-color="505657"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2024-01-24 094925</span><span class="informations">1300×766 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-01-24 15:56 UTC)

<p>You need to be sure to close the scene (from the file menu).  Otherwise the existing segmentations are retained.</p>

---
