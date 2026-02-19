---
topic_id: 30529
title: "Obtaining Surface Area From Volume Shape"
date: 2023-07-11
url: https://discourse.slicer.org/t/30529
---

# Obtaining Surface Area from Volume Shape

**Topic ID**: 30529
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/obtaining-surface-area-from-volume-shape/30529

---

## Post #1 by @JasonMunoz (2023-07-11 19:36 UTC)

<p>OS: Windows 11<br>
Version: 3D Slicer 5.2.2</p>
<p>Good morning,</p>
<p>I am relatively new to the world of 3D Slicer and had some questions for the use of the program. Obviously, some questions I ask may be very easy to deny/accept because I have not used the program for long enough to know, with stability, if a feature is available or not. That being said, please take kind regards with my questions, I appreciate it and your help greatly.</p>
<p>I was interested in discovering the surface area of the airways shown in my CT scans of the lung region. Namely, I wanted to use the Model given in the Volume Rendering &gt; Display &gt; Preset: CT Air, as it looked the best. I’ve read around and watched videos explaining how Segmentation was the only way to retrieve information(Surface Area) in a 3D model. I was hoping to somehow extract these Airways automatically, so that I can efficiently retrieve data of the Airways.</p>
<p>Thank you for reading and your response, any advice would help greatly.</p>
<p>Best,<br>
Jason Munoz</p>

---

## Post #2 by @pieper (2023-07-11 19:39 UTC)

<p>You can start with the LungCTAnalyzer, which has an airway segmentation tool.  Once you have the segmentation you can get the surface area with the SegmentStatistics module.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/3a76d569dd478438f1a2ee9d36994b7b46e4bf85ff9fba5dea3f45246253c7b2/rbumm/SlicerLungCTAnalyzer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rbumm/SlicerLungCTAnalyzer" target="_blank" rel="noopener">GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer extension for...</a></h3>

  <p>This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.  - GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @JasonMunoz (2023-07-17 20:43 UTC)

<p>Pieper,</p>
<p>Thank you for your assistance. I was unaware of this extension for 3D Slicer. I have been using the AirwaySegmentation Extension, but this program and your advice has given me the data that I need.</p>
<p>Many Thanks,<br>
Jason Munoz</p>

---
