---
topic_id: 16886
title: "Ridgeline Artifacts From Wrap Solidify Effect Segment Editor"
date: 2021-04-01
url: https://discourse.slicer.org/t/16886
---

# Ridgeline Artifacts from Wrap Solidify Effect (Segment Editor Module)

**Topic ID**: 16886
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/ridgeline-artifacts-from-wrap-solidify-effect-segment-editor-module/16886

---

## Post #1 by @davidboerma (2021-04-01 02:56 UTC)

<p>Hi folks, the “Wrap Solidify” effect intermittently introduces thin raised lines onto the models it produces from my segmentations. It tends to occur on a specimen-by-specimen basis and hasn’t responded to increasing the smoothing factor or number of iterations.</p>
<p>Here are my settings for Wrap Solidify:<br>
Region: Outer surface, Carve holes = 0.5 mm<br>
Output: Model<br>
Advanced: Smoothing factor = 0; Oversampling = 1.00; Iterations = 6</p>
<p>Anyone else experiencing this, or know how to resolve it? Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0ce9518197c24d9cd155c642c6a2cfdb054ff89c.jpeg" data-download-href="/uploads/short-url/1QdBWrfC4JsL9xQLhdyitSQ9lMM.jpeg?dl=1" title="Wrap Solidify Artifact" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9518197c24d9cd155c642c6a2cfdb054ff89c_2_690x472.jpeg" alt="Wrap Solidify Artifact" data-base62-sha1="1QdBWrfC4JsL9xQLhdyitSQ9lMM" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9518197c24d9cd155c642c6a2cfdb054ff89c_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9518197c24d9cd155c642c6a2cfdb054ff89c_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ce9518197c24d9cd155c642c6a2cfdb054ff89c_2_1380x944.jpeg 2x" data-dominant-color="7A7784"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Wrap Solidify Artifact</span><span class="informations">1929×1320 434 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-04-02 19:29 UTC)

<p>This happens sometimes. Smoothing the segmentation before solidifying and/or increasing the number of iterations should fix the problem.</p>

---
