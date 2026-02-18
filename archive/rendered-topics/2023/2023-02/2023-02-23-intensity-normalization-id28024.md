# Intensity normalization

**Topic ID**: 28024
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/intensity-normalization/28024

---

## Post #1 by @Floren (2023-02-23 21:03 UTC)

<p>Hello, everyone!</p>
<p>I am working with prostate adc maps and trying to measure adc value for prostate tumors in order to demonstrate that there is a correlation between adc value and Gleason score.</p>
<p>I understood that i must first normalize the intensity of the images. The problem is that i don’t really know how to do that.</p>
<p>I appreciate any information you may have.</p>

---

## Post #2 by @lassoan (2023-03-02 06:24 UTC)

<p>I’m not sure what image intensity normalization you mean. Do you mean image intensity inhomogeneity (bias) correction due to using an endorectal coil? You can use “N4ITK MRI Bias correction” module for that.</p>

---
