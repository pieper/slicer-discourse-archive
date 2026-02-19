---
topic_id: 7425
title: "How To Duplicate A Segment Easily For Other Master Volume"
date: 2019-07-05
url: https://discourse.slicer.org/t/7425
---

# How to duplicate a segment easily for other master volume?

**Topic ID**: 7425
**Date**: 2019-07-05
**URL**: https://discourse.slicer.org/t/how-to-duplicate-a-segment-easily-for-other-master-volume/7425

---

## Post #1 by @TingtingYu (2019-07-05 06:08 UTC)

<p>Hi~,</p>
<p>I first created a segment using Segment Editor when CT is the master volume. Then I want to create a same segment when I choose MRI image as the master volume. Is there a easy way to do that? (CT volume and MRI volume have different grid size) I also read the similar topic " <a href="https://discourse.slicer.org/t/how-to-copy-segment-between-multi-sequence-mri-images/1677">How to copy segment between multi-Sequence MRI images</a>" . The answer that you gave is “Add new segments, select the other MRI image as master volume, and segment structures using that volume.” That means I still need to re-segment the structure if I choose MRI image as new master volume. I want to have a same segment and export it into binary labelmap which has the same grid size as MRI volume.</p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @cpinter (2019-07-05 13:06 UTC)

<p>You don’t need to duplicate and resample your segment to export it with a different geometry. You can export segments with given geometry in the Segmentations module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f7b9edfff475ba7b933bff5d8ef746aad68f840.png" alt="image" data-base62-sha1="ibLuFwljzBZ5qF1tv2RBMllOm1a" width="538" height="215"></p>
<p>However if you want to duplicate and resample, you can go to Data module, right-click the segmentation, choose Clone, go to Segment Editor, select the clone, then click the geometry icon in the row of the master volume selector. However for export purposes I suggest the first approach above.</p>

---

## Post #3 by @TingtingYu (2019-07-08 02:19 UTC)

<p>Hi Csaba,</p>
<p>Thank you for your help. I prefer the first approach.</p>
<p>Best,<br>
Tingting</p>

---
