---
topic_id: 14046
title: "Volume Representation Without Noise And Garbage"
date: 2020-10-14
url: https://discourse.slicer.org/t/14046
---

# Volume representation without noise and garbage

**Topic ID**: 14046
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/volume-representation-without-noise-and-garbage/14046

---

## Post #1 by @a10227 (2020-10-14 22:52 UTC)

<p>Good day,<br>
I have dicom images and when I render them I see a 3D model without any noise, but the thing is, it is only because of the visualization presets, when I change some values on the “scalar opacity maping” widget, some noise appears. My goal is to have images from that a 3D model without any noise can be created, no visualization presets should be applied.</p>
<p>Could you please tell me, is it possible to export the model that I see in the “Volume rendering” tab to another dicom /3D image so that this  3D image will produce a clean model without any visualization presets?</p>

---

## Post #2 by @JanWitowski (2020-10-14 23:22 UTC)

<p>You can’t export volume rendering as a 3D mesh, this visualization method does not create a model. Please refer <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/">to other topics</a> for more details.</p>
<p>You are most likely looking for surface rendering: you would need to perform segmentation (Segment Editor/Segmentation modules) on your loaded DICOM images. Then you can clean it up with available tools (brushes, scissors, smoothing etc.) to your liking and export as a 3D mesh.</p>

---

## Post #3 by @a10227 (2020-10-15 10:22 UTC)

<p>Unfortunately this solution is not for my case because my model can’t be re-segmented, it takes a long time. So I need to somehow find a way to export the clean model or to do something else. Thanks for the reply anyway.</p>

---
