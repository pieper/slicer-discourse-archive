---
topic_id: 28845
title: "How To Export Files That Pyradiomics Need"
date: 2023-04-11
url: https://discourse.slicer.org/t/28845
---

# How to export files that pyradiomics need?

**Topic ID**: 28845
**Date**: 2023-04-11
**URL**: https://discourse.slicer.org/t/how-to-export-files-that-pyradiomics-need/28845

---

## Post #1 by @onkaparinga (2023-04-11 18:56 UTC)

<p>As pyradiomics examples show, it requires two files:<br>
a image file and a label file.<br>
Both files are .nrrd format.</p>
<p>What are the steps that 3D slicer export these files after drawing ROI ?</p>

---

## Post #2 by @pieper (2023-04-11 20:36 UTC)

<p>You don’t need to export them if you use the SlicerRadiomics extension.</p>

---

## Post #3 by @onkaparinga (2023-04-12 00:29 UTC)

<p>SlicerRadiomics crashes on my 3d slicer.<br>
I use python to export features.</p>

---

## Post #4 by @pieper (2023-04-12 12:56 UTC)

<p>Be sure to file an issue describing how to replicate any crashes you see:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/6e4a9be0dfdb949c7acd55ff6e2255af584c820022e8f71c1c5b86547d9f7e0f/AIM-Harvard/SlicerRadiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues" target="_blank" rel="noopener">Issues · AIM-Harvard/SlicerRadiomics</a></h3>

  <p>A Slicer extension to provide a GUI around pyradiomics - Issues · AIM-Harvard/SlicerRadiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For running PyRadiomics, best to start with working example data from the tutorials or documentation and then compare the headers with what you get on your data to narrow down why something may not be working.</p>

---

## Post #5 by @onkaparinga (2023-04-12 13:17 UTC)

<p>Thank you for your reply.<br>
I worked with the example data of pyradiomics: a image file (.nrrd) and a mask file (.nrrd).<br>
Next I used 3d slicer to draw my ROI. Then I need to export these two files: image and mask file (.nrrd). This is what I am confused with.</p>

---

## Post #6 by @pieper (2023-04-12 13:20 UTC)

<p>It should work to just save the data. Can you describe what isn’t working?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---
