---
topic_id: 10735
title: "Resize Roi To Same Image Size"
date: 2020-03-18
url: https://discourse.slicer.org/t/10735
---

# Resize ROI to same image size

**Topic ID**: 10735
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/resize-roi-to-same-image-size/10735

---

## Post #1 by @trypag (2020-03-18 14:05 UTC)

<p>Hello,</p>
<p>I am in the process of making a head CT template, there is one thing I would like to do with Slicer, though I am not sure it’s even possible. The CT scan has a size of 512x512, I would like to apply a linear scaling so that the brain volume occupies a larger portion of the original image. I can manually decide which portion of the image is interesting.<br>
I was not able to find the solution in the transform module, is it possible ?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-18 14:27 UTC)

<p>You can use “Crop volume” module to choose an arbitrary portion of a volume and resample it at any resolution you choose.</p>

---

## Post #3 by @trypag (2020-03-18 15:49 UTC)

<p>Thank you !</p>
<p>I am adding a link to a video explaining how to crop : <a href="https://youtu.be/GGgP89uTOLo?t=179" rel="nofollow noopener">https://youtu.be/GGgP89uTOLo?t=179</a></p>

---
