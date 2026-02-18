# Import pixelation

**Topic ID**: 2075
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/import-pixelation/2075

---

## Post #1 by @Ella (2018-02-12 23:05 UTC)

<p>Hi there,</p>
<p>When I import DICOM data I have been finding that sometimes it pixelates some of the views. Does anyone know why and how to prevent this from happening?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd43ddfc27d571bed0bbe57a91bf55faa2a631f9.jpeg" data-download-href="/uploads/short-url/A8ucGM9sB0rwDNE78VjVGdvv0aR.jpeg?dl=1" title="slicerforum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd43ddfc27d571bed0bbe57a91bf55faa2a631f9_2_656x500.jpeg" alt="slicerforum" data-base62-sha1="A8ucGM9sB0rwDNE78VjVGdvv0aR" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd43ddfc27d571bed0bbe57a91bf55faa2a631f9_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd43ddfc27d571bed0bbe57a91bf55faa2a631f9_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd43ddfc27d571bed0bbe57a91bf55faa2a631f9_2_1312x1000.jpeg 2x" data-dominant-color="535360"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerforum</span><span class="informations">1374×1046 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks</p>

---

## Post #2 by @pieper (2018-02-12 23:34 UTC)

<p>That looks normal to me - probably the data is sampled less finely in the front to back axis - you can look at the pixel sizes in the Volumes module and you can see the original pixels by turning off interpolation in the slice controller (checkerboard button next to the volume name).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb3491285541e22fa13f6df44e3add665d2c1f9.jpeg" data-download-href="/uploads/short-url/Albotw08lTvdIYC4G99VBdJ0ZkZ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb3491285541e22fa13f6df44e3add665d2c1f9_2_690x311.jpg" alt="image" data-base62-sha1="Albotw08lTvdIYC4G99VBdJ0ZkZ" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb3491285541e22fa13f6df44e3add665d2c1f9_2_690x311.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/feb3491285541e22fa13f6df44e3add665d2c1f9_2_1035x466.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feb3491285541e22fa13f6df44e3add665d2c1f9.jpeg 2x" data-dominant-color="DCDBDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1185×535 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2018-02-13 00:01 UTC)

<aside class="quote no-group" data-username="Ella" data-post="1" data-topic="2075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/cdc98d/48.png" class="avatar"> Ella:</div>
<blockquote>
<p>how to prevent this from happening?</p>
</blockquote>
</aside>
<p>If you acquire more image slices (with less space between them) then you can have high resolution along all axes. However, acquiring more image slices would expose the patient to higher X-ray dose. Therefore, when imaging live patients, spacing between slices is often chosen to be 2-10x larger than pixel spacing within an image slice.</p>

---
