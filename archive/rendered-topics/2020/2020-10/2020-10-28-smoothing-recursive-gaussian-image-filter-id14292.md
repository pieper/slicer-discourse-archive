# Smoothing Recursive Gaussian Image Filter

**Topic ID**: 14292
**Date**: 2020-10-28
**URL**: https://discourse.slicer.org/t/smoothing-recursive-gaussian-image-filter/14292

---

## Post #1 by @aseman (2020-10-28 19:45 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D Slicer experts and all<br>
I used Smoothing Recursive Gaussian Image Filter from simple filters module. My input volume is a CT image and I chose various sigma values, which in the below figure, the result of this selection in each row, have been shown. (σ1= 3, 0.0001, 0.0001 / σ2= 0.0001, 3, 0.0001 / σ3= 0.0001, 0.0001, 3).<br>
I can’t distinguish each of this σ values affect on which view (axial, sagittal or coronal). In the other words, what is the difference among σ1, σ2 and σ3 ?<br>
Also,  along which axis or on which  view ( axial, sagittal, or coronal) does σ1 have the greatest influence?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7a47ab6fc3720f1b1edfe154e65b03cbb89200.png" data-download-href="/uploads/short-url/oBO6J9XQWX19BbY3ftkYoFWcH0Q.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7a47ab6fc3720f1b1edfe154e65b03cbb89200_2_517x230.png" alt="Screenshot_1" data-base62-sha1="oBO6J9XQWX19BbY3ftkYoFWcH0Q" width="517" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7a47ab6fc3720f1b1edfe154e65b03cbb89200_2_517x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7a47ab6fc3720f1b1edfe154e65b03cbb89200_2_775x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7a47ab6fc3720f1b1edfe154e65b03cbb89200_2_1034x460.png 2x" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1366×609 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @aseman (2020-11-01 20:27 UTC)

<p>Hi 3D slicer experts and all<br>
Unfortunately, I didn’t receive any feedback. In Smoothing Recursive Gaussian  Image Filter, I selected different values for Sigma. Finally, I find that for Sigma with three components (a,b,c),  it seems that if a&gt;&gt; b and c , the Sagittal view is  the sharpest. Also, for b&gt;&gt; a and c; Coronal view is the sharpest and for c&gt;&gt; a and b,  Axial view is the sharpest (like the below figure).<br>
So, can we conclude that “a” component has the most smoothing on L-R axis,  “b” component on A-P and “c” component on  S-I? In other words, do the “a, b,and c” components have the most smoothing on RAS, respectively?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad170b619252327c3cf069924e8c3c5add8d5472.png" data-download-href="/uploads/short-url/oHdYryqFSYHQZR2yY4tvVyQTc9c.png?dl=1" title="pic1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad170b619252327c3cf069924e8c3c5add8d5472_2_242x500.png" alt="pic1" data-base62-sha1="oHdYryqFSYHQZR2yY4tvVyQTc9c" width="242" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad170b619252327c3cf069924e8c3c5add8d5472_2_242x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad170b619252327c3cf069924e8c3c5add8d5472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad170b619252327c3cf069924e8c3c5add8d5472.png 2x" data-dominant-color="353434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic1</span><span class="informations">295×609 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-11-01 20:34 UTC)

<p>Yes, what you describe is correct, and it is so because Slicer uses <a href="https://www.slicer.org/wiki/Coordinate_systems">RAS coordinate system</a>.</p>

---
