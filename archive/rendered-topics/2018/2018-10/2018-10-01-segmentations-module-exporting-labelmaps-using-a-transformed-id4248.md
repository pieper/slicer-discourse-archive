# Segmentations Module: Exporting labelmaps using a transformed Reference volume

**Topic ID**: 4248
**Date**: 2018-10-01
**URL**: https://discourse.slicer.org/t/segmentations-module-exporting-labelmaps-using-a-transformed-reference-volume/4248

---

## Post #1 by @baverso (2018-10-01 21:48 UTC)

<p>Hello, I have some question concerning translations and resampling of segmentation objects.</p>
<p>Background: I have two imaging volumes and a segmentation in my Data. Image volume (‘alpha’) is the original medical image, unaltered. Image volume (‘bravo’) is downsampled and translated to a slightly new origin. In addition to these volumes, I have a segmentation object. It’s unaltered by any transformations or resampling, and as such, the Master volume remains the original imaging volume.</p>
<p>Objective: To perform the same translation and downsampling on this segmentation, so it accurately maps to the  image volume bravo.</p>
<p>Option 1) Convert to a binary labelmap, and perform resampling on the labelmap. In my particular use case, I am downsampling with interpolation, and specifying a new origin to create a translational shift. All parameters will match imaging volume bravo.</p>
<p>Option 2) In the Segmentations module I can directly export a binary labelmap with the Reference volume (in ‘advanced’) set to imaging volume bravo.</p>
<p>In both situations, I can verify the segmentation has been accurately translated and resampled in the Volumes module. My questions are:<br>
A)In option 2 (exporting directly using reference volume bravo), what interpolation, if any, was performed to derive the new labelmap?<br>
B) I noted that method 1 yielded a lower quality segmentation (before and after picture attached, after being the one with little unsegmented islands in it). Is option 2 a more standard approach than than option 1?</p>
<p>Thank you for your advice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/537447f579b86bbefef948853eaef65b1a069367.png" data-download-href="/uploads/short-url/bUgLbN9k8x3jYrxG2lHbFwNJAPl.png?dl=1" title="32%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/537447f579b86bbefef948853eaef65b1a069367_2_690x360.png" alt="32%20PM" data-base62-sha1="bUgLbN9k8x3jYrxG2lHbFwNJAPl" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/537447f579b86bbefef948853eaef65b1a069367_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/537447f579b86bbefef948853eaef65b1a069367_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/537447f579b86bbefef948853eaef65b1a069367_2_1380x720.png 2x" data-dominant-color="616161"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">32%20PM</span><span class="informations">3360×1756 414 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8f11ddd99f2bb59822009d2c1d5d2d60d586e5b.png" data-download-href="/uploads/short-url/sFC5duXQSUWV2HTxwDb6yS5pJP5.png?dl=1" title="04%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8f11ddd99f2bb59822009d2c1d5d2d60d586e5b_2_690x362.png" alt="04%20PM" data-base62-sha1="sFC5duXQSUWV2HTxwDb6yS5pJP5" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8f11ddd99f2bb59822009d2c1d5d2d60d586e5b_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8f11ddd99f2bb59822009d2c1d5d2d60d586e5b_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8f11ddd99f2bb59822009d2c1d5d2d60d586e5b_2_1380x724.png 2x" data-dominant-color="5F6061"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20PM</span><span class="informations">3360×1766 425 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-10-01 22:54 UTC)

<aside class="quote no-group" data-username="baverso" data-post="1" data-topic="4248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c5a1d2/48.png" class="avatar"> baverso:</div>
<blockquote>
<p>A)In option 2 (exporting directly using reference volume bravo), what interpolation, if any, was performed to derive the new labelmap?</p>
</blockquote>
</aside>
<p>Nearest neighbor “interpolation” is used, i.e., there is no interpolation but the value of the closest input voxel is used.</p>
<aside class="quote no-group" data-username="baverso" data-post="1" data-topic="4248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c5a1d2/48.png" class="avatar"> baverso:</div>
<blockquote>
<p>I noted that method 1 yielded a lower quality segmentation</p>
</blockquote>
</aside>
<p>There can be many explanations. One possible reason is that voxel values are stored in integer values (unsigned char), 0 = outside, 1 = inside. If you interpolate the value then due to numerical instabilities you might get 0.9999 as interpolated value, which may be converted to 0 integer value. If you want to interpolate (e.g., because you want to have smoother edges when you oversample) then probably you need to rescale values to 0=outside, 255=outside, apply Gaussian smoothing, resample with linear or spline kernel, then threshold with level=127.</p>

---
