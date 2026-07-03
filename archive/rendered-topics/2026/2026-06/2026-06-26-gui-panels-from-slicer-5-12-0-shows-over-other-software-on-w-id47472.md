---
topic_id: 47472
title: "GUI panels from Slicer 5.12.0 shows over other software on Windows 11"
date: 2026-06-26
url: https://discourse.slicer.org/t/47472
last_bumped: 2026-07-02T19:23:38.999Z
---

# GUI panels from Slicer 5.12.0 shows over other software on Windows 11

**Topic ID**: 47472
**Date**: 2026-06-26
**URL**: https://discourse.slicer.org/t/gui-panels-from-slicer-5-12-0-shows-over-other-software-on-windows-11/47472

---

## Post #1 by @Esteban_Barreiro (2026-06-26 14:42 UTC)

<p>Hello.</p>
<p>I’m experiencing some GUI glitches in the Slicer 5.12.0 version.</p>
<p>Some of the menus, from the Red, Green, Yellow viewers stay visible over every other software. I’m on Windows 11.</p>
<p>In the attached image you can see some Slicer menus showing over other software (Paint)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc.jpeg" data-download-href="/uploads/short-url/97p6MU12JGbvgU9fvaKaYOnWy7y.jpeg?dl=1" title="Captura de pantalla 2026-06-26 113730" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_690x371.jpeg" alt="Captura de pantalla 2026-06-26 113730" data-base62-sha1="97p6MU12JGbvgU9fvaKaYOnWy7y" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_1380x742.jpeg 2x" data-dominant-color="87878C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2026-06-26 113730</span><span class="informations">1917×1032 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-06-28 12:37 UTC)

<p>It seems that it is related to pinning the ciew controllers to keep them always visible. Could you please try if tou can reproduce it with Slicer-5.10?</p>

---

## Post #3 by @Esteban_Barreiro (2026-06-28 19:47 UTC)

<p>Hi Andras, thanks for your response.</p>
<p>It doesnt happen in the 5.10 version, just in 5.12.</p>

---

## Post #4 by @jamesobutler (2026-06-29 20:46 UTC)

<p>I can confirm this also happens using Slicer 5.12.0 on macOS. Below shows the pinned pop-up widget displaying over a Finder window. This seems to point to a possible CTK regression where this pop-up widget is maintained.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816.png" data-download-href="/uploads/short-url/aK1mo4PYUZ2HfeZc5qqvETcqx4a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_690x182.png" alt="image" data-base62-sha1="aK1mo4PYUZ2HfeZc5qqvETcqx4a" width="690" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_690x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_1035x273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816.png 2x" data-dominant-color="DCDCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1258×333 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Esteban_Barreiro (2026-07-02 19:23 UTC)

<p>Hi!</p>
<p>Thanks for your response James.</p>
<p>I’m lacking of time, but, should we open a Bug Report on the bugtracker on Github? I’m afraid if I do it, maybe I can’t follow it up as is needed.</p>

---
