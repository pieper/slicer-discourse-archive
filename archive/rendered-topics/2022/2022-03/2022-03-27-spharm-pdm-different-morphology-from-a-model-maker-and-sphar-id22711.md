# SPHARM-PDM: Different morphology from a model maker and SPHARM

**Topic ID**: 22711
**Date**: 2022-03-27
**URL**: https://discourse.slicer.org/t/spharm-pdm-different-morphology-from-a-model-maker-and-spharm/22711

---

## Post #1 by @Bryan_Jung (2022-03-27 16:05 UTC)

<p>Dear Slicer community,</p>
<p>I am teaching myself how to use SPHARM-PDM for my future research projects. I have been using publicly available CBCT images. Recently, I successfully segmented a TMJ from a CBCT file using ITK-Snap 3.6 and produced a vtk file using a model maker module.</p>
<p>Interestingly, the model generated from a model maker model and SPHARM-PDM looked much different. I followed the tutorial from the Slicer website. Does anyone know if I possibly made any big mistakes? Please find the attached images.</p>
<p>Thank you for reading my post. Have a blessed day! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b946e15cd420b2211e11a6616ca489fc92e6ee.png" alt="Screen Shot 2022-03-26 at 10.30.13 PM" data-base62-sha1="imK4lrouKon0pGTlc7D8foI4n4W" width="363" height="354"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/811762735247b98c5c229cf0d1dea8fe46263032.png" alt="Screen Shot 2022-03-26 at 10.31.08 PM" data-base62-sha1="ipZH5cMbiOWAumijZrdO7lIvfcC" width="343" height="323"></p>

---

## Post #2 by @muratmaga (2022-03-28 16:09 UTC)

<p>You didn’t tell us which one is which, but in general there is no reason for two models generated from two different pipelines to look exactly similar, even though they might originate from the same dataset. That’s because details of the pipelines matter.</p>
<p>Looking at your white model, the triangles that constitute the polygon are much larger. This implies the model (or the original CBCT) is decimated/downsampled at some point. This might be done to speed up the computations or for many other reasons. There is also less smoothing in this model.</p>
<p>So again, if you apply different pipelines with different settings you will get different outcomes. To the degree they differ will depend on specifics of the pipeline.</p>

---

## Post #3 by @Bryan_Jung (2022-03-28 17:01 UTC)

<p>It makes sense. Thank you so much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
