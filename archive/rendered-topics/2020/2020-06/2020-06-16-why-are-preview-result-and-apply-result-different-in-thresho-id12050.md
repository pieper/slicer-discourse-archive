---
topic_id: 12050
title: "Why Are Preview Result And Apply Result Different In Thresho"
date: 2020-06-16
url: https://discourse.slicer.org/t/12050
---

# why are preview result and apply result different in threshold segmentation？ 

**Topic ID**: 12050
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/why-are-preview-result-and-apply-result-different-in-threshold-segmentation/12050

---

## Post #1 by @SummerZ2020 (2020-06-16 02:22 UTC)

<p>Operating system:windows<br>
Slicer version:4.10.2 and 4.11<br>
Expected behavior:the segmentation result after the “Apply” button is clicked should be same with the preview result in Threshold segmentation.<br>
Actual behavior: the segmentation result after the “Apply” button is clicked  is worse than the preview result in Threshold segmentation.<br>
ps:The image thickness is 5mm.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db4252b8b35dbc524f5d3d6c8ce6ffc86c211fbd.png" data-download-href="/uploads/short-url/vhEF5lnwaKxtT8QR1SRcJTWlUmN.png?dl=1" title="apply" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db4252b8b35dbc524f5d3d6c8ce6ffc86c211fbd_2_690x372.png" alt="apply" data-base62-sha1="vhEF5lnwaKxtT8QR1SRcJTWlUmN" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db4252b8b35dbc524f5d3d6c8ce6ffc86c211fbd_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db4252b8b35dbc524f5d3d6c8ce6ffc86c211fbd_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db4252b8b35dbc524f5d3d6c8ce6ffc86c211fbd_2_1380x744.png 2x" data-dominant-color="747473"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">apply</span><span class="informations">2560×1383 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab8700487d8e6d918b323ec3ac065beb899967e6.png" data-download-href="/uploads/short-url/otoSVItTVsnUrUfFLKpp431LCzs.png?dl=1" title="preview" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab8700487d8e6d918b323ec3ac065beb899967e6_2_690x371.png" alt="preview" data-base62-sha1="otoSVItTVsnUrUfFLKpp431LCzs" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab8700487d8e6d918b323ec3ac065beb899967e6_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab8700487d8e6d918b323ec3ac065beb899967e6_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab8700487d8e6d918b323ec3ac065beb899967e6_2_1380x742.png 2x" data-dominant-color="757472"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">preview</span><span class="informations">2560×1380 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-06-16 02:30 UTC)

<p>Preview is displayed at the screen resolution, but when you apply the threshold then the segmentation’s resolution is used. The preview just looks smoother, but it actually contains the same information as the thresholding result.</p>

---

## Post #4 by @SummerZ2020 (2020-06-17 06:38 UTC)

<p>Thanks for your answer. but it seems that it is not caused only by the resolution as the result difference is differ widely.And some pixel points value is not reasonable, for example, the pixel value is smaller when it looks more lighter(white) obviously. I tried to install the latest version (4.11 2020.6.15), it works better in this senario. thanks again. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---
