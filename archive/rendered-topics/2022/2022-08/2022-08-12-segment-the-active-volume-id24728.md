# Segment the Active Volume

**Topic ID**: 24728
**Date**: 2022-08-12
**URL**: https://discourse.slicer.org/t/segment-the-active-volume/24728

---

## Post #1 by @michabermoy (2022-08-12 16:35 UTC)

<p>Is it possible to segment the active volume so that all other components of the volume are completely removed? For example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e371a0c5c0426c7c94f7adc55be0473cd4a23b.jpeg" data-download-href="/uploads/short-url/pOdeW1LkFnkgRxWBgWwcGCkGRQv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e371a0c5c0426c7c94f7adc55be0473cd4a23b.jpeg" alt="image" data-base62-sha1="pOdeW1LkFnkgRxWBgWwcGCkGRQv" width="690" height="286" data-dominant-color="7C7A74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×289 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2022-08-12 16:55 UTC)

<p>You can use the “Mask volume” editor effect to erase areas in the volume outside of the segment.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60bd3e7c586a6ba5a68b1c6334507727b3166146.png" alt="image" data-base62-sha1="dNNi1CFExjK6TSyoeiuXaILiHEa" width="37" height="34"></p>

---

## Post #3 by @michabermoy (2022-08-29 19:59 UTC)

<p>Do you happen to know how to accomplish this with Python code?</p>

---

## Post #4 by @jay1987 (2022-08-31 02:12 UTC)

<p>try the python code below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3112bf8d9bdfec679b966aa9231ddef3797f3df9.png" data-download-href="/uploads/short-url/707yY1ugpVK9jS6B3aJ9Isnqb8Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3112bf8d9bdfec679b966aa9231ddef3797f3df9.png" alt="image" data-base62-sha1="707yY1ugpVK9jS6B3aJ9Isnqb8Z" width="690" height="360" data-dominant-color="242524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×514 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
