---
topic_id: 9221
title: "New Feature Histogram For Setting Threshold Range In Segment"
date: 2019-11-19
url: https://discourse.slicer.org/t/9221
---

# New feature: Histogram for setting threshold range in Segment Editor

**Topic ID**: 9221
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/new-feature-histogram-for-setting-threshold-range-in-segment-editor/9221

---

## Post #1 by @Sunderlandkyl (2019-11-19 19:08 UTC)

<p>In the latest 3D Slicer 4.11.0 releases, the Threshold effect in the Segment Editor module now includes the option to specify the minimum and maximum thresholds based on the histogram of a region of interest in the slice view.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="pGVbhmsyXhY" data-video-title="Segment Editor: Local histogram in threshold effect" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=pGVbhmsyXhY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/pGVbhmsyXhY/maxresdefault.jpg" title="Segment Editor: Local histogram in threshold effect" width="" height="">
  </a>
</div>

<p>Clicking and dragging on a slice view will create a yellow border that encompasses the region of interest. Several different shapes can be used to draw the region of interest including: box, circle, freeform draw, or line.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa5d1ceba6ad42340528403296f9d0a1f63ae83.png" alt="localThreshold" data-base62-sha1="tCW6owiEczpNtjOOMosx4qzre2T" width="373" height="326"></p>
<p>The local histogram for this region will be automatically calculated and displayed within the segment editor panel.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1f53cda194f1f4822ca5222f4ee92c6a98d2a03.png" alt="histogram" data-base62-sha1="pohVLagVmuJ59itWmQmydS4frX5" width="599" height="182"></p>
<p>Clicking and dragging on the histogram will manually change the values used in the automatic calculation of the upper and lower threshold values. Right clicking on the histogram will revert back to automatic calculation from the histogram.</p>
<p>Suggestions and feedback are welcome.</p>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748</p>

---

## Post #2 by @muratmaga (2019-11-19 19:21 UTC)

<p>This looks awesome. Thank you!</p>

---
