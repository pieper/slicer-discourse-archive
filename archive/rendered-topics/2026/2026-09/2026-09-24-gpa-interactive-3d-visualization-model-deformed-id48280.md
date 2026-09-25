---
topic_id: 48280
title: "GPA interactive 3D visualization model deformed"
date: 2026-09-24
url: https://discourse.slicer.org/t/48280
last_bumped: 2026-09-25T05:12:03.340Z
---

# GPA interactive 3D visualization model deformed

**Topic ID**: 48280
**Date**: 2026-09-24
**URL**: https://discourse.slicer.org/t/gpa-interactive-3d-visualization-model-deformed/48280

---

## Post #1 by @PitaChib (2026-09-24 19:27 UTC)

<p>Thanks ahead of time, been scratching my head about this for a day so I think it’s time to ask…</p>
<p>I’m trying to generate animation of PC warping on my closest to mean shape model (a rodent brain), and when I loaded the reference model and the LM set, it seems like they align well, but the endocast is just deformed. I then tried to load the endocast .ply outside of gpa, it looks completely normal. I even tried loading the same endocast model with the LM set outside of GPA module to see if they align, and they align perfectly and endocast not deflated. See attached figures. Any clue?</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d529139c59aa641112c30537f9374ef607cd48eb.jpeg" data-download-href="/uploads/short-url/upHHRl93UJjjaVzq68MYCjuSMAz.jpeg?dl=1" title="Screenshot 2026-09-24 at 14.09.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d529139c59aa641112c30537f9374ef607cd48eb_2_517x190.jpeg" alt="Screenshot 2026-09-24 at 14.09.50" data-base62-sha1="upHHRl93UJjjaVzq68MYCjuSMAz" width="517" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d529139c59aa641112c30537f9374ef607cd48eb_2_517x190.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d529139c59aa641112c30537f9374ef607cd48eb_2_775x285.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d529139c59aa641112c30537f9374ef607cd48eb_2_1034x380.jpeg 2x" data-dominant-color="C0BFD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-24 at 14.09.50</span><span class="informations">1920×709 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Deflated brain.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d109cb877fc2a238a56c2e6432b56af4af7e72c6.jpeg" data-download-href="/uploads/short-url/tPeMb8RySTZi4rFT8ee0SPsbnEO.jpeg?dl=1" title="Screenshot 2026-09-24 at 14.11.41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d109cb877fc2a238a56c2e6432b56af4af7e72c6_2_643x500.jpeg" alt="Screenshot 2026-09-24 at 14.11.41" data-base62-sha1="tPeMb8RySTZi4rFT8ee0SPsbnEO" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d109cb877fc2a238a56c2e6432b56af4af7e72c6_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d109cb877fc2a238a56c2e6432b56af4af7e72c6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d109cb877fc2a238a56c2e6432b56af4af7e72c6.jpeg 2x" data-dominant-color="A1A3C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-24 at 14.11.41</span><span class="informations">934×726 55.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>loaded outside of GPA module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88722fdff869d9d0588cce4bed01dacf9e75bc21.jpeg" data-download-href="/uploads/short-url/jt3zZxdU65hpnUjNl2GaVwUQlMd.jpeg?dl=1" title="Screenshot 2026-09-24 at 14.12.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88722fdff869d9d0588cce4bed01dacf9e75bc21_2_676x500.jpeg" alt="Screenshot 2026-09-24 at 14.12.15" data-base62-sha1="jt3zZxdU65hpnUjNl2GaVwUQlMd" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88722fdff869d9d0588cce4bed01dacf9e75bc21_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88722fdff869d9d0588cce4bed01dacf9e75bc21_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88722fdff869d9d0588cce4bed01dacf9e75bc21.jpeg 2x" data-dominant-color="9898BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-24 at 14.12.15</span><span class="informations">1188×878 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Inside GPA module</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1057eeb303d47654ed922508f46a848821f393.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f4d157d9f963e4ec6b0879ccdba400e271fe95b.png" data-video-base62-sha1="8ZT5YxLtDeQzV5HjG4VrVMR02XN.mp4">
  </div>Recording of the warping<p></p>

---

## Post #2 by @PitaChib (2026-09-24 19:36 UTC)

<p>I suppose I should add, I used the sample dataset on mouse skull and it worked perfectly fine for me.</p>

---

## Post #3 by @muratmaga (2026-09-24 20:08 UTC)

<p>I am not sure I understood the problem. Are you saying yellow model is also deformed (because it shouldnt, that the visual of the reference model). Blue is the one that should get deformed by the PC axes, which seems to work in your recording.</p>

---

## Post #4 by @PitaChib (2026-09-24 20:16 UTC)

<p>Sorry for the confusion Murat, yes when I load the reference model seems like both windows are equally flattened before I apply any of the PC axis warping on it (Fig 1).  But this flattening seems to only appear loading it into the GPA module, because when I load it outside in general data, it’s not flattened (Fig 2).<br>
To test this out, I then loaded the sample data inside the GPA module, which is not flattening the models loaded in the same way as my samples.</p>
<p>Hope this is better described, and thanks!</p>

