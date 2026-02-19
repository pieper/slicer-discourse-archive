---
topic_id: 17029
title: "3Dslicer Difussion Tractogoraphy"
date: 2021-04-11
url: https://discourse.slicer.org/t/17029
---

# 3Dslicer Difussion Tractogoraphy

**Topic ID**: 17029
**Date**: 2021-04-11
**URL**: https://discourse.slicer.org/t/3dslicer-difussion-tractogoraphy/17029

---

## Post #1 by @xinnosige (2021-04-11 14:13 UTC)

<p>At present, I have a batch of DSI data, and the scanning data of each subject is divided into AP and PA directions. I have fitted the data of each subject in two directions through FSL, and finally obtained the files of NII, Bvec, Bval and Mask. Now I want to use 3D Slicer to track the fiber at the population level, is it feasible?Because I read in the relevant forum that the fiber bundle reconstruction of 3D Slicer must be required to be native DICOM data, the semi-finished product is not feasible.Therefore, I would like to ask you whether this situation of mine cannot be processed by 3D Slicer software in the future.</p>

---

## Post #2 by @pieper (2021-04-11 14:35 UTC)

<p>These scripts should handle converting nii dmri to nrrd.  Then you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/UKFTractography">ukf tractography</a> and the <a href="http://dmri.slicer.org/">SlicerDMRI</a> tools.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/3407942?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">pnlbwh/conversion</a></h3>


  <p><span class="label1">Various mri conversion/modification scripts. Contribute to pnlbwh/conversion development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @xinnosige (2021-04-16 06:43 UTC)

<ul>
<li>Thank you for your answers</li>
</ul>

---
