# How to crop volume rendering by slices

**Topic ID**: 42953
**Date**: 2025-05-15
**URL**: https://discourse.slicer.org/t/how-to-crop-volume-rendering-by-slices/42953

---

## Post #1 by @muratmaga (2025-05-15 20:19 UTC)

<p>The detail in the slice views are often useful for me when I am looking at 3D rendering in cropped view. The way rendering works, details are often hidden and contrast is harder to adjust. I find it useful to crop and then enable to slice view in 3D.</p>
<p>However, this is too tedious to do it continuously. Is there a way I can make this work easier? (i.e., crop box is controlled by the active slice view and where I am on the slice slider?</p>
<p>For comparison this is normal cropped view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6742e2c146a1a36d93a5e3faf2f3df920953e92a.jpeg" data-download-href="/uploads/short-url/eJutR2oo1dg1qemrScv2EjByVyG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6742e2c146a1a36d93a5e3faf2f3df920953e92a_2_616x500.jpeg" alt="image" data-base62-sha1="eJutR2oo1dg1qemrScv2EjByVyG" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6742e2c146a1a36d93a5e3faf2f3df920953e92a_2_616x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6742e2c146a1a36d93a5e3faf2f3df920953e92a_2_924x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6742e2c146a1a36d93a5e3faf2f3df920953e92a_2_1232x1000.jpeg 2x" data-dominant-color="70717E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1556 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is when overlay the slice view closest to where the cropping is happening.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34547d280c2520947b31d35fc76fc4edb9b979a4.jpeg" data-download-href="/uploads/short-url/7sVQouiJl3vHYb8RjZy3agQHeDi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34547d280c2520947b31d35fc76fc4edb9b979a4_2_616x500.jpeg" alt="image" data-base62-sha1="7sVQouiJl3vHYb8RjZy3agQHeDi" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34547d280c2520947b31d35fc76fc4edb9b979a4_2_616x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34547d280c2520947b31d35fc76fc4edb9b979a4_2_924x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34547d280c2520947b31d35fc76fc4edb9b979a4_2_1232x1000.jpeg 2x" data-dominant-color="777884"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1557 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-05-15 21:30 UTC)

<p>Found it. It is called <strong>clipping</strong> and in its in Volume Rendering.. It is not as fluid it as I would like, but seems to work.</p>

---
