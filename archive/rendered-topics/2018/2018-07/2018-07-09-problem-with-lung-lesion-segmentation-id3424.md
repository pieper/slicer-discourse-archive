---
topic_id: 3424
title: "Problem With Lung Lesion Segmentation"
date: 2018-07-09
url: https://discourse.slicer.org/t/3424
---

# Problem with Lung lesion segmentation

**Topic ID**: 3424
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/problem-with-lung-lesion-segmentation/3424

---

## Post #1 by @Daan (2018-07-09 12:30 UTC)

<p>Dear all,</p>
<p>We are using the lung lesion analyser to make segmentations of lung nodules. When we segment the nodule, we also get some kind of planes in our segmentations as can be seen in the image I have added. When we change the threshold it sometimes disappears. Unfortunately, we cannot use different thresholds. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2463f3876726d1718ac8c9c83eb1e071fe3b1a.png" data-download-href="/uploads/short-url/69EuPUEfs8aC0MTvQ5sESjIj1fI.png?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2463f3876726d1718ac8c9c83eb1e071fe3b1a_2_690x373.png" alt="3dslicer" data-base62-sha1="69EuPUEfs8aC0MTvQ5sESjIj1fI" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2463f3876726d1718ac8c9c83eb1e071fe3b1a_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2463f3876726d1718ac8c9c83eb1e071fe3b1a_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2463f3876726d1718ac8c9c83eb1e071fe3b1a_2_1380x746.png 2x" data-dominant-color="9B9FB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">1920×1040 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Does anybody know how to solve this issue?</p>
<p>With kind regards,</p>
<p>Daan</p>

---

## Post #2 by @lassoan (2018-07-10 03:21 UTC)

<p>Are the planes present in the images? Can you see bright lines in the images in slice views and/or see the planes in volume rendering?</p>
<p>If yes, then you may need to mask out these objects. You can use Mask volume effect in Segment editor module (after you installed SegmentEditorExtraEffects extension) for this.</p>

---

## Post #3 by @Daan (2018-07-10 07:34 UTC)

<p>Unfortunately, the planes are not present in the images originaly, but are added when we do the segmentation. It does not matter where we do the segmentation or what we segment, the planes are added everytime.</p>

---

## Post #4 by @lassoan (2018-07-10 14:48 UTC)

<p><a class="mention" href="/u/raul">@raul</a> <a class="mention" href="/u/jonieva">@jonieva</a> Can you advise?</p>

---

## Post #5 by @fedorov (2018-07-10 16:14 UTC)

<p>I’ve experienced similar behavior of the lesion segmenter when I tried it a year ago. It created an extra segmented plane. I think I reported this to <a class="mention" href="/u/jonieva">@jonieva</a>.</p>
<p>A practical workaround could be to have a simple post-processing script that discards the segmented component that is not connected to the lesion, which in turn can be easily identified using the seed point.</p>

---

## Post #6 by @jonieva (2018-07-10 17:08 UTC)

<p>Unfortunately I could not reproduce this problem so far. Do you think it would be possible to share a scan where you are having this issue?</p>
<p>Thanks,<br>
Jorge</p>

---

## Post #7 by @fedorov (2018-07-10 17:21 UTC)

<p><a class="mention" href="/u/jonieva">@jonieva</a> I believe I experienced this issue with the example dataset available here: <a href="http://slicer.kitware.com/midas3/download/item/245513/LIDC-IDRI-0314-CT.zip">http://slicer.kitware.com/midas3/download/item/245513/LIDC-IDRI-0314-CT.zip</a></p>

---

## Post #8 by @jonieva (2018-07-10 17:38 UTC)

<p>Thx <a class="mention" href="/u/fedorov">@fedorov</a> !</p>
<p>Indeed I could reproduce the problem with that scan. Let me look into it and I’ll keep you posted</p>

---

## Post #9 by @jonieva (2018-07-12 14:11 UTC)

<p>Hi guys</p>
<p>Good news, we succeeded to fix this problem, it is working now in the Slicer 4.8.1 Stable Release version (you will need to reinstall the extension).</p>
<p>However, I just found out that the Chest_Imaging_Platform extension is not available in the Nightly build, despite everything looks good in CDash. I will touch base with the experts <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>
<p>Best,</p>
<p>Jorge Onieva</p>

---

## Post #10 by @Daan (2018-07-13 08:27 UTC)

<p>Dear jorge,</p>
<p>Your work has indeed solved the problem for us as well. Thank you very much for this and your quick action.</p>
<p>With kind regards,</p>
<p>Daan</p>

---
