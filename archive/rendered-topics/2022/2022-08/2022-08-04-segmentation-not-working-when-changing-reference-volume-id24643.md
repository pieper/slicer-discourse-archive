---
topic_id: 24643
title: "Segmentation Not Working When Changing Reference Volume"
date: 2022-08-04
url: https://discourse.slicer.org/t/24643
---

# Segmentation not working when changing reference volume

**Topic ID**: 24643
**Date**: 2022-08-04
**URL**: https://discourse.slicer.org/t/segmentation-not-working-when-changing-reference-volume/24643

---

## Post #1 by @bserrano (2022-08-04 13:40 UTC)

<p>Hi all,</p>
<p>I segmented some structures using a cropped volume from a bigger one. I realized that I wanted a bigger volume so I cropped the original again. However, the segmentation I had is not working in the new area.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6bc0a99f5cf28a8aad5bf24ee49350a83223dcb.png" alt="imagen" data-base62-sha1="nN08utG7X4aQ0AW33sqV8DmC6Zt" width="310" height="297"><br>
I can’t use tools outside the original area (green). How can I fix this? I tryied to change the master volume but if I do “mask volume” it does not work. I tryied to create another segmentation node and copy the segment but nothing. I’m becoming a bit crazy.<br>
Slicer version: 4.11.20210226</p>

---

## Post #2 by @pieper (2022-08-04 13:48 UTC)

<p>You could try setting the segmentation’s geometry to match the uncropped volume.</p>

---

## Post #3 by @bserrano (2022-08-04 14:02 UTC)

<p>I tried but I’m experimenting a weird behaviour cause other tools like logical operators or mask volume stop working properly.</p>

---

## Post #4 by @lassoan (2022-08-05 17:05 UTC)

<p>If you can provide step-by-step description (or screen capture video) of the unexpected behavior then we can investigate. In the meantime, after your change the segment geometry, you may try to apply smoothing to all segments to force using the new geometry.</p>

---

## Post #5 by @bserrano (2022-08-05 21:20 UTC)

<p>Here are the steps:</p>
<p>1- Open volume. Let’s call it <em>volume</em>.<br>
2- Crop volume to obtain a smaller one. Let’s call it <em>smallCroppedVolume</em>.<br>
3- Segment croppedVolume. Here I have several segments.<br>
4- Crop <em>volume</em> again but this time we obtain a bigger one, <em>bigCroppedVolume</em>.<br>
5- Try to segment <em>bigCroppedVolume</em>. Realize that tools only work on the area of <em>smallCroppedVolume</em>.<br>
6- Change geometry and master volume to <em>bigCropppedVolume</em>. Now paint tool works but if I try to mask <em>bigCroppedVolume</em>, then it does not work.</p>
<p>It seems to work when applying smothing. Is there a way to apply smoothing and then undo the results (with code), so I don’t want to modify the segments.</p>
<p>Many thanks</p>

---
