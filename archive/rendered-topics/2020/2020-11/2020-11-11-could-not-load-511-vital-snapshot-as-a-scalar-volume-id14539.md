---
topic_id: 14539
title: "Could Not Load 511 Vital Snapshot As A Scalar Volume"
date: 2020-11-11
url: https://discourse.slicer.org/t/14539
---

# Could not load: 511: Vital Snapshot as a Scalar Volume

**Topic ID**: 14539
**Date**: 2020-11-11
**URL**: https://discourse.slicer.org/t/could-not-load-511-vital-snapshot-as-a-scalar-volume/14539

---

## Post #1 by @Rocha_Low (2020-11-11 03:19 UTC)

<p>Hi, I’m curious and working on Slice. Can someone help me with this error. It’s a color image, can you give me the steps to correct this error?</p>
<p>[image]</p>

---

## Post #2 by @lassoan (2020-11-11 15:50 UTC)

<p>Most likely this is just a screenshot, a 2D image, which is not usable for much. What do you expect the image to contain and what would you like to use it for?</p>
<p>Anyway, you can probably get the image loaded by trying the suggestions described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #3 by @Rocha_Low (2020-11-12 03:08 UTC)

<p>Lasso, I actually have a 3D of a carotid aorta from a friend’s heart and I wanted to print it out as a 3D print job. I speak of Brazil and this part of impressions is still a bit difficult. I would love to see the steps as I try to fix this flaw, I will read this link. Thank you, for helping me I will be reading this article now!</p>

---

## Post #4 by @lassoan (2020-11-12 06:21 UTC)

<p>Most likely the imaging study contains a few other series, one of them should be a 3D CT or CBCT that Slicer should be able to load.</p>

---

## Post #5 by @lassoan (2020-11-12 14:49 UTC)

<p>We checked the image headers and the files contain 2D screenshots with a small amount of additional private data that is not likely to contain any 3D information. No 3D geometry can be extracted from these images using standard DICOM compliant software.</p>

---

## Post #6 by @Rocha_Low (2020-11-12 16:44 UTC)

<p>hey, got it, i’ll see if he can give me these Dicom patterns. But the media I have is 2.5GB now that you gave me a tip I will look for if it is not mixed in the folders. Thank you Lasso, thank you very much friend.</p>
<p>[image]</p>

---

## Post #7 by @lassoan (2020-11-13 19:51 UTC)

<p>You can switch to DICOM module and drag-and-drop the top-level folder into the application screen. Then Slicer will automatically scan for all the DICOM files in the folder hierarchy and provide a list of what can be loaded.</p>

---
