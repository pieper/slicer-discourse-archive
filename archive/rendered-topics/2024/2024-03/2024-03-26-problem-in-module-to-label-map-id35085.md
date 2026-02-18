# Problem in module to label map

**Topic ID**: 35085
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/problem-in-module-to-label-map/35085

---

## Post #1 by @Pranali (2024-03-26 04:50 UTC)

<p>Hello, I have a fiber bundle saved as .vtk, I want it to convert to label volume. The model to label the map takes input as a model and an input volume (what is this? How do you give the volume that specifies the geometry of the model?). If someone knows, please help.</p>
<p>Thank You</p>

---

## Post #2 by @pieper (2024-03-26 19:44 UTC)

<p>Usually you will have a reference MR scan that you want to use as the sampling grid and you use that as the input volume.  The output labelmap volume is sampled in that space.  You could start with any volume and then use the CropVolume module if you want to specify the exact geometry.  There’s also an ImageMaker extension if you want to control it manually.</p>

---

## Post #3 by @Pranali (2024-04-03 04:37 UTC)

<p>Hello, I tried using reference volume, but it gives an empty volume. I used dipy library to slove this! Thanks</p>

---
