# Why not working monai pathology?

**Topic ID**: 24703
**Date**: 2022-08-10
**URL**: https://discourse.slicer.org/t/why-not-working-monai-pathology/24703

---

## Post #1 by @jhchoi (2022-08-10 06:18 UTC)

<p>I installed monai to 3d slicer 5.0.<br>
It was working very well(as using radiology with sample files).<br>
so I want to change from radiology to pathology and other sample files.<br>
but in this pic, it was not working…<br>
how to work normally?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38d8765e9b23349555995823fdb1ca47f654bd2b.jpeg" data-download-href="/uploads/short-url/86SvqmnXbz37RXVuumSZYekdrtx.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d8765e9b23349555995823fdb1ca47f654bd2b_2_690x262.jpeg" alt="1" data-base62-sha1="86SvqmnXbz37RXVuumSZYekdrtx" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d8765e9b23349555995823fdb1ca47f654bd2b_2_690x262.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d8765e9b23349555995823fdb1ca47f654bd2b_2_1035x393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d8765e9b23349555995823fdb1ca47f654bd2b_2_1380x524.jpeg 2x" data-dominant-color="1B1B1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1650×628 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-08-10 13:48 UTC)

<p>MONAI Label for pathology introduced a dependency on OpenSlide, so you need to install that on your system or else disable the pathology app from MONAI Label if you don’t need it - I don’t think there’s a high level option so you would need to edit the code.</p>

---
