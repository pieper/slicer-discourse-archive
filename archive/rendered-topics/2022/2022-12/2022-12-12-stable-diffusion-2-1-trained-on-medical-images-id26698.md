# Stable diffusion 2.1 trained on Medical images?

**Topic ID**: 26698
**Date**: 2022-12-12
**URL**: https://discourse.slicer.org/t/stable-diffusion-2-1-trained-on-medical-images/26698

---

## Post #1 by @mau_igna_06 (2022-12-12 20:22 UTC)

<p>It would be very nice to see a NCI-IDC (medical images) trained model such as the open-source Stable Difussion 2.1 for image-from-text-generation</p>
<p>Here is a picture from it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee8fc6e07e9ae826f914de4e675dfcc7423cdee2.jpeg" data-download-href="/uploads/short-url/y2pG43DLFkXnQ1Sq970pUOKBJ50.jpeg?dl=1" title="Screenshot_20221212-171444_Firefox" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8fc6e07e9ae826f914de4e675dfcc7423cdee2_2_225x500.jpeg" alt="Screenshot_20221212-171444_Firefox" data-base62-sha1="y2pG43DLFkXnQ1Sq970pUOKBJ50" width="225" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8fc6e07e9ae826f914de4e675dfcc7423cdee2_2_225x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8fc6e07e9ae826f914de4e675dfcc7423cdee2_2_337x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8fc6e07e9ae826f914de4e675dfcc7423cdee2_2_450x1000.jpeg 2x" data-dominant-color="ADB0B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20221212-171444_Firefox</span><span class="informations">1080×2400 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mikebind (2022-12-12 23:32 UTC)

<p>Depending on the equipment you have available (especially GPU) and willingness to invest some time on this, this is something you could likely accomplish yourself by fine-tuning Stable Diffusion (i.e. you start from a Stable Diffusion model and then extend the training on a set of images you curate and label). If you don’t have a sufficiently powerful GPU on a local machine, it is very possible to rent enough time on cloud services to accomplish this (probably doable with much less than $50 USD).  I’d be happy to point you to some resources and suggest the approach I think it would make sense to take, but first I wonder what you would be hoping to accomplish if you were successful.  The likely result would be a model which can generate images which, at first glance, look like the types of medical images you trained in, but which generally look wrong on closer inspection (e.g. bones connecting to the wrong other bones, features which don’t make sense anatomically, the wrong number of ribs, mixtures of kinds of images, etc.; Stable Diffusion famously still struggles mightily to produce images where hands are not obviously deformed, despite being trained on literally millions of images which have hands in them).  I’m not sure what use these sorts of images would be, but perhaps you have some good ideas.</p>

---

## Post #3 by @mikebind (2022-12-13 01:12 UTC)

<p>I just had a reference to this pop up in a news feed: <a href="https://arxiv.org/pdf/2210.04133.pdf" rel="noopener nofollow ugc">https://arxiv.org/pdf/2210.04133.pdf</a> Some Stanford researchers did a pretty comprehensive-looking version of what I was about to suggest to you in a small way.  I haven’t had a chance to dig into this paper at all, but you might find it very relevant.</p>

---

## Post #4 by @mau_igna_06 (2022-12-13 01:21 UTC)

<p>Nice. I’ll take a look</p>

---

## Post #5 by @mikbuch (2023-02-21 14:18 UTC)

<p>An update from the same group: <a href="https://arxiv.org/pdf/2211.12737.pdf" rel="noopener nofollow ugc">https://arxiv.org/pdf/2211.12737.pdf</a></p>

---
