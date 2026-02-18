# 3D view of AI detected area

**Topic ID**: 1932
**Date**: 2018-01-25
**URL**: https://discourse.slicer.org/t/3d-view-of-ai-detected-area/1932

---

## Post #1 by @js0701 (2018-01-25 17:24 UTC)

<p>Hello, I am a new user.<br>
What I want to do with 3dslicer:<br>
I have a series of DICOM. On each DICOM slicer I want to use a deep learning framework to detect a interesting area(AOI), the detected area is 2D area in a 2d slicer. But finally I want to generate 3D view of the detected region by a series of detected 2D area.<br>
I am not sure if I have explained clearly but I want to know if is there any example of doing those stuff by 3d slicer?</p>

---

## Post #2 by @pieper (2018-01-25 19:24 UTC)

<p>The DeepInfer and TOMAAT extensions represent a couple ways to get deep learning segmentations into Slicer for 3D modeling.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/DeepInfer/Slicer-DeepInfer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/DeepInfer/Slicer-DeepInfer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/4f9af569b2cee478c7a44de63edfb9b2f6815c110930d237dec858858ab7e524/DeepInfer/Slicer-DeepInfer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/DeepInfer/Slicer-DeepInfer" target="_blank" rel="noopener">GitHub - DeepInfer/Slicer-DeepInfer: 3D Slicer Module for connecting to model...</a></h3>

  <p>3D Slicer Module for connecting to model repository and use models for image analysis. - GitHub - DeepInfer/Slicer-DeepInfer: 3D Slicer Module for connecting to model repository and use models for ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/faustomilletari/TOMAAT-Slicer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/faustomilletari/TOMAAT-Slicer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d4fb2fde8b660e7fd26ab0e2e9bc402163781a7065333f65e9137c5aa84ecb6f/faustomilletari/TOMAAT-Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/faustomilletari/TOMAAT-Slicer" target="_blank" rel="noopener">GitHub - faustomilletari/TOMAAT-Slicer: Slicer extension for TOMAAT</a></h3>

  <p>Slicer extension for TOMAAT. Contribute to faustomilletari/TOMAAT-Slicer development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
