# Colour map for model comparison

**Topic ID**: 8446
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/colour-map-for-model-comparison/8446

---

## Post #1 by @Andrew_Kanawati (2019-09-16 16:07 UTC)

<p>Hello</p>
<p>I have registered 2 spine models and computed Hausdorff and Dice measurements, however is there a way of making the colour map change according to the distance difference? I’ve used a similar function in mesh lab</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8178575d65025f3ee2de42ed1eea887ad762d50.jpeg" data-download-href="/uploads/short-url/nZ0BLXAiXo0nkKpQsms0g4dEKv6.jpeg?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8178575d65025f3ee2de42ed1eea887ad762d50_2_690x388.jpeg" alt="01" data-base62-sha1="nZ0BLXAiXo0nkKpQsms0g4dEKv6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8178575d65025f3ee2de42ed1eea887ad762d50_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8178575d65025f3ee2de42ed1eea887ad762d50_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8178575d65025f3ee2de42ed1eea887ad762d50_2_1380x776.jpeg 2x" data-dominant-color="908FA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">5120×2880 2.04 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-09-17 00:38 UTC)

<p>To see a colormap, you need to compute distance between the two meshes using ModelToModelDistance extension. Once you have computed the output model, you can configure how to display colors in Models module / Scalars section.</p>

---
