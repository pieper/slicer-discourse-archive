---
topic_id: 3389
title: "Import Mhd Data"
date: 2018-07-05
url: https://discourse.slicer.org/t/3389
---

# Import mhd data

**Topic ID**: 3389
**Date**: 2018-07-05
**URL**: https://discourse.slicer.org/t/import-mhd-data/3389

---

## Post #1 by @weianlin (2018-07-05 16:34 UTC)

<p>Hi, I’m new to 3D Slicer. I’d like to know how the mhd metadata would affect the image rendered in 3D Slicer.  To my knowledge, 3D Slicer uses RAS coordinate system. And in mhd file, we can specify <strong>AnatomicalOrientation</strong> and <strong>TransformMatrix</strong> to define relation between (i, j, k) and RAS coordinate system. But I’m not so sure about how they interact with each other. My questions include:</p>
<p>(1) Does the <strong>TransformationMatrix</strong> specify rotation between (i,j,k) and the RAS coordinate?<br>
(2) What’s the effect of different <strong>AnatomicalOrientation</strong> in 3D Slicer? In an mhd file, I’ve manually switched between LPS, RAI, RAS for the same raw data, but the rendered image, and the IJKtoRAS Direction Matrix remains the same.</p>

---

## Post #2 by @lassoan (2018-07-05 17:54 UTC)

<p>Slicer uses ITK image reader to load metaimage files. This reader intentionally ignores AnatomicalOrientation (I’ve raised this question before to ITK developers and Kitware and they confirmed that this is not a bug and they will not change the behavior) and considers the image to be in LPS coordinate system. Slicer converts the image to RAS when it is loaded into the scene, and Slicer converts it back to LPS when it is saved to file.</p>
<p>If you want to specify coordinate system using anatomical axes then you need to use nrrd file format.</p>
<aside class="quote no-group" data-username="weianlin" data-post="1" data-topic="3389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/9d8465/48.png" class="avatar"> weianlin:</div>
<blockquote>
<p>Does the <strong>TransformationMatrix</strong> specify rotation between (i,j,k) and the RAS coordinate?</p>
</blockquote>
</aside>
<p>Yes.</p>

---
