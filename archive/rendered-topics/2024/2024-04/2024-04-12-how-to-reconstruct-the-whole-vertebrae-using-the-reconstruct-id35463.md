# How to reconstruct the whole vertebrae using the reconstructed volume

**Topic ID**: 35463
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/how-to-reconstruct-the-whole-vertebrae-using-the-reconstructed-volume/35463

---

## Post #1 by @LeidyMoraV (2024-04-12 20:06 UTC)

<p>Hello everyone,</p>
<p>I am currently involved in a project aiming to reconstruct the complete volume of vertebrae solely from ultrasound images, specifically focusing on the posterior aspect. Our approach involves utilizing Principal Component Analysis (PCA) with SlicerMorph to generate a shape model.</p>
<p>Our objective is to optimize the weights of the Principal Components (PCs) to align the reconstructed partial volume as closely as possible to the shape model derived from the ultrasound image. Ultimately, we aim to reconstruct the entire volume based on this optimized approach.</p>
<p>Despite our efforts, we are encountering challenges and uncertainties regarding the necessary steps to achieve this goal. At present, we have successfully generated the reconstructed ultrasound volume and obtained the output of the PCA.</p>
<p>I would greatly appreciate any insights, guidance, or suggestions on the next steps to take in this process. Additionally, if anyone has experience or knowledge in similar projects, your input would be invaluable.</p>
<p>Thank you for your time and assistance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bff62723519cb696a691e7a1b318b7c79d61ed7.png" data-download-href="/uploads/short-url/fpofoaJAjMjPXFB08EmX5LOrKB1.png?dl=1" title="2024-04-04-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bff62723519cb696a691e7a1b318b7c79d61ed7_2_690x399.png" alt="2024-04-04-Scene" data-base62-sha1="fpofoaJAjMjPXFB08EmX5LOrKB1" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bff62723519cb696a691e7a1b318b7c79d61ed7_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bff62723519cb696a691e7a1b318b7c79d61ed7_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bff62723519cb696a691e7a1b318b7c79d61ed7.png 2x" data-dominant-color="9194CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-04-04-Scene</span><span class="informations">1366×790 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/335152b9cdfd3165a71f7ddfaf66ed2bf413c5e7.jpeg" data-download-href="/uploads/short-url/7jYAgRN0pT2lNjWNJVLgue158xx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/335152b9cdfd3165a71f7ddfaf66ed2bf413c5e7_2_689x347.jpeg" alt="image" data-base62-sha1="7jYAgRN0pT2lNjWNJVLgue158xx" width="689" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/335152b9cdfd3165a71f7ddfaf66ed2bf413c5e7_2_689x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/335152b9cdfd3165a71f7ddfaf66ed2bf413c5e7_2_1033x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/335152b9cdfd3165a71f7ddfaf66ed2bf413c5e7.jpeg 2x" data-dominant-color="9393C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1268×639 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-04-23 15:24 UTC)

<aside class="quote no-group" data-username="LeidyMoraV" data-post="1" data-topic="35463">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leidymorav/48/70144_2.png" class="avatar"> LeidyMoraV:</div>
<blockquote>
<p>Our approach involves utilizing Principal Component Analysis (PCA) with SlicerMorph to generate a shape model.</p>
</blockquote>
</aside>
<p>This is the part I am not sure what you mean. The way it is implemented in SlicerMorph, PCA finds the major axes of variation. It has nothing to do with generating a shape model (you can use weights from PCA to create a 3D shape using a reference model. Is that what you are referring?)</p>
<p>Anyways, if you run GPA model, you can generate an “average” shape model, if you provide a reference model. These are all documented usage in our tutorials. Looking at your landmarks in your screenshot, I would stay you need to optimize their distribution and uniformness prior to running ALPACA. That may require smoothing and editing your reference model after segmentation. You can use ‘Surface Toolbox’ to do that (smoothing/decimation and possibly uniform remeshing).</p>
<p>As for the second part of your inquiry, using the mean vertebra to reconstruct partial vertebra from US, I am not sure how you can do it. It sort of depends how “partial” the US object is. Can you share a screenshot of a what “partial vertebra” from US looks like?</p>

---

## Post #3 by @LeidyMoraV (2024-04-23 18:59 UTC)

<p>Thank you! I’ll optimize the landmark distribution. By a partial vertebra I’m refering to the model reconstruction of the ultrasound image, and it looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfd175a6a1dae2a08f789b691e8feea296f27b9c.jpeg" data-download-href="/uploads/short-url/rmTXDDcxSUFrRyjGk6ZDup4DQkc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfd175a6a1dae2a08f789b691e8feea296f27b9c.jpeg" alt="image" data-base62-sha1="rmTXDDcxSUFrRyjGk6ZDup4DQkc" width="688" height="500" data-dominant-color="9EA0A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">728×529 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’ve use the ALPACA module to reconstruct CT partial volumes (as shown in the next image) and it works, but when I do it with the U.S it seems to deform the Warp shape too much.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab9d7e399d1604f74b5638249dc86c3b498ced98.png" alt="image" data-base62-sha1="oub4Dtygi1SUqVWPRgS4e29vVoc" width="599" height="429"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a7325b749a559bbd4f2bd28d35a5201726fb25.png" data-download-href="/uploads/short-url/c4Sk8zV4K3D2RLM25oDVPi53bfv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a7325b749a559bbd4f2bd28d35a5201726fb25_2_675x500.png" alt="image" data-base62-sha1="c4Sk8zV4K3D2RLM25oDVPi53bfv" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a7325b749a559bbd4f2bd28d35a5201726fb25_2_675x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a7325b749a559bbd4f2bd28d35a5201726fb25.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a7325b749a559bbd4f2bd28d35a5201726fb25.png 2x" data-dominant-color="7DA692"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×544 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-04-23 23:36 UTC)

