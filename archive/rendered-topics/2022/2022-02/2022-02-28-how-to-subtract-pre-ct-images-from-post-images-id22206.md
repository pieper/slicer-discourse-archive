---
topic_id: 22206
title: "How To Subtract Pre Ct Images From Post Images"
date: 2022-02-28
url: https://discourse.slicer.org/t/22206
---

# How to subtract pre CT images from post images

**Topic ID**: 22206
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/how-to-subtract-pre-ct-images-from-post-images/22206

---

## Post #1 by @Kawtar_Lakrad (2022-02-28 08:13 UTC)

<p>Operating system: windows 11<br>
Slicer version: 4.13<br>
Expected behavior: no idea<br>
Actual behavior: no idea</p>
<p>I am trying to subtract pre CTs from post CTs, and I was wondering if it is feasible using 3D slicer?<br>
Thank you so much.</p>

---

## Post #2 by @pieper (2022-02-28 21:04 UTC)

<p>It depends on what the scans are pre- and post- of.  Contrast?  Operations?</p>
<p>If it’s same subject in a part of the body that doesn’t deform (e.g. the head or a bone) you can typically register and just subtract (there’s a module in slicer to subtract volumes).  Soft body parts are very hard to co-register well enough for subtraction to work.</p>

---

## Post #3 by @Kawtar_Lakrad (2022-03-03 20:05 UTC)

<p>Okey, I am going to try this.<br>
Thank you so much</p>

---
