---
topic_id: 25226
title: "Lung Ct Segmenter Supports Totalsegmentator Nnu Net Deep Lea"
date: 2022-09-12
url: https://discourse.slicer.org/t/25226
---

# Lung CT Segmenter supports TotalSegmentator nnU-Net deep learning

**Topic ID**: 25226
**Date**: 2022-09-12
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter-supports-totalsegmentator-nnu-net-deep-learning/25226

---

## Post #1 by @rbumm (2022-09-12 20:10 UTC)

<p>A new engine has been added to “experimental AI” in the Lung CT Segmenter module of the Lung CT Analyzer extension: <a href="https://github.com/wasserth/totalsegmentator">TotalSegmentator</a> by Jakob Wasserthal (University of Basel and colleagues from DKFZ). Please cite the authors.<br>
TotalSegmentator involves nnU-Net deep learning and automatically segments 104 organ classes from which we pick lung lobes, trachea, pulmonary artery, and left atrium of the heart for lung segmentation. All created organ classes are converted into a single 3D Slicer segmentation with the correct naming.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bc02d2268b075bfc4a08f03cc8a6fb4067480ad.jpeg" data-download-href="/uploads/short-url/hEKsOjD2WY6vgrMNtsvk0omtkst.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc02d2268b075bfc4a08f03cc8a6fb4067480ad_2_690x308.jpeg" alt="image" data-base62-sha1="hEKsOjD2WY6vgrMNtsvk0omtkst" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc02d2268b075bfc4a08f03cc8a6fb4067480ad_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc02d2268b075bfc4a08f03cc8a6fb4067480ad_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc02d2268b075bfc4a08f03cc8a6fb4067480ad_2_1380x616.jpeg 2x" data-dominant-color="9C9A9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×859 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The new updated version of the extension (2.53)  should be available tomorrow via the extension manager.</p>
<p>For installation details (Windows is a bit tricky) see this wiki page:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/96d82c57408aab878a903e8b922095d383150d1769adc14ae3ef049de332fce8/rbumm/SlicerLungCTAnalyzer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/" target="_blank" rel="noopener">Home</a></h3>

  <p>This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.  - rbumm/SlicerLungCTAnalyzer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @dave3d (2022-09-12 22:06 UTC)

<p>Looks really cool.  The TotalSegmentator repo says you need an Nvidia GPU to use it.  Is that true for the Slicer extension also?</p>

---

## Post #3 by @rbumm (2022-09-13 07:36 UTC)

<p>Hi Dave, 3D Slicer and this extension will run on all major operating systems with a wide range of GPU.<br>
See the hardware requirements <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">here</a>.</p>

---

## Post #4 by @dave3d (2022-09-13 13:53 UTC)

<p>Great!</p>
<p>Yeah, I use Slicer on my MacBook Pro with an AMD gpu all the time. I tried out the Lung CT Segmenter, and it produced a very nice result on the one data set I used.  I just wanted to be sure about TotalSegmentator, before I try it.</p>

---
