# How to associate colormap with the model

**Topic ID**: 12724
**Date**: 2020-07-24
**URL**: https://discourse.slicer.org/t/how-to-associate-colormap-with-the-model/12724

---

## Post #1 by @siaeleni (2020-07-24 17:00 UTC)

<p>Hi,</p>
<p>I want to add a colormap in 3DView and show the min-max actual values with the same color as my model. I am generating a model and you can see the output at the image attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c303f499a9941d3c5c031d0bb143a3c9cb7d6c.jpeg" data-download-href="/uploads/short-url/rMWrLTBDmSO1ZV1kyWVU4coGz4U.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c303f499a9941d3c5c031d0bb143a3c9cb7d6c_2_517x191.jpeg" alt="Capture" data-base62-sha1="rMWrLTBDmSO1ZV1kyWVU4coGz4U" width="517" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c303f499a9941d3c5c031d0bb143a3c9cb7d6c_2_517x191.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c303f499a9941d3c5c031d0bb143a3c9cb7d6c_2_775x286.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c303f499a9941d3c5c031d0bb143a3c9cb7d6c.jpeg 2x" data-dominant-color="5C5E91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">910×337 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I can display a color map, but I haven’t figured out yet how to associate it with my model values.<br>
In other words, I want to show a colormap depending on the “Active Scalar” in the Models module.</p>
<p>I imagine that I should set the color table at Models properties, but I am not sure where exactly.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-07-24 17:51 UTC)

<p>To make sure the range of color scalar bar is in sync with the active scalar display, you can choose in Models module: Display / Scalars / Scalar Range Mode -&gt; Color table (LUT).</p>

---
