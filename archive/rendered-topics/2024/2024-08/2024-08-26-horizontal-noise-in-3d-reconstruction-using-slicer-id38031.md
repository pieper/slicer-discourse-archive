---
topic_id: 38031
title: "Horizontal Noise In 3D Reconstruction Using Slicer"
date: 2024-08-26
url: https://discourse.slicer.org/t/38031
---

# Horizontal Noise in 3D Reconstruction Using Slicer

**Topic ID**: 38031
**Date**: 2024-08-26
**URL**: https://discourse.slicer.org/t/horizontal-noise-in-3d-reconstruction-using-slicer/38031

---

## Post #1 by @ypd04474 (2024-08-26 08:51 UTC)

<p>I’m currently working on a 3D reconstruction project using Slicer, but I’ve encountered an issue where horizontal noise appears in the final 3D model.<br>
The source images are 2D slices, and the reconstruction generally looks good, but there are noticeable horizontal artifacts that are affecting the quality.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fa83338d73e354e573d36925d28f2fa9417e7ec.jpeg" data-download-href="/uploads/short-url/958rKO4YxACWs5yqRJ79YmZNkU4.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fa83338d73e354e573d36925d28f2fa9417e7ec_2_690x375.jpeg" alt="slicer" data-base62-sha1="958rKO4YxACWs5yqRJ79YmZNkU4" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fa83338d73e354e573d36925d28f2fa9417e7ec_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fa83338d73e354e573d36925d28f2fa9417e7ec_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fa83338d73e354e573d36925d28f2fa9417e7ec_2_1380x750.jpeg 2x" data-dominant-color="757985"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1920×1044 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Has anyone else experienced this issue or have any suggestions on how to reduce or eliminate this noise? Any advice would be greatly appreciated!</p>

---

## Post #2 by @pieper (2024-08-26 12:33 UTC)

<p>From what I can see, that’s an accurate reconstruction of your data.  The noise you see is probably related to the acquisition method.</p>

---

## Post #3 by @ypd04474 (2024-08-27 08:03 UTC)

<p>I believe you’re right—the horizontal noise likely results from an error during the acquisition process, rather than being a feature of the actual structure.<br>
Given this, I’m curious if there are any methods or tools within Slicer that could help correct or mitigate this kind of error.<br>
Are there specific techniques or settings in Slicer that you would recommend for dealing with acquisition-related artifacts like this? Any advice would be greatly appreciated!</p>

---
