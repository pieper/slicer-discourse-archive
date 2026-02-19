---
topic_id: 11318
title: "Covariate Significance Testing Help"
date: 2020-04-27
url: https://discourse.slicer.org/t/11318
---

# Covariate Significance Testing HELP

**Topic ID**: 11318
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/covariate-significance-testing-help/11318

---

## Post #1 by @Lyndon_Pardo (2020-04-27 16:04 UTC)

<p>I am new to slicer SALT and I was trying to run this feature using sample data from <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5d5c1f1f85f25b11ff3e276a" class="inline-onebox" rel="noopener nofollow ugc">Kitware Data</a></p>
<p>What do I input in shape for p-values? I’m using version 2.3.0-2020-04-06.<br>
Also, when I try to select any random VTK file from the sample data, the only output I get is a CSV file, without any VTK files included.</p>
<p>I am familiarizing myself first with the sample data before I use them on my actual data.<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/137b40c7f035cc701fa474060fe6deb6f0e2f4c9.png" data-download-href="/uploads/short-url/2Ml8HCY8j8pgUlUnXmSmVo4fiLn.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/137b40c7f035cc701fa474060fe6deb6f0e2f4c9.png" alt="Capture" data-base62-sha1="2Ml8HCY8j8pgUlUnXmSmVo4fiLn" width="690" height="450" data-dominant-color="D9E3EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">743×485 9.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @bpaniagua (2020-04-28 20:20 UTC)

<p>Hi <a class="mention" href="/u/lyndon_pardo">@Lyndon_Pardo</a></p>
<p>Does your csv file include the absolute paths to the input data? Any input data with inherent correspondence should work to include your p-values.</p>
<p>Thanks,<br>
Bea</p>

---

## Post #3 by @Lyndon_Pardo (2020-05-02 15:04 UTC)

<p>Hi! I already figured it out. Just a question, what is the protocol/framework of covariate significance testing? For documentation in my paper. Thanks!</p>

---

## Post #4 by @styner (2020-05-02 15:59 UTC)

<p>A few references for the testing framework:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://www.ncbi.nlm.nih.gov/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6494085/" target="_blank" rel="nofollow noopener">PubMed Central (PMC)</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:113/59;"><img src="https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/pmc-logo-share.png" class="thumbnail" width="113" height="59"></div>

<h3><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6494085/" target="_blank" rel="nofollow noopener">A web-based system for statistical shape analysis in temporomandibular joint...</a></h3>

<p>This study presents a web-system repository: Data Storage for Computation and Integration (DSCI) for Osteoarthritis of the temporomandibular joint (TMJ OA). This environment aims to maintain and allow contributions to the database from multi-clinical...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/DCBIA-OrthoLab/MFSDA" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/11340280?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/DCBIA-OrthoLab/MFSDA" target="_blank" rel="nofollow noopener">DCBIA-OrthoLab/MFSDA</a></h3>

<p>Multivariate Functional Shape Data Analysis (MFSDA) is a Matlab based package for statistical shape analysis. A multivariate varying coefficient model is introduced to build the association between...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
