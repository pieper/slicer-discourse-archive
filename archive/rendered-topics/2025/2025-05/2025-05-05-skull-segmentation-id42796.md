---
topic_id: 42796
title: "Skull Segmentation"
date: 2025-05-05
url: https://discourse.slicer.org/t/42796
---

# Skull Segmentation

**Topic ID**: 42796
**Date**: 2025-05-05
**URL**: https://discourse.slicer.org/t/skull-segmentation/42796

---

## Post #1 by @palomar (2025-05-05 10:49 UTC)

<p>Hi,<br>
I am currently working on a project that involves a whole body PET/CT scan of a healthy patient. The goal is to segment the skull, simulate a localized defect, and create a customized prosthetic patch that fits the curvature of the skull.</p>
<p>So far I have implemented workflows using both manual and automatic segmentation with TotalSegmentator. Unfortunately, the results of TotalSegmentator have not been satisfactory, probably due to the limitations of my computer in processing AI calculations.</p>
<p>I am considering combining different segmentation approaches, but I am not yet sure which one is the most effective solution.</p>
<p>Could you please give me some advice on the most suitable segmentation methods or workflows?<br>
Thanks in advance for any advice you can give me.</p>
<p>Kind regards</p>

---

## Post #2 by @MarkusHeller (2025-05-05 19:53 UTC)

<p>Have a look at the DentalSegmentator - the underlying model has a much higher resolution than TotalSegmentator, and likely more targeted at what you want here; may help, especially if you have a higher resolution CT scan.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/1f0d2cf02701ee5fa182d442494abf94/gaudot/SlicerDentalSegmentator" class="thumbnail">

  <h3><a href="https://github.com/gaudot/SlicerDentalSegmentator" target="_blank" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Best wishes,</p>

---

## Post #3 by @PitaChib (2025-05-07 03:12 UTC)

<p>I work with microCT scans, and I follow <a href="https://slicermorph.github.io/Endocast_creation.html" rel="noopener nofollow ugc">this</a> tutorial (you only need to follow the 1st step) to get my cranium segmentations. Is manually thresholding but it does the job really fast for me. Maybe worth a try?</p>

---
