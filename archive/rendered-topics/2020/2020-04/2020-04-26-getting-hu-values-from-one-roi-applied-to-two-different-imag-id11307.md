---
topic_id: 11307
title: "Getting Hu Values From One Roi Applied To Two Different Imag"
date: 2020-04-26
url: https://discourse.slicer.org/t/11307
---

# Getting HU values from one ROI applied to two different images

**Topic ID**: 11307
**Date**: 2020-04-26
**URL**: https://discourse.slicer.org/t/getting-hu-values-from-one-roi-applied-to-two-different-images/11307

---

## Post #1 by @gmadevs (2020-04-26 17:21 UTC)

<p>Hi all, is there a way to extract ROI values as arrays by using the same ROI on different images?<br>
Suppose I want to register two CT scan in two different timepoints, I’d like to draw a ROI and then having the HU values as array with coordinates of image 1 and image 2. I read about the command <code>slicer.util.</code> <code>arrayFromVolume</code> but I’m not sure it’s the same case as mine.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-04-28 13:58 UTC)

<p>Be sure to resample the data to the same pixel space (e.g. using the Resample Image (BRAINS) module) before doing array-level access to the pixel data.</p>

---