<aside class="quote no-group" data-username="LeidyMoraV" data-post="3" data-topic="35463">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leidymorav/48/70144_2.png" class="avatar"> LeidyMoraV:</div>
<blockquote>
<p>I’ve use the ALPACA module to reconstruct CT partial volumes</p>
</blockquote>
</aside>
<p>Can you please elaborate on steps you have done in ALPACA to achieve these two last screenshot? Specifically what you mean by “reconstruct CT Partial volume”. ALPACA is a module to transfer landmark from a reference model to a target model using point cloud registration. It is not clear to me what you are using it for.</p>

---

## Post #5 by @LeidyMoraV (2024-04-24 14:30 UTC)

<p>The aim of my project is to determine if it’s possible to obtain the entire volume of vertebrae solely through ultrasound reconstruction. To achieve this, I’ve observed that ALPACA has the capability to deform a source model into a target model, thus creating the TPS Warped Source Model. This skill appears to be beneficial for my objective. I’ve conducted tests to ascertain the extent to which the source model can be deformed to accommodate partial volumes. To do so, I’ve manually cropped a CT vertebra and utilized it as the target model to assess if the Warp model adjusts accordingly. This test has proven successful. However, when I attempt the same procedure with ultrasound reconstruction, the Warp model loses its general shape.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85da4a6512e89152c1b58d40068163662237f283.jpeg" data-download-href="/uploads/short-url/j67bIDYmLo2qgd9JLHPYQmQ0HhV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85da4a6512e89152c1b58d40068163662237f283_2_690x439.jpeg" alt="image" data-base62-sha1="j67bIDYmLo2qgd9JLHPYQmQ0HhV" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85da4a6512e89152c1b58d40068163662237f283_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85da4a6512e89152c1b58d40068163662237f283.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85da4a6512e89152c1b58d40068163662237f283.jpeg 2x" data-dominant-color="CAC5D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1015×647 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258e37efdaafbf3a0e72f3414ec7f354534a12f8.jpeg" data-download-href="/uploads/short-url/5memP9lTuBCX5Lhx8vuFCaQGKPS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258e37efdaafbf3a0e72f3414ec7f354534a12f8_2_690x423.jpeg" alt="image" data-base62-sha1="5memP9lTuBCX5Lhx8vuFCaQGKPS" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258e37efdaafbf3a0e72f3414ec7f354534a12f8_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/258e37efdaafbf3a0e72f3414ec7f354534a12f8_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258e37efdaafbf3a0e72f3414ec7f354534a12f8.jpeg 2x" data-dominant-color="C1C0C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×671 60.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2024-04-24 15:50 UTC)

<p>TPS visualization on alpaca is not the best way to evaluate the outcome. That’s because those deformations rely on the transferred landmarks, and if there is any issue during the landmark transform (which is likely with your rough U/S model) the warp will not work smoothly.</p>
<p>If you have enabled projection during the ALPACA, disable it and see if it helps a bit.</p>
<p>The proper way to do is to use the FastModelAlign, which is very similar to ALPACA, but solely focused on registration of models. FastModelAlign does similarity and affine transforms, but the deformable registration phase is not implemented yet. Is this something you have time to work on with us?</p>

---

## Post #7 by @LeidyMoraV (2024-04-24 17:39 UTC)

<p>Thank you, I’ve also tried different approaches, such as the one you mentioned about disabling the projection during ALPACA. Additionally, I’ve experimented with various landmarks, as shown in the picture. I’ve also attempted to utilize the Target Landmark Set option in ALPACA with my manual points. However, none of these methods seem to work properly.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4368e8aeb104f492226958a6fb2e0e4be6ebf024.png" alt="image" data-base62-sha1="9CkKVgZPyejl9t0ODhg9InkdWw4" width="541" height="355"></p>
<p>I’ve also explored FastModelAlign, but it only works with cut volumes of the vertebrae. Unfortunately, the registered model appears too flat and distorted.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebe0b09b87824a29866e1102adee48602ccb2fc.jpeg" data-download-href="/uploads/short-url/kmKXUtmzyFBLTZc8bIOOSaDkyTi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebe0b09b87824a29866e1102adee48602ccb2fc.jpeg" alt="image" data-base62-sha1="kmKXUtmzyFBLTZc8bIOOSaDkyTi" width="465" height="500" data-dominant-color="A08881"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">469×504 52.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally, I do have the time to collaborate with you on the deformable registration phase. Please let me know what you need! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
