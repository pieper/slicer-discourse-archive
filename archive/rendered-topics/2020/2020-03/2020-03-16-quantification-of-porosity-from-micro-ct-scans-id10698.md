# Quantification of Porosity from micro CT scans

**Topic ID**: 10698
**Date**: 2020-03-16
**URL**: https://discourse.slicer.org/t/quantification-of-porosity-from-micro-ct-scans/10698

---

## Post #1 by @gretaa (2020-03-16 11:07 UTC)

<p>Operating system: Mac OS Catalina<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi guys,</p>
<p>I have a bmp dataset of micro CT scans (1.3 mm diameter, 600 nm = 1 pixel resolution).<br>
I would like to quantify porosity (pore size, pore distribution, pore density).<br>
Would it be possible to do with 3D Slicer? If yes, could anybody tell me how?</p>
<p>Many thanks,</p>
<p>Greta</p>

---

## Post #2 by @pieper (2020-03-16 17:02 UTC)

<p>You can probably get some good results with the texture metrics in SlicerRadiomics.  If you really need to count each hole it would be harder.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/Radiomics/SlicerRadiomics" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/13385545?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/Radiomics/SlicerRadiomics" target="_blank">Radiomics/SlicerRadiomics</a></h3>

<p>A Slicer extension to provide a GUI around pyradiomics - Radiomics/SlicerRadiomics</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Varsha (2020-11-05 16:00 UTC)

<p>Could you provide more details on how to go about using Radiomics to visualise features like microporosity, macroporosity and texture on the surface of bone from 3D CT scans using Slicer? My study is aimed at just visualizing the same and not quantifying any of it.</p>

---

## Post #4 by @pieper (2020-11-05 16:55 UTC)

<p>Probably the best is to refer to the material here: <a href="https://www.radiomics.io/">https://www.radiomics.io/</a></p>

---
