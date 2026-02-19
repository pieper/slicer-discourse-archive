---
topic_id: 35377
title: "Issue With Face Segmentation Using Total Segmentator"
date: 2024-04-09
url: https://discourse.slicer.org/t/35377
---

# Issue with face segmentation using Total Segmentator

**Topic ID**: 35377
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/issue-with-face-segmentation-using-total-segmentator/35377

---

## Post #1 by @KSL (2024-04-09 05:11 UTC)

<p>Hello friends, I am facing an issue segmenting the face using the face segmentation in Total segmentator module. I have the license but was unable to complete the task. I attach a photo of the output for your information. I would be glad if I<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51b27ba9d3027f21d63d5fdd9528eb11b0dca981.png" data-download-href="/uploads/short-url/bEJ4xLbZQzcvHUWhHPpxmBADDXP.png?dl=1" title="Screenshot 2024-04-09 103458" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b27ba9d3027f21d63d5fdd9528eb11b0dca981_2_690x483.png" alt="Screenshot 2024-04-09 103458" data-base62-sha1="bEJ4xLbZQzcvHUWhHPpxmBADDXP" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b27ba9d3027f21d63d5fdd9528eb11b0dca981_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51b27ba9d3027f21d63d5fdd9528eb11b0dca981_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51b27ba9d3027f21d63d5fdd9528eb11b0dca981.png 2x" data-dominant-color="DDDCDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-09 103458</span><span class="informations">1091×764 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
could get your assistance. Thank you.</p>

---

## Post #2 by @lassoan (2024-04-10 03:49 UTC)

<p>This is not an issue, the model has been trained to do exactly this. It is not for getting the skin surface but to get a mask that can be used for face blurring. See some more details in the <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#face-segment-is-inaccurate">documentation</a>.</p>

---
