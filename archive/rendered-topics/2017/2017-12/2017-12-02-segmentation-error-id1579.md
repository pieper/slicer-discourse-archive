# Segmentation error

**Topic ID**: 1579
**Date**: 2017-12-02
**URL**: https://discourse.slicer.org/t/segmentation-error/1579

---

## Post #1 by @Hamburgerfinger (2017-12-02 22:51 UTC)

<p>Hi!</p>
<p>I have an error in segmentation that’s recurrent…  Sometimes when drawing or painting a segment in a given slice, a portion of the segment is applied onto the adjacent slices – please see pictures (circular segment was applied in first image only, but diagonal line is missing, which appears in the adjacent slice).  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c37c208f6770e62ffa3f005cd511d70173251d7.jpeg" data-download-href="/uploads/short-url/1K5bOhEPn98JffFwLckqGfRdvZd.jpg?dl=1" title="02 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0c37c208f6770e62ffa3f005cd511d70173251d7_2_522x500.jpg" alt="02 PM" data-base62-sha1="1K5bOhEPn98JffFwLckqGfRdvZd" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0c37c208f6770e62ffa3f005cd511d70173251d7_2_522x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0c37c208f6770e62ffa3f005cd511d70173251d7_2_783x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0c37c208f6770e62ffa3f005cd511d70173251d7_2_1044x1000.jpg 2x" data-dominant-color="BFC7BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02 PM</span><span class="informations">1068×1022 86.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I observe this in any of the slices I’ve defined segments with, “Fill between slices” doesn’t work properly then either.</p>
<p>Why is this and how can I prevent it from happening?</p>
<p>Thanks!<br>
Luke</p>

---

## Post #2 by @lassoan (2017-12-03 00:02 UTC)

<p>This happens when you paint on oblique slices: you either you’ve changed the slice orientation (not likely) or your image was acquired with tilted axes. See this post for instructions how to edit such images: <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">Segmentation Editor - How to disable painting on adjacent slices?</a></p>

---
