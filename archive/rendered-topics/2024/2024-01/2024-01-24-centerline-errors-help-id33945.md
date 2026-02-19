---
topic_id: 33945
title: "Centerline Errors Help"
date: 2024-01-24
url: https://discourse.slicer.org/t/33945
---

# Centerline errors - help

**Topic ID**: 33945
**Date**: 2024-01-24
**URL**: https://discourse.slicer.org/t/centerline-errors-help/33945

---

## Post #1 by @tahmidullah (2024-01-24 04:53 UTC)

<p>Hi all,</p>
<p>I am having some trouble deriving the centerline from my stl. I have attached some pictures of the settings and the issues with the centerline when using the vascular modeling toolkit extension. Thank you so much!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a025a4e0f0dac383b7a28413bd2c204c18d13c1.jpeg" data-download-href="/uploads/short-url/lYqzpH3SR1iTurIyUkHpSxYPwhr.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a025a4e0f0dac383b7a28413bd2c204c18d13c1_2_690x473.jpeg" alt="Untitled" data-base62-sha1="lYqzpH3SR1iTurIyUkHpSxYPwhr" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a025a4e0f0dac383b7a28413bd2c204c18d13c1_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a025a4e0f0dac383b7a28413bd2c204c18d13c1_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a025a4e0f0dac383b7a28413bd2c204c18d13c1_2_1380x946.jpeg 2x" data-dominant-color="9B9BAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1737×1193 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0832825f42d40d3a6ce2e282247c9ac61f1085d.png" data-download-href="/uploads/short-url/rt2FWBCZEbed6vXHnSHqP5VbhrT.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0832825f42d40d3a6ce2e282247c9ac61f1085d_2_378x500.png" alt="2" data-base62-sha1="rt2FWBCZEbed6vXHnSHqP5VbhrT" width="378" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0832825f42d40d3a6ce2e282247c9ac61f1085d_2_378x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0832825f42d40d3a6ce2e282247c9ac61f1085d_2_567x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0832825f42d40d3a6ce2e282247c9ac61f1085d.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">635×839 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d0993f505df3c5c56cbbc1fee06c76ca3df3c3a.png" data-download-href="/uploads/short-url/dh2Vnm8tcgIme6PQ3Go9QAohGUa.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d0993f505df3c5c56cbbc1fee06c76ca3df3c3a_2_690x477.png" alt="3" data-base62-sha1="dh2Vnm8tcgIme6PQ3Go9QAohGUa" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d0993f505df3c5c56cbbc1fee06c76ca3df3c3a_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d0993f505df3c5c56cbbc1fee06c76ca3df3c3a_2_1035x715.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d0993f505df3c5c56cbbc1fee06c76ca3df3c3a_2_1380x954.png 2x" data-dominant-color="9B9DCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1745×1207 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-01-24 04:55 UTC)

<p>The images look good. Let us know if you have any specific questions or problems.</p>

---

## Post #3 by @tahmidullah (2024-01-24 15:15 UTC)

<p>Hi Andras,</p>
<p>Hope all is well! The network model for the centerline does not connect to the endpoints that had been placed. Is there anyway to have a curved line connecting the two endpoints in the aortic arch as presented in the first image there. The spiked triangle isn’t representative of the true centerline of an aortic arch. Thank you for your help!</p>
<p>Kind regards,</p>
<p>Mohammad Tahmid Ullah</p>

---

## Post #4 by @lassoan (2024-01-26 02:46 UTC)

<p>Network extraction does not need endpoints as input, it provides endpoints as a result. If you want to get shortest path withina centerline graph then you can use model output and constrain a markup curve to that model:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UpfDP6ejCjg" data-video-title="Finding shortest path between two points in the bronchial tree" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UpfDP6ejCjg/maxresdefault.jpg" title="Finding shortest path between two points in the bronchial tree" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="tahmidullah" data-post="3" data-topic="33945">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tahmidullah/48/69095_2.png" class="avatar"> tahmidullah:</div>
<blockquote>
<p>The spiked triangle isn’t representative of the true centerline of an aortic arch.</p>
</blockquote>
</aside>
<p>Determining continuous centerline from a very large diameter vessel to a small diameter can be tricky, but VMTK uses a very clean, reproducible method to produce a meaningful centerline curve - see <a href="https://lantiga.github.io/media/AntigaPhDThesis.pdf">Luca Antiga’s PhD Thesis</a>. Maybe you did not use the cenerline extraction method or the segmented part of the aortic arch was way too short (compared to the large diameter of the vessel).</p>

---
