---
topic_id: 28087
title: "Extract Segment Labelmap As 2D Slices"
date: 2023-02-28
url: https://discourse.slicer.org/t/28087
---

# Extract segment labelmap as 2D slices

**Topic ID**: 28087
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/extract-segment-labelmap-as-2d-slices/28087

---

## Post #1 by @Marc-3d (2023-02-28 09:17 UTC)

<p>Hi there,</p>
<p>I intend to use 3D slicer to create annotations for training a Detectron2 model. I have found the examples for converting segmentations (labelmaps) into numpy arrays using the Python API. My data is 3D, and the example scripts generate labelmaps that are 3D arrays.</p>
<p>My problem now is that Detectron2 is a 2D CNN, so I need to provide 2D masks and their bounding boxes. Since I painted the segmentations through the “axial slice view”, I was wondering if there is a built-in way to retrieve the 2D strokes that I used to paint the segmentations for each segment.</p>
<p>Below, you can see that I am annotating spherical structures. Each segment contains multiple annotated slices, and I would like to export each slice as a 2D Mask.</p>
<p>Thank you in advance,<br>
Marc</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95fc3c8be28d7674048d7c0bc02ad71ae72cdc88.png" data-download-href="/uploads/short-url/loPyympEDrBdPOQI8zwIHvOvY6s.png?dl=1" title="Screenshot_slicer_mask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fc3c8be28d7674048d7c0bc02ad71ae72cdc88_2_690x270.png" alt="Screenshot_slicer_mask" data-base62-sha1="loPyympEDrBdPOQI8zwIHvOvY6s" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fc3c8be28d7674048d7c0bc02ad71ae72cdc88_2_690x270.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fc3c8be28d7674048d7c0bc02ad71ae72cdc88_2_1035x405.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95fc3c8be28d7674048d7c0bc02ad71ae72cdc88.png 2x" data-dominant-color="808182"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_slicer_mask</span><span class="informations">1205×472 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
