# Segmenting 4D echo volume sequence

**Topic ID**: 16661
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/segmenting-4d-echo-volume-sequence/16661

---

## Post #1 by @Rodrigo_Visconti (2021-03-20 19:58 UTC)

<p>How can I create a moving valve from a sequence volume? Do I need to segment all frames separately? Can I use it to create a VR movie? Thanks</p>

---

## Post #2 by @lassoan (2021-03-25 20:27 UTC)

<p>We typically use volume rendering for displaying 4D echo, as segmentation is too tedious and doing it for all frames of a sequence would just take too much effort.</p>
<p>You can try segmenting one frame and computing displacement field for all other frames. This approach should be able to track the annulus and the valve overall. However, since the displacement field is discontinuous near the leaflet tips, you would need to manually fix up the leaflet segmentation.</p>
<p>We have developed deep learning models for automatic leaflet segmentation on 3D echo, which we will publicly release when the associated papers are accepted for publication (probably within 6-12 months). These segmentation modules will allow you to segment all frames of a time sequence with very little manual effort.</p>

---

## Post #3 by @Rodrigo_Visconti (2021-03-26 00:18 UTC)

<p>Thanks. The module will be of great value I hope it will be available soon. For the segmentation process I need to open one new segment for every frame or it can be made in the same segment?</p>

---

## Post #4 by @lassoan (2021-03-29 13:32 UTC)

<p>You need to create a single segmentation node, then add a new sequence node in Sequences module and assign the segmentation node as proxy node.</p>

---

## Post #5 by @Rodrigo_Visconti (2021-04-04 04:24 UTC)

<p>Thanks for your reply. I’ve tried these steps but how to extend the segmentation to other frames? Do you have any video or tutorial on how to do this?</p>

---

## Post #6 by @lassoan (2021-04-09 01:19 UTC)

<p>You can create a segmentation node and then create a new sequence and use the segmentation node as proxy node:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6d6510b50d1495e37439205e802c57ef8932ff.jpeg" data-download-href="/uploads/short-url/rjrzAR6YgaJ9qILTnGnXpXbHc8D.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6d6510b50d1495e37439205e802c57ef8932ff_2_690x440.jpeg" alt="image" data-base62-sha1="rjrzAR6YgaJ9qILTnGnXpXbHc8D" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6d6510b50d1495e37439205e802c57ef8932ff_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6d6510b50d1495e37439205e802c57ef8932ff_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6d6510b50d1495e37439205e802c57ef8932ff_2_1380x880.jpeg 2x" data-dominant-color="DDDBD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2025×1294 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After this, Sequences module will create a new segmentation for each time point that you browse to (by copying the segmentation from the previous time point).</p>

---
