# Tiff images loaded brighter

**Topic ID**: 20248
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/tiff-images-loaded-brighter/20248

---

## Post #1 by @Leo_Pacheco (2021-10-19 19:16 UTC)

<p>Hello everyone,<br>
Something strange just happened. I don’t know why but suddenly 3dSlicer is loading my tiff and dcom images brighter than the original (as I show below).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1711a4b1132fca0cb9f4a118a7dd933cf3cb14a3.jpeg" alt="Mestra 1_rec00000521" data-base62-sha1="3i4MvPstn8qsLInAaMpRc84TCVR" width="384" height="384"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af61ccb4af3f6fd0b5167a5dc3b439ab173f97a0.png" data-download-href="/uploads/short-url/p1v5HVLZmXHDkcXAi0PFsQ9CG2s.png?dl=1" title="Captura de pantalla (47)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af61ccb4af3f6fd0b5167a5dc3b439ab173f97a0_2_678x500.png" alt="Captura de pantalla (47)" data-base62-sha1="p1v5HVLZmXHDkcXAi0PFsQ9CG2s" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af61ccb4af3f6fd0b5167a5dc3b439ab173f97a0_2_678x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af61ccb4af3f6fd0b5167a5dc3b439ab173f97a0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af61ccb4af3f6fd0b5167a5dc3b439ab173f97a0.png 2x" data-dominant-color="6F6E7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla (47)</span><span class="informations">833×614 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The thing is I used to be able to see this and other files accordingly, at least on another computer. I was able to adjust the contrast and brightness to somewhat fix this, but, does someone know how can I fix it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f1eb66a9a6065ae59fd854cfb9cf8cc8e32365.png" data-download-href="/uploads/short-url/hfVBC1UBCjbkRBJeklBVmCqDNsN.png?dl=1" title="Captura de pantalla (48)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f1eb66a9a6065ae59fd854cfb9cf8cc8e32365_2_690x477.png" alt="Captura de pantalla (48)" data-base62-sha1="hfVBC1UBCjbkRBJeklBVmCqDNsN" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f1eb66a9a6065ae59fd854cfb9cf8cc8e32365_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f1eb66a9a6065ae59fd854cfb9cf8cc8e32365.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f1eb66a9a6065ae59fd854cfb9cf8cc8e32365.png 2x" data-dominant-color="464651"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla (48)</span><span class="informations">887×614 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2021-10-19 19:25 UTC)

<p>Does the min/max ranges of your older and newer datasets are similar?</p>

---

## Post #3 by @lassoan (2021-10-20 05:19 UTC)

<p>Probably you use a very old Slicer release. <a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284">Behavior of current Slicer versions are not like this anymore</a>.</p>
<p>Let us know if the problem persists.</p>

---

## Post #4 by @Leo_Pacheco (2021-10-20 18:14 UTC)

<p>thank you very much, that was the problem. The version in this PC was outdated</p>

---
