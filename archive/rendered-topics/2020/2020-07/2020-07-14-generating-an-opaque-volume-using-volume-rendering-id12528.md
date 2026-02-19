---
topic_id: 12528
title: "Generating An Opaque Volume Using Volume Rendering"
date: 2020-07-14
url: https://discourse.slicer.org/t/12528
---

# Generating an opaque volume using volume rendering

**Topic ID**: 12528
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/generating-an-opaque-volume-using-volume-rendering/12528

---

## Post #1 by @mwyburd (2020-07-14 13:14 UTC)

<p>I have a volume which contains continuous measures of depth and I want an opaque 3D volume rendering. I have thresholded the volume (in the volume module), to remove the background and have used “synchronize with volumes module” in Volume Rendering. However, when I try to adjust the “scalar opacity mapping” it turn the whole volume dark blue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d00d68b42a1939be7c587cea0691bd0b2fedbb0a.jpeg" data-download-href="/uploads/short-url/tGw2DnhRPxEkQGWGdTjXhPYzATw.jpeg?dl=1" title="Screenshot 2020-07-14 at 12.37.07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d00d68b42a1939be7c587cea0691bd0b2fedbb0a_2_690x275.jpeg" alt="Screenshot 2020-07-14 at 12.37.07" data-base62-sha1="tGw2DnhRPxEkQGWGdTjXhPYzATw" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d00d68b42a1939be7c587cea0691bd0b2fedbb0a_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d00d68b42a1939be7c587cea0691bd0b2fedbb0a_2_1035x412.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d00d68b42a1939be7c587cea0691bd0b2fedbb0a_2_1380x550.jpeg 2x" data-dominant-color="6E7176"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-14 at 12.37.07</span><span class="informations">2602×1038 433 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4fd157fbda50d784fe40401376cbec555ebf6ac.jpeg" data-download-href="/uploads/short-url/pP6aPc0zfSfu7SCY4FGDjHgJEvi.jpeg?dl=1" title="Screenshot 2020-07-14 at 12.36.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4fd157fbda50d784fe40401376cbec555ebf6ac_2_690x268.jpeg" alt="Screenshot 2020-07-14 at 12.36.48" data-base62-sha1="pP6aPc0zfSfu7SCY4FGDjHgJEvi" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4fd157fbda50d784fe40401376cbec555ebf6ac_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4fd157fbda50d784fe40401376cbec555ebf6ac_2_1035x402.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4fd157fbda50d784fe40401376cbec555ebf6ac_2_1380x536.jpeg 2x" data-dominant-color="73777A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-14 at 12.36.48</span><span class="informations">2464×960 399 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: Ubantu<br>
Slicer version: 4.10.2<br>
Expected behavior: opaque 3D volume displaying different depths<br>
Actual behavior: dark blue opaque volume or transparent volume with correct colours</p>

---

## Post #2 by @lassoan (2020-07-14 13:55 UTC)

<p>You will always have near-zero values at the edge of the volume, so if you make the opaque then they will occlude all the other colors.</p>
<p>Since you want to display a surface, a surface rendering is more appropriate: faster, higher quality, and you can of course make it opaque without any problems. To render a colored surface:</p>
<ul>
<li>export the segment to model</li>
<li>use “Probe volume with model” module to add a scalar containing the volume’s voxel values</li>
<li>use Models module Scalars section to enable scalar display, choose colormap, range, optionally threshold</li>
</ul>

---
