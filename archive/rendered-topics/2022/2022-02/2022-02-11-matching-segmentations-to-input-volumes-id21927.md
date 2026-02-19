---
topic_id: 21927
title: "Matching Segmentations To Input Volumes"
date: 2022-02-11
url: https://discourse.slicer.org/t/21927
---

# Matching segmentations to input volumes

**Topic ID**: 21927
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/matching-segmentations-to-input-volumes/21927

---

## Post #1 by @paullane (2022-02-11 22:01 UTC)

<p>Hi,</p>
<p>I am curious if there is a module to match segmentations to input volume images in order to train a neural network?<br>
I have converted DICOM to PNG and converted segmented images into labelmaps and numpy arrays. The arrangement of segmented masks are not in order of the original image data.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2022-02-11 22:09 UTC)

<aside class="quote no-group" data-username="paullane" data-post="1" data-topic="21927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c5a1d2/48.png" class="avatar"> paullane:</div>
<blockquote>
<p>I have converted DICOM to PNG and converted segmented images</p>
</blockquote>
</aside>
<p>That’s not a good operation because you loose the spatial reference system of the data. <a href="https://github.com/Project-MONAI/MONAILabel">MonaiLabel extension</a> in slicer allows you to train a segmentation model by simply providing the 3D images and the associated segmentations, all in Slicer format. No need to convert anything to anything.</p>
<p>It might be easier for you to start from there.</p>

---

## Post #3 by @paullane (2022-02-18 01:29 UTC)

<p>Thank you for your response and sorry for the late reply.<br>
I am not sure I am allowed to use the Preview Release version of 3D slicer for my project.<br>
Is there a way to work around this without using Monai?</p>
<p>Thanks</p>

---
