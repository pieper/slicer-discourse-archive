---
topic_id: 18612
title: "How Do Figure Out Superficial Area Of The Green Part Which I"
date: 2021-07-10
url: https://discourse.slicer.org/t/18612
---

# How do figure out superficial area of the green part which is covered by red?

**Topic ID**: 18612
**Date**: 2021-07-10
**URL**: https://discourse.slicer.org/t/how-do-figure-out-superficial-area-of-the-green-part-which-is-covered-by-red/18612

---

## Post #1 by @QSX747 (2021-07-10 07:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd97684efe475bbe6fd6537ecbab29db917aa3b7.jpeg" data-download-href="/uploads/short-url/r3cD79cjUDQS7o7vXEpLY9uoVKL.jpeg?dl=1" title="1111" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd97684efe475bbe6fd6537ecbab29db917aa3b7_2_690x374.jpeg" alt="1111" data-base62-sha1="r3cD79cjUDQS7o7vXEpLY9uoVKL" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd97684efe475bbe6fd6537ecbab29db917aa3b7_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd97684efe475bbe6fd6537ecbab29db917aa3b7_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd97684efe475bbe6fd6537ecbab29db917aa3b7_2_1380x748.jpeg 2x" data-dominant-color="7B7B80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1111</span><span class="informations">2559×1390 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hi!<br>
Based on the preoperative MRI, I am trying to reconstruct the sellar region tumor( green part) and the surrounding peritumor capsule( red part) by using 3Dslicer, and try to calculate the coverage of the sellar diaphragm barrier through the reconstruction of the sellar diaphragm barrier, so as to further study the risk of intraoperative cerebrospinal fluid leakage. The core problem was: is it possible to figure out the superficial area of green part which is covered by red? and how?<br>
Thanks !</p>

---

## Post #2 by @lassoan (2021-07-14 03:15 UTC)

<p>It is not a trivial task, but you can try the following. Export the segmentation to models, then compute distance between the two meshes (using Model to Model Distance extension). Then  extract the parts that are at a certain distance range. You can experiment with the threshold range in Models module, in Display → Scalars → Threshold.</p>

---

## Post #3 by @QSX747 (2021-07-19 05:58 UTC)

<p>I have try the Models section but I can’t compute distance between the two meshes (using Model to Model Distance extension) as you said before,  Can you provide more details on this kind of calculation method ? Or show a simple example ? thank you very much!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66d663fef436858dc4699fa9e9d0870b7346ec40.jpeg" data-download-href="/uploads/short-url/eFK1Y2gdzhghS6O1fe2acvkDSOA.jpeg?dl=1" title="1626674417(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66d663fef436858dc4699fa9e9d0870b7346ec40_2_690x365.jpeg" alt="1626674417(1)" data-base62-sha1="eFK1Y2gdzhghS6O1fe2acvkDSOA" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66d663fef436858dc4699fa9e9d0870b7346ec40_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66d663fef436858dc4699fa9e9d0870b7346ec40_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66d663fef436858dc4699fa9e9d0870b7346ec40_2_1380x730.jpeg 2x" data-dominant-color="C4C1D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1626674417(1)</span><span class="informations">3061×1622 427 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-07-19 11:35 UTC)

<aside class="quote no-group" data-username="QSX747" data-post="3" data-topic="18612">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/71c47a/48.png" class="avatar"> QSX747:</div>
<blockquote>
<p>I have try the Models section but I can’t compute distance between the two meshes (using Model to Model Distance extension)</p>
</blockquote>
</aside>
<p>Please describe what you did, what you expected to happen, and what happened instead.</p>

---

## Post #5 by @QSX747 (2021-07-19 16:37 UTC)

<p>I think I’m stuck at the first step. I exported the two segmentations to models as the picture shows, then I try to find the “model to model distance extension” in the models section menu but I couldn’t . All I can do were just changing the look of the model and clipping selected model(I was confused about this clipping also).  My goal is to figure out the superficial area of specific part which is covered by the other part, for example can we calculate the surface area of the skull covered by the green part ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa69fb6d9aea94f47879920f4cfd2beac0e3463d.jpeg" data-download-href="/uploads/short-url/zJgqRC84YirXBMYdxEsjRRyVRox.jpeg?dl=1" title="111" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa69fb6d9aea94f47879920f4cfd2beac0e3463d_2_690x347.jpeg" alt="111" data-base62-sha1="zJgqRC84YirXBMYdxEsjRRyVRox" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa69fb6d9aea94f47879920f4cfd2beac0e3463d_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa69fb6d9aea94f47879920f4cfd2beac0e3463d_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa69fb6d9aea94f47879920f4cfd2beac0e3463d_2_1380x694.jpeg 2x" data-dominant-color="7D7C78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">111</span><span class="informations">3052×1538 560 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-07-19 16:45 UTC)

<p>Model to model distance module takes model nodes as inputs. You can export the segmentation to model node by right-clicking on it in Data module.</p>

---

## Post #7 by @QSX747 (2021-07-20 07:50 UTC)

<p>I can not find the model node <img src="https://emoji.discourse-cdn.com/twitter/cold_face.png?v=12" title=":cold_face:" class="emoji" alt=":cold_face:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f0d18e210725766eee03d8f7c170a5c0e3758b.jpeg" data-download-href="/uploads/short-url/8jWZfo39AMBY7ffY41RPYHgMZl.jpeg?dl=1" title="962627475f8b0edb525520f9bf54b53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00f0d18e210725766eee03d8f7c170a5c0e3758b_2_690x388.jpeg" alt="962627475f8b0edb525520f9bf54b53" data-base62-sha1="8jWZfo39AMBY7ffY41RPYHgMZl" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00f0d18e210725766eee03d8f7c170a5c0e3758b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00f0d18e210725766eee03d8f7c170a5c0e3758b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00f0d18e210725766eee03d8f7c170a5c0e3758b_2_1380x776.jpeg 2x" data-dominant-color="919496"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">962627475f8b0edb525520f9bf54b53</span><span class="informations">1920×1080 540 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-07-20 11:41 UTC)

<p>Select the “Export visible segments to models” menu item.</p>

---
