# Omitting the rotation of needle around its axis in the transformation module

**Topic ID**: 8247
**Date**: 2019-08-31
**URL**: https://discourse.slicer.org/t/omitting-the-rotation-of-needle-around-its-axis-in-the-transformation-module/8247

---

## Post #1 by @Mary7291 (2019-08-31 07:20 UTC)

<p>Operating system: window 7<br>
Slicer version:4.8.1</p>
<p>Hello,<br>
To plan a needle insertion process, i need to load a needle in slicer and finding the transformation of the needle to obtain the position and orientation if the needle tip. I use the transformation module to achieve this purpose. But i found that the rotation of the needle around its axis affects the transformation module.<br>
I need to know how can i omit the effect of the rotation around the needle axis?<br>
I would be so appreciated if anyone could help me…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7607f35e00aae038d18e359047c67c9fcf0f0ae5.png" data-download-href="/uploads/short-url/gQ9nidUpgQlumqslIUwYxztPqCN.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7607f35e00aae038d18e359047c67c9fcf0f0ae5_2_690x499.png" alt="Capture" data-base62-sha1="gQ9nidUpgQlumqslIUwYxztPqCN" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7607f35e00aae038d18e359047c67c9fcf0f0ae5_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7607f35e00aae038d18e359047c67c9fcf0f0ae5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7607f35e00aae038d18e359047c67c9fcf0f0ae5.png 2x" data-dominant-color="BEBDC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">851×616 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-08-31 16:38 UTC)

<p>It is not completely clear what you would like to achieve, but switching the order of translation/rotation may help (toggle button next to invert button with an icon of translation/rotation arrows).</p>
<p>For setting remote center of rotation and create any kind of combination of transforms, you can create a transform hierarchy by applying transforms to transforms.</p>

---
