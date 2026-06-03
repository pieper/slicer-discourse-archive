---
topic_id: 47214
title: "Division of the brain into individual parts"
date: 2026-06-02
url: https://discourse.slicer.org/t/47214
last_bumped: 2026-06-02T19:24:37.636Z
---

# Division of the brain into individual parts

**Topic ID**: 47214
**Date**: 2026-06-02
**URL**: https://discourse.slicer.org/t/division-of-the-brain-into-individual-parts/47214

---

## Post #1 by @Tedy (2026-06-02 14:58 UTC)

<p>Hi, can someone please help me cut out the brain parts from an MRI?<br>
I had a brain tumor and I want to make 3D models of the parts of my brain that were compressed by the tumor. It will help me come to terms with the diagnosis, treatment, and it will help with education. Thank you very much</p>

---

## Post #2 by @JASON (2026-06-02 19:18 UTC)

<p>Hello Tedy,</p>
<p>Sorry to hear about the diagnosis, but welcome to the world of medical imaging!</p>
<p>There are a few AI brain segmentation models, but the easiest to use without installing anything is <a href="https://brainchop.org/" rel="noopener nofollow ugc">https://brainchop.org/</a></p>
<ol>
<li>You can save your MRI image to NIFTI format (*.nii.gz) and then drag &amp; drop it into BrainChop.</li>
<li>There are a few different model options to choose from from model dropdown at the top.</li>
<li>Once it completes processing, press “Save Seg” button at the top to download the segmentation in NIFTI format.</li>
<li>Import the segmentation into 3D slicer (as ‘segmentation’ not as volume)</li>
<li>Press the 3D button to see it in the 3D view.</li>
</ol>

---

## Post #3 by @JASON (2026-06-02 19:24 UTC)

<p>These models are likely trained on healthy brains so may not capture tumor &amp; compression accurately.</p>
<p>I’m working on a brain &amp; tumor segmentation service, you’ll be able to sign up for a free trial when the patient-specific features are added in a few weeks:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://sim.atlasmeditech.com">
  <header class="source">
      <img src="https://sim.atlasmeditech.com/favicon.svg" class="site-icon" alt="" width="44" height="45">

      <a href="https://sim.atlasmeditech.com" target="_blank" rel="noopener nofollow ugc">sim.atlasmeditech.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://sim.atlasmeditech.com" target="_blank" rel="noopener nofollow ugc">ATLAS Simulation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you would like to learn more about neurosurgery and patient resources, you may find these links useful:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.neurosurgicalatlas.com/">
  <header class="source">

      <a href="https://www.neurosurgicalatlas.com/" target="_blank" rel="noopener nofollow ugc">The Neurosurgical Atlas</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/361;"><img src="https://www.neurosurgicalatlas.com/opengraph-image-1wvhsx?3ce848c290273f7c" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://www.neurosurgicalatlas.com/" target="_blank" rel="noopener nofollow ugc">The Neurosurgical Atlas, by Aaron Cohen-Gadol, M.D.</a></h3>

  <p>The most comprehensive and respected resource for advanced neurosurgical techniques in the world.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.aaroncohen-gadol.com/en/patients/preface">
  <header class="source">
      <img src="https://www.aaroncohen-gadol.com/favicon-32x32.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://www.aaroncohen-gadol.com/en/patients/preface" target="_blank" rel="noopener nofollow ugc">aaroncohen-gadol.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/361;"><img src="https://www.aaroncohen-gadol.com/assets/images/aaron-cohen-gadol-meta-image.jpg" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://www.aaroncohen-gadol.com/en/patients/preface" target="_blank" rel="noopener nofollow ugc">Best Care for Your Brain Tumor</a></h3>

  <p>Get access to the best resource and necessary information on brain surgery for patients to make the best decision for care and promote life after surgery.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
