# DWI radiomic features looking awkward?

**Topic ID**: 41782
**Date**: 2025-02-19
**URL**: https://discourse.slicer.org/t/dwi-radiomic-features-looking-awkward/41782

---

## Post #1 by @Fazilhan_Altintas (2025-02-19 21:21 UTC)

<p>Hello Dear 3d Slicer Community,</p>
<p>I was segmenting a lesion on mulitple mri sequances to extract radiomic features. After I did I realized something very weird. For example I drew a mask on DWI and then slapped it onto adc. When I extracted radiomic features from both, meshvolume, which should be similar for both, was extremely different. This never happens with t2 t1 adc or contrast segmentations just with DWI. And this problem is prevelant across all other DWI segmentations and radiomic extractions I have produced (not just for meshvolume, though it was what made me suspect in the first place). Is there a secret sauce to using radiomics module on diffusion weighted imaging? What am I doing wrong. I greatly appreciate any help</p>

---

## Post #2 by @pieper (2025-02-19 22:12 UTC)

<p>This sounds like something you should try to work out at the pyradiomics level since SlicerRadiomics is just a wrapper.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/pyradiomics/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/4c75f14b5d3e74aa35367a27ae77808883d40d96b5e506cba3cc368d74534c4a/AIM-Harvard/pyradiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/pyradiomics/issues" target="_blank" rel="noopener">AIM-Harvard/pyradiomics</a></h3>

  <p>Open-source python package for the extraction of Radiomics features from 2D and 3D images and binary masks. Support: https://discourse.slicer.org/c/community/radiomics - AIM-Harvard/pyradiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
