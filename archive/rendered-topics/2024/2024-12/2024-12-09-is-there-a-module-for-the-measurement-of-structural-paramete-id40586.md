---
topic_id: 40586
title: "Is There A Module For The Measurement Of Structural Paramete"
date: 2024-12-09
url: https://discourse.slicer.org/t/40586
---

# Is there a module for the measurement of structural parameters of X-CTs of the proximal femur?

**Topic ID**: 40586
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/is-there-a-module-for-the-measurement-of-structural-parameters-of-x-cts-of-the-proximal-femur/40586

---

## Post #1 by @nikkos (2024-12-09 16:06 UTC)

<p>Hello dear community,</p>
<p>I am planning to calculate structural parameters from X-CTs of the proximal femur, such as measuring the thickness of the corticalis and the trabecular distances. Is there a possible module for this? If not, has anyone had any experience with a Python library for this?</p>
<p>Best regards</p>

---

## Post #2 by @pieper (2024-12-09 16:29 UTC)

<p>This module is probably what you need:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/Kitware/BoneTextureExtension">
  <header class="source">

      <a href="https://github.com/Kitware/BoneTextureExtension" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/05154986a0f19ebbc606902b5b15fb05/Kitware/BoneTextureExtension" class="thumbnail">

  <h3><a href="https://github.com/Kitware/BoneTextureExtension" target="_blank" rel="noopener">GitHub - Kitware/BoneTextureExtension: Slicer extensions for computing feature maps of...</a></h3>

    <p><span class="github-repo-description">Slicer extensions for computing feature maps of N-Dimensional images using well-known texture analysis methods.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or there is <a href="https://github.com/AIM-Harvard/SlicerRadiomics">SlicerRadiomics</a>.</p>

---

## Post #3 by @nikkos (2024-12-09 17:44 UTC)

<p>Thank you for your reply. That definitely sounds very interesting. I did a quick check and unfortunately I couldn’t see which of the modules could give me the Corticalis Dickle or the trabecular distances? I am currently considering whether it would be best to build such a script <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2024-12-09 18:15 UTC)

<p>I’m not familiar with the details, but if you don’t see what you need in the existing extension you could contact the authors and ideally contribute new code to cover any missing calculations.</p>

---
