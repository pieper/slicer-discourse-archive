---
topic_id: 42369
title: "Sequence Browsing Loss Of Spatial Movement After Saving In S"
date: 2025-03-30
url: https://discourse.slicer.org/t/42369
---

# Sequence Browsing: Loss of Spatial Movement After Saving in Slicer

**Topic ID**: 42369
**Date**: 2025-03-30
**URL**: https://discourse.slicer.org/t/sequence-browsing-loss-of-spatial-movement-after-saving-in-slicer/42369

---

## Post #1 by @rcpr (2025-03-30 04:53 UTC)

<p>Hi everyone!<br>
First of all, I’d like to thank you for your availability!</p>
<p>I’m using fCal to receive ultrasound images from a frame grabber while simultaneously acquiring spatial information from the sensor attached to the probe (I’m using the Aurora motion tracking system). After performing the calibrations, I used the Plus Server to stream the <strong>TrackedVideoStream</strong> channel, where I sent <strong>Name=“Image”</strong> with <strong>EmbeddedTransformToFrame=“Tracker”</strong>.</p>
<p>To perform the reconstructions in Slicer, I recorded the frames over time using the Sequence Browsing module and then proceeded with the reconstruction. The problem is that when I save the sequence for later visualization, upon reloading it in Slicer, I can no longer see the frames moving spatially. I only get a static spatial frame, although the images are being updated. However, when I record the sequence in real-time and then click on the sequence visualization, it does move through the 3D space.</p>
<p>Am I doing something wrong?<br>
I would really appreciate any help!</p>

---

## Post #2 by @lassoan (2025-03-31 20:13 UTC)

<p>Can you share a sample data set (upload somewhere and post the link here)?</p>

---

## Post #3 by @rcpr (2025-04-01 17:19 UTC)

<p>Good afternoon! Thank you for your quick response!<br>
In the meantime, I managed to understand what my mistake was, but another question came up. Is it possible to define a 2D window to crop each frame individually, instead of using a 3D region of interest?<br>
This is because when I use the Crop Volume Sequence module, I end up defining a 3D region that captures areas that are not of interest, while also missing areas that should be included, as the frames are not static (since it is a freehand scan). Is there a way to achieve this? Something that would allow me to apply a crop directly to the image received from the Plus server, so I can then work with the region of interest only for the sequence recording?<br>
Thank you so much for your help!</p>

---
