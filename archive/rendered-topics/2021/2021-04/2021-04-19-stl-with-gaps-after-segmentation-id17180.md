---
topic_id: 17180
title: "Stl With Gaps After Segmentation"
date: 2021-04-19
url: https://discourse.slicer.org/t/17180
---

# STL with gaps after segmentation

**Topic ID**: 17180
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/stl-with-gaps-after-segmentation/17180

---

## Post #1 by @Marknagel (2021-04-19 17:13 UTC)

<p>Hey everybody!<br>
I’m pretty new to 3D Slicer, basically using it to 3d print bones out of CT-data.<br>
Managed to print a femur once, but i’m now having a hard time to print a humerus:</p>
<p>I seperated the humuers from the rest with the segmentation editor, but when i export the segmentation into a stl-file the stl-file is filled with many gaps. The gaps are in the planes where i didn’t manually segment the bone from the rest, but i don’t want to brush all the 1000 planes? After initializing from seeds the computer nicely finds what’s humerus and what’s not, but the segmented STL is full of gaps?</p>
<p>A little help appreciated!<br>
Thank you!</p>

---

## Post #2 by @lassoan (2021-04-19 17:18 UTC)

<p>You can use “Fill between slices” effect in Segment Editor to interpolate between slices. If the preview results look good then don’t forget to go back to “Fill between slices” effect and hit “Apply”.</p>

---

## Post #3 by @Marknagel (2021-04-19 17:51 UTC)

<p>Thank you for your advice <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
I wonder why i can’t export a stl-model from what the computer already identified as bone, because this is pretty precise?!</p>

---

## Post #4 by @lassoan (2021-04-19 17:53 UTC)

<p>You can export a segmentation as STL anytime. If this is not what you need then maybe you could attach a screenshot and explain with a bit more details of what you would like to achieve.</p>

---

## Post #5 by @Marknagel (2021-04-19 18:07 UTC)

<p>What i mean is:<br>
Let’s say i manually brushed the bone in maybe 50 planes out of 150 and hit the “grow out of seeds” button. The computer precisely identifies the bone in all 150 planes.<br>
Now i want to seperate the bone - which is correctly identified by the “grow out of seed”-algorithm - from the rest. So i create a STL-model out of my segmentation. Unfortunately i get a STL with many gaps. What i used to do is brushing the missing 100 planes manually, which is plenty of work. I think this must be unnecessary as the computer already identified the bone in all planes?</p>

---

## Post #6 by @lassoan (2021-04-19 18:13 UTC)

<p>What you saw was just the live preview. That is just a temporary overlay, which is not included in the export. If you use “Grow from seeds” (or other effects with live preview feature, such as “Fill between slices” or “Watershed”), you need to click “Apply” if the previewed results are good.</p>
<p>Note that with “Grow from seeds” effect it is not necessary to segment complete slices, just paint seeds inside each object of interest (and one “other” segment, if you don’t use masking). If you segment complete slices and just want fill the gaps between them then “Fill between slices” effect is more appropriate.</p>

---

## Post #7 by @Marknagel (2021-04-19 18:58 UTC)

<p>Got it! Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
