---
topic_id: 38243
title: "Center Of Mass Calculation"
date: 2024-09-05
url: https://discourse.slicer.org/t/38243
---

# Center of mass calculation

**Topic ID**: 38243
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/center-of-mass-calculation/38243

---

## Post #1 by @francois (2024-09-05 17:38 UTC)

<p>How can we ignore part a volume in order to calculate a center of mass, based on HU. It seems that each tine it takes into account the “empty” voxels whatever value is applied: 0 or NaN.</p>

---

## Post #2 by @cpinter (2024-09-06 09:03 UTC)

<p>You need to segment your region of interest with Segment Editor, then from there it’s very easy to get the center of mass of the segment using Segment Statistics for example.</p>

---

## Post #3 by @lassoan (2024-09-06 10:48 UTC)

<p><a class="mention" href="/u/francois">@francois</a> You can ignore part of a volume that is outside a segment as <a class="mention" href="/u/cpinter">@cpinter</a> described. You can also get a point inside a segment nearest to its center using <a href="https://discourse.slicer.org/t/get-center-of-gravity-of-a-segment/4287/4">segmentationNode.GetSegmentCenterRAS</a> (this is useful if you want to jump to a slice where the segment is visible; the center of gravity may be outside the segment). If to7 want to compute the center of gravity yourself then you can do so using numpy (you can use <code>np.where</code> to ignore values that are outside the range you are interested in).</p>
<p>Note that 0 HU value corresponds to water (fat, soft tissue, …) so it might not be suitable as a threshold. HU value of air is -1000, you can use that as a thrshold for determining if a voxel is “empty”.</p>
<p>What would you like to use center of gravity for?</p>

---

## Post #4 by @francois (2024-09-06 11:16 UTC)

<p>Well I work on bone (foot bones) using WBCT dicoms. I want to transform both the dicom volume and the segment to a new reference frame where the COM is the origin.</p>

---

## Post #5 by @lassoan (2024-09-06 13:37 UTC)

<p>In this case, center of gravity computed based on HU might not what you need (you don’t want cortical bone to throw off computation of the bone axis), but you may want to use solidified segmentation of the bone.</p>
<p>Check out this extension - it may provide useful features for you:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/jmhuie/SlicerBiomech">
  <header class="source">

      <a href="https://github.com/jmhuie/SlicerBiomech" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/bf221d6cd383a80796914805af7534f1/jmhuie/SlicerBiomech" class="thumbnail">

  <h3><a href="https://github.com/jmhuie/SlicerBiomech" target="_blank" rel="noopener">GitHub - jmhuie/SlicerBiomech: Extension for the collection and analysis of...</a></h3>

    <p><span class="github-repo-description">Extension for the collection and analysis of biomechanical data from 3D specimen data</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can get fully automatic human feet bones segmentation from TotalSegmentator extension.</p>

---

## Post #6 by @ChristopherGray (2024-09-18 13:42 UTC)

<p>Thank you so much for the extension link.</p>

---
