---
topic_id: 44835
title: "Show 3D But Not Shading In Red Window"
date: 2025-10-21
url: https://discourse.slicer.org/t/44835
---

# Show 3D but not shading in red window

**Topic ID**: 44835
**Date**: 2025-10-21
**URL**: https://discourse.slicer.org/t/show-3d-but-not-shading-in-red-window/44835

---

## Post #1 by @Hannnonk (2025-10-21 10:48 UTC)

<p>Is there a way to keep the 3D view but turn off the shading in the Red window in the conventional view?</p>
<p>thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55870be904a2142c5060d8ab6f85086eb9b11db8.jpeg" data-download-href="/uploads/short-url/ccBV5G4Y31pRnXaPlanShlWVNuU.jpeg?dl=1" title="2025-10-21_6-45-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55870be904a2142c5060d8ab6f85086eb9b11db8_2_690x484.jpeg" alt="2025-10-21_6-45-16" data-base62-sha1="ccBV5G4Y31pRnXaPlanShlWVNuU" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55870be904a2142c5060d8ab6f85086eb9b11db8_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55870be904a2142c5060d8ab6f85086eb9b11db8_2_1035x726.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55870be904a2142c5060d8ab6f85086eb9b11db8.jpeg 2x" data-dominant-color="7B7578"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-10-21_6-45-16</span><span class="informations">1321×928 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-10-21 10:51 UTC)

<p>If I understand correctly you want to show the whole model in 3D (not just the intersection), but with no shading. You can achieve that by modifying the lighting options</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13cd24fd411339c1951ddfafa46f1576a3cb2b82.png" data-download-href="/uploads/short-url/2PaAHzoh3uAqO95VUHsReIVO73I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cd24fd411339c1951ddfafa46f1576a3cb2b82_2_245x500.png" alt="image" data-base62-sha1="2PaAHzoh3uAqO95VUHsReIVO73I" width="245" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cd24fd411339c1951ddfafa46f1576a3cb2b82_2_245x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cd24fd411339c1951ddfafa46f1576a3cb2b82_2_367x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cd24fd411339c1951ddfafa46f1576a3cb2b82_2_490x1000.png 2x" data-dominant-color="EFEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">519×1058 39.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Hannnonk (2025-10-21 11:29 UTC)

<p>Maybe I should reword- I want to see the 3D view, but just a plain CT window.</p>
<p>thanks</p>

---

## Post #4 by @cpinter (2025-10-21 11:59 UTC)

<p>The slice intersection in 3D shows exactly the slice image from the 2D view. If you want to have a slice in 3D without the contour, you need to create such a view in 2D and show that in 3D.</p>

---

## Post #5 by @mau_igna_06 (2025-10-21 12:30 UTC)

<p>Try using the options marked on the red square of the picture below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fbc567a6181410e668a734de36742e65c4dad5c.jpeg" data-download-href="/uploads/short-url/95PAJF7OlSzlVaHulBEyXsmB2fW.jpeg?dl=1" title="Screenshot from 2025-10-21 09-29-02_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fbc567a6181410e668a734de36742e65c4dad5c_2_690x387.jpeg" alt="Screenshot from 2025-10-21 09-29-02_2" data-base62-sha1="95PAJF7OlSzlVaHulBEyXsmB2fW" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fbc567a6181410e668a734de36742e65c4dad5c_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fbc567a6181410e668a734de36742e65c4dad5c_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fbc567a6181410e668a734de36742e65c4dad5c_2_1380x774.jpeg 2x" data-dominant-color="879B84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-10-21 09-29-02_2</span><span class="informations">1920×1079 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>HIH</p>

---

## Post #6 by @cpinter (2025-10-21 12:33 UTC)

<p>I believe the goal is to keep the contour in 2D but not in 3D.</p>

---

## Post #7 by @Hannnonk (2025-10-21 12:53 UTC)

<p>This does work thank you<br>
KH</p>

---
