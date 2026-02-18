# Questions about CT Scan Analysis for Muscle and Fat Evaluation Using 3D Slicer

**Topic ID**: 37906
**Date**: 2024-08-15
**URL**: https://discourse.slicer.org/t/questions-about-ct-scan-analysis-for-muscle-and-fat-evaluation-using-3d-slicer/37906

---

## Post #1 by @marcelovoltani (2024-08-15 14:59 UTC)

<p>Hello, I am starting CT scan analyses to evaluate muscle and fat in different slices. I have some questions regarding the data extracted from 3D Slicer and would like some help.</p>
<ol>
<li>When a new segment is added to be analyzed, is the quantification of that segment combined with the previous segment, or does the software separate the analyses?</li>
<li>When quantifying a defined segment, the table shows a volume value (cm³). What formula does the software use to calculate this volume? Is it based on just a single slice?</li>
<li>Using the “Sandbox” extension, it is possible to analyze the cross-sectional area of the segment, but 3D Slicer itself quantifies the segment’s surface area. What is the difference between surface area and cross-sectional area?</li>
<li>Regarding the analysis of myosteatosis, are there any recommendations for performing this analysis without considering the muscle fascia or other structures that might interfere? Do you recommend any specific method for assessing muscle fat?</li>
</ol>

---

## Post #2 by @lassoan (2024-08-15 15:11 UTC)

<p>Traditional body composition evaluation used manual tools, so most metrics are based on manually segmenting a few slices. If you want to reproduce these established metrics then you can do the same - manually segment slices and work with cross-sectional areas (computed by Cross-sectional area module).</p>
<p>If you are ready to challenge the established methods and work with more accurate 3D metrics then you can segment entire body regions and work with segment volumes (computed by Segment Statistics module).</p>
<aside class="quote no-group" data-username="marcelovoltani" data-post="1" data-topic="37906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> marcelovoltani:</div>
<blockquote>
<p>When a new segment is added to be analyzed, is the quantification of that segment combined with the previous segment, or does the software separate the analyses?</p>
</blockquote>
</aside>
<p>Segment Statistics module computes metrics for each segment independently.</p>
<aside class="quote no-group" data-username="marcelovoltani" data-post="1" data-topic="37906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> marcelovoltani:</div>
<blockquote>
<p>When quantifying a defined segment, the table shows a volume value (cm³). What formula does the software use to calculate this volume? Is it based on just a single slice?</p>
</blockquote>
</aside>
<p>Number of voxels multiplied by volume of one voxel.</p>
<aside class="quote no-group" data-username="marcelovoltani" data-post="1" data-topic="37906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> marcelovoltani:</div>
<blockquote>
<p>Using the “Sandbox” extension, it is possible to analyze the cross-sectional area of the segment, but 3D Slicer itself quantifies the segment’s surface area. What is the difference between surface area and cross-sectional area?</p>
</blockquote>
</aside>
<p>“Surface area” is the surface area of the segment you see in the 3D view. For a single slice it is approximately 2x larger than the area of the cross-section, because the segment is flat and its two sides each has approximately the same area as the cross-sectional area.</p>
<aside class="quote no-group" data-username="marcelovoltani" data-post="1" data-topic="37906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e0b2c6/48.png" class="avatar"> marcelovoltani:</div>
<blockquote>
<p>Regarding the analysis of myosteatosis, are there any recommendations for performing this analysis without considering the muscle fascia or other structures that might interfere? Do you recommend any specific method for assessing muscle fat?</p>
</blockquote>
</aside>
<p>You can segment the structures that might interfere with your analysis and do not include them in your measurements.</p>

---
