---
topic_id: 43413
title: "Creating A New Extension Module For Real Time Denoising Inte"
date: 2025-06-18
url: https://discourse.slicer.org/t/43413
---

# Creating a new extension module for real-time denoising integrating trained model (.h5 or .pth Model) into a custom module

**Topic ID**: 43413
**Date**: 2025-06-18
**URL**: https://discourse.slicer.org/t/creating-a-new-extension-module-for-real-time-denoising-integrating-trained-model-h5-or-pth-model-into-a-custom-module/43413

---

## Post #1 by @anpus (2025-06-18 18:09 UTC)

<p>I am currently working on integrating a “real-time denoising” into “3D Slicer (v 5.4.0)” by creating a “new extension module”. I have a trained “TensorFlow model saved in ‘.h5’ format” that I would like to deploy within a custom module to enhance image quality as images are streamed into the software.</p>
<p>I followed the SegmentationUNet scripted module as a reference and modified the code to implement a denoising module using my trained model. However, I encountered several errors in the console, the output volume displays as ‘No Image,’ and the output volume data streaming stops.</p>
<p>If there are any related “GitHub repositories, or documentation references” for my issue, I would greatly appreciate it.</p>

---
