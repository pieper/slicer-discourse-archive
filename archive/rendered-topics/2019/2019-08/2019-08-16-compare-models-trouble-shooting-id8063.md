# Compare models trouble shooting

**Topic ID**: 8063
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/compare-models-trouble-shooting/8063

---

## Post #1 by @Andrew_Kanawati (2019-08-16 16:52 UTC)

<p>I am having trouble comparing and aligning two models.</p>
<p>I am registering the fixed segment as a CT scan.</p>
<p>Then for the moving segment, created a new volume from a STL (converted to a segment).</p>
<p>However the 2 models are not aligning.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7cb4a1c2d3b7cb1fed0aa10eb4173803cc5cc8f.jpeg" data-download-href="/uploads/short-url/nWnhyYQSf8mYfcKhEcVScjELymb.jpeg?dl=1" title="46%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7cb4a1c2d3b7cb1fed0aa10eb4173803cc5cc8f_2_690x220.jpeg" alt="46%20PM" data-base62-sha1="nWnhyYQSf8mYfcKhEcVScjELymb" width="690" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7cb4a1c2d3b7cb1fed0aa10eb4173803cc5cc8f_2_690x220.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7cb4a1c2d3b7cb1fed0aa10eb4173803cc5cc8f_2_1035x330.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7cb4a1c2d3b7cb1fed0aa10eb4173803cc5cc8f_2_1380x440.jpeg 2x" data-dominant-color="7B7A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">46%20PM</span><span class="informations">1622×518 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like the models to align to then compare models and perform Hausdorff distances.</p>
<p>Thanks very much.</p>

---

## Post #2 by @lassoan (2019-08-17 19:34 UTC)

<p>You can align two segments using Segment Registration extension then compare them using Segment Comparison module (provided by SlicerRT extension).</p>

---

## Post #3 by @Andrew_Kanawati (2019-08-19 13:31 UTC)

<p>Thanks</p>
<p>I was able to align segments, however the moving segment is not appearing on the 3D view as it is in the axial/sag/cor reconstructions.</p>
<p>Thanks again</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eecf4c4d0c0b013d8a7a71e52a2d725a02a7b77b.jpeg" data-download-href="/uploads/short-url/y4BLRxk0WU5zwPwI0zyuYO5mCmL.jpeg?dl=1" title="31%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eecf4c4d0c0b013d8a7a71e52a2d725a02a7b77b_2_690x414.jpeg" alt="31%20AM" data-base62-sha1="y4BLRxk0WU5zwPwI0zyuYO5mCmL" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eecf4c4d0c0b013d8a7a71e52a2d725a02a7b77b_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eecf4c4d0c0b013d8a7a71e52a2d725a02a7b77b_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eecf4c4d0c0b013d8a7a71e52a2d725a02a7b77b_2_1380x828.jpeg 2x" data-dominant-color="837A81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">31%20AM</span><span class="informations">1677×1007 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Juicy (2019-08-22 10:09 UTC)

<p>Have you tried going into ‘Segment Editor’ module and ensuring that the ‘Show 3d’ button at the top of the module is pressed?</p>

---
