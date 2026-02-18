# Can't build Slicer

**Topic ID**: 1280
**Date**: 2017-10-24
**URL**: https://discourse.slicer.org/t/cant-build-slicer/1280

---

## Post #1 by @HolyVisp (2017-10-24 21:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba1a5ea4e47b180b0a6423cfa2ba8cdf7cd4f00d.png" data-download-href="/uploads/short-url/qyliZxGYBluCavsfs5StfdZRxMx.png?dl=1" title="ошибка" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a5ea4e47b180b0a6423cfa2ba8cdf7cd4f00d_2_690x350.png" alt="ошибка" data-base62-sha1="qyliZxGYBluCavsfs5StfdZRxMx" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a5ea4e47b180b0a6423cfa2ba8cdf7cd4f00d_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a5ea4e47b180b0a6423cfa2ba8cdf7cd4f00d_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a5ea4e47b180b0a6423cfa2ba8cdf7cd4f00d_2_1380x700.png 2x" data-dominant-color="C0C7D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ошибка</span><span class="informations">1920×976 98.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Please help i don’t know what i do wrong.How i can resolve this problem</p>

---

## Post #2 by @lassoan (2017-10-24 21:12 UTC)

<p>All I can see from this screen is that your build path (C:\slicer-build) is longer than the recommended C:\S4D.<br>
To say anything more, we would need to see the Output window (not just the Error List window), with English error messages.</p>

---

## Post #3 by @jcfr (2017-10-25 02:37 UTC)

<p>Considering that the line in the error log mention <code>X86</code>, and that the build seems to be a 64-bit one. It might a problem of using a 32-bit build of Qt.</p>

---

## Post #4 by @ihnorton (2017-10-25 10:40 UTC)

<p>3 posts were split to a new topic: <a href="/t/linux-build-issues/1284">Linux build issues</a></p>

---
