# Ukftractography

**Topic ID**: 693
**Date**: 2017-07-15
**URL**: https://discourse.slicer.org/t/ukftractography/693

---

## Post #1 by @ElvaChen (2017-07-15 18:31 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.5.0-1</p>
<p>Hi:</p>
<p>I wonder if there is any way to view the saved output of free water fraction (free water imaging volume) in UKF? I use Slicer version 4.5.0-1.</p>
<p>Thanks.</p>
<p>Elva</p>

---

## Post #2 by @ihnorton (2017-07-16 12:18 UTC)

<p>Go to Modules-&gt;<code>Tractography Display</code> and select <code>Color By -&gt; Scalar Value</code> as below (note: if it does not work, please try a newer version than 4.5, ideally the nightly):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc8c3f945a54d011f4b37491dfab80b951e7328.png" data-download-href="/uploads/short-url/A4esyVWKe8p6ZxOPuqx8WbRiQek.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc8c3f945a54d011f4b37491dfab80b951e7328_2_474x499.png" alt="image" data-base62-sha1="A4esyVWKe8p6ZxOPuqx8WbRiQek" width="474" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc8c3f945a54d011f4b37491dfab80b951e7328_2_474x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc8c3f945a54d011f4b37491dfab80b951e7328_2_711x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc8c3f945a54d011f4b37491dfab80b951e7328_2_948x998.png 2x" data-dominant-color="EAECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1154×1216 88.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ElvaChen (2017-07-21 15:17 UTC)

<p>Hi Isaiah:</p>
<p>Thanks a lot for the prompt response.<br>
However, looks like Tractography Display is to show the tractography.<br>
I was wondering if it is possible to generate the scalar volume of free water maps using UKF or other modules.</p>
<p>Thanks.</p>
<p>Elva</p>

---

## Post #4 by @ihnorton (2017-07-22 01:12 UTC)

<p>UKF computes these other measures in the process of fitting tractography streamlines, so it doesn’t provide any volumetric output.</p>

---

## Post #5 by @ElvaChen (2017-07-22 08:57 UTC)

<p>Dear Isaiah:</p>
<p>Got it. Still appreciate your kind response.</p>
<p>Thanks.</p>
<p>Elva</p>

---

## Post #6 by @ljod (2017-07-22 10:19 UTC)

<p>If you are interested in free water maps, please contact our colleague Ofer Pasternak for software:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://lmi.med.harvard.edu/files/lmi/files/lmi16x16_0.ico?m=1438370840" class="site-icon" width="16" height="16">
      <a href="https://lmi.med.harvard.edu/people/ofer-pasternak" target="_blank" rel="nofollow noopener">lmi.med.harvard.edu</a>
  </header>
  <article class="onebox-body">
    <img src="https://lmi.med.harvard.edu/files/lmi/files/ofer_pasternak.jpg?m=1429666522" class="thumbnail onebox-avatar" width="220" height="220">

<h3><a href="https://lmi.med.harvard.edu/people/ofer-pasternak" target="_blank" rel="nofollow noopener">Ofer Pasternak</a></h3>

<p>Ofer graduated from the Interdisciplinary Program for Outstanding Students at Tel-Aviv University, Israel, where he obtained his B.Sc and PhD in computer science. For his PhD research, he worked on analysis and acquisition of Diffusion MRI, aiming at...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
