---
topic_id: 16059
title: "How To Describe The Position Relationship Between Lung Tumor"
date: 2021-02-18
url: https://discourse.slicer.org/t/16059
---

# How to describe the position relationship between lung tumor and trachea

**Topic ID**: 16059
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/how-to-describe-the-position-relationship-between-lung-tumor-and-trachea/16059

---

## Post #1 by @zzm (2021-02-18 12:10 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior: After the lung and trachea are separated, what parameters describe their position relationship<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-02-18 12:19 UTC)

<p>How would you like to describe the spatial relationship? For what purpose? Can you describe the overall goal of your or your project?</p>

---

## Post #3 by @zzm (2021-02-23 01:58 UTC)

<p>Thanks for your help.<br>
I am a radiotherapy physician. I want to analyze the effect of the relative spatial location of central lung cancer and the main trachea on the curative effect, but I do not know how to obtain the spatial location relationship data of lung mass and trachea.<br>
sincere thanks <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #4 by @lassoan (2021-02-23 02:20 UTC)

<p>You can get position of each segment as oriented bounding box, center of gravity, principal axes, etc. <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">using Segment Statistics module</a>. This provides you rich spatial relationship information.</p>

---
