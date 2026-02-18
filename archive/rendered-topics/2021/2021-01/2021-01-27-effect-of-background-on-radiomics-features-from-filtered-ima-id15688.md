# Effect of background on radiomics features from filtered images

**Topic ID**: 15688
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/effect-of-background-on-radiomics-features-from-filtered-images/15688

---

## Post #1 by @mcastro (2021-01-27 03:46 UTC)

<p>I am studying the stability of radiomics features on a segmented whole organ at different time points.</p>
<p>When masking the image using Mask Volume in Segment Editor, the user can set the background to any value, say 0. Feature values are consistent among time points with a low variability.</p>
<p>However, if a different value for the background is used, the radiomics features computed from filtered images (LoGs, Gradient, Logarithm, Square, Square Root, and Wavelets) are also different. This does not happen with the original image and if the Exponential is used (?).</p>
<p>I am not normalizing the image. I understand that normalization uses all voxels from the image, not only the VOI (mask), so the feature values depend on the background intensity, even for the original (unfiltered) image. But this is not my case.</p>
<p>LoG and gradient uses information slightly beyond the mask boundary, so there should be some minor dependence on the background intensity.</p>
<p>But this is not the case of Square or Square Root, for example. I understand that the features are computed only within the VOI (mask). Is that correct?</p>
<p>Am I missing anything?</p>
<p>Thanks!</p>

---

## Post #2 by @JoostJM (2021-03-09 12:46 UTC)

<p>No entirely correct. The only addition I have is that Wavelet and LBP (in addition to LoG, Gradient) also use voxels outside the boundary of the mask.</p>
<p>Are you using any other form of pre-processing (e.g. interpolation)?</p>

---
