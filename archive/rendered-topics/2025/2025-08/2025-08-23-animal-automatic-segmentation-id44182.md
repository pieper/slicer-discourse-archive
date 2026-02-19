---
topic_id: 44182
title: "Animal Automatic Segmentation"
date: 2025-08-23
url: https://discourse.slicer.org/t/44182
---

# Animal automatic segmentation

**Topic ID**: 44182
**Date**: 2025-08-23
**URL**: https://discourse.slicer.org/t/animal-automatic-segmentation/44182

---

## Post #1 by @Melodicpinpon (2025-08-23 18:46 UTC)

<p>Hi everyone,</p>
<p>As the tools for automatic segmentation are evolving rapidly, Is there any similar tool meant for animals (dogs or cats?).</p>
<p>I’ve tried Total Segmentator on a dog CTscan and on a pig and it kind of work but can only be used to provide the main volumes and will miss/bridge some ribs, etc.</p>
<p>Such tool would facilitate my professional activity for the coming year: Z-Anatomy will produce a veterinary model under CC-BY-SA in partnership with an University.<br>
Happy year 2025/2026 to you!</p>

---

## Post #2 by @pieper (2025-08-23 19:50 UTC)

<p>The links below give some idea of what’s possible given the various tools available.  I’m not aware of off the shelf models for anything but the MEMOS mouse embryo case, but as the nnmouse example shows, if you have several example cases then using nnU-Net to train a model is very doable.  At a recent meeting we tried the nnInteractive tool on the leg bones and muscles of a microCT of a salamander and also on the vertebrae and other bones of some fish and it worked great.  So I think there’s plenty of tooling available for anyone who wants to invest some time in making TotalSegmentator-style packages for non-human species.  That’s definitely something the SlicerMorph project aims for, but mostly for biology purposes and not so much veterinary.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/SlicerMEMOS">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMEMOS" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/6cc8d8d5240b5610256bff36a084f591/SlicerMorph/SlicerMEMOS" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/SlicerMEMOS" target="_blank" rel="noopener">GitHub - SlicerMorph/SlicerMEMOS: Mouse Embryo Multi-Organ Segmentations </a></h3>

    <p><span class="github-repo-description">Mouse Embryo Multi-Organ Segmentations </span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/nnmouse">
  <header class="source">

      <a href="https://github.com/pieper/nnmouse" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/b3ed1f96fd861b64b82f0a73c7cb7e92/pieper/nnmouse" class="thumbnail">

  <h3><a href="https://github.com/pieper/nnmouse" target="_blank" rel="noopener">GitHub - pieper/nnmouse: Sample scripts for training nnU-Net on mouse fetus...</a></h3>

    <p><span class="github-repo-description">Sample scripts for training nnU-Net on mouse fetus data</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/coendevente/SlicerNNInteractive">
  <header class="source">

      <a href="https://github.com/coendevente/SlicerNNInteractive" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/88666fa6f0eac22198c2ea1ee71b378a/coendevente/SlicerNNInteractive" class="thumbnail">

  <h3><a href="https://github.com/coendevente/SlicerNNInteractive" target="_blank" rel="noopener">GitHub - coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation...</a></h3>

    <p><span class="github-repo-description">A 3D Slicer extension for efficient segmentation with nnInteractive.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Esteban_Barreiro (2025-08-24 18:40 UTC)

<p>Maybe you should take a look at the MONAI Project, and train some model with your segmentations.<br>
<a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#developers" rel="noopener nofollow ugc">https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#developers</a></p>

---
