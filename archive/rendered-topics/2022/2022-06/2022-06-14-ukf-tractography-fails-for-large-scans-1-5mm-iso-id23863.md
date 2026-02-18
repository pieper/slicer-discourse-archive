# UKF tractography fails for large scans (~1.5mm iso)

**Topic ID**: 23863
**Date**: 2022-06-14
**URL**: https://discourse.slicer.org/t/ukf-tractography-fails-for-large-scans-1-5mm-iso/23863

---

## Post #1 by @phoebeimms (2022-06-14 00:41 UTC)

<p>Hi!</p>
<p>We are running whole brain 2-tensor UKF tractography, using 5 seeds ver voxel and otherwise default parameters, on a large range of scans (from various online repositories, e.g., HCP, UKBB, etc). Depending on the acquisition parameters, some of the scans are ‘larger’ than others - i.e., smaller voxel sizes thus more seed points. For these subjects, UKF tractography runs but finishes without creating a .vtk file (see output below). We are able to run these subjects with 3 seeds per voxel, and by reducing the output step length from 0.9 to 1.5, however it isn’t ideal to change the tractography parameters between subjects and we would prefer to stay with our original settings.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da24975a1d82a25eeb2b679a13d7855183ae74be.png" alt="image" data-base62-sha1="v7Mu3T6oXw36nTMrU1Pve6KaLWC" width="583" height="332"></p>
<p>Right now we are allocating at least 17 cores and about 30GB ram, and we have plenty of hard drive storage. The output sizes of our ‘regular’ sized subjects are ~600MB (5 seeds per voxel), and our ‘large’ subjects are ~1.5GB (3 seeds per voxel).</p>
<p>Given the available ram and storage, we are not sure why Slicer is unable to create the .vtk file, but based on our experiments it seems to have something to do with the size of the file, i.e., if the file is smaller it runs, if it’s larger it fails. Is there a way run these subjects without changing our tractography parameters?</p>

---

## Post #2 by @pieper (2022-06-14 15:46 UTC)

<p>It looks like you are just running out of memory on these higher resolution scans.  The most straightforward thing would be to just add more virtual memory (two or three times the physical RAM could be good).</p>
<p>It looks like you are using a linux based VM so maybe these instructions will help:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/QIICR/SlicerGCPSetup#swap-space">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/QIICR/SlicerGCPSetup#swap-space" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/c17ad5f550a8562424f6e2e478eca3b67898d53b330daa4280c6a36a40ae0bcf/QIICR/SlicerGCPSetup" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/QIICR/SlicerGCPSetup#swap-space" target="_blank" rel="noopener">GitHub - QIICR/SlicerGCPSetup</a></h3>

  <p>Contribute to QIICR/SlicerGCPSetup development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
