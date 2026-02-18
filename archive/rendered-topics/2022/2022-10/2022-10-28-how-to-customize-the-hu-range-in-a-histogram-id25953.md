# How to customize the HU range in a histogram?

**Topic ID**: 25953
**Date**: 2022-10-28
**URL**: https://discourse.slicer.org/t/how-to-customize-the-hu-range-in-a-histogram/25953

---

## Post #1 by @shansra11 (2022-10-28 11:58 UTC)

<p>How would I go about assessing what percent of a mass is cystic (-100 to -10 HU), cystic (0-20 HU), or solid (20+ HU).  Is there any way to assess macroscopic fat, meaning confluent areas of fat attenuation as opposed to interspersed fat voxels?</p>

---

## Post #2 by @lassoan (2022-10-30 02:11 UTC)

<p>After you segmented the mass, it is very easy to partition it by HU value range. You can set editable region to be within segments, and then for each HU range: create a new segment and fill it using Threshold effect.</p>

---

## Post #3 by @shansra11 (2022-11-03 21:58 UTC)

<p>Great idea and so far it’s working!<br>
I am an academic researcher so the goal would be to publish my findings in a journal.<br>
Do the threshold values correlate 1:1 with HU value on CT?  If my goal is to provide a % of fat in a mass, is there anything else I should be considering when it comes to standardizing my results?  I’m assuming interpolation etc. is not relevant in this case?<br>
Thanks for your help.</p>

---

## Post #4 by @lassoan (2022-11-04 14:22 UTC)

<aside class="quote no-group" data-username="shansra11" data-post="3" data-topic="25953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/94ad74/48.png" class="avatar"> shansra11:</div>
<blockquote>
<p>Do the threshold values correlate 1:1 with HU value on CT?</p>
</blockquote>
</aside>
<p>Yes, in clinical CT images, voxel values are calibrated so that they are in HU.</p>
<aside class="quote no-group" data-username="shansra11" data-post="3" data-topic="25953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/94ad74/48.png" class="avatar"> shansra11:</div>
<blockquote>
<p>If my goal is to provide a % of fat in a mass, is there anything else I should be considering when it comes to standardizing my results?</p>
</blockquote>
</aside>
<p>If the segmentation looks correct (regions that are marked as fat are actually fat) then the computed % values will be correct. If you evaluate the same anatomical region of similar patients with the same imaging protocol then most likely the results will be consistent across all cases. If there are some variations then it makes sense to check a number of cases in each group to ensure that your method works consistently well.</p>

---

## Post #5 by @Eka_Mulyani (2025-05-15 04:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361327ff0be8f828b3f2751b95395b8bf6a5f54c.png" data-download-href="/uploads/short-url/7ImPb1HXRS6rcFl1FbZa4DKT97K.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361327ff0be8f828b3f2751b95395b8bf6a5f54c_2_690x368.png" alt="image" data-base62-sha1="7ImPb1HXRS6rcFl1FbZa4DKT97K" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361327ff0be8f828b3f2751b95395b8bf6a5f54c_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361327ff0be8f828b3f2751b95395b8bf6a5f54c_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361327ff0be8f828b3f2751b95395b8bf6a5f54c_2_1380x736.png 2x" data-dominant-color="44464A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1831×978 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi Andras, can you help me? I have a problem with dicom images, I want the HU value to be around 200 but I only get 1. How do I fix this?</p>

---
