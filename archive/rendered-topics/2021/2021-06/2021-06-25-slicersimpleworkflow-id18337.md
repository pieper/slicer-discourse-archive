---
topic_id: 18337
title: "Slicersimpleworkflow"
date: 2021-06-25
url: https://discourse.slicer.org/t/18337
---

# SlicerSimpleWorkflow

**Topic ID**: 18337
**Date**: 2021-06-25
**URL**: https://discourse.slicer.org/t/slicersimpleworkflow/18337

---

## Post #1 by @seanchoi0519 (2021-06-25 10:56 UTC)

<p>Hi, if I want to test/explore a slicelet such as the following:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerSimpleWorkflows">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="20" height="20">

      <a href="https://github.com/lassoan/SlicerSimpleWorkflows" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/082edb86d9d9560856ffacb8d1d857cf14823aeed5d733e70d20f9253bc59f55/lassoan/SlicerSimpleWorkflows" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerSimpleWorkflows" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSimpleWorkflows</a></h3>

  <p>Examples of simple application-specific workflows implemented using 3D Slicer - lassoan/SlicerSimpleWorkflows</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/LumpNav">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="20" height="20">

      <a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/138fb1536bc1914008b9612fb845668b768dbaeeca03d0415f8b99ec306562d3/SlicerIGT/LumpNav" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener nofollow ugc">SlicerIGT/LumpNav</a></h3>

  <p>Slicer extension for ultrasound-guided breast tumor resection (lumpectomy) - SlicerIGT/LumpNav</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>How can I load them on Slicer? How can I launch it?<br>
Sincerely</p>

---

## Post #2 by @lassoan (2021-06-25 17:54 UTC)

<p>If you only have Python scripted modules then they don’t require compilation, therefore you can simply add the module’s folder to the “Additional module paths” in application settings. See details in the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab Slicer Programming Tutorial</a>.</p>

---
