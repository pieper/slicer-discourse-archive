# Slope and intercept for pixel intensity MRI

**Topic ID**: 37400
**Date**: 2024-07-16
**URL**: https://discourse.slicer.org/t/slope-and-intercept-for-pixel-intensity-mri/37400

---

## Post #1 by @IrisM (2024-07-16 14:05 UTC)

<p>I want to use 3D slicer to extract first order features with the radiomics module from RTstructs of MRI images. However, I want all the pixel intensities from my MR image to be adapted first by a certain slope and intercept before I extract the features. If this is possible in 3D slicer, how would I be able to do this?<br>
Thank you in advance!</p>

---

## Post #2 by @pieper (2024-07-17 15:42 UTC)

<p>You can just access the pixels as a numpy array and manipulate them as you see fit before running radiomics.</p>

---
