# Change number of scalers

**Topic ID**: 26422
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/change-number-of-scalers/26422

---

## Post #1 by @RCJOSHI (2022-11-24 14:21 UTC)

<p>I have *.nrrd images and has “Number of scaler” parameter (under the volume information tab in 3-d-slicer) has value 8. I want change this file to the *.nrrd file having “Number of scaler parameter” is equal to 1. Because it is creating the issue while executing those files having “number of scalers” greater than 1 to run on Pyradiomic platform.</p>

---

## Post #2 by @lassoan (2022-11-24 14:25 UTC)

<p>You can convert this 8-component (vector) image to a single-component (scalar) image using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/vectortoscalarvolume.html">Vector to scalar volume</a> module.</p>

---

## Post #4 by @RCJOSHI (2022-11-24 15:11 UTC)

<p>Thanks for the prompt response. My *.nrrd image is not of vector type. The volume type for given image is “MRMLMulti” having the “Number of scalars” is equal to 8. I need to convert this image to a scalar with “number of scalars” equal to 1</p>

---

## Post #5 by @lassoan (2022-11-25 06:22 UTC)

<p>You can either use MultiVolume module to copy the currently selected frame into a scalar volume, or load the volume as a “Volume Sequence” (you can choose how to load a node in the “Description” column in “Add data” window).</p>

---

## Post #6 by @RCJOSHI (2022-11-25 06:30 UTC)

<p>Thank you so much. It worked for me.</p>

---
