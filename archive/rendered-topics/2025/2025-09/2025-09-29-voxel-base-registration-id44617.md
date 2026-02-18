# Voxel-base registration?

**Topic ID**: 44617
**Date**: 2025-09-29
**URL**: https://discourse.slicer.org/t/voxel-base-registration/44617

---

## Post #1 by @Sule (2025-09-29 03:11 UTC)

<p>I’d like to make superimposition these 3D views but i couldnt do it whatever i tried. Can you help me please?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef04d0f052f79794d65727a8ab5055027c42dd23.jpeg" data-download-href="/uploads/short-url/y6sqUoWnvMgrBgkdXjBBMevFKgz.jpeg?dl=1" title="IMG_2094" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef04d0f052f79794d65727a8ab5055027c42dd23_2_375x500.jpeg" alt="IMG_2094" data-base62-sha1="y6sqUoWnvMgrBgkdXjBBMevFKgz" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef04d0f052f79794d65727a8ab5055027c42dd23_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef04d0f052f79794d65727a8ab5055027c42dd23_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef04d0f052f79794d65727a8ab5055027c42dd23_2_750x1000.jpeg 2x" data-dominant-color="3C3B36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_2094</span><span class="informations">1920×2560 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-29 03:17 UTC)

<p>Did you try the modules listed under Registration, specifically General Registration (BRAINS)</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/index.html#registration">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/index.html#registration" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/index.html#registration" target="_blank" rel="noopener nofollow ugc">Modules — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Sule (2025-09-29 06:27 UTC)

<p>i tried them, i want to make it on voxel-based but i wait in Growing Registration module for a while and nothing happens. I used transform module to make it manuelly but that’s not what i really want actually.</p>

---

## Post #4 by @muratmaga (2025-09-29 15:21 UTC)

<aside class="quote no-group" data-username="Sule" data-post="3" data-topic="44617">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sule/48/81165_2.png" class="avatar"> Sule:</div>
<blockquote>
<p>i wait in Growing Registration module for a while and nothing happens.</p>
</blockquote>
</aside>
<p>I am not sure what you mean by that. What’s the <strong>Growing Registration</strong> module? Maybe you mean <strong>Grow from the seeds</strong> in segmen editor module?</p>
<p>If your goal is compare segments before and after, you should register your volumes first, and then segment. For registration you need to use the General Registration module.</p>

---
