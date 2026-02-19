---
topic_id: 11150
title: "My 3D Rendering Looks Like 3 Planes Instead Of A 3D Volume"
date: 2020-04-16
url: https://discourse.slicer.org/t/11150
---

# My 3D rendering looks like 3 planes instead of a 3D volume

**Topic ID**: 11150
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/my-3d-rendering-looks-like-3-planes-instead-of-a-3d-volume/11150

---

## Post #1 by @malvaradolaos (2020-04-16 13:46 UTC)

<p>Hello, i`m starting to use 3dslicer, but my rendering does not work as i wish.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d34cc8dd49dc5c049f3ae6e274c4661738cb1ede.jpeg" data-download-href="/uploads/short-url/u9ffUfsBlhGKC3v9g0WhYwF0fYa.jpeg?dl=1" title="Captura de Pantalla 2020-04-15 a la(s) 22.22.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34cc8dd49dc5c049f3ae6e274c4661738cb1ede_2_690x431.jpeg" alt="Captura de Pantalla 2020-04-15 a la(s) 22.22.36" data-base62-sha1="u9ffUfsBlhGKC3v9g0WhYwF0fYa" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34cc8dd49dc5c049f3ae6e274c4661738cb1ede_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34cc8dd49dc5c049f3ae6e274c4661738cb1ede_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34cc8dd49dc5c049f3ae6e274c4661738cb1ede_2_1380x862.jpeg 2x" data-dominant-color="B3B3B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2020-04-15 a la(s) 22.22.36</span><span class="informations">2560×1600 877 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> It looks like 3 planes in orientation, but no 3d.<br>
Thanks</p>

---

## Post #2 by @pieper (2020-04-16 14:25 UTC)

<p>Try the techniques in the tutorials, and then report if anything doesn’t work for your data.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#3D_Visualization" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#3D_Visualization</a></p>

---

## Post #3 by @lassoan (2020-04-16 14:38 UTC)

<p>You can use “Volume rendering” module (see page 34 in the tutorial that Steve linked above).</p>

---

## Post #4 by @joachim (2020-04-29 16:01 UTC)

<p>From what I can see:</p>
<ul>
<li>In order to show the volume rendering in the 3D-view, click the “closed eye” icon right below <em>Help &amp; Acknowledment</em>
</li>
<li>The 3 planes are shown in the 3D-view because each of the 3 slider views (red, yellow and green) has enabled the plane to be shown by their respective “open eye” icons (to the right of the “link” icon).</li>
</ul>

---
