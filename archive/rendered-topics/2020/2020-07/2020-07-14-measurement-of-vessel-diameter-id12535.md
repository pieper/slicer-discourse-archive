---
topic_id: 12535
title: "Measurement Of Vessel Diameter"
date: 2020-07-14
url: https://discourse.slicer.org/t/12535
---

# Measurement of vessel diameter

**Topic ID**: 12535
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/measurement-of-vessel-diameter/12535

---

## Post #1 by @Andreas (2020-07-14 15:05 UTC)

<p>Hello,</p>
<p>I want to determine the diameter of a vessel and use the ‘ruler’ tool for this.</p>
<p>How can I make a vertical cut through the vessel? To do this with the curser, it’s a matter of luck. Usually there is an oblique cut and thus a distortion.<br>
Another measurement error arises when determining the transverse diamond with the ruler. Instead of fine lines, I have 2 relatively thick points as a limitation.</p>
<p>Is there no tool to determine the transverse diamter at any point in the vessel with one click?</p>
<p>best regards</p>

---

## Post #2 by @lassoan (2020-07-14 15:55 UTC)

<p>I would recommend to do all cross-sectional measurements on straightened (curved planar reformatted) image of the vessel. You can use Curved Planar Reformat module in Sandbox extension in recent Slicer Preview Releases:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>We have been working on replacing the old annotation ruler and ROI tools with the new “markups” tools (line, angle, curve, closed curve, plane, etc.). In markups line by default the control point size is fix in screen space, so it you zoom in then the physical size of the control point can be reduced a lot. You can also use glyph types that occlude less of the image, for example “Cross2D” or “Starburst2D”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9afa2ef7c10c27d2940ffce7ccc4f9b08487eac5.jpeg" data-download-href="/uploads/short-url/m6ZxR2HlIapPEUwrUky682l99sh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9afa2ef7c10c27d2940ffce7ccc4f9b08487eac5_2_690x489.jpeg" alt="image" data-base62-sha1="m6ZxR2HlIapPEUwrUky682l99sh" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9afa2ef7c10c27d2940ffce7ccc4f9b08487eac5_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9afa2ef7c10c27d2940ffce7ccc4f9b08487eac5_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9afa2ef7c10c27d2940ffce7ccc4f9b08487eac5_2_1380x978.jpeg 2x" data-dominant-color="CFD0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1720×1219 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Let us know if you have any further comments, we are keep improving things based on the feedback we get from users.</p>

---
