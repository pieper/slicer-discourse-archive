# How to create a label map for heterogeneityCAD?

**Topic ID**: 3425
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/how-to-create-a-label-map-for-heterogeneitycad/3425

---

## Post #1 by @danceward (2018-07-09 12:30 UTC)

<p>I’m learning texture analysis from CT images,  which modules can create right label maps for heterogeneityCAD?  Modules such as segment editor and editor can not export right volumes, segment CAD just for MRI, how to do this?<br>
Thank you!</p>

---

## Post #2 by @fedorov (2018-07-09 14:38 UTC)

<p>I cannot answer questions about HeterogeneityCAD, but you can also look into the Radiomics extension, which is described in the documentation and paper referenced therein:</p>
<p><a href="http://pyradiomics.readthedocs.io/en/latest/" class="onebox" target="_blank" rel="noopener">http://pyradiomics.readthedocs.io/en/latest/</a></p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/6e4a9be0dfdb949c7acd55ff6e2255af584c820022e8f71c1c5b86547d9f7e0f/AIM-Harvard/SlicerRadiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI...</a></h3>

  <p>A Slicer extension to provide a GUI around pyradiomics - GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @danceward (2018-07-09 15:26 UTC)

<p>Thank you for your help！I’ll have a try.</p>

---

## Post #4 by @lassoan (2018-07-09 19:15 UTC)

<p>I don’t fully understand the question, I would just note that Segment editor creates segmentations, which you can export to a labelmap volume node by a few clicks (in Segmentations module, Export/Import section; or in Data module, by right-clicking on the segmentation node and selecting labelmap export option).</p>

---
