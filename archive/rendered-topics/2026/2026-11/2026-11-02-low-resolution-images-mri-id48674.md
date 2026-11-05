---
topic_id: 48674
title: "Low resolution images - MRI"
date: 2026-11-02
url: https://discourse.slicer.org/t/48674
last_bumped: 2026-11-05T08:25:12.545Z
---

# Low resolution images - MRI

**Topic ID**: 48674
**Date**: 2026-11-02
**URL**: https://discourse.slicer.org/t/low-resolution-images-mri/48674

---

## Post #1 by @phero1190 (2026-11-02 16:12 UTC)

<p>I am trying to create a good image of my brain from an MRI I just had but when I load in the DICOM data, some of the planes are low resolution. The data I have is broken down into different subsections; sagittal, axial, coronal, etc. and when I click on one of them, the main part of the image looks good but the other planes are low resolution. I feel like I need to combine the subsections in order to pull in the high resolution images for all the planes, but I have no idea how. Any tips are appreciated.</p>
<p><a href="https://imgur.com/a/ZtuSsH5" rel="noopener nofollow ugc">Low  resolution images for sagittal and coronal planes.</a></p>

---

## Post #2 by @pieper (2026-11-02 18:16 UTC)

<p>This is exactly the use case for SynthSR.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSR">
  <header class="source">

      <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSR" target="_blank" rel="noopener">surfer.nmr.mgh.harvard.edu</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSR" target="_blank" rel="noopener">SynthSR - Free Surfer Wiki</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @markcprosser (2026-11-05 08:25 UTC)

<p>I think I am experiencing a similar issue except with MRI scans of my knee.</p>
<p>vertical is as it should be, but the other 2 are low resolution and there are MORE slides than there should be - the resolution should be around 4mm, but it is more like 1mm for some strange reason!</p>
<p>Maybe some attempt at interpolation has gone on?</p>

---
