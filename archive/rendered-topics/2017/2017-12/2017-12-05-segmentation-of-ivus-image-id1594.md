---
topic_id: 1594
title: "Segmentation Of Ivus Image"
date: 2017-12-05
url: https://discourse.slicer.org/t/1594
---

# segmentation of ivus image

**Topic ID**: 1594
**Date**: 2017-12-05
**URL**: https://discourse.slicer.org/t/segmentation-of-ivus-image/1594

---

## Post #1 by @Emily_BM (2017-12-05 13:29 UTC)

<p>can we use “3D slicer” for building 3d model from ivus data?<br>
what will be the appropriate segmentation approach  for that?</p>
<p>Operating system:64<br>
Slicer version:4.8<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-12-05 18:47 UTC)

<p>Slicer has lots of infrastructure that could be used for this, but you would need to do some custom scripting to generate 3D model.</p>
<p>Would you like to display a colored surface model?<br>
Do you have information on the 3D trajectory of the IVUS probe motion?</p>

---

## Post #3 by @Emily_BM (2017-12-06 07:55 UTC)

<p>i want a 3d model of artery with plaque in it(preferably colored)but i dont<br>
have information about 3D trajectory!!</p>

---

## Post #4 by @pieper (2017-12-06 12:52 UTC)

<p>Can you post a screenshot of what your ivus data looks like and (if possible) and example of what you’d like to see?</p>

---

## Post #5 by @lassoan (2017-12-06 14:58 UTC)

<p>To have a 3D model of the artery, you would need to know at least the vessel centerline in 3D. Do you have other imaging (CTA, MRA, …) where the vessel is visible in 3D?</p>

---
