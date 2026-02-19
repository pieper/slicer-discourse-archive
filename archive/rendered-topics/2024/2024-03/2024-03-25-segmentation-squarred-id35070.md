---
topic_id: 35070
title: "Segmentation Squarred"
date: 2024-03-25
url: https://discourse.slicer.org/t/35070
---

# Segmentation squarred

**Topic ID**: 35070
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/segmentation-squarred/35070

---

## Post #1 by @candide74 (2024-03-25 19:53 UTC)

<p>Hi,<br>
I don’t understand why the segmentation looks so bad compare to other software.<br>
Do you have a idea to increase that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/058f64a5b2693227a3abd9b7b1da5bd0bbc074ca.png" data-download-href="/uploads/short-url/NbByz5Gumjpf2K7wVXnBg5CEpY.png?dl=1" title="Capture d’écran 2024-03-25 à 08.55.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/058f64a5b2693227a3abd9b7b1da5bd0bbc074ca.png" alt="Capture d’écran 2024-03-25 à 08.55.20" data-base62-sha1="NbByz5Gumjpf2K7wVXnBg5CEpY" width="439" height="500" data-dominant-color="484948"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-03-25 à 08.55.20</span><span class="informations">448×510 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a34d2bfbd943f1deb5607fa6cb95b1b2db7c9dd.png" data-download-href="/uploads/short-url/m0aHD50TVeJnYph0ur60CBYo1ZP.png?dl=1" title="Capture d’écran 2024-03-25 à 08.58.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a34d2bfbd943f1deb5607fa6cb95b1b2db7c9dd_2_466x499.png" alt="Capture d’écran 2024-03-25 à 08.58.23" data-base62-sha1="m0aHD50TVeJnYph0ur60CBYo1ZP" width="466" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a34d2bfbd943f1deb5607fa6cb95b1b2db7c9dd_2_466x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a34d2bfbd943f1deb5607fa6cb95b1b2db7c9dd_2_699x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a34d2bfbd943f1deb5607fa6cb95b1b2db7c9dd.png 2x" data-dominant-color="656565"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-03-25 à 08.58.23</span><span class="informations">852×914 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am looking to calculate volume. The 3D object looks also to squarred, and when I apply a smoothing on it, it shrinks the volume on the 3D objet (not the calculated size)<br>
Thanks you for your help</p>

---

## Post #2 by @pieper (2024-03-25 20:06 UTC)

<p>In the segmentations advanced section you can change the way the 2D views are displayed.  Typically we like to see the binary labelmap version since that’s what you are actually editing, but showing the smoothed contour can also be useful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1ddae51dfedc0316ca87b31e376d47bbd545aa.png" data-download-href="/uploads/short-url/oyC5wruAaRB0PDWyxF2YYjht934.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac1ddae51dfedc0316ca87b31e376d47bbd545aa_2_690x298.png" alt="image" data-base62-sha1="oyC5wruAaRB0PDWyxF2YYjht934" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac1ddae51dfedc0316ca87b31e376d47bbd545aa_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1ddae51dfedc0316ca87b31e376d47bbd545aa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1ddae51dfedc0316ca87b31e376d47bbd545aa.png 2x" data-dominant-color="D7DBE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×426 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
