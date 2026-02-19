---
topic_id: 27771
title: "Generate 360 Panoramic View From Cbct Dicom Images"
date: 2023-02-11
url: https://discourse.slicer.org/t/27771
---

# Generate 360 Panoramic View from CBCT Dicom Images

**Topic ID**: 27771
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/generate-360-panoramic-view-from-cbct-dicom-images/27771

---

## Post #1 by @NX_Dev (2023-02-11 13:57 UTC)

<p>I have 288 dicom images of cbct series, I have generated axial, saggital, coronal and also 3d rendering view from these images, the last thing I want to generate is the 360 panoramic view. I am unable to generate it in python.</p>
<p>Please Help…</p>

---

## Post #2 by @lassoan (2023-02-11 20:05 UTC)

<p>This should be no problem (takes very little Python scripting), as long as you have the dental arch (curve connecting all the teeth) for each image. Do you have these curves?</p>

---

## Post #3 by @NX_Dev (2023-02-13 09:19 UTC)

<p>No, I do not have these curves, can you please guide me how can I have dental arch curve for each image.</p>
<p>I only have dicom series of cbct dataset.</p>

---

## Post #4 by @NX_Dev (2023-02-14 12:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> can you please guide me about the dental arch curve for cbct dicom images?</p>

---

## Post #5 by @lassoan (2023-04-14 01:53 UTC)

<p>The simplest is to draw the curve manually. However, it would probably not too hard to train a neural network to do it automatically. Perhaps there are already trained networks that someone shared publicly. If not, then you can train one yourself.</p>

---

## Post #6 by @Mohamed_Hamdy (2024-07-10 17:15 UTC)

<p>please in a simple way for a beginner how to draw the curve mannually</p>

---

## Post #7 by @lassoan (2024-08-03 21:43 UTC)

<p>The module uses an open curve as input that you can draw by: switching to the Markups module, creating a new curve, and then clicking on the slice or 3D views.</p>

---
