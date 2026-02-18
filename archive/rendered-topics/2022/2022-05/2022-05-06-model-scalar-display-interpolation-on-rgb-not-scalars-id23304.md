# Model Scalar Display interpolation on RGB not Scalars

**Topic ID**: 23304
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/model-scalar-display-interpolation-on-rgb-not-scalars/23304

---

## Post #1 by @wabwan25 (2022-05-06 12:39 UTC)

<p>I am not sure my observation is correct, but i get an issue on model scalar display in the transition area.  As below image show, the color within triangle seems from interpolation of vertex RGB colors. What I expect is interpolation of vertex scalar values in the transition area, then map the scalar value to color for display, not directly interpolate the vertex RGB colors showing no meaningful colors. Any suggestion to get that? Thank you very much for any comments.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3c2ff2250f588182f8bf8105f0baa57874b1d25.jpeg" alt="image" data-base62-sha1="pEffdQblgFqPSCOy62eoWbUVAjz" width="519" height="297"></p>

---

## Post #2 by @pieper (2022-05-06 14:04 UTC)

<p>I think yes, that rgb interpolation would be happening in the GPU based on the vertex scalars being mapped to colors in the rendering pipeline.  Using a higher resolution mesh is one option.  A better solution would involve a custom fragment, but that’s a challenge for a lot of reasons.</p>

---

## Post #3 by @wabwan25 (2022-05-09 16:53 UTC)

<p>Thanks for the reply. Looks like I am going to live with it.</p>

---
