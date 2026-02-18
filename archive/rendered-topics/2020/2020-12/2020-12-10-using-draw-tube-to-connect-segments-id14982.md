# Using draw tube to connect segments

**Topic ID**: 14982
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/using-draw-tube-to-connect-segments/14982

---

## Post #1 by @Deepa (2020-12-10 11:06 UTC)

<p>Hi All,</p>
<p>I’d like to connect two segments displayed in the image below. I tried using <code>Draw Tube</code> in segment editor extra effects. Unfortunately, I am not able to place the fiducial marker on the surface of the segment and draw the tube. I’d like to ask for suggestions on how to connect these segments.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf13f65a49cb9918bdd1c82a52ba8b9d646b3c4a.jpeg" data-download-href="/uploads/short-url/rglXSZuWtSgbmb6hhGzUSRPoqDw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf13f65a49cb9918bdd1c82a52ba8b9d646b3c4a_2_345x209.jpeg" alt="image" data-base62-sha1="rglXSZuWtSgbmb6hhGzUSRPoqDw" width="345" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf13f65a49cb9918bdd1c82a52ba8b9d646b3c4a_2_345x209.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf13f65a49cb9918bdd1c82a52ba8b9d646b3c4a_2_517x313.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf13f65a49cb9918bdd1c82a52ba8b9d646b3c4a_2_690x418.jpeg 2x" data-dominant-color="A3B1A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×587 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Deepa (2020-12-11 05:10 UTC)

<p>Hi All,</p>
<p>I would like to know if it is recommended to use <code>fill between slices</code> instead of  <code>draw tube</code> for establishing the connection.</p>

---

## Post #3 by @lassoan (2020-12-11 14:05 UTC)

<p>Draw tube works great for drawing tubular shapes, so it is great for filing gaps in vasculature. Fill between slices is good if you segment structures that have complex cross-section shape but that shape does not change much between neighbor slices.</p>

---
