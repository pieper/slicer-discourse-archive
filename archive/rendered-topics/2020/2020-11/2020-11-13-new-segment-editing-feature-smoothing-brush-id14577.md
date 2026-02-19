---
topic_id: 14577
title: "New Segment Editing Feature Smoothing Brush"
date: 2020-11-13
url: https://discourse.slicer.org/t/14577
---

# New segment editing feature: Smoothing brush

**Topic ID**: 14577
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577

---

## Post #1 by @lassoan (2020-11-13 00:51 UTC)

<p>We added a new interactive <em>smoothing brush</em> tool to Segment editor. Select the smoothing effect and start “paint” in the slice or 3D views to smooth the highlighted region, while keeping the rest of the segment kept unchanged. This is useful for touching up small segmentation errors in some areas, while preserving all details in other regions.</p>
<p>Short demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="rjNcvefBaNU" data-video-title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rjNcvefBaNU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rjNcvefBaNU/maxresdefault.jpg" title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" width="" height="">
  </a>
</div>

<p>Painting in 3D is disabled by default, can be enabled by checking “Edit in 3D views” checkbox in “Smoothing brush options” section.</p>
<p>“Median” and “Gaussian” method fills holes and remove extrusions to make surfaces smoother. “Opening” method only removes material (flattens the surface), “Closing” method only adds material (fills holes and gaps).</p>
<p>Smoothing strength is not affected by brush size, or how many times a region is painted over within the same stroke. The painted area just specifies where the smoothing operation is applied to.</p>
<p>Any suggestions and feedback are welcome.</p>

---
