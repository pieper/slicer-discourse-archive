# How to remove staircase artifacts in ModelNode like mimics fill hole mode?

**Topic ID**: 29833
**Date**: 2023-06-05
**URL**: https://discourse.slicer.org/t/how-to-remove-staircase-artifacts-in-modelnode-like-mimics-fill-hole-mode/29833

---

## Post #1 by @jay1987 (2023-06-05 08:13 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f428e234710a25b8c701c2e3c4d3a8e73a9b5ba8.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f428e234710a25b8c701c2e3c4d3a8e73a9b5ba8.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f428e234710a25b8c701c2e3c4d3a8e73a9b5ba8.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @jay1987 (2023-06-05 08:15 UTC)

<p>i got a model node in slicer , is there any extension or any algorithm to make the surface of the modelnode smooth?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5034db7c4acf2a71156ebfa2c37bf0b4a276029.png" data-download-href="/uploads/short-url/pPjv0bXSUOOIlQCSjj6LhGMAPB7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5034db7c4acf2a71156ebfa2c37bf0b4a276029.png" alt="image" data-base62-sha1="pPjv0bXSUOOIlQCSjj6LhGMAPB7" width="640" height="500" data-dominant-color="87871E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×533 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @muratmaga (2023-06-05 23:53 UTC)

<p>You can use the smoothing and remeshing options in the Surface Toolbox.</p>

---

## Post #4 by @jay1987 (2023-06-06 01:42 UTC)

<p>thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> ,it’s really work , if i want to smooth part of my model,is there any extension can do this work?</p>

---

## Post #5 by @muratmaga (2023-06-06 01:49 UTC)

<p>You can probably use the dynamic modeller and plane or curve cut to split your model into two parts, and smooth the part you would like to more. Then use the mergeModels to put them together…</p>

---

## Post #6 by @jay1987 (2023-06-06 02:17 UTC)

<p>thank you <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---
