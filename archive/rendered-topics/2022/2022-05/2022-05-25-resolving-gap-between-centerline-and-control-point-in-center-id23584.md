# Resolving gap between centerline and control point in centerline extraction

**Topic ID**: 23584
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/resolving-gap-between-centerline-and-control-point-in-centerline-extraction/23584

---

## Post #1 by @kvmontez (2022-05-25 11:44 UTC)

<p>Hi! I’ve been working with the centerline extraction feature to create a centerline network in the built-in CTACardio data in 3D Slicer 5.1.0-2022-05-23.</p>
<p>However, when the centerline is generated, there is a gap between the end of the centerline and the control point as shown in the attached image. In some cases, the centerline appears to be on the same ‘plane’ as the control point (end at the same general region), but it is skewed away from the control point.</p>
<p>I have used the following videos for reference: <a href="https://www.youtube.com/watch?v=yi07mjr3JeU&amp;t=215s" rel="noopener nofollow ugc">‘New vessel branch extraction module for 3D Slicer’</a> and <a href="https://youtu.be/caEuwJ7pCWs?t=162" rel="noopener nofollow ugc">‘Vessel segmentation and centerline extraction using 3D Slicer and VMTK’</a>.</p>
<p>In the latter video (at 2:42), the centerline appears to touch the control points directly such that there are no gaps present as I am seeing in my centerline extraction.</p>
<p>How do I go about resolving this issue? Is there a setting that I may be overlooking? Please advise.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b76e8d3f73ef798cc34440bc780257e3ebceca63.jpeg" data-download-href="/uploads/short-url/qaIes7KigrjwRGfUsBHPTMWnGPV.jpeg?dl=1" title="Centerline and control point gap.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b76e8d3f73ef798cc34440bc780257e3ebceca63_2_555x500.jpeg" alt="Centerline and control point gap.PNG" data-base62-sha1="qaIes7KigrjwRGfUsBHPTMWnGPV" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b76e8d3f73ef798cc34440bc780257e3ebceca63_2_555x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b76e8d3f73ef798cc34440bc780257e3ebceca63_2_832x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b76e8d3f73ef798cc34440bc780257e3ebceca63_2_1110x1000.jpeg 2x" data-dominant-color="A695B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Centerline and control point gap.PNG</span><span class="informations">1427×1285 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-05-25 12:09 UTC)

<p>Centerline extraction computes the medial surface and the designated endpoints are only used for finding paths within that. The medial surface typically does not reach the outer surface (except there can be spikes where the outer surface has protrusions).</p>
<p>The distance between the designated endpoint and the closest point on the medial surface is small if the radius of the vessel branch is small or if there is a protrusion in the outer surface nearby.</p>

---
