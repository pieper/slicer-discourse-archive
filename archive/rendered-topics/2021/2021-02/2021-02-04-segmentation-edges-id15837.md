# Segmentation edges

**Topic ID**: 15837
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/segmentation-edges/15837

---

## Post #1 by @Giulia1 (2021-02-04 13:24 UTC)

<p>Hi! I have a problem during knee segmentation, as the segments are not created with a linear and defined line on the edges (image below). I would like to understand if there is a way to get the outline obtained from the segments equal to the one in the image above.</p>
<p>Thanks!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bbf6642b635f3868d091bdd8911d7f5fe763372.jpeg" data-download-href="/uploads/short-url/fnb9Y2oNnlQVIOEPAp3HFwh5JWa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbf6642b635f3868d091bdd8911d7f5fe763372_2_248x500.jpeg" alt="image" data-base62-sha1="fnb9Y2oNnlQVIOEPAp3HFwh5JWa" width="248" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbf6642b635f3868d091bdd8911d7f5fe763372_2_248x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbf6642b635f3868d091bdd8911d7f5fe763372_2_372x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbf6642b635f3868d091bdd8911d7f5fe763372_2_496x1000.jpeg 2x" data-dominant-color="655E4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1934×3893 1.82 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-04 14:00 UTC)

<p>The input volume is highly anisotropic and by default Slicer uses the same resolution for the segmentation as the input volume. See instruction on how to refine the segmentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---
