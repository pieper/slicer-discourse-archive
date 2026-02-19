---
topic_id: 2888
title: "Labelmap Vs Segment Editor"
date: 2018-05-22
url: https://discourse.slicer.org/t/2888
---

# LabelMap vs Segment Editor

**Topic ID**: 2888
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/labelmap-vs-segment-editor/2888

---

## Post #1 by @cphillips (2018-05-22 19:05 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1</p>
<p>I have been using the Grow From Seeds effect (in the Segment Editor) to segment out an infarct from a T2W MRI and calculate its volume. I initially tried the GrowCut Effect option in the Label editor, but it only works with images of a “short” data type. When I casted my image to short, it resulted in a pixelated, poor quality image. I was wondering if there is any difference in accuracy in the two effects (both were implemented using the GrowCut algorithm, to my understanding).</p>

---

## Post #2 by @lassoan (2018-05-22 19:18 UTC)

<p>“GrowCut effect” in the legacy Editor module is a very old, unoptimized version of the algorithm used in “Grow from seeds” effect of Segment editor module. In most cases, same inputs both effects should generate the same output. If there is a difference then most likely “Grow from seeds” effect produces the correct result.</p>

---
