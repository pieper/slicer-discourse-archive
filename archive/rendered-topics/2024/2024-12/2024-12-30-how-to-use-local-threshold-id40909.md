# How to use local threshold

**Topic ID**: 40909
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/how-to-use-local-threshold/40909

---

## Post #1 by @Dan_Cheng (2024-12-30 17:53 UTC)

<p>Hi<br>
I am trying to using local threshold in 5.6.2. When I press cmd + left click, there is no segment at all. Can anyone help me? Many thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4edbfdb7c927fd0653e73ad532007c10ec7bb75.jpeg" data-download-href="/uploads/short-url/unEBaJFIpW63g83OBj3vW7QK8Pb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4edbfdb7c927fd0653e73ad532007c10ec7bb75_2_690x376.jpeg" alt="image" data-base62-sha1="unEBaJFIpW63g83OBj3vW7QK8Pb" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4edbfdb7c927fd0653e73ad532007c10ec7bb75_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4edbfdb7c927fd0653e73ad532007c10ec7bb75_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4edbfdb7c927fd0653e73ad532007c10ec7bb75_2_1380x752.jpeg 2x" data-dominant-color="717271"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1048 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-01-01 17:35 UTC)

<p>The histogram is empty. Is the volume you see in the viewer the same as the source volume of the segmentation?</p>
<p>Have you set anything in the masking section that could prevent painting in the segment?</p>

---

## Post #3 by @muratmaga (2025-01-03 22:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> While useful, I find the local threshold tool difficult to use. Mostly because I get no feedback when things don’t work and I have no idea what I need to do/change. I am not sure if it is possible but when things are not being painted, would it be possible to give some feedback about what to change?</p>
<p>For example, in here I am trying to segment the enamel within the ROI, but I cannot never seem to finalize the selection. It just keeps blinking. CMD+left click doesn’t seem to do anything. Selection continues to fade in and out.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ea4c4d5c8ab7a1a96cbb45cbc71318e065a910c.png" data-download-href="/uploads/short-url/4n5l4i2veAsKJpRcFy2SHRt6a0A.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea4c4d5c8ab7a1a96cbb45cbc71318e065a910c_2_650x500.png" alt="image" data-base62-sha1="4n5l4i2veAsKJpRcFy2SHRt6a0A" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea4c4d5c8ab7a1a96cbb45cbc71318e065a910c_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea4c4d5c8ab7a1a96cbb45cbc71318e065a910c_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ea4c4d5c8ab7a1a96cbb45cbc71318e065a910c_2_1300x1000.png 2x" data-dominant-color="868489"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1702×1309 447 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2025-01-03 22:49 UTC)

<p>Generally it is the minimum diameter of the GrowCut algorithm that has to be adjusted for local threshold as the effect is more so a combo effect that is “Threshold+Grow From Seeds”.</p><aside class="quote quote-modified" data-post="2" data-topic="40671">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/local-threshold-bugs-or-features/40671/2">local threshold: bugs or features?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Creates a seed for segmentation and then uses that seed for region growing. 
The seed is generated by thresholding with the chosen intensity range, then keeping the island where you Ctrl-clicked. 

You can certainly do this, by simply using the Paint effect and then using Grow from seeds effect. Local threshold just automates painting of the seed (replaced 5-10 clicks by one click). 

When the island at the clicked position is determined, the thresholding result is eroded to prevent small, thin…
  </blockquote>
</aside>

<p><a class="mention" href="/u/thomas_k">@Thomas_K</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> and myself diiscussed this same topic about the confusion of the effect at the following hangout (linked below) with Thomas proposing a “Fast local threshold” which always picks the selected voxels such as a “Threshold+Islands” type of combo effect rather than being only based on the Grow From Seeds approach. That way what you click is what you get. From that discussion it seemed that <a class="mention" href="/u/lassoan">@lassoan</a> recognized the confusion in the current effect, but there was no clear consensus about the integration of such a “Threshold+Islands” type approach.</p><aside class="quote" data-post="2" data-topic="40250">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9d8465/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/2024-10-19-weekly-meeting-11-am-start/40250/2">2024.10.19 Weekly Meeting - 11 AM start!</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" style="--category-badge-color: #12A89D; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
  </div>
  <blockquote>
    Agenda item topic: Modification / addition to Local Thresholding segment effect (<a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorLocalThreshold" class="inline-onebox" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects/SegmentEditorLocalThreshold at master · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a>)
  </blockquote>
</aside>

<p>The regular “Threshold” effect supports local histogram selection (drawn below), but then you have to use another effect to ultimately pick which selected voxels to keep from the full selection.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af6d22d8e2c5d2993e55a7d58e9d50eb61ceb03.jpeg" data-download-href="/uploads/short-url/m6SlcIJx0rEfax9VuMPXGv5vrBF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af6d22d8e2c5d2993e55a7d58e9d50eb61ceb03_2_690x370.jpeg" alt="image" data-base62-sha1="m6SlcIJx0rEfax9VuMPXGv5vrBF" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af6d22d8e2c5d2993e55a7d58e9d50eb61ceb03_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af6d22d8e2c5d2993e55a7d58e9d50eb61ceb03_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9af6d22d8e2c5d2993e55a7d58e9d50eb61ceb03_2_1380x740.jpeg 2x" data-dominant-color="7C7B79"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
