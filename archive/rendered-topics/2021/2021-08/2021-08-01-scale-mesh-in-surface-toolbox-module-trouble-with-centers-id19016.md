---
topic_id: 19016
title: "Scale Mesh In Surface Toolbox Module Trouble With Centers"
date: 2021-08-01
url: https://discourse.slicer.org/t/19016
---

# Scale Mesh in Surface Toolbox Module trouble with centers

**Topic ID**: 19016
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/scale-mesh-in-surface-toolbox-module-trouble-with-centers/19016

---

## Post #1 by @apparrilla (2021-08-01 20:03 UTC)

<p>Hi everyone,</p>
<p>I´m trying to scale a model with Scale Mesh Tool of Surface Toolbox Module and I have some problem with the way it works with centers.</p>
<p>An example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/300769bfceaa13ef486a58e153ab36e3f1411caf.jpeg" data-download-href="/uploads/short-url/6QSNFbVTb8404vXSAyz8OJFFzkz.jpeg?dl=1" title="Scale_1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/300769bfceaa13ef486a58e153ab36e3f1411caf_2_218x250.jpeg" alt="Scale_1.PNG" data-base62-sha1="6QSNFbVTb8404vXSAyz8OJFFzkz" width="218" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/300769bfceaa13ef486a58e153ab36e3f1411caf_2_218x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/300769bfceaa13ef486a58e153ab36e3f1411caf_2_327x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/300769bfceaa13ef486a58e153ab36e3f1411caf_2_436x500.jpeg 2x" data-dominant-color="A582A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scale_1.PNG</span><span class="informations">909×1039 78.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Red model is the result of a 2x scale operation of the yellow model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69416551b15e5368f9079802496200a438d3bc7d.png" data-download-href="/uploads/short-url/f18f8IRfWckgD8TWeMuv3gV8nHD.png?dl=1" title="Scale_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69416551b15e5368f9079802496200a438d3bc7d_2_183x250.png" alt="Scale_2" data-base62-sha1="f18f8IRfWckgD8TWeMuv3gV8nHD" width="183" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69416551b15e5368f9079802496200a438d3bc7d_2_183x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69416551b15e5368f9079802496200a438d3bc7d_2_274x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69416551b15e5368f9079802496200a438d3bc7d_2_366x500.png 2x" data-dominant-color="978DB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scale_2</span><span class="informations">693×943 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I do a “Translate center to origin” operation li ke this (red is traslated model),<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3069d5b69e0c91a784148ae0976cdff7682f8b43.png" data-download-href="/uploads/short-url/6UhFsdVTV01vKRMqnAjn5acV0UX.png?dl=1" title="Scale_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d5b69e0c91a784148ae0976cdff7682f8b43_2_205x250.png" alt="Scale_3" data-base62-sha1="6UhFsdVTV01vKRMqnAjn5acV0UX" width="205" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d5b69e0c91a784148ae0976cdff7682f8b43_2_205x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d5b69e0c91a784148ae0976cdff7682f8b43_2_307x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3069d5b69e0c91a784148ae0976cdff7682f8b43_2_410x500.png 2x" data-dominant-color="9F657F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scale_3</span><span class="informations">785×953 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Big red model is right what I need from smal red model…</p>
<p>Is there any way to add an options to the tool? Something like “from origin” and “from model center”. Or just fix it…</p>
<p>PD: Why result models form operations are all red? What does it mean?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c234716f805db8ef5583946e86c2a123e401d8d.png" data-download-href="/uploads/short-url/8A0ehq3gKPoDv6mazY8uRg8tLRz.png?dl=1" title="Scale_4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c234716f805db8ef5583946e86c2a123e401d8d_2_517x78.png" alt="Scale_4" data-base62-sha1="8A0ehq3gKPoDv6mazY8uRg8tLRz" width="517" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c234716f805db8ef5583946e86c2a123e401d8d_2_517x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c234716f805db8ef5583946e86c2a123e401d8d_2_775x117.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c234716f805db8ef5583946e86c2a123e401d8d_2_1034x156.png 2x" data-dominant-color="2B3F4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scale_4</span><span class="informations">1238×188 8.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks on advance!!!</p>

---

## Post #2 by @apparrilla (2021-08-02 21:01 UTC)

<p>I´ve been looking for in Slicer Github how to access this souce code but I just have found the dll of scale mesh module? Any idea how to fix it?<br>
Thanks on advance</p>

---

## Post #3 by @lassoan (2021-08-03 17:39 UTC)

<p>The reason why scaling does not happen using some arbitrary centerpoint, such as center of gravity of a model because you would end up with intersecting models when you scale multiple models. The translation provides space for the enlarged models.</p>
<p>If you want to make your model centered after scaling then you can enable the Translate / Center option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a03877c7e403f378712f760e8ea73b36d08c0e3.png" data-download-href="/uploads/short-url/hpnOognjkAdwTHH4tu3ECOGACr1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a03877c7e403f378712f760e8ea73b36d08c0e3_2_328x500.png" alt="image" data-base62-sha1="hpnOognjkAdwTHH4tu3ECOGACr1" width="328" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a03877c7e403f378712f760e8ea73b36d08c0e3_2_328x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a03877c7e403f378712f760e8ea73b36d08c0e3_2_492x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a03877c7e403f378712f760e8ea73b36d08c0e3_2_656x1000.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×1095 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to scale the model by keeping a certain point at a fixed position then you can apply a translation transform that moves the model’s coordinate system to that point, concatenate it with a scaling transform, and concatenate it with a transform that reverses the first translation.</p>

---
