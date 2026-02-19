---
topic_id: 42561
title: "Ct Perfusion Coregistration To Atlas"
date: 2025-04-14
url: https://discourse.slicer.org/t/42561
---

# CT perfusion coregistration to atlas

**Topic ID**: 42561
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/ct-perfusion-coregistration-to-atlas/42561

---

## Post #1 by @GioM (2025-04-14 16:51 UTC)

<p>Hi all,<br>
starting from the CT perfusion DICOM files I obtained the nifti penumbra VOI.<br>
Now I want to check which anatomical areas are affected based on the AAL atlas. I am stuck in the coregistration phase. How can I adapt a VOI extracted from a CT to an atlas?</p>
<p>Thanks for the advice, I am new to neuroimaging analysis, so any suggestions are welcome.</p>

---

## Post #2 by @pieper (2025-04-14 17:09 UTC)

<p>You should be able to use any of the registration techniques to get a reasonable alignment.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" target="_blank" rel="noopener">Registration — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You may also want to see if SynthSeg can segment your CT directly.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/BBillot/SynthSeg">
  <header class="source">

      <a href="https://github.com/BBillot/SynthSeg" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/b5e944ac40281562a949c2140576201d/BBillot/SynthSeg" class="thumbnail">

  <h3><a href="https://github.com/BBillot/SynthSeg" target="_blank" rel="noopener">GitHub - BBillot/SynthSeg: Contrast-agnostic segmentation of MRI scans</a></h3>

    <p><span class="github-repo-description">Contrast-agnostic segmentation of MRI scans</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @GioM (2025-05-25 08:40 UTC)

<p>Thanks. I first applied manual transformation to align the perfusion map to NCCT brain, then I used the same transformation for the segmented VOI (to align VOI to subject brain). And at last I run an affine registration of subject brain to a CT template and applied the same affine registration to the VOI (this last steps with antspyx script or with DSI Studio integrated tools). It works fine for my goal</p>

---
