# 3d reconstruction of implants in ct image

**Topic ID**: 16062
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/3d-reconstruction-of-implants-in-ct-image/16062

---

## Post #1 by @labixin (2021-02-18 14:01 UTC)

<p>Hi all,</p>
<p>I have an issue of reconstructing implants in CT image.</p>
<p>The ultimate goal is to form a 3d convex hull which could encompass all the clips. My solution would be 1) reconstruct these clips, 2) choose some surface points on each clips, 3) create a model (closed surface) based on these points using Markups to Model module.</p>
<p>In my case, the Titanium clip is relatively small (only 6x1x0.5 mm3) and I found I couldn’t make precise segmentation. The original spacing of CT image is 1.37x1.37x5 (mm). I wonder whether I should also resample the image for finer segmentation (<a href="https://discourse.slicer.org/t/the-impact-of-image-spacing-on-the-quality-of-3d-reconstruction/11793">like this</a>). Or is there better way to solve my problem? The related picture is attached below.</p>
<p>Thanks in advance. Your help is highly appreciated.</p>
<p>Crayon</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e29be025a91774a6b22eb7cf6abd96ab0ac84229.jpeg" data-download-href="/uploads/short-url/wkFRX315omwQT0y9MOoihzHsDMZ.jpeg?dl=1" title="Q1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e29be025a91774a6b22eb7cf6abd96ab0ac84229_2_690x142.jpeg" alt="Q1" data-base62-sha1="wkFRX315omwQT0y9MOoihzHsDMZ" width="690" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e29be025a91774a6b22eb7cf6abd96ab0ac84229_2_690x142.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e29be025a91774a6b22eb7cf6abd96ab0ac84229_2_1035x213.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e29be025a91774a6b22eb7cf6abd96ab0ac84229.jpeg 2x" data-dominant-color="323232"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Q1</span><span class="informations">1314×272 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-18 17:09 UTC)

<p>Would you like to visualize each clip? You should be able to get optimal (as good as it gets) visualization by volume rendering as the clips have very high density compared to surrounding tissues.</p>

---
