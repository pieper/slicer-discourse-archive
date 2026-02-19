---
topic_id: 34526
title: "3D Slicer For Us Segmentation"
date: 2024-02-25
url: https://discourse.slicer.org/t/34526
---

# 3D slicer for US segmentation

**Topic ID**: 34526
**Date**: 2024-02-25
**URL**: https://discourse.slicer.org/t/3d-slicer-for-us-segmentation/34526

---

## Post #1 by @eden_altman (2024-02-25 14:13 UTC)

<p>Hi everyone,</p>
<p>New here and would like to know if the 3D slicer is useful for segmentation of ultrasound images?<br>
Im trying to segment ultrasound images of the thigh to 3 different layers- fat, muscle and bone.</p>

---

## Post #2 by @lassoan (2024-02-25 14:16 UTC)

<p>3D Slicer is frequently used for ultrasound segmentation training and real-time segmentation of live ultrasound.</p>
<p><a class="mention" href="/u/ungi">@ungi</a> could you provide a good link to get started?</p>

---

## Post #3 by @ungi (2024-02-25 17:39 UTC)

<p>I think segmentation itself is best done outside of Slicer. I used to install TensorFlow and PyTorch in Slicer’s python environment and run segmentation in Slicer, but then it seemed better to run segmentation in everyone’s favorite AI environment, and communicate with Slicer via OpenIGTLink. You can stream the ultrasound images from Slicer or PLUS to an Anaconda environment and receive the segmentations back in Slicer (or whatever your application is) nearly real time.</p>
<p>I still use Slicer for manual segmentations, for generating training data. Like this: <a href="https://youtu.be/zlrUFaP9q1w?si=4UgkGDA9U_Jpyz5S" rel="noopener nofollow ugc">https://youtu.be/zlrUFaP9q1w?si=4UgkGDA9U_Jpyz5S</a></p>
<p>And Slicer is great for visualization, 3D volume reconstruction (if you track your ultrasound images), and providing a custom user interface if necessary for clinical users.</p>
<p>For ultrasound segmentation AI training, I’m using this code (under development): <a href="https://github.com/SlicerIGT/aigt/tree/master/UltrasoundSegmentation" rel="noopener nofollow ugc">aigt/UltrasoundSegmentation at master · SlicerIGT/aigt (github.com)</a></p>

---
