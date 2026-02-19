---
topic_id: 45916
title: "Issue With Surface Area Measurement In L3 Skeletal Muscle Se"
date: 2026-01-26
url: https://discourse.slicer.org/t/45916
---

# Issue with surface area measurement in L3 skeletal muscle segmentation

**Topic ID**: 45916
**Date**: 2026-01-26
**URL**: https://discourse.slicer.org/t/issue-with-surface-area-measurement-in-l3-skeletal-muscle-segmentation/45916

---

## Post #1 by @NutritionDepartment (2026-01-26 10:34 UTC)

<p>Dear 3D Slicer Development Team,</p>
<p>I am using 3D Slicer to segment skeletal muscle on a single axial CT slice at the L3 level for body composition research.</p>
<p>After segmentation, the Segment Statistics module reports a reasonable volume (~10720,7 mm³) but an unexpectedly large surface area (~20610,5 mm²), which does not reflect the true cross-sectional muscle area and seems physiologically unrealistic.<br>
My research goal is to measure cross-sectional muscle area at L3 (cm²) to calculate SMI and assess muscle change over time.</p>
<p>Could you please clarify:</p>
<ol>
<li>
<p>What the “surface area” value represents in this context.</p>
</li>
<li>
<p>Whether this metric is appropriate for L3 cross-sectional muscle analysis.</p>
</li>
<li>
<p>The recommended workflow in 3D Slicer to obtain accurate muscle cross-sectional area from a single CT slice (e.g., area = volume ÷ slice thickness, or another method).</p>
</li>
</ol>
<p>I have attached an example image and statistics output for reference.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a147c47fa311f56212b74575e325c80b8265ea1a.jpeg" alt="z7465522995229_b00e115904a32426832560f1f7f6b185" data-base62-sha1="n0KDjjDwT29MLxvsutULY58wtpU" width="460" height="66"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256fef98ec7e48280cd1921ac74fc8f97f0f738e.jpeg" data-download-href="/uploads/short-url/5lbufXUPwpeD7BKkXnzQzGE9Qt0.jpeg?dl=1" title="z7465519967685_cd8eae851a970155a900277ef024e32c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/256fef98ec7e48280cd1921ac74fc8f97f0f738e_2_654x499.jpeg" alt="z7465519967685_cd8eae851a970155a900277ef024e32c" data-base62-sha1="5lbufXUPwpeD7BKkXnzQzGE9Qt0" width="654" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/256fef98ec7e48280cd1921ac74fc8f97f0f738e_2_654x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256fef98ec7e48280cd1921ac74fc8f97f0f738e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256fef98ec7e48280cd1921ac74fc8f97f0f738e.jpeg 2x" data-dominant-color="1F1B1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">z7465519967685_cd8eae851a970155a900277ef024e32c</span><span class="informations">911×696 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your support.</p>

---

## Post #2 by @muratmaga (2026-01-26 18:29 UTC)

<aside class="quote no-group" data-username="NutritionDepartment" data-post="1" data-topic="45916">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/nutritiondepartment/48/81822_2.png" class="avatar"> NutritionDepartment:</div>
<blockquote>
<p>Could you please clarify:</p>
</blockquote>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#computed-metrics">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#computed-metrics" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#computed-metrics" target="_blank" rel="noopener nofollow ugc">Computed metrics - Segment statistics — 3D Slicer  documentation</a></h3>

  <p>This is a module for the calculation of statistics related to the structure of segmentations, such as volume, surface area, mean intensity, and various other metrics for each segment.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2026-01-26 18:31 UTC)

<p>There are two different representations (labelmap and surface area) that gives SA estimate. Which one did you use?</p>

---
