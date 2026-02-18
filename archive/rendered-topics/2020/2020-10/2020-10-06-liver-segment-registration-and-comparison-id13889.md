# Liver segment registration and comparison

**Topic ID**: 13889
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/liver-segment-registration-and-comparison/13889

---

## Post #1 by @yann (2020-10-06 13:22 UTC)

<p>Hello,<br>
How to register two liver segmentation masks before to compare them?<br>
In practis, I have liver segmentations masks from two different CT and I want to register this segmentations before to compare them (DICE comparisons and Hausdorff distances) with slicer RT.<br>
I found how to register two exams but not two segmentation masks.<br>
Can some one help me?</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-10-07 11:47 UTC)

<p>Hello <a class="mention" href="/u/yann">@yann</a></p>
<aside class="quote no-group" data-username="yann" data-post="1" data-topic="13889" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bc79bd/48.png" class="avatar"> yann:</div>
<blockquote>
<p>Hello,<br>
How to register two liver segmentation masks before to compare them?<br>
In practis, I have liver segmentations masks from two different CT and I want to register this segmentations before to compare them (DICE comparisons and Hausdorff distances) with slicer RT.<br>
I found how to register two exams but not two segmentation masks.<br>
Can some one help me?</p>
</blockquote>
</aside>
<p>There are a couple tools available to do this.</p>
<ol>
<li>Segment Registration module</li>
</ol>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SegmentRegistration" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d59aea3b2e136dd0ea7910870d2d99a1c2387b6f629ff2952c0be55b41b16d5a/SlicerRt/SegmentRegistration" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/SegmentRegistration" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment...</a></h3>

  <p>3D Slicer extension for segment registration (aka fusion, contour propagation) - GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment registration (aka fusion, contour propagation)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
(you have to install SlicerRT extension module )</p>
<ol start="2">
<li>Surface registration module</li>
</ol>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceRegistration" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceRegistration</a></p>
<p>( You will have to install CMFreg extension module for this)</p>
<p>-Andinet</p>

---
