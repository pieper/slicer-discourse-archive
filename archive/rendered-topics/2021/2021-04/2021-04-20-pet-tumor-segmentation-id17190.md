---
topic_id: 17190
title: "Pet Tumor Segmentation"
date: 2021-04-20
url: https://discourse.slicer.org/t/17190
---

# Pet Tumor Segmentation

**Topic ID**: 17190
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/pet-tumor-segmentation/17190

---

## Post #1 by @akmal871026 (2021-04-20 00:50 UTC)

<p>Hi Everyone,</p>
<p>Does anyone know what is the method that used in PET Tumor Segmentation tool? is it gradientwieght method? or otsu method? or adaptive method? or Fourier Surface method?</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-04-20 10:59 UTC)

<p>Hi <a class="mention" href="/u/akmal871026">@akmal871026</a></p>
<p>If you are asking about the the following extension</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PETTumorSegmentation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PETTumorSegmentation</a></p>
<p>Here is a paper that explains the algorithm</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.ncbi.nlm.nih.gov/favicon.ico" class="site-icon" width="15" height="15">
      <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4874930/" target="_blank" rel="noopener nofollow ugc">PubMed Central (PMC)</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:130/68;"><img src="https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/pmc-logo-share.png" class="thumbnail" width="130" height="68"></div>

<h3><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4874930/" target="_blank" rel="noopener nofollow ugc">Semiautomated segmentation of head and neck cancers in 18F-FDG PET scans: A...</a></h3>

<p>The purpose of this work was to develop, validate, and compare a highly computer-aided method for the segmentation of hot lesions in head and neck 18F-FDG PET scans.A semiautomated segmentation method was developed, which transforms the segmentation...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and here is the code repository</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="15" height="15">
      <a href="https://github.com/QIICR/PETTumorSegmentation" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/c30dc44e370350d70bdd735cd1682b821cfb56bb45675f2794c9835cd9deb880/QIICR/PETTumorSegmentation" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/QIICR/PETTumorSegmentation" target="_blank" rel="noopener nofollow ugc">QIICR/PETTumorSegmentation</a></h3>


  <p><span class="label1">3D Slicer Extension for PETTumorSegmentation. Contribute to QIICR/PETTumorSegmentation development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>-Andinet</p>

---
