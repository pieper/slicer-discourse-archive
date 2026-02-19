---
topic_id: 5816
title: "Noise Reduction In Cone Beam Ct Image"
date: 2019-02-18
url: https://discourse.slicer.org/t/5816
---

# Noise reduction in cone-beam CT image

**Topic ID**: 5816
**Date**: 2019-02-18
**URL**: https://discourse.slicer.org/t/noise-reduction-in-cone-beam-ct-image/5816

---

## Post #1 by @VincentYu (2019-02-18 08:41 UTC)

<p>Hi everyone.</p>
<p>We are trying to segment cranial-facial bone in cone-beam CT (CBCT) image, but the low SNR ratio nature of cone-beam CT makes it hard to determine a threshold.</p>
<p>We notice that “filtering” may be possible answer, but there are too many filters in 3D Slicer to try them all. Hoping someone has experience in this topic could give us some hints.</p>
<p>Any workaround to improve the segmentation quality of cranial-facial bone in cone-beam CT is appreciated as well.</p>

---

## Post #2 by @pieper (2019-02-18 16:54 UTC)

<p>Hi <a class="mention" href="/u/vincentyu">@VincentYu</a> - you can probably find some good literature on this topic and then match that to the filters available in Slicer (e.g. through SimpleFilters or elsewhere).  If you want to experiment, I think a non-linear filter like gradient anisotropic diffusion would be a good place to start.</p>

---

## Post #3 by @VincentYu (2019-02-20 09:29 UTC)

<p>Thank you. I’ll try gradient anisotropic diffusion first !</p>

---
