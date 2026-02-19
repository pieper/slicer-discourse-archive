---
topic_id: 13546
title: "Cast Scalar Volume"
date: 2020-09-18
url: https://discourse.slicer.org/t/13546
---

# cast scalar volume

**Topic ID**: 13546
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/cast-scalar-volume/13546

---

## Post #1 by @jianyuan (2020-09-18 13:41 UTC)

<p>I faied in the segmentation of tumors with the growcuteffect. I cast PET images to ‘short’ type (using Cast Scalar Volume module). However, the regions of high intensity turned black in “shot” type, and it seems that 3D slicer could not differentiate these regions from the background. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fec3533f365d4498090389518493c1d45096631.png" alt="NO1" data-base62-sha1="97u9wjly06YPJlfIxNsSBNL755f" width="381" height="203"></p>

---

## Post #2 by @lassoan (2020-09-18 13:44 UTC)

<p>It seems that you image contains values that cannot be represented in <code>short</code> type. To resolve this, you can <a href="https://discourse.slicer.org/t/image-quantization-techniques/13420/2">rescale the image intensity</a> before casting to a different scalar type.</p>

---

## Post #3 by @jianyuan (2020-09-18 17:24 UTC)

<p>Thanks!  Is it possible to resolve this problem using 3D slicer？ I wonder how to rescale the image intensity using 3D slicer?</p>

---

## Post #4 by @lassoan (2020-09-18 18:34 UTC)

<p>Yes, see which modules you can use to rescale image intensity at the link in my previous post.</p>

---
