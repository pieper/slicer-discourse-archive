---
topic_id: 42594
title: "Monai Auto3Dseg Segmentation Error"
date: 2025-04-17
url: https://discourse.slicer.org/t/42594
---

# MONAI Auto3DSeg Segmentation Error

**Topic ID**: 42594
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/monai-auto3dseg-segmentation-error/42594

---

## Post #1 by @ShoopD (2025-04-17 06:11 UTC)

<p>Greetings.</p>
<p>I did a whole-body segmentation with the MONAI Auto3DSeg (Whole body segmentation TS1) and exported it in the RTSTRUCT format. There were a few missing parts after the segmentation, especially in the brain part. While exporting, I deleted a few segmentations as they were unnecessary for my calculation.</p>
<p>However, when I opened the exported segmentation RTSTRUCT file again in 3D Slicer, it showed that in many slices, some of the organs were missing. What could be the reason for this? Are there any solutions to ensure a good segmentation?</p>
<p>Thanks in advance! I’m attaching a screen recording of the segmentaion file.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9771e3b90d02f7b1faa820cb73f494502dc02f7e.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b508446fabf46567aaea2393bd56de1e6db615.jpeg" data-video-base62-sha1="lBK6wBHA5obAIXtvZ8p9n5afp5s.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2025-04-17 12:55 UTC)

<p>RTSTRUCT can be challenging for a variety of reasons, so if you don’t need that particular format you should consider another, like DICOM SEG or even a research format like .seg.nrrd.</p>
<p>If you absolutely need RTSTRUCT you may need to simplify the structures segment-by-segment or do other workarounds.  Posting examples of what segments work and which don’t might give people ideas that could help you.</p>

---
