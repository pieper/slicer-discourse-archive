# Converting 2d hand drawn atlas into 3d atlas with region volumes

**Topic ID**: 41920
**Date**: 2025-02-28
**URL**: https://discourse.slicer.org/t/converting-2d-hand-drawn-atlas-into-3d-atlas-with-region-volumes/41920

---

## Post #1 by @imillercrews (2025-02-28 16:00 UTC)

<p>My field uses an old hand drawn bird brain atlas from the 70’s for doing dissections and I wanted to try and convert the 2d images into a 3d model for demonstration and training purposes. Does this seem like something 3D slicer can do this?</p>
<p>I’ve attached two sample screenshots of the atlas to give an idea of what the data is like (these drawings are only one hemisphere so half the brain). The two slices (A6.0 and A5.0) have axes for coordinates with the “A” indicating depth. So it shouldn’t be a problem aligning everything. I’m guessing that the names of the regions will need to be removed. Being able to keep and match up the internal lines would be helpful, but not a deal breaker.</p>
<p>Ideally, I would want to overlay the regions we are interested in. For example, I made some mock color images where the red and yellow areas represent two example regions. In the 3d model, it would be great to have the volume of the red and yellow areas across sections and therefore show where the two regions are across the brain.</p>
<p>Looking around the forums it seems like this might be possible with SlicerMorph:</p><aside class="quote" data-post="1" data-topic="30175">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/8797f3/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-model-creation-through-multiple-image-slices/30175">3D model creation through multiple image slices</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    After trying multiple tools, I think this tool may work for my project. Is this software able to take a set of 2D images and create a 3D model by stacking the 2D images one on top of another? 
Sorry if this question is super simple. Thanks in advance.
  </blockquote>
</aside>

<p>Apologies if this is a rather basic question. Any insight would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2673f858dec3aeb5a36cf8faa89f7658fc422ed5.png" data-download-href="/uploads/short-url/5uaBJMi0OnFrxuhDlB8QyLKaAcJ.png?dl=1" title="Brain_section_A5.0_color" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2673f858dec3aeb5a36cf8faa89f7658fc422ed5.png" alt="Brain_section_A5.0_color" data-base62-sha1="5uaBJMi0OnFrxuhDlB8QyLKaAcJ" width="263" height="397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brain_section_A5.0_color</span><span class="informations">263×397 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbadbb96726a05a421c694034abdcd0049edfdca.png" data-download-href="/uploads/short-url/qMhvtCjP7jnZkQSsbCDMKl2v5I6.png?dl=1" title="Brain_section_A6.0_color" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbadbb96726a05a421c694034abdcd0049edfdca.png" alt="Brain_section_A6.0_color" data-base62-sha1="qMhvtCjP7jnZkQSsbCDMKl2v5I6" width="261" height="405"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brain_section_A6.0_color</span><span class="informations">261×405 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b743761a70668d509b57466619245aa7c25afc89.png" data-download-href="/uploads/short-url/q9dUz4cmCSruD7OKbn16DhujeyJ.png?dl=1" title="Brain_section_A5.0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b743761a70668d509b57466619245aa7c25afc89.png" alt="Brain_section_A5.0" data-base62-sha1="q9dUz4cmCSruD7OKbn16DhujeyJ" width="263" height="397"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brain_section_A5.0</span><span class="informations">263×397 9.27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/392ed9567748fcbe8c2c0a0dcc322a30aea7a3f0.png" data-download-href="/uploads/short-url/89RAxcCEt7aTWZnvPW9KNxXHo8E.png?dl=1" title="Brain_section_A6.0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/392ed9567748fcbe8c2c0a0dcc322a30aea7a3f0.png" alt="Brain_section_A6.0" data-base62-sha1="89RAxcCEt7aTWZnvPW9KNxXHo8E" width="261" height="405"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brain_section_A6.0</span><span class="informations">261×405 9.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-02-28 17:15 UTC)

<p>yes, you should be able to load them and display them in 3D.  You can play around with the spacing so the slices are in the right aspect ratio to try to connect things up, but of course it’s going to be very approximate.   You eventually want to scan a real brain and transfer the labels to that space.</p>

---

## Post #3 by @imillercrews (2025-03-03 13:58 UTC)

<p>Thank you! Sounds like I should give it a shot.</p>
<p>Funnily enough, there is a more recent 3D brain but most labs stick to this older atlas. Probably due to institutional inertia. So, it will be helpful to have a 3D version of this one just to help with training.</p>

---
