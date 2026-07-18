---
topic_id: 47656
title: "Recurring bug on Shoulder tracking"
date: 2026-07-17
url: https://discourse.slicer.org/t/47656
last_bumped: 2026-07-17T20:46:45.895Z
---

# Recurring bug on Shoulder tracking

**Topic ID**: 47656
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/recurring-bug-on-shoulder-tracking/47656

---

## Post #1 by @AlonsoFigueroa (2026-07-17 13:14 UTC)

<p>Hello SAM team,</p>
<p>We are encountering an issue while tracking a scapula in Autoscoper during an arm elevation task.</p>
<p>For one participant, Autoscoper consistently crashes when saving frames within specific ranges of motion. The crash occurs during tracking of the shoulder/scapula and is reproducible across multiple trials. We have attempted to process the same participant data on different computers and obtained the same result each time.</p>
<p>I found an older issue that appears to describe a very similar problem, although it does not seem to have been resolved:</p>
<p><a href="https://github.com/BrownBiomechanics/Autoscoper/issues/305" rel="noopener nofollow ugc">BrownBiomechanics/Autoscoper#305</a></p>
<p>System information:</p>
<p>3D Slicer version: 5.10.1<br>
Operating System: Windows<br>
GPU: NVIDIA RTX 3080 Ti</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cb90a5436921c99d7fcd2f5cf8672ebc0338cfc.gif" alt="Adobe Express - 2026-07-09_15-41-23" data-base62-sha1="6nDsg9GlDl8T0RCDrHwJ6aTYUs4" width="422" height="226" class="animated"></p>

---

## Post #2 by @John_Holtgrewe (2026-07-17 15:03 UTC)

<p>Hi Alonso,</p>
<p>Thanks for bringing this to our attention. My experience with SAM is limited to tracking the femur and tibia, and I have not encountered this issue. However, I know that other groups have used SAM to successfully track the scapula. <a class="mention" href="/u/cesar">@Cesar</a> Did you have this issue with any of your data?</p>
<p>Does this happen when processing data from other participants, or just this one?</p>

---

## Post #3 by @Cesar (2026-07-17 17:53 UTC)

<p>I remember running into a similar issue while using the optimization feature, but it was fixed fairly quickly. I haven’t seen this specific problem before. I wonder if the graphics card could be causing the crash. Alonso, are you running SAM on a remote computer?</p>

---

## Post #4 by @AlonsoFigueroa (2026-07-17 20:46 UTC)

<p>Hello Cesar and John,</p>
<p>Thank you for taking the time to investigate this issue.</p>
<p>We are currently running SAM on a local workstation. We’ve tested multiple computers and several different subjects, and it appears that approximately half of the subjects we upload to SAM encounter this issue.</p>
<p>The workstations we have been using for these trials have the following specifications:</p>
<ul>
<li>Dell Precision 5860</li>
<li>Intel Xeon W3-2423</li>
<li>NVIDIA RTX 3080 Ti</li>
</ul>
<p>I’d be happy to share the files with your team if you’d like to investigate further. However, the image files are too large to upload through this platform. Please let me know the best way to transfer them, and I’ll send them over.</p>

---
