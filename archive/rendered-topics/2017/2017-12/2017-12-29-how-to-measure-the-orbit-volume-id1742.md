---
topic_id: 1742
title: "How To Measure The Orbit Volume"
date: 2017-12-29
url: https://discourse.slicer.org/t/1742
---

# How to measure the Orbit-Volume?

**Topic ID**: 1742
**Date**: 2017-12-29
**URL**: https://discourse.slicer.org/t/how-to-measure-the-orbit-volume/1742

---

## Post #1 by @Eva-Maria (2017-12-29 21:39 UTC)

<p>Hi,</p>
<p>I’m new in using slicer 4.8.0.<br>
I’ve tried to use the slicer in order to calculate the orbit volume but I was not able to find the tool/path.<br>
Can somebody please help me?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2017-12-29 23:08 UTC)

<p>You can segment the orbit using Segment Editor module then use Segment Statistics module to get the volume.</p>

---

## Post #3 by @Eva-Maria (2018-01-01 21:11 UTC)

<p>Thank you a lot for the fast response!<br>
I’ve tried to use the Segment Editor  in order to select the region of interest using the Tools on each slice.<br>
But I’m wondering whether there is the possibility to automatically generate a model deformed to the shape of the Orbit?<br>
Thank you in advance for the support!</p>

---

## Post #4 by @lassoan (2018-01-01 23:13 UTC)

<p>I’m not sure what you mean by orbit (content of the orbital cavity, orbital bone, etc) and what imaging modality you are using, but in general you should be able to quickly segment structures by painting a small “seed” somewhere inside them then use “Grow from seeds” effect to expand the seeds to create a complete segmentation.</p>
<p>See detailed instructions in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials</a>. Whole heart segmentation video tutorial shows how to use “Grow from seeds” effect (you’ll need a left orbit, right orbit, and other segments).</p>

---
