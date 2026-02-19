---
topic_id: 4059
title: "How To Correlate Mra Images With Mip Reconstructed Images"
date: 2018-09-11
url: https://discourse.slicer.org/t/4059
---

# How to correlate MRA images with MIP reconstructed images?

**Topic ID**: 4059
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/how-to-correlate-mra-images-with-mip-reconstructed-images/4059

---

## Post #1 by @pfz_biomind (2018-09-11 04:46 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I have MRA images of brains, and also have MIP reconstructed images based on the MRA images. My question is how to correlate these two sets of images in 3D slicer. Thanks a lot!</p>

---

## Post #2 by @pieper (2018-09-11 12:48 UTC)

<p>Probably you cannot do that because the MIPs are likely stored as secondary capture and don’t contain any geometry information.  You can generate MIPs inside Slicer as an option in the Volume Rendering module.</p>

---

## Post #3 by @lassoan (2018-09-11 13:09 UTC)

<p>What is the clinical use case? Registration of pre-procedural MRI with X-ray/fluro images?</p>
<p>Such 2D/3D registration may be feasible using ITK (bundled with Slicer) or Elastix (available in SlicerElastix extension) registration libraries, but you need to figure out how to set them up. For that, probably the best is to write on the ITK forum or Elastix mailing list.</p>

---
