---
topic_id: 13327
title: "Alignment Of 2 Models For Landmark Recognition"
date: 2020-09-03
url: https://discourse.slicer.org/t/13327
---

# Alignment of 2 models for landmark recognition

**Topic ID**: 13327
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/alignment-of-2-models-for-landmark-recognition/13327

---

## Post #1 by @Cesar_Puga (2020-09-03 16:23 UTC)

<p>Hello All, im having doubts/difficulties on how to approach a specific task in Slicer that will be used for a needle insertion project,</p>
<p>i want to align a body model (composed of bones, skin and organs) with specific information (needle entry points, potential trajectories, etc.,) with a newly loaded body model coming from a ct scan, the purpose of this is to adjust and be able to visualize this valuable information in any different body shape coming from an individual patient CT Scan loaded and segmented in slicer,</p>
<p>is there a specific module/segmentation recipe/ tutorial that would be able to tackle this task? i am looking for something similar to the basel face morphable model that is useful to identify face landmarks but in this case to a human body to recognize for example important landmarks to perform, for example, a liver biopsy,</p>
<p>thanks for your kind support</p>

---

## Post #2 by @lassoan (2020-09-03 16:37 UTC)

<p>Alignment of a physical object with an image of that object is a very common task, which is usually accomplished by landmark registration. See step-by-step description in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> - more specifically: U-12 Landmark registration.</p>

---
