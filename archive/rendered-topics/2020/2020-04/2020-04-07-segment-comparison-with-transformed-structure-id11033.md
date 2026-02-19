---
topic_id: 11033
title: "Segment Comparison With Transformed Structure"
date: 2020-04-07
url: https://discourse.slicer.org/t/11033
---

# Segment comparison with transformed structure

**Topic ID**: 11033
**Date**: 2020-04-07
**URL**: https://discourse.slicer.org/t/segment-comparison-with-transformed-structure/11033

---

## Post #1 by @izzatizulkarnain (2020-04-07 22:41 UTC)

<p>Hi, I am trying to get the dice coefficient and hausdorff distance to compare 2 structures from a TPS (red) and a DIR software (blue). I registered the blue GTV to the red GTV using the Transforms module and calculated the dice coefficient and HD. Despite the overlap of the two structures, why is the dice coefficient very small? Is there a better way for me to do the structure registration?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a0ea3573733748234bc8b9ec9aab9f8f24bc7b.jpeg" data-download-href="/uploads/short-url/llFTTSrrOcWOtqUnD1xkz0D8W6L.jpeg?dl=1" title="Segment comparison" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95a0ea3573733748234bc8b9ec9aab9f8f24bc7b_2_690x339.jpeg" alt="Segment comparison" data-base62-sha1="llFTTSrrOcWOtqUnD1xkz0D8W6L" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95a0ea3573733748234bc8b9ec9aab9f8f24bc7b_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95a0ea3573733748234bc8b9ec9aab9f8f24bc7b_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95a0ea3573733748234bc8b9ec9aab9f8f24bc7b.jpeg 2x" data-dominant-color="BAB9BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment comparison</span><span class="informations">1365×671 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @gregsharp.geo (2020-04-07 23:03 UTC)

<p>Something looks wrong. Can you try hardening the transform?  That shouldn’t be necessary but worth a try.</p>

---
