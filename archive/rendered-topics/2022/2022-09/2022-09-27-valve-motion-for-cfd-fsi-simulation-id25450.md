# Valve motion for CFD/FSI simulation

**Topic ID**: 25450
**Date**: 2022-09-27
**URL**: https://discourse.slicer.org/t/valve-motion-for-cfd-fsi-simulation/25450

---

## Post #1 by @Gening_Dong (2022-09-27 17:26 UTC)

<p>Hi all,</p>
<p>I’m trying to run CFD/FSI based on a 4D longitude ultrasound dataset. I try to segment the heart (especially the outflow tract) and used the module <code>Transform</code> to apply transform sequence to the segmentation. In actual, at some time points the valves inside the outflow tract should be completely closed, so there won’t be any blood flow. Since the segmentation is based on ultrasound images, when the valves close, the segmentation should has breaks (see the screenshot below).<br>
I hope that after I apply the transform sequence, the breakpoint can be reconnected at some time points to simulate valve opening and blood flow out. But when I apply the transform sequence, the nodes don’t reconnect.<br>
Is it possible to achieve this in 3D Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e566cfff3b24a1f555e043f2d6ca232311e3665.jpeg" data-download-href="/uploads/short-url/fK5GFaGFBdKvWdUupgeGIk4XN77.jpeg?dl=1" title="Screenshot 2022-09-27 132040" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e566cfff3b24a1f555e043f2d6ca232311e3665_2_526x500.jpeg" alt="Screenshot 2022-09-27 132040" data-base62-sha1="fK5GFaGFBdKvWdUupgeGIk4XN77" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e566cfff3b24a1f555e043f2d6ca232311e3665_2_526x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e566cfff3b24a1f555e043f2d6ca232311e3665.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e566cfff3b24a1f555e043f2d6ca232311e3665.jpeg 2x" data-dominant-color="74838F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-09-27 132040</span><span class="informations">726×689 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-09-28 04:09 UTC)

<p>You probably need to edit the segmentation manually in Segment Editor to make small adjustments.</p>

---
