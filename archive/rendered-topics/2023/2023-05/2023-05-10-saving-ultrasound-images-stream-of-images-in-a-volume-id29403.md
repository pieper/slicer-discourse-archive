---
topic_id: 29403
title: "Saving Ultrasound Images Stream Of Images In A Volume"
date: 2023-05-10
url: https://discourse.slicer.org/t/29403
---

# Saving ultrasound images (stream of images) in a volume

**Topic ID**: 29403
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/saving-ultrasound-images-stream-of-images-in-a-volume/29403

---

## Post #1 by @Mary_89 (2023-05-10 16:04 UTC)

<p>Hi everyone,</p>
<p>I have a question regarding how to save a stream of images that I receive in 3D Slicer in a volume. I want to use this volume of images to navigate through each slice and manually segment my images. I am sending the Ultrasound images and position data by OpenIGTLink to the slicer and I can reconstruct the 3D volume from the stream. The problem is that the reconstructed volume does not have the original images and it just includes slices that come from reconstruction. However, I need to annotate the original US images. I have checked the Sequence module in 3D slicer and it seems it is not what I am looking for. Because I would like to save all the slices that I receive without manually initiating the start and stop time and changing the sampling rate.</p>
<p>I am new to 3D Slicer, so any help would be appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @ungi (2023-05-12 21:38 UTC)

<p>Hi Mary,</p>
<p>Sequences is the right module to save US images in real time as they arrive in Slicer through OpenIGTLink. Sequences allows you to save and load all data with the Slicer scene. If by annotations you mean segmentation, then I recommend that you check out this module: <a href="https://github.com/SlicerIGT/aigt/tree/master/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation" class="inline-onebox" rel="noopener nofollow ugc">aigt/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation at master · SlicerIGT/aigt · GitHub</a><br>
There is an earlier version of the module in this video: <a href="https://youtu.be/zlrUFaP9q1w" class="inline-onebox" rel="noopener nofollow ugc">Fast ultrasound segmentation for generating AI training data - YouTube</a><br>
You need to create a new sequence browser and save the segmentations along with the original ultrasound images. Single Slice Segmentation just makes it more convenient and also provides export function to numpy array files.<br>
Alternatively, you could convert your data into a 3D volume so the 3rd dimension is time, but it’s better to use Sequences for time series data.</p>
<p>I hope this helps,<br>
Tamas</p>

---

## Post #3 by @Mary_89 (2023-05-15 04:18 UTC)

<p>Hi Tamas,</p>
<p>Thank you so much for your explanation. I have just tested the sequences module as you explained and it is what I needed.</p>
<p>Best,<br>
Mary</p>

---
