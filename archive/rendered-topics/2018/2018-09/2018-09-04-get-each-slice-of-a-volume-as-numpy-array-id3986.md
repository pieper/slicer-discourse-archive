---
topic_id: 3986
title: "Get Each Slice Of A Volume As Numpy Array"
date: 2018-09-04
url: https://discourse.slicer.org/t/3986
---

# Get each slice of a volume as numpy array

**Topic ID**: 3986
**Date**: 2018-09-04
**URL**: https://discourse.slicer.org/t/get-each-slice-of-a-volume-as-numpy-array/3986

---

## Post #1 by @Saima (2018-09-04 05:44 UTC)

<p>Hi Andras,<br>
Would you please tell me how to split the volume into slices after having volume into numpy array?</p>
<p>What I need to do is to apply clustering FCM algorithm on volume to get classified volume. For which I am thinking in this way.<br>
Get the volume<br>
Split it into slices<br>
convert each slice into its respective numpy array<br>
passing numpy array of a slice to algorithm<br>
Getting the updated numpy array<br>
converting numpy back to slice of volume<br>
Then collectivly combining all the slices into volume</p>
<p>Thank you</p>
<p>Looking forward for your reply</p>

---

## Post #2 by @lassoan (2018-09-04 18:43 UTC)

<p>You can easily get a slice of a volume by standard numpy indexing of arrays. Here is an example: <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02">https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02</a></p>
<p>However, I would recommend to segment in 3D rather than arbitrarily splitting the volume to 2D pieces and re-assembling it.</p>

---

## Post #3 by @Saima (2018-09-05 02:28 UTC)

<p>Hi Andras,<br>
Thank you for suggesting. Please tell where should I start from if I want to do 3D segmentation.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @lassoan (2018-09-05 03:32 UTC)

<p>What would you like to segment? On what imaging modality? For what clinical purpose?</p>

---

## Post #5 by @Saima (2018-09-05 04:26 UTC)

<p>Hi,<br>
want to segment three parts brain, ventricles and tumor, MRI. automating the segmentation process and then using it for brain deformation calculation.</p>

---
