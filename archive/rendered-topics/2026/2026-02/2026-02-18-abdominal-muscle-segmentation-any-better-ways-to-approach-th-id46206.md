---
topic_id: 46206
title: "Abdominal Muscle Segmentation Any Better Ways To Approach Th"
date: 2026-02-18
url: https://discourse.slicer.org/t/46206
---

# Abdominal Muscle Segmentation any better ways to approach this?

**Topic ID**: 46206
**Date**: 2026-02-18
**URL**: https://discourse.slicer.org/t/abdominal-muscle-segmentation-any-better-ways-to-approach-this/46206

---

## Post #1 by @CS1 (2026-02-18 05:18 UTC)

<p>Hello there,</p>
<p>I’ve been using total segmentator, 3D slicer for the past few months trying to get the volumetric data for body composition of the lumbar region. I have to say that it is a great resource and gives you a decent segmentation result, however, I’ve also noticed multiple issues such as some muscle groups are poorly segmented requiring lots of manual correction or there is segmentation error when it comes to intermuscular fat which requires thresholding with HU.</p>
<p>I intended to train my own model however I have zero background in coding, python and I had no dataset for me to train my own AI. On top of that I don’t even know if it’s gonna perform better than total segmentator which was trained using triple the number of segmented CTs than what I’ve got…</p>
<p>I’m now very stuck, each CT takes me 30-40 mins to segment including the time requires for manual correction, took me 4 months to go through 130 patients with 2 CT scans each…</p>
<p>Any suggestions on how I can improve my workflow and methods.. any other tools that I could potentially use? I’d love to include more patients but I don’t think this is a sustainable approach..</p>
<p>I’m very grateful for this supportive community, I don’t think I could make it this far without this forum and all the help I’ve received. thank you thank you.</p>

---

## Post #2 by @rkikinis (2026-02-18 06:43 UTC)

<p>Hi<br>
there are several options in terms of trained networks. Have you checked them out?<br>
<a href="https://arxiv.org/pdf/2512.15921" class="onebox" target="_blank" rel="noopener nofollow ugc">https://arxiv.org/pdf/2512.15921</a><br>
Best<br>
Ron</p>

---
