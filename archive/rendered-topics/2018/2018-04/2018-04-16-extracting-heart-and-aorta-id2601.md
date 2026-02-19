---
topic_id: 2601
title: "Extracting Heart And Aorta"
date: 2018-04-16
url: https://discourse.slicer.org/t/2601
---

# Extracting Heart and Aorta

**Topic ID**: 2601
**Date**: 2018-04-16
**URL**: https://discourse.slicer.org/t/extracting-heart-and-aorta/2601

---

## Post #1 by @zsa26 (2018-04-16 14:59 UTC)

<p>Hi everyone,</p>
<p>I am a new user to this software and I have been assigned the task of extracting an aorta to make a 3D print. However, whenever I get to the editor and I select threshold, It always recognizes bones and other materials as the same as the heart. I am wondering if anyone can help me accomplish this task.</p>
<p>Thanks,</p>
<p>Zein</p>

---

## Post #2 by @lassoan (2018-04-16 16:57 UTC)

<p>You can learn this from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">Video tutorial: Whole heart segmentation from cardiac CT</a>.</p>

---

## Post #3 by @jamesmoe (2019-01-31 01:46 UTC)

<p>i am in the same situation and carefully went through the tutorial. I am having a really hard time cleanly isolating the aorta. Is there a way to segment the aorta without segmenting the rest of the heart??</p>

---

## Post #4 by @lassoan (2019-01-31 02:05 UTC)

<p>Yes, sure, you can just paint seeds inside the aorta with one color and paint outside (through everything nearby that is not aorta) with another color. Then use Grow from seeds on these two segments.</p>

---
