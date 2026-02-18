# Segmentation pixel roblem

**Topic ID**: 16810
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/segmentation-pixel-roblem/16810

---

## Post #1 by @bio (2021-03-28 23:02 UTC)

<p>Hi. I have a problem with my segmentation pixels for dataset from datastore lung segmentation. I had to fix right side and segment the left. But when trying to segment left side the size of pixels in the segmentation is larger than in right. I tried to crop image and  use isotropic spacing with smaller spacing but still get the same problem<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1c94127bbed64b7ab4f46aee07eb336ff4793ea.png" data-download-href="/uploads/short-url/n5e3D3lq3GQsnvFds5qPy9shCKm.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1c94127bbed64b7ab4f46aee07eb336ff4793ea_2_690x428.png" alt="Capture" data-base62-sha1="n5e3D3lq3GQsnvFds5qPy9shCKm" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1c94127bbed64b7ab4f46aee07eb336ff4793ea_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1c94127bbed64b7ab4f46aee07eb336ff4793ea_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1c94127bbed64b7ab4f46aee07eb336ff4793ea.png 2x" data-dominant-color="4F504F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1066×662 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-03-29 00:43 UTC)

<p>When you move segments between segmentations then the segment is not immediately resampled to the segmentation’s resolution (to avoid quality loss when you move segments around between different segmentations). You can apply very slight smoothing (with Joint smoothing method) to bring all segments to the same resolution.</p>

---

## Post #3 by @bio (2021-03-29 07:17 UTC)

<p>Thank you for the respond. I tried that and every other smoothing but it doesn’t do much. I will try again to see if it helps. I tried to load the sesion again and crop this time it looks better but still not the same.</p>

---

## Post #4 by @lassoan (2021-03-29 13:30 UTC)

<p>Overall, this looks normal (binary labelmap representation requires very high resolution to look similar to a smoothed closed surface representation), but if you share this segmentation file with us (upload somewhere and copy the link here) then we can tell what exactly happens with your data.</p>

---

## Post #5 by @bio (2021-03-29 17:24 UTC)

<p>Here is the link <a href="https://drive.google.com/file/d/1bnjK13uc69AE90TwsMDbFhrlpchL_A9d/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">214347_LungSegments_Scene.mrb - Google Drive</a></p>

---

## Post #6 by @bio (2021-03-29 17:33 UTC)

<p>Really thank you for your help. I reinstalled slicer to newer version, i used 4.10, and for some reason when i cropped it again today it looks the way i wanted it to look maybe it was some kind of bug…</p>

---
