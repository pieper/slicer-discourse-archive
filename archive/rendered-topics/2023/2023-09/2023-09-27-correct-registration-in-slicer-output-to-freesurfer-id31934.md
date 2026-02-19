---
topic_id: 31934
title: "Correct Registration In Slicer Output To Freesurfer"
date: 2023-09-27
url: https://discourse.slicer.org/t/31934
---

# Correct registration in Slicer output to Freesurfer

**Topic ID**: 31934
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/correct-registration-in-slicer-output-to-freesurfer/31934

---

## Post #1 by @Victor_Zeng (2023-09-27 14:49 UTC)

<p>Hi all, for this project here, I am inputting into Slicer a brain image made in Freesurfer, namely the orig.mgz. Then I am managing manual segmentations done in Slicer using Segment Editor. Then I click on Export visible segments to binary labelmap and click on the resulting new labelmap export to file, and save as a .mgz file. When I use the freesurfer command:</p>
<p>tkmedit 1 orig.mgz -segmentation Slicerlabel.mgz, the Slicerlabel.mgz does not correct overlay with the orig.mgz.</p>
<p>(I know tkmedit is somewhat deprecated, but I think it wouldn’t overlay in freeview either)</p>
<p>Does anyone have any pointers on where to go?</p>

---

## Post #2 by @pieper (2023-09-27 17:29 UTC)

<p>If you haven’t already, you should try to use the SlicerFreeSurfer extension:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PerkLab/SlicerFreeSurfer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PerkLab/SlicerFreeSurfer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/ec1a8136f8ea693ad3e0b4931b4fc166324b2e1216de69b15e6aea471b488c24/PerkLab/SlicerFreeSurfer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PerkLab/SlicerFreeSurfer" target="_blank" rel="noopener">GitHub - PerkLab/SlicerFreeSurfer: This repository contains the...</a></h3>

  <p>This repository contains the SlicerFreeSurferImporter extension for 3D Slicer. The extension implements a module for importing models, scalar overlays, and segmentations from FreeSurfer, as well as...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
