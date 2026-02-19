---
topic_id: 20493
title: "Removing 3D Model To View Segmentation"
date: 2021-11-05
url: https://discourse.slicer.org/t/20493
---

# Removing 3D model to view segmentation

**Topic ID**: 20493
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/removing-3d-model-to-view-segmentation/20493

---

## Post #1 by @Maddie (2021-11-05 03:27 UTC)

<p>Hello all. I had some questions regarding segmentation. I have recently finished segmenting a 3D soft tissue model. The issue I am having is the grey 3D model I had segmented still remains in the image. I have attached a screenshot (<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c27b4792a6ef27f002de922a33242f2f111993.jpeg" data-download-href="/uploads/short-url/76c4orn2aTUNfxyMyxA8Ikwgbib.jpeg?dl=1" title="Screen Shot 2021-11-04 at 5.06.32 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c27b4792a6ef27f002de922a33242f2f111993_2_690x405.jpeg" alt="Screen Shot 2021-11-04 at 5.06.32 PM" data-base62-sha1="76c4orn2aTUNfxyMyxA8Ikwgbib" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c27b4792a6ef27f002de922a33242f2f111993_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31c27b4792a6ef27f002de922a33242f2f111993_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c27b4792a6ef27f002de922a33242f2f111993.jpeg 2x" data-dominant-color="8F90AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-11-04 at 5.06.32 PM</span><span class="informations">1208×710 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>) I have segmented the grey part but have removed it to show the original  grey model that I would like to remove. Is there any way to remove it temporarily to just see the segmented tissues? Thanks!</p>

---

## Post #2 by @lassoan (2021-11-05 03:36 UTC)

<p>The gray object seems to be volume rendering of the image. If you use a recent Slicer Preview Release then you can toggle visibility in data module by right-clicking on the visibility column:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aafddb546547afd3e509331d62d5f76e0759d979.jpeg" data-download-href="/uploads/short-url/ooF3rBByQUaH1vGOyZQ0zGx50cF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aafddb546547afd3e509331d62d5f76e0759d979_2_690x409.jpeg" alt="image" data-base62-sha1="ooF3rBByQUaH1vGOyZQ0zGx50cF" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aafddb546547afd3e509331d62d5f76e0759d979_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aafddb546547afd3e509331d62d5f76e0759d979_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aafddb546547afd3e509331d62d5f76e0759d979.jpeg 2x" data-dominant-color="C6C1BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1201×712 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
