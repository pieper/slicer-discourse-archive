# multimodal radiomics

**Topic ID**: 13908
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/multimodal-radiomics/13908

---

## Post #1 by @icetin (2020-10-06 20:50 UTC)

<p>Hi!<br>
Is it possible to extract radiomics features on pairs of images using pyradiomics? i.e. features based on the joint histogram, or a way to manage the data so pyradiomics knows that they are two views of the same thing, as opposed to two independent images?<br>
Best,</p>

---

## Post #2 by @JoostJM (2020-10-10 13:44 UTC)

<p>Not directly, no. The problem is that the link between the two images can be defined in multiple ways, many of which have no unit (e.g. comparing T2W vs T1W images in MRI), whereas others do (e.g. time series in dynamic contrast enhanced images, b-values in DWI imaging).</p>
<p>However, features can be extracted from multiple input images using the same mask (be sure to enable <code>correctMask</code> when not resampling), in which case each feature has a value for each input image, which can be combined into a single predictive model. This is currently how I use multimodal input in radiomics research.</p>

---
