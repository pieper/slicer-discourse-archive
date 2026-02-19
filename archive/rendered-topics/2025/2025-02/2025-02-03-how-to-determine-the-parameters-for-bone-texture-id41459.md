---
topic_id: 41459
title: "How To Determine The Parameters For Bone Texture"
date: 2025-02-03
url: https://discourse.slicer.org/t/41459
---

# How to determine the parameters for bone texture

**Topic ID**: 41459
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/how-to-determine-the-parameters-for-bone-texture/41459

---

## Post #1 by @cycycy (2025-02-03 11:25 UTC)

<p>I am currently trying to use the bone texture module of the 3D Slicer software (ver. 5.6.2) to evaluate the bone quality of the bone that has grown in the cleft after bone grafting in patients with cleft palate using MDCT data. I have upsampled the image spacing from 0.3125 x 0.3125 x 2.0 (mm) to 0.3125 x 0.3125 x 0.5 (mm) .<br>
I extracted the relevant bones and the values seem to be reasonable, but I can’t distinguish the trabeculae in my CT data with the naked eye, and I don’t know what process was used to calculate the values, so I doubt their reliability. (figure)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fefcd47a0d109cb87587ae242ed60d8b942b6e2.png" data-download-href="/uploads/short-url/kxk3bESkoY5niGIQGrklY7ns7LQ.png?dl=1" title="Screenshot_8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fefcd47a0d109cb87587ae242ed60d8b942b6e2_2_651x500.png" alt="Screenshot_8" data-base62-sha1="kxk3bESkoY5niGIQGrklY7ns7LQ" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fefcd47a0d109cb87587ae242ed60d8b942b6e2_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fefcd47a0d109cb87587ae242ed60d8b942b6e2_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fefcd47a0d109cb87587ae242ed60d8b942b6e2.png 2x" data-dominant-color="5C5659"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_8</span><span class="informations">1100×844 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1576d808e910ed3d359d7bdbbac2ec009ce3514.png" data-download-href="/uploads/short-url/tRV6tjdR11H2wNYkqYsbtJX8pWk.png?dl=1" title="Screenshot_9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1576d808e910ed3d359d7bdbbac2ec009ce3514_2_651x500.png" alt="Screenshot_9" data-base62-sha1="tRV6tjdR11H2wNYkqYsbtJX8pWk" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1576d808e910ed3d359d7bdbbac2ec009ce3514_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1576d808e910ed3d359d7bdbbac2ec009ce3514_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1576d808e910ed3d359d7bdbbac2ec009ce3514.png 2x" data-dominant-color="5A585D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_9</span><span class="informations">1100×844 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0871e0607177e01a77f8a203312be606028583a1.png" data-download-href="/uploads/short-url/1cHNxh13T37aKpl69eLRF56eKR3.png?dl=1" title="Screenshot (11)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0871e0607177e01a77f8a203312be606028583a1_2_690x388.png" alt="Screenshot (11)" data-base62-sha1="1cHNxh13T37aKpl69eLRF56eKR3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0871e0607177e01a77f8a203312be606028583a1_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0871e0607177e01a77f8a203312be606028583a1_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0871e0607177e01a77f8a203312be606028583a1_2_1380x776.png 2x" data-dominant-color="A7A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (11)</span><span class="informations">1920×1080 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To begin with, I don’t really understand the meaning of being able to set only one threshold value, so for now I have set the approximate boundary between the cortical bone and the trabecular bone in this data.<br>
The segmentation is roughly done to separate the cortical bone and trabecular bone, but it is very rough.</p>
<p>So, I would like to ask the following.</p>
<ol>
<li>What is recognized when the bone texture parameter is set to what and how? (cortical bone? trabecular bone? cancellous bone? bone marrow?)</li>
<li>What values does the bone texture of 3d slicer refer to and what kind of calculation is done?</li>
<li>Is the data not reliable when resampling is performed in this way?</li>
<li>I have not yet been able to find enough previous reports, but is there anyone who has evaluated the accuracy of the bone texture of 3d slicer?</li>
</ol>
<p>Sorry for my broken English.<br>
I would be grateful if you could tell me.</p>

---

## Post #2 by @pieper (2025-02-10 16:45 UTC)

<aside class="quote no-group" data-username="cycycy" data-post="1" data-topic="41459">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c67d28/48.png" class="avatar"> cycycy:</div>
<blockquote>
<p>bone texture module of the 3D Slicer</p>
</blockquote>
</aside>
<p>You may wish to file an issue or contact the developers directly:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Kitware/BoneTextureExtension/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/f0d6906306a3d357a53ff55b2dfe6942242012944d8ea2c6a5940d5f5ca01df5/Kitware/BoneTextureExtension" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">Kitware/BoneTextureExtension</a></h3>

  <p>Slicer extensions for computing feature maps of N-Dimensional images using well-known texture analysis methods. - Kitware/BoneTextureExtension</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @cycycy (2025-03-03 09:50 UTC)

<p>I’m very sorry for the delay in my reply!<br>
I’d like to ask the developers directly. Thank you for your helpful advice.</p>

---
