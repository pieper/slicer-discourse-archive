---
topic_id: 17580
title: "Subtracting Volumes From Two Different Scans"
date: 2021-05-12
url: https://discourse.slicer.org/t/17580
---

# Subtracting volumes from two different scans

**Topic ID**: 17580
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/subtracting-volumes-from-two-different-scans/17580

---

## Post #1 by @Shrb_Show (2021-05-12 01:16 UTC)

<p>Hi,<br>
I am a beginner at 3D Slicers and would like some suggestion on how can I subtract volumes from two different CT scans. My goal is obtained the amount (Volume) of bone removed from the first image by comparing to it the second volume.</p>
<p>Thanks in advance</p>

---

## Post #2 by @JanWitowski (2021-05-12 01:36 UTC)

<p>To create subtraction images you can use Subtract Scalar Volume module that is pre-built inside 3D Slicer. Alternatively, you can use Python and perform simple subtraction between two volumes. Relevant thread: <a href="https://discourse.slicer.org/t/scalar-subtraction/4401" class="inline-onebox">Scalar subtraction</a></p>
<p>However, if you are calculating difference between two segmentations (bone segmented on image 1 - bone segmented on image 2), you don’t need to subtract them, just segment both and calculate their respective volumes with Segment Statistics module.</p>

---

## Post #3 by @Shrb_Show (2021-05-12 01:43 UTC)

<p>Thanks for the reply.<br>
But I am looking to calculate the amount of bone removed during reaming by comparing the two images</p>

---

## Post #4 by @JanWitowski (2021-05-12 01:52 UTC)

<p>So to answer your original question – how to subtract volumes from two different CT scans – look at my post above: you can use either Subtract Scalar Volume or python.</p>

---
