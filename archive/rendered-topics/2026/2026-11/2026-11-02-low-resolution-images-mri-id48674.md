---
topic_id: 48674
title: "Low resolution images - MRI"
date: 2026-11-02
url: https://discourse.slicer.org/t/48674
last_bumped: 2026-11-05T18:30:23.862Z
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

## Post #4 by @pieper (2026-11-05 16:01 UTC)

<p><em>[AI-assisted reply: drafted with Claude and checked by me]</em></p>
<p>This is a common issue with clinical MRI, and the explanation in this thread applies to knees too:</p><aside class="quote" data-post="1" data-topic="1799">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/97f17d/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/1799">Problem loading MRI scan. Only one view, axial, is clear, the other two are blurry</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square "><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version: 4.8.0 
Expected behavior: All three views are clear 
Actual behavior: Only axial is clear and the other views are a bit titled and blurry. Unable to get a good 3d model out of this data. I’ve attached images for reference.
  </blockquote>
</aside>

<p>In short, each series is high-resolution only in the plane it was acquired in, typically 0.3–0.5 mm pixels with 3–4 mm slices. The other two views are reconstructed across those thick slices, so they look blurry. They also seem to have “more slices” because the slider steps through the fine in-plane spacing, not through new data. To see each plane sharply, show the series acquired in that plane in the matching view. Combining the separate series into one high-resolution volume is a hard problem with no standard solution. See <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing? - #2 by lassoan</a>.</p>

---

## Post #5 by @markcprosser (2026-11-05 18:15 UTC)

<p>Thanks Steve!</p>
<p>Do you think SynthSR that you mention above only works for brain scans or would it work for MRIs of knees/abdomens too?</p>

---

## Post #6 by @pieper (2026-11-05 18:30 UTC)

<p>No, at this point I don’t think there’s any knee-specific superresolution.  SynthSR only works on brains.</p>

---
