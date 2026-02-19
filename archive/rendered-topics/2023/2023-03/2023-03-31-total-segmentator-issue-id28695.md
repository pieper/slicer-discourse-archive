---
topic_id: 28695
title: "Total Segmentator Issue"
date: 2023-03-31
url: https://discourse.slicer.org/t/28695
---

# Total segmentator issue

**Topic ID**: 28695
**Date**: 2023-03-31
**URL**: https://discourse.slicer.org/t/total-segmentator-issue/28695

---

## Post #1 by @KSL (2023-03-31 12:22 UTC)

<p>Hello dear Slicer users,<br>
I am posting this query in continuation with my previous post relating to the Total Segmentator module. I am currently using Slicer 5.2.1. I am able to install Pytorch, but the total Segmentator is not working. My computer runs on Intel Iris Xe graphics. I am attaching images for your reference. Need your guidance… Thanks in advance<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa0a3b76b3c320486b80a18094b279766c9976df.png" alt="Graphics" data-base62-sha1="zFXhZpT66YPv9gQjalyGN2Z59W7" width="312" height="64"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65b4e5858f22ff54834cd9923501debc7a808dc.jpeg" data-download-href="/uploads/short-url/z9n4Xyv3dNdSisFSW0wZDJkSI44.jpeg?dl=1" title="TotSeg 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65b4e5858f22ff54834cd9923501debc7a808dc.jpeg" alt="TotSeg 1" data-base62-sha1="z9n4Xyv3dNdSisFSW0wZDJkSI44" width="690" height="433" data-dominant-color="ADACB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TotSeg 1</span><span class="informations">1920×1207 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfcb613039b28b978b52d402b45fd4309a0df81.jpeg" data-download-href="/uploads/short-url/zXbh8rGcEKeEtTV8RVfZSI9CS3f.jpeg?dl=1" title="TotSeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfcb613039b28b978b52d402b45fd4309a0df81.jpeg" alt="TotSeg" data-base62-sha1="zXbh8rGcEKeEtTV8RVfZSI9CS3f" width="690" height="435" data-dominant-color="9E9EA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TotSeg</span><span class="informations">1920×1211 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bac60597f10cc7bf14c14574ab98bd066d94cfa.jpeg" data-download-href="/uploads/short-url/6elQrB7o3t70fxZoF1cuiILK3XA.jpeg?dl=1" title="Pytorch" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bac60597f10cc7bf14c14574ab98bd066d94cfa.jpeg" alt="Pytorch" data-base62-sha1="6elQrB7o3t70fxZoF1cuiILK3XA" width="690" height="435" data-dominant-color="A0A0A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pytorch</span><span class="informations">1920×1212 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2023-03-31 12:54 UTC)

<p>This is probably because your system does not support CUDA so TotalSegmentator fails to run in GPU mode. Please go to the PyTorch extension, uninstall Pytorch, restart 3D Slicer, select the computation backend “cpu” and install PyTorch again. Or consider upgrading your GPU.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/264647517c85e8a12f66e6c8e24fd0400740d913.png" alt="image" data-base62-sha1="5sAIkFLo95mHCrrdrpSAi4QaeNd" width="397" height="416"></p>

---

## Post #3 by @jamesobutler (2023-03-31 13:12 UTC)

<p>That error message appears to happen after it tries to install the TotalSegmentor python package.</p>
<p>Please take a look at the following troubleshooting guidance:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator#failed-to-compute-results-error-at-the-first-run">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator#failed-to-compute-results-error-at-the-first-run" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/b995bee5dbe70a2d6743254103765300a54d857081c2bfdb0edb1f9643c488dc/lassoan/SlicerTotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerTotalSegmentator#failed-to-compute-results-error-at-the-first-run" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body...</a></h3>

  <p>Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model - GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer usin...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would also suggest the you update to Slicer 5.2.2 (<a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>) to be able to install the latest version of the Slicer TotalSegmentor extension.</p>

---

## Post #4 by @KSL (2023-04-01 09:21 UTC)

<p>Thank you, everyone, for helping me out. Now,  I can run TotalSegmentator.</p>

---

## Post #5 by @rbumm (2023-04-03 00:02 UTC)

<p><a class="mention" href="/u/ksl">@KSL</a> Could you share with the community what solved the problem on your side? Are you now running Totalsegmentator in CPU mode? Thank you.</p>

---

## Post #6 by @KSL (2023-04-03 09:20 UTC)

<p>Sir, I am running the Total Segmentator module in CPU mode. The issue I encountered previously was because of Incompatibility (I suppose) of the module with Slicer 5.2.1. After installing the new version 5.2.2 and following the instructions, the Total Segmentator works.</p>

---
