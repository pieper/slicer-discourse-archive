---
topic_id: 25132
title: "Parenchyma Analysis"
date: 2022-09-07
url: https://discourse.slicer.org/t/25132
---

# Parenchyma analysis

**Topic ID**: 25132
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/parenchyma-analysis/25132

---

## Post #1 by @kalbim (2022-09-07 03:06 UTC)

<p>Hello, this is my first time trying this software and I don’t really understand programming and coding. I followed the tutorials but for some reason the software doesn’t create the lung density histogram.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61c7f4ceb10b89dc7fa106590b4408fe10cd4c4d.jpeg" data-download-href="/uploads/short-url/dX0IzMjwP1CEYQVg6dneZpILSkR.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61c7f4ceb10b89dc7fa106590b4408fe10cd4c4d_2_690x367.jpeg" alt="1" data-base62-sha1="dX0IzMjwP1CEYQVg6dneZpILSkR" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61c7f4ceb10b89dc7fa106590b4408fe10cd4c4d_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61c7f4ceb10b89dc7fa106590b4408fe10cd4c4d_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61c7f4ceb10b89dc7fa106590b4408fe10cd4c4d_2_1380x734.jpeg 2x" data-dominant-color="A6A6AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1022 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f1728c1c070bf8e59572fcf95545e184168f2c1.jpeg" data-download-href="/uploads/short-url/i8ifWmp4pRY8spAEw2luHIzgOcx.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f1728c1c070bf8e59572fcf95545e184168f2c1_2_690x370.jpeg" alt="2" data-base62-sha1="i8ifWmp4pRY8spAEw2luHIzgOcx" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f1728c1c070bf8e59572fcf95545e184168f2c1_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f1728c1c070bf8e59572fcf95545e184168f2c1_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f1728c1c070bf8e59572fcf95545e184168f2c1_2_1380x740.jpeg 2x" data-dominant-color="A7A6AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1032 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
As label map volume, whether I pick none or partial lung label map, it just creates another partial lung label map and the image viewers show only one slice.<br>
When I tried interactive lobe segmentation, the same thing happened.<br>
I appreciate any help. Thanks a lot.</p>

---

## Post #2 by @rbumm (2022-09-07 07:45 UTC)

<p>Hi,<br>
You seem to be using an outdated version of Slicer.<br>
Please install Slicer 5.0.3 stable and use Parenchyma Analysis like this:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14fb00f504b709626c2d32db48abc80a7d917d87.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14fb00f504b709626c2d32db48abc80a7d917d87.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14fb00f504b709626c2d32db48abc80a7d917d87.mp4</a>
    </source></video>
  </div><p></p>
<p>(Video 2 x speed, Slicer demo data)</p>

---

## Post #3 by @yopi.simargi (2022-10-25 01:54 UTC)

<p>Hi all, I am trying to use  Parenchyma Analysis (version Slicer 5.0.3) but the software just did not work (only creating label map). I did without segmentation. I appreciate any help. Thank you.</p>

---

## Post #4 by @rbumm (2022-10-25 06:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> could we find a solution for integrating the <a href="https://github.com/acil-bwh/SlicerCIP">SlicerCIP</a> develop branch into the CIP extension update mechanism?<br>
My last maintenance work on Parenchyma Analysis was done in this branch.</p>

---

## Post #5 by @lassoan (2022-10-25 12:30 UTC)

<p>Slicer Preview Release uses <a href="https://github.com/acil-bwh/SlicerCIP:">https://github.com/acil-bwh/SlicerCIP:</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/main/Chest_Imaging_Platform.s4ext">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/Chest_Imaging_Platform.s4ext" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/main/Chest_Imaging_Platform.s4ext" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/main/Chest_Imaging_Platform.s4ext</a></h4>


      <pre><code class="lang-s4ext">build_subdirectory inner-build
category Chest Imaging Platform
contributors Applied Chest Imaging Laboratory, Brigham and Women's Hospital
depends NA
description Chest Imaging Platform is an extension for quantitative CT imaging biomarkers for lung diseases. This work is funded by the National Heart, Lung, And Blood Institute of the National  Institutes of Health under Award Number R01HL116931. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.
enabled 1
homepage http://www.chestimagingplatform.org
iconurl https://raw.githubusercontent.com/acil-bwh/SlicerCIP/master/Resources/SlicerCIPLogo.png
scm git
scmrevision develop
scmurl https://github.com/acil-bwh/SlicerCIP
screenshoturls https://raw.githubusercontent.com/acil-bwh/SlicerCIP/master/Resources/Screenshot1.png https://raw.githubusercontent.com/acil-bwh/SlicerCIP/master/Resources/Screenshot2.png
status Alpha
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This causes CIP not being available for Slicer Preview Releases. So, I would not hurry switching to <a href="https://github.com/acil-bwh/SlicerCIP" class="inline-onebox">GitHub - acil-bwh/SlicerCIP: Slicer extension for the Chest Imaging Platform</a> just yet.</p>
<p>We still don’t have write access to <a href="https://github.com/acil-bwh/ChestImagingPlatform" class="inline-onebox">GitHub - acil-bwh/ChestImagingPlatform: Chest Imaging Platform (CIP)</a> and the <a href="https://github.com/acil-bwh/ChestImagingPlatform/pull/45">pull request that is required for Slicer to build CIP</a> is still not integrated, so I’m considering switching back to our fork.</p>

---
