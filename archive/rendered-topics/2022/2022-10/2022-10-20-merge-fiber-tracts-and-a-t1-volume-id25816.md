---
topic_id: 25816
title: "Merge Fiber Tracts And A T1 Volume"
date: 2022-10-20
url: https://discourse.slicer.org/t/25816
---

# Merge fiber tracts and a T1 volume

**Topic ID**: 25816
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/merge-fiber-tracts-and-a-t1-volume/25816

---

## Post #1 by @ferru (2022-10-20 20:42 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 5.02<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, I have fiber tracts from WMA.  I want to merge two of them with the anatomical T1 volume and save as DICOM to export to a Radiotherapy planning software.<br>
Is it possible to do that?</p>
<p>Thanks for advance!</p>

---

## Post #2 by @pieper (2022-10-20 20:48 UTC)

<p>Can you explain what you mean by merge here?  Do you mean spatially register or you you mean make a blended image that has both images?  What do you expect to see in the RT software?</p>

---

## Post #3 by @ferru (2022-10-20 21:24 UTC)

<p>Hi Steve, thanks for your answer.<br>
Yes, I want to make a blended image (T1+fiber tracts) with the fiber tract as binary mask.<br>
The aim is the integration of fiber bundles as critical structure into the planning system.</p>
<p>Thanks!</p>

---

## Post #4 by @pieper (2022-10-20 21:54 UTC)

<p>Thanks for clarifying.  I don’t know of an easy way to do that with the UI, so some amount of scripting would be needed.  Perhaps the most versatile method would be to show the tract intersections with the T1 in the slice views and then export a screen capture of those to dicom.  You can get the exact coordinates of the slices in order to make an accurate dicom header with some calculation and scripting.</p>

---
