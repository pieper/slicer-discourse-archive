# Crop volume with specified ROI e.g. 5mm x 5mm x 5mm

**Topic ID**: 28012
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/crop-volume-with-specified-roi-e-g-5mm-x-5mm-x-5mm/28012

---

## Post #1 by @Young_Wang (2023-02-23 13:43 UTC)

<p>Hi everyone, if there is an easy way to crop volume into a defined ROI, e.g. 5mm x 5mm x 5mm? The current setting allows for dragging the ROI boundaries. I wonder if we can specify the volume we need and drag the ROI location instead?</p>

---

## Post #2 by @muratmaga (2023-02-23 16:14 UTC)

<p>You can specify the dimensions of the ROI as I did in the screenshot below, and then use the middle handle (orange one) to drag it wherever you want.</p>
<p>You may want to disable to scaling and rotation interactions during the move to avoid the issue of acciendetally changing the dimensions…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32442dd8588e887fcff5419770772047573a7c5b.png" data-download-href="/uploads/short-url/7aFWGthJmbn7bmXlv4oJ6qR9UE3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32442dd8588e887fcff5419770772047573a7c5b_2_690x493.png" alt="image" data-base62-sha1="7aFWGthJmbn7bmXlv4oJ6qR9UE3" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32442dd8588e887fcff5419770772047573a7c5b_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32442dd8588e887fcff5419770772047573a7c5b_2_1035x739.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32442dd8588e887fcff5419770772047573a7c5b.png 2x" data-dominant-color="C5BED4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1368×978 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Young_Wang (2023-02-23 20:27 UTC)

<p>This is exactly what I was looking for. Thank you so much! I was trying to find it from the crop volume module. 3Dslicer is great but sometimes you have to know where one feature might be hidden.</p>

---

## Post #4 by @lassoan (2023-03-21 02:24 UTC)



---
