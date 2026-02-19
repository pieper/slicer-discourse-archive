---
topic_id: 20196
title: "Extract Sub Segment From Segmentation Based On Seed And Volu"
date: 2021-10-17
url: https://discourse.slicer.org/t/20196
---

# Extract sub-segment from segmentation based on seed and volume (in Python)

**Topic ID**: 20196
**Date**: 2021-10-17
**URL**: https://discourse.slicer.org/t/extract-sub-segment-from-segmentation-based-on-seed-and-volume-in-python/20196

---

## Post #1 by @kkkkkkk123 (2021-10-17 20:30 UTC)

<p>Hi everyone,</p>
<p>I’m currently having a segmented image, but now I want to create a new (sub-)segmentation from the segmented image based on an initial seed point (x,y,z) and with a given volume threshold, e.g. max 20 cc. I want to implement it in Python.<br>
Has anyone ever done this or any idea what the easiest way is to do this?<br>
Thanks in advance!</p>
<p>Kylie</p>

---

## Post #2 by @lassoan (2021-10-17 20:40 UTC)

<p>This is exactly what Fast Marching segment editor effect does. It is provided by SegmentEditorExtraEffects extension.</p>
<p>I don’t think that this is effect can take into account masking during the region growing operation. But you can blank out the volume (set it to a very different intensity) outside the mask before applying Fast Marching.</p>

---

## Post #3 by @kkkkkkk123 (2021-10-18 06:21 UTC)

<p>Thank you for the fast reply! I’ll look into it <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=10" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:"></p>

---

## Post #4 by @kkkkkkk123 (2021-10-19 08:57 UTC)

<p>So I’m currently still struggling with it. The situation is that I already have a segmentation result, so I should set the output data of the vtkPichonFastMarching() either with setOutData() or SetOutput(), right? And add the seed point with either addSeed() or addSeedIJK()? So I can then perform the fm.show() operation with the given fraction? Or is there still additional information that I need to provide for the vtkPichonFastMarching?</p>
<p>Thanks in advance!</p>

---

## Post #5 by @lassoan (2021-10-20 05:46 UTC)

<p>I would recommend to first just use the GUI. Once you confirmed that everything works as expected you can start Python scripting to automate everything.</p>

---