---

## Post #5 by @PitaChib (2026-09-24 20:20 UTC)

<p>And yes the PC axes deforming works, but I wanted to show how flat it was because it seems like it’s not touching any of the midline landmarks but hanging on to other landmarks So I just don’t know why would this happen.</p>

---

## Post #6 by @muratmaga (2026-09-24 21:06 UTC)

<aside class="quote no-group" data-username="PitaChib" data-post="4" data-topic="48280">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pitachib/48/78512_2.png" class="avatar"> PitaChib:</div>
<blockquote>
<p>when I load the reference model seems like both windows are equally flattened before I apply any of the PC axis warping</p>
</blockquote>
</aside>
<p>Note that reference model loaded is not used as-is. First it is transformed into the meanshape of the population. Because every result is with respect to that mean shape. And what you see as the yellow model is the meanshape approximation from that reference model.</p>
<p>If you are seeing a strong deformation on the reference model, it might come in couple places.</p>
<ol>
<li>You didn’t choose the sample closest to the meanshape, and you are using an outlier.</li>
<li>You have very distinct samples in your model, so the the calculated meanshape is really not representative of any specific sample. This commonly happens with multi-species datasets with disparate morphology, or datasets that have very strong outliers (so that they shift the mean so much).</li>
</ol>

---

## Post #7 by @PitaChib (2026-09-25 04:52 UTC)

<p>Thanks for the response Murat, this is super interesting. I went back and looked for my landmarks alone, they seems fine and I have already removed the ones that are likely juvenile with different shape.</p>
<p>I chose the specimen that is closest sample to mean when it first returned in log of the GPA. Also this is the least procrustes distance specimen. My dataset is only one species. I’d think I don’t have a really strong outlier. (see later for plots)</p>
<p>So i was thinking, maybe the one side flatten is from my landmarking scheme, which is only on half of a cranium? And you can see alone the midridge is actually a set of sliding semilandmarks that I merged into a set of fixed landmarks (before I discovered GPA i was using geomorph package in R so that can slide around I suppose). And maybe that’s the reason the model isn’t sticking to those mid-ridge landmarks but sticks to other regular fixed landmarks? I see in the analysis.json there’s “SemiLandmarks”: <span class="chcklst-box fa fa-square-o" data-chk-src="4:0"></span>, but  I don’t see where to set it up in the window. Should I alternatively load the pre-merged landmark files (same specimen would have multiple files) to one analysis?</p>
<p>Again, thanks so much for your time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cee33338348850a289fedfecd3819dfdf7464b7b.jpeg" data-download-href="/uploads/short-url/twd8eBnOB3qI4TSa2azueKspoCL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cee33338348850a289fedfecd3819dfdf7464b7b_2_673x500.jpeg" alt="image" data-base62-sha1="twd8eBnOB3qI4TSa2azueKspoCL" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cee33338348850a289fedfecd3819dfdf7464b7b_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cee33338348850a289fedfecd3819dfdf7464b7b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cee33338348850a289fedfecd3819dfdf7464b7b.jpeg 2x" data-dominant-color="8E91AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">922×684 90.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf21a5d459662826a8eaade7829e2f38fb0a0f9.png" data-download-href="/uploads/short-url/qFNvN2DdUuBOW87TW6b90cvTrm1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf21a5d459662826a8eaade7829e2f38fb0a0f9_2_624x500.png" alt="image" data-base62-sha1="qFNvN2DdUuBOW87TW6b90cvTrm1" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf21a5d459662826a8eaade7829e2f38fb0a0f9_2_624x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf21a5d459662826a8eaade7829e2f38fb0a0f9_2_936x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf21a5d459662826a8eaade7829e2f38fb0a0f9_2_1248x1000.png 2x" data-dominant-color="787774"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1654×1324 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec476d54e6a393cfa298e8228a9347628a62eecc.png" data-download-href="/uploads/short-url/xIdIjOvoChWc3ttCD41ejN4Zqa0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec476d54e6a393cfa298e8228a9347628a62eecc_2_599x499.png" alt="image" data-base62-sha1="xIdIjOvoChWc3ttCD41ejN4Zqa0" width="599" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec476d54e6a393cfa298e8228a9347628a62eecc_2_599x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec476d54e6a393cfa298e8228a9347628a62eecc_2_898x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec476d54e6a393cfa298e8228a9347628a62eecc_2_1198x998.png 2x" data-dominant-color="F3F7F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1670×1392 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2026-09-25 05:12 UTC)

<aside class="quote no-group" data-username="PitaChib" data-post="7" data-topic="48280">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pitachib/48/78512_2.png" class="avatar"> PitaChib:</div>
<blockquote>
<p>So i was thinking, maybe the one side flatten is from my landmarking scheme, which is only on half of a cranium?</p>
</blockquote>
</aside>
<p>Yep, most likely. There is nothing to constrain the TPS deformation on the other side. I suggest using the Dynamic Modeller and crop the reference model to contain only the landmarked half and see if it help.</p>

---
