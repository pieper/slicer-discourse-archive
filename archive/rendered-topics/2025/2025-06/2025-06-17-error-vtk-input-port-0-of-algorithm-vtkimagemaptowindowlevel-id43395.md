---
topic_id: 43395
title: "Error Vtk Input Port 0 Of Algorithm Vtkimagemaptowindowlevel"
date: 2025-06-17
url: https://discourse.slicer.org/t/43395
---

# Error: [VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (000001A807D0A830) has 0 connections but is not optional. [VTK] Input port 0 of algorithm vtkImageThreshold (000001A86BF0BB60) has 0 connections but is not optional.

**Topic ID**: 43395
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/error-vtk-input-port-0-of-algorithm-vtkimagemaptowindowlevelcolors-000001a807d0a830-has-0-connections-but-is-not-optional-vtk-input-port-0-of-algorithm-vtkimagethreshold-000001a86bf0bb60-has-0-connections-but-is-not-optional/43395

---

## Post #1 by @anpus (2025-06-17 16:52 UTC)

<p>Hi,</p>
<p>I am using 3D slicer (Slicer version 5.4.0.) for improving the image quality in real-time by integrating .h5 model.<br>
But I’m getting a lot of errors in the console.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (000001A807D0A830) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageThreshold (000001A86BF0BB60) has 0 connections but is not optional.</p>
<p>Has anybody encountered this error before?<br>
I hope you can help me, Thank you in adavance!.</p>

---

## Post #2 by @lassoan (2025-06-17 16:52 UTC)

<p>Probably in one of the slice views you selected to display an empty image.</p>

---

## Post #3 by @anpus (2025-06-17 17:08 UTC)

<p>Hi, thank you for the reply!.</p>
<p>yes, you are absolutely right-- I can see the “No Image” text in one of the slice views, so it seems like an empty image is selected. I’m not sure how to fix this.</p>
<p>I trained a DL model to remove noise and then tried to integrate it into 3D Slicer (v5.4.0) as a scripted module (similar to SegmentationUNet). My goal is to perform denoising in real-time.</p>
<p>Is there something I should check in my code to avoid this?</p>
<p>Thanks a lot in advance for your help!</p>

---
