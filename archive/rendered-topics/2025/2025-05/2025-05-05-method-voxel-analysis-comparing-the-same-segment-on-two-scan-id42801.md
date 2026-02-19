---
topic_id: 42801
title: "Method Voxel Analysis Comparing The Same Segment On Two Scan"
date: 2025-05-05
url: https://discourse.slicer.org/t/42801
---

# Method-Voxel Analysis comparing the same segment on two scans

**Topic ID**: 42801
**Date**: 2025-05-05
**URL**: https://discourse.slicer.org/t/method-voxel-analysis-comparing-the-same-segment-on-two-scans/42801

---

## Post #1 by @CSalt (2025-05-05 18:37 UTC)

<p>I am trying to perform voxel analysis for scans taken at different time periods to track tumor uptake at varying time points. I am using registered images. I was able to plot a voxel histogram like the one in this documentation:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I want to find out if anyone has guidance to plot a comparison of the voxels. I would like to do something very similar to figure one in the following paper:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pmc.ncbi.nlm.nih.gov/articles/PMC2804941/">
  <header class="source">
      <img src="https://pmc.ncbi.nlm.nih.gov/static/img/favicons/favicon-48x48.png" class="site-icon" width="48" height="48">

      <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2804941/" target="_blank" rel="noopener nofollow ugc">PubMed Central (PMC)</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/360;"><img src="https://cdn.ncbi.nlm.nih.gov/pmc/cms/images/pmc-card-share.jpg?_=0" class="thumbnail" width="690" height="360"></div>

<h3><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC2804941/" target="_blank" rel="noopener nofollow ugc">Voxel-by-Voxel Functional Diffusion Mapping for Early Evaluation of Breast...</a></h3>

  <p>Quantitative isotropic diffusion MRI and voxel-based analysis of the apparent diffusion coefficient (ADC) changes have been demonstrated to be able to accurately predict early response of brain tumors to therapy. The ADC value changes measured ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>but I am not certain how to go about it. Please let me know if you have any ideas.</p>
<p>Thanks in advance.</p>

---
