---
topic_id: 35498
title: "How To Edit Segmentations In Total Segmentator"
date: 2024-04-15
url: https://discourse.slicer.org/t/35498
---

# How to edit segmentations in total segmentator

**Topic ID**: 35498
**Date**: 2024-04-15
**URL**: https://discourse.slicer.org/t/how-to-edit-segmentations-in-total-segmentator/35498

---

## Post #1 by @jake14 (2024-04-15 15:30 UTC)

<p>Used total segmentor for one case and there was an incorrect segmentation done where it has a gap in a structure I am intersted in. Is there an easy was to correct and edit the segmentation that is not accurate? every other segmentation looks good but hoping there is an easy way to clean up and fix the areas that dont look correct.</p>

---

## Post #2 by @jake14 (2024-04-22 17:10 UTC)

<p>Still could use some help on this</p>

---

## Post #3 by @muratmaga (2024-04-22 17:47 UTC)

<p>You should be able to use Segment Editor in Slicer to manually edit the incorrect sections.</p>
<p>I don’t think there is an easier way to fix than that.</p>

---

## Post #4 by @jake14 (2024-04-22 18:38 UTC)

<p>that is what i assumed and tried however it would not allow these segments to be added in a 3d space and rather would appear as segmentations with no depth</p>

---

## Post #5 by @muratmaga (2024-04-22 20:00 UTC)

<p>Please share a screenshot of the problem or a link to the offending data.</p>

---

## Post #6 by @jake14 (2024-04-23 17:08 UTC)

<p>there is a cap in the given area I was segmenting using total segmentator extension, to fix this i used the draw and fill grow from seeds function however when doing so it only creates the image you see. hopefully this help clarify the issue I have.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab6679943e424ea95adde4bdf87a2eda37b6c25d.jpeg" data-download-href="/uploads/short-url/oshckKxQUxTQn71yuOOBLkKCWJv.jpeg?dl=1" title="IMG_4063" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab6679943e424ea95adde4bdf87a2eda37b6c25d_2_375x500.jpeg" alt="IMG_4063" data-base62-sha1="oshckKxQUxTQn71yuOOBLkKCWJv" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab6679943e424ea95adde4bdf87a2eda37b6c25d_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab6679943e424ea95adde4bdf87a2eda37b6c25d_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab6679943e424ea95adde4bdf87a2eda37b6c25d_2_750x1000.jpeg 2x" data-dominant-color="8D889A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4063</span><span class="informations">1920×2560 829 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @liu1 (2025-09-17 13:23 UTC)

<p>你好，请问现在你解决这个问题了吗？因为我和你遇到了相同的问题：TotalSegmentor分割了整个椎骨，我只希望得到锥体的松质骨部分</p>
<p>Hello, may I ask if you have resolved this issue now? Because I encountered the same problem as you: TotalSegmentor segmented the entire vertebra, but I only want the trabecular bone part of the cone.</p>

---

## Post #8 by @lassoan (2025-09-20 22:27 UTC)

<p>It all looks good. You can edit segmentations in 2D and in 3D using the Segment Editor module. For manual touchup you may also consider using <code>nnInteractive</code> extension. If you have any specific questions or trouble doing some corrections then let us know.</p>

---
