---
topic_id: 14649
title: "Display Image Mask Pair After Mask Correction"
date: 2020-11-16
url: https://discourse.slicer.org/t/14649
---

# Display image/mask pair after mask correction?

**Topic ID**: 14649
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/display-image-mask-pair-after-mask-correction/14649

---

## Post #1 by @Cody_Keller (2020-11-16 23:40 UTC)

<p>Operating system: Windows10 64-bit<br>
Slicer version: 4.11.0</p>
<p>Hello,</p>
<p>I’ve been working through some bugs in feature extraction with a data set of image/mask pairs that are pretty heterogenous in terms of size and file type. Developing code in Jupyter notebook with python 3.7.6.</p>
<p>Currently getting successful extraction on all my images, but results aren’t up to snuff on sanity checks. My best lead is to explore image/mask alignment as it occurs when correctMask is called, but as of yet have not been unable to figure out how.</p>
<p>I’d like to be able to display the image/mask after correctMask is executed. Any help to that end is greatly appreciated.</p>

---

## Post #2 by @JoostJM (2020-11-18 18:48 UTC)

<p>You can visualize the alignment of image and mask by loading them into 3D slicer, though this may not completely accurately display the corrected mask (as it does not accont for segmented voxels ‘lost’ when resampling to another spacing), it does show correct alignment, as it is also inside PyRadiomics.</p>
<p>Correction of the mask uses SimpleITK under the hood. (i.e. ResamleImageFilter with interpolator NearestNeighbor and the input image set as reference image).</p>
<p>Additionally, it may help to review the diagnostic features (part of the output by default). This provides information on the mask and image at various steps in pre-processing.</p>

---
