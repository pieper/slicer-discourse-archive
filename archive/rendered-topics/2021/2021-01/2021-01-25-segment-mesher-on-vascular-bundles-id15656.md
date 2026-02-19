---
topic_id: 15656
title: "Segment Mesher On Vascular Bundles"
date: 2021-01-25
url: https://discourse.slicer.org/t/15656
---

# Segment Mesher on Vascular Bundles

**Topic ID**: 15656
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/segment-mesher-on-vascular-bundles/15656

---

## Post #1 by @Shajia_Ali (2021-01-25 15:56 UTC)

<p>Hi everyone.<br>
I have a question regarding SegmentMesher. I know that SegmentMesher usually creates a mesh on the simplified Segmented Volume. But my Segmentation is rather ‘detailed’. I don’t want SegmentMesher ignore these small detailed parts. Is there a way so that SegmentMesher doesn’t see these parts as artifacts? I tried with blend_sigma and it did something but not enough. I have added my Segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/735808bc48b0bc74ab95ad8599ebc13bfce63908.png" data-download-href="/uploads/short-url/gsnwk1YWv6Kdq3ef3BO3DG6nCbu.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/735808bc48b0bc74ab95ad8599ebc13bfce63908_2_534x499.png" alt="grafik" data-base62-sha1="gsnwk1YWv6Kdq3ef3BO3DG6nCbu" width="534" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/735808bc48b0bc74ab95ad8599ebc13bfce63908_2_534x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/735808bc48b0bc74ab95ad8599ebc13bfce63908_2_801x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/735808bc48b0bc74ab95ad8599ebc13bfce63908.png 2x" data-dominant-color="4C3C42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1043×976 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
kind regards</p>
<p>Shajia</p>

---

## Post #2 by @lassoan (2021-01-26 00:16 UTC)

<p>You can get arbitrarily fine volumetric mesh using segment mesher, but it could take very long time to generate it and might require hundreds of GB RAM during computation. A very large mesh would also impractical for finite-element modeling.</p>
<p>Instead, you can create a uniform-resolution mesh with a reasonable element size and modulate material properties of the mesh based on samples taken from the image or the segmentation.</p>

---
