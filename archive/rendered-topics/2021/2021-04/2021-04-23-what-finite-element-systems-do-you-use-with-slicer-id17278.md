# What finite element systems do you use with Slicer?

**Topic ID**: 17278
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/what-finite-element-systems-do-you-use-with-slicer/17278

---

## Post #1 by @pieper (2021-04-23 14:04 UTC)

<p>Hi -</p>
<p>We are doing large deformation mechanical simulation project that currently uses <a href="https://www.mathworks.com/products/matlab.html">matlab</a> and <a href="https://www.comsol.com/">comsol</a> and would like to switch to something more Slicer-like (free, python-based, extendable, etc).</p>
<p>What packages have people used and what was your experience?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @muratmaga (2021-04-23 15:09 UTC)

<p>As I recall, there has been multiple threads about getting data from Slicer into FEBio, which I think is open source.</p>
<aside class="quote" data-post="1" data-topic="10444">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-it-possible-to-do-a-segmentation-of-the-lumbar-spine-from-ct-data-and-use-the-3d-model-igs-for-further-finite-element-analysis-in-abaqus-or-febio/10444">Is it possible to do a segmentation of the lumbar spine from CT-data and use the 3D model (.igs) for further finite element analysis in ABAQUS or FEBio?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have never worked with 3D Slicer before and I am quiet new in this field. But I would like create a 3D model out of CT-DICOM-data. It is important that the HU values of the cortical and trabecular bone will be safed in the output (as .igs) for further Finite element analysis in ABAQUS or FEBio. 
Furthermore I would like to know if it is possible in 3D Slicer to do material assignment and volumetric meshing. 
I would appreciate any support. 
Thank you in advance
  </blockquote>
</aside>


---

## Post #3 by @pieper (2021-04-23 17:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="17278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>FEBio</p>
</blockquote>
</aside>
<p>Ah, yes, that’s the one I was trying to remember the name of.</p>
<p>Any other suggestions from the crowd?</p>

---

## Post #4 by @robertf (2021-04-23 18:19 UTC)

<p>We use Code_Aster (uses Python for scripting etc.) as well as FEBio.</p>

---

## Post #5 by @eftaxiop (2021-04-23 22:07 UTC)

<p>Στις Παρασκευή, 23 Απριλίου 2021 8:54:06 Μ.Μ. EEST Steve Pieper (Isomics Inc.)<br>
via 3D Slicer Community έγραψε:</p>
<blockquote>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="17278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>FEBio</p>
</blockquote>
</aside>
<p>Ah, yes, that’s the one I was trying to remember the name of.</p>
<p>Any other suggestions from the crowd?</p>
</blockquote>
<p>FreeFem is another option.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://freefem.org/">
  <header class="source">
      <img src="https://freefem.org/img/symbol_FreeFEM_97x97.png" class="site-icon" width="489" height="489">

      <a href="https://freefem.org/" target="_blank" rel="noopener nofollow ugc">freefem.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://freefem.org/" target="_blank" rel="noopener nofollow ugc">FreeFEM - An open-source PDE Solver using the Finite Element Method</a></h3>

  <p>A free and open source software to solve partial differential equations (PDE) using the Finite Element Method (FEM)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
