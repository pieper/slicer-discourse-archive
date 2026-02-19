---
topic_id: 24819
title: "Use Mesh To Mask A Segmentation"
date: 2022-08-18
url: https://discourse.slicer.org/t/24819
---

# Use Mesh to Mask a Segmentation

**Topic ID**: 24819
**Date**: 2022-08-18
**URL**: https://discourse.slicer.org/t/use-mesh-to-mask-a-segmentation/24819

---

## Post #1 by @connorh (2022-08-18 13:34 UTC)

<p>Hello,</p>
<p>I have a polydata mesh (currently loaded as a modelNode) that I would like to use the geometry to mask a segmentation of the registered CT scan. I’m looking for a way to convert this mesh to a filled segmentation which I can then use as a mask when segmenting the underlying CT.</p>
<p>Is there a way to fill mesh geometry and convert it to a format that can be used to mask in a segmentation?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb3c686346e9410c9f7145f14537a9e3b9aae283.jpeg" data-download-href="/uploads/short-url/xyZCYjKfEn4PzVzvKJ1VzCYvdBh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3c686346e9410c9f7145f14537a9e3b9aae283_2_682x500.jpeg" alt="image" data-base62-sha1="xyZCYjKfEn4PzVzvKJ1VzCYvdBh" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3c686346e9410c9f7145f14537a9e3b9aae283_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3c686346e9410c9f7145f14537a9e3b9aae283_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3c686346e9410c9f7145f14537a9e3b9aae283_2_1364x1000.jpeg 2x" data-dominant-color="777371"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1406 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @connorh (2022-08-18 17:36 UTC)

<p>Resolved - was able to find this:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node</a></p>

---
