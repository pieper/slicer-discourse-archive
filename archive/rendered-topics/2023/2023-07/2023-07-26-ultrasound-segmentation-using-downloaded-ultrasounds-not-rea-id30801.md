---
topic_id: 30801
title: "Ultrasound Segmentation Using Downloaded Ultrasounds Not Rea"
date: 2023-07-26
url: https://discourse.slicer.org/t/30801
---

# Ultrasound Segmentation Using Downloaded Ultrasounds (not real time)

**Topic ID**: 30801
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/ultrasound-segmentation-using-downloaded-ultrasounds-not-real-time/30801

---

## Post #1 by @jsarsam (2023-07-26 14:02 UTC)

<p>Hello! I am interested in reconstructing segmentations of echocardiograms using 3D slicer. I saw this video tutorial (<a href="https://www.youtube.com/watch?v=WyscpAee3vw" class="inline-onebox" rel="noopener nofollow ugc">Real-time ultrasound AI segmentation and volume reconstruction - YouTube</a>) about how to do this if the ultrasound is being captured in real time. However, would it be possible to achieve this offline, i.e. using a DICOM file loaded to my computer (instead of doing it in real time with PLUS connected to 3D slicer)?</p>
<p>Additionally, to construct segmentations of the ultrasound/echo images, does the ultrasound image data have to be in the form of a sweep? Or would it also work if it was a clip of a beating heart?</p>
<p>Thanks so much!</p>

---

## Post #2 by @ungi (2023-07-27 21:58 UTC)

<p>Hi, if you want to reconstruct a series of 2D ultrasound images into a 3D volume, you will need to know where each frame is in space. In the example video, there is a position tracker attached to the ultrasound probe. Additionally in the heart, you cannot use frames at random time points, because the heart periodically changes its shape. You would also need to match images to certain phases of the heart cycle. If you need 3D heart images, I think it’s simpler to just buy a 3D ultrasound probe to avoid both challenges, tracking and ECG gating.</p>

---

## Post #3 by @Blackmasc (2025-02-17 02:29 UTC)

<p>I’m working on ultrasound image segmentation and was wondering if you have any datasets with pre-sliced ultrasound images that I could use. If so, I’d really appreciate any guidance on how to access them.</p>
<p>Thanks in advance for your help!</p>

---
