# How to smooth a volume rendering

**Topic ID**: 1370
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/how-to-smooth-a-volume-rendering/1370

---

## Post #1 by @AndFor (2017-11-03 22:54 UTC)

<p>Hello<br>
I’ve find some topics about Model surface smoothing, but nothing for smoothing a Volume in volume rendering<br>
Is possible?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f095a5a2691c15b7f6cec4fdcff0127dc9327b4.jpeg" data-download-href="/uploads/short-url/i7OFZDnXiNjTHyh3FgF45xJNekY.jpg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7f095a5a2691c15b7f6cec4fdcff0127dc9327b4_2_659x500.jpg" alt="Screenshot" data-base62-sha1="i7OFZDnXiNjTHyh3FgF45xJNekY" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7f095a5a2691c15b7f6cec4fdcff0127dc9327b4_2_659x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7f095a5a2691c15b7f6cec4fdcff0127dc9327b4_2_988x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f095a5a2691c15b7f6cec4fdcff0127dc9327b4.jpeg 2x" data-dominant-color="16090B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1209×916 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-11-03 23:32 UTC)

<p>You can achieve a lot by tuning volume rendering transfer functions, but if that’s not enough then you can apply noise reduction filters, such as Anisotropic diffusion or Gaussian smoothing modules, ITK image filters in SimpleFilters module, or filters in Anomalous filters extension (<a href="http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=192777&amp;layout=layout">http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=192777&amp;layout=layout</a>). Optimal choice of filter and parameters depend on the characteristics of noise in the image.</p>

---
