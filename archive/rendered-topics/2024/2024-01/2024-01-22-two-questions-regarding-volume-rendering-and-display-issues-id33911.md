---
topic_id: 33911
title: "Two Questions Regarding Volume Rendering And Display Issues"
date: 2024-01-22
url: https://discourse.slicer.org/t/33911
---

# Two Questions Regarding Volume Rendering and Display Issues

**Topic ID**: 33911
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/two-questions-regarding-volume-rendering-and-display-issues/33911

---

## Post #1 by @Saki (2024-01-22 15:05 UTC)

<p>I am having trouble with 3D rendering of the brain using Volume Rendering in 3D Slicer. How should I configure the settings? (See first screenshot attached). Also, in the second screenshot, the number of displayed items marked in yellow has somehow decreased. How can I retrieve the original amount of information? Thank you for your assistance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90b381a20443fe5889608b289759ece5ad39f9ee.jpeg" data-download-href="/uploads/short-url/kE5ltvEKs3RygdbyL7r0H3V7yMe.jpeg?dl=1" title="Screenshot (524)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90b381a20443fe5889608b289759ece5ad39f9ee_2_690x388.jpeg" alt="Screenshot (524)" data-base62-sha1="kE5ltvEKs3RygdbyL7r0H3V7yMe" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90b381a20443fe5889608b289759ece5ad39f9ee_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90b381a20443fe5889608b289759ece5ad39f9ee_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90b381a20443fe5889608b289759ece5ad39f9ee_2_1380x776.jpeg 2x" data-dominant-color="AEACB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (524)</span><span class="informations">1920×1080 309 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303a5e784ebe682c9d8e23c8a5f3163742a432af.png" data-download-href="/uploads/short-url/6SDYmEZastaapXZ1wQ0zYCaEU6X.png?dl=1" title="Screenshot (525)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303a5e784ebe682c9d8e23c8a5f3163742a432af_2_690x388.png" alt="Screenshot (525)" data-base62-sha1="6SDYmEZastaapXZ1wQ0zYCaEU6X" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303a5e784ebe682c9d8e23c8a5f3163742a432af_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303a5e784ebe682c9d8e23c8a5f3163742a432af_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303a5e784ebe682c9d8e23c8a5f3163742a432af_2_1380x776.png 2x" data-dominant-color="ACAAAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (525)</span><span class="informations">1920×1080 484 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-01-22 15:52 UTC)

<aside class="quote no-group" data-username="Saki" data-post="1" data-topic="33911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/35a633/48.png" class="avatar"> Saki:</div>
<blockquote>
<p>How can I retrieve the original amount of information? Thank you for your assistance!</p>
</blockquote>
</aside>
<p>Somehow you reset the scene after you import the DICOM series? not sure.</p>
<p>Anyways, the easiest way to activate 3D rendering, is to go to the <code>Data</code> module and drag’n’drop the specific 3D volume you would like to render into the 3D view window.</p>

---

## Post #3 by @Saki (2024-01-24 01:18 UTC)

<p>I was able to successfully create a 3D model by dragging and dropping into the Data module!<br>
Thank you very much for your help. <img src="https://emoji.discourse-cdn.com/twitter/man_bowing.png?v=12" title=":man_bowing:" class="emoji" alt=":man_bowing:" loading="lazy" width="20" height="20"></p>

---
