# Spinal cord segmentation MRI

**Topic ID**: 16249
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/spinal-cord-segmentation-mri/16249

---

## Post #1 by @gloria (2021-02-26 20:43 UTC)

<p>Hello!<br>
Hopefully someone can help me.<br>
I need to segment a rat’s spinal cord. From T8-T10 and obtain volumes of gray matter and white matter as well as total volume of the spinal cord, from MRI.<br>
I used segment editor for each structure, but I am not getting the proper volumes because the addition of gray and white matter don´t give me the total volume of spinal cord.<br>
Does anyone know how I can properly segment spinal cord, gray matter and white matter? help!</p>

---

## Post #2 by @pieper (2021-02-26 21:52 UTC)

<p>Hi - It sounds like you are doing the right thing, maybe you can post a screenshot?</p>

---

## Post #3 by @gloria (2021-02-27 01:37 UTC)

<p>Hi!! Pieper</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca22e9ab880473b9ed98a14b98a9a8c122d6be0.jpeg" data-download-href="/uploads/short-url/vtOw3634sa3jbUNqjFIptf79MS4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca22e9ab880473b9ed98a14b98a9a8c122d6be0_2_690x459.jpeg" alt="image" data-base62-sha1="vtOw3634sa3jbUNqjFIptf79MS4" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca22e9ab880473b9ed98a14b98a9a8c122d6be0_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca22e9ab880473b9ed98a14b98a9a8c122d6be0_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca22e9ab880473b9ed98a14b98a9a8c122d6be0_2_1380x918.jpeg 2x" data-dominant-color="BABBBE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2160×1440 413 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is!</p>
<p>I did the segmentation and the volumes are shown there. I am starting to use 3D Slicer.</p>
<p>My question is because the volume of the spinal cord is different from the addition of gray matter and white matter ??? in theory it should be the addition.<br>
But I don’t know what happens there, I don’t understand.</p>

---

## Post #4 by @lassoan (2021-02-27 02:14 UTC)

<p>These volumes tell that either gray matter and white matter segments overlap or they partially lie outside the spinal cord segment. You can use use Logical Operators effect to remove overlaps or remove those parts of GM or WM segments that are outside the SC.</p>

---

## Post #5 by @gloria (2021-02-28 03:45 UTC)

<p>Hi!!!  Andras Lasso</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99a5519b978593885d2ed6bdaa607c6d5379c08.png" data-download-href="/uploads/short-url/ocnlAtxl6sSdsXHLHRtEMnKo9aU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a99a5519b978593885d2ed6bdaa607c6d5379c08_2_690x459.png" alt="image" data-base62-sha1="ocnlAtxl6sSdsXHLHRtEMnKo9aU" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a99a5519b978593885d2ed6bdaa607c6d5379c08_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a99a5519b978593885d2ed6bdaa607c6d5379c08_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a99a5519b978593885d2ed6bdaa607c6d5379c08_2_1380x918.png 2x" data-dominant-color="C4C5C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2160×1440 587 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t know if I’m doing the right thing. Addition gray and white matter with the operator (Add) and spinal cord (subtract).<br>
Could you guide me, for use logic operators??<br>
I want also that in the view 3D, see the “h” characteristic of the gray matter of the spinal cord. And I don’t get any of that, it seems to just give me only the structure of the spinal cord.</p>

---
