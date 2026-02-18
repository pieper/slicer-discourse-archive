# Improve total segmentator lung lobes masks

**Topic ID**: 40358
**Date**: 2024-11-24
**URL**: https://discourse.slicer.org/t/improve-total-segmentator-lung-lobes-masks/40358

---

## Post #1 by @mau_igna_06 (2024-11-24 16:26 UTC)

<p>Hi</p>
<p>In the picture below, there are a CT slice (on the left) and its lung lobes segmentation from TotalSegmentator (on the right)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d5239116b114a20236ff2c1a81766974ae3051.jpeg" data-download-href="/uploads/short-url/heVWyHpUvDfuWEXXVUWlmI8YtYR.jpeg?dl=1" title="Screenshot from 2024-11-24 13-12-08_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5239116b114a20236ff2c1a81766974ae3051_2_690x443.jpeg" alt="Screenshot from 2024-11-24 13-12-08_2" data-base62-sha1="heVWyHpUvDfuWEXXVUWlmI8YtYR" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5239116b114a20236ff2c1a81766974ae3051_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5239116b114a20236ff2c1a81766974ae3051_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d5239116b114a20236ff2c1a81766974ae3051_2_1380x886.jpeg 2x" data-dominant-color="2F2E2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-11-24 13-12-08_2</span><span class="informations">1920×1235 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The picture shows that, on the right lung, the lobes segments border does not lie over the lung fissure (yellow arrow shows fissure, red arrow shows lobes segments limits) so that could be improved. At the same time, the left lung fissure is very dim, but TotalSegmentator identifies it well.</p>
<p>Do you think there could be any chance of getting better results training an AI with TotalSegmentator dataset just for lung lobes segmentation? If so, how?</p>

---

## Post #2 by @pieper (2024-11-25 14:08 UTC)

<p>This person appears to have significant lung disease.  The TotalSeg,entator training set contained people who were generally healthy, so it’s not a surprise that it doesn’t perform well on unhealthy subjects.</p>

---
