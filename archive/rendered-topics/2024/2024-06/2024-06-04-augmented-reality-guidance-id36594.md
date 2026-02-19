---
topic_id: 36594
title: "Augmented Reality Guidance"
date: 2024-06-04
url: https://discourse.slicer.org/t/36594
---

# Augmented reality guidance

**Topic ID**: 36594
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/augmented-reality-guidance/36594

---

## Post #1 by @LeidyMoraV (2024-06-04 19:12 UTC)

<p>Hello everyone,</p>
<p>I’m interested in performing landmark registration of an existing model to a patient, specifically focusing on the spine. I assume the procedure is similar to what’s shown in this <a href="https://www.youtube.com/watch?v=KdUdFQ44h3U" rel="noopener nofollow ugc">Augmented reality guidance for burr hole placement using HoloLens - YouTube</a> with some minor adjustments. Does anyone know if the codes used in the tool featured in the video are available somewhere?</p>

---

## Post #2 by @Sunderlandkyl (2024-06-04 19:17 UTC)

<p>This repository was in the video description, so I assume that it was the code used for the video:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PerkLab/HololensQuickNav">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PerkLab/HololensQuickNav" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/68cf01d49f03fbb8b5711b5bd2ceeeace62f7283a7e3abc7debeed594c447e68/PerkLab/HololensQuickNav" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PerkLab/HololensQuickNav" target="_blank" rel="noopener nofollow ugc">GitHub - PerkLab/HololensQuickNav</a></h3>

  <p>Contribute to PerkLab/HololensQuickNav development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2024-06-05 12:25 UTC)

<p>We developed that Unity app when Slicer did not support HoloLens yet. Since Slicer can now directly render 3D content to HoloLens2, I would probably use that now instead of Unity.</p>

---

## Post #4 by @LeidyMoraV (2024-06-17 15:33 UTC)

<p>Can you please further explain how to render de 3D slicer content to HoloLens2? Are you talking about the Virtual Reality Module?</p>

---

## Post #5 by @lassoan (2024-06-17 23:00 UTC)

<p>Slicer VirtualReality extension can be used with both virtual and augmented reality headsets. See setup instructions for HoloLens <a href="https://github.com/KitwareMedical/SlicerVirtualReality?tab=readme-ov-file#how-to-set-up-my-hololens-2-headset">here</a>.</p>

---
