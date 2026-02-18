# Modules failed to be instantiated

**Topic ID**: 24912
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/modules-failed-to-be-instantiated/24912

---

## Post #1 by @miniminic (2022-08-25 02:45 UTC)

<p>This is fine under debug, but has a lot of errors under Release<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4dc39c0d25d6083e0cc71a2caaffe80bbe4823d.png" data-download-href="/uploads/short-url/un33p384cEoGdzSdqfmCpIq63Nz.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4dc39c0d25d6083e0cc71a2caaffe80bbe4823d_2_690x335.png" alt="捕获" data-base62-sha1="un33p384cEoGdzSdqfmCpIq63Nz" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4dc39c0d25d6083e0cc71a2caaffe80bbe4823d_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4dc39c0d25d6083e0cc71a2caaffe80bbe4823d_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4dc39c0d25d6083e0cc71a2caaffe80bbe4823d_2_1380x670.png 2x" data-dominant-color="34343C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">2384×1159 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c8042b6a55bda5d4dfbaeea311545a981b8dea9.png" data-download-href="/uploads/short-url/k2VDRqbv50T0ZrdBVM6vybI3l8t.png?dl=1" title="捕获2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c8042b6a55bda5d4dfbaeea311545a981b8dea9.png" alt="捕获2" data-base62-sha1="k2VDRqbv50T0ZrdBVM6vybI3l8t" width="690" height="461" data-dominant-color="101010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获2</span><span class="informations">1477×988 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @miniminic (2022-08-25 06:35 UTC)

<p>I rebuilt the Slicer in a different folder to temporarily fix the problem,but I don’t know if it will happen again</p>

---

## Post #3 by @jamesobutler (2022-08-25 13:00 UTC)

<p>Make sure you don’t build debug and release into the same build tree. You will need separate build trees such as at C:/S5D and C:/S5R.</p>

---

## Post #4 by @miniminic (2022-08-28 03:10 UTC)

<p>Thank for your answer.</p>

---
