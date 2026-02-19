---
topic_id: 34125
title: "Best Way To Extract Isolate Areas From A Segment"
date: 2024-02-02
url: https://discourse.slicer.org/t/34125
---

# Best way to extract/isolate areas from a segment ? 

**Topic ID**: 34125
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/best-way-to-extract-isolate-areas-from-a-segment/34125

---

## Post #1 by @dcg494 (2024-02-02 19:48 UTC)

<p>Hi all, i’m looking for help getting parts of this segment isolated. As you can see in the picture, the green area is the segment and i’m trying to isolate the airways from the area outside of the head.</p>
<p>Very new to 3-d slicer and segmentation. Thought i could just work with thresholding and logic operators, but didn’t work. Appreciate any advice on this !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f4126037e03ac7aef2adbea5f8a7133d362073.jpeg" data-download-href="/uploads/short-url/iY9WK6sA269An4Pj7894PPyT0Ur.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f4126037e03ac7aef2adbea5f8a7133d362073_2_690x485.jpeg" alt="image" data-base62-sha1="iY9WK6sA269An4Pj7894PPyT0Ur" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f4126037e03ac7aef2adbea5f8a7133d362073_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f4126037e03ac7aef2adbea5f8a7133d362073_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f4126037e03ac7aef2adbea5f8a7133d362073.jpeg 2x" data-dominant-color="53595F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1234×869 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2024-02-02 19:55 UTC)

<p>You could try the “Islands” tool in Segment Editor!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca2f41602e20f9e5137ec80f866b2155b46aad3.gif" alt="2024-02-02_14-54-27" data-base62-sha1="vtQawf99OTB8bnsCcG4L1a4rKxR" width="690" height="406" class="animated"></p>

---

## Post #3 by @muratmaga (2024-02-02 20:01 UTC)

<p>I believe their is already “airways extraction” extension. Did you give that a try?</p>
<p><a href="https://github.com/PietroNardelli/Slicer-AirwaySegmentation">PietroNardelli/Slicer-AirwaySegmentation: CLI module for airway segmentation starting from chest CT images (github.com)</a></p>

---

## Post #4 by @lassoan (2024-02-04 19:24 UTC)

<p>Islands effect should work well if the regions are not connected. If airways are connected through the nose or mouth then you can extract the skin surface as described <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">in this recipe</a> and use Logical operators effect to only keep air that is inside the body.</p>

---
