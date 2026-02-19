---
topic_id: 20374
title: "Discrepancy Between Segmentation Threshold And First Order R"
date: 2021-10-26
url: https://discourse.slicer.org/t/20374
---

# Discrepancy between segmentation threshold and first order radiomics

**Topic ID**: 20374
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/discrepancy-between-segmentation-threshold-and-first-order-radiomics/20374

---

## Post #1 by @Fabio_Nunes (2021-10-26 22:58 UTC)

<p>Hello,</p>
<p>Thanks to the advice of Mr. <a href="https://discourse.slicer.org/u/lassoan">Andras Lasso</a>, I’ve been able to segment the pericardium of the heart (using the Surface Cut option from Slicer). I’ve then applied a threshold to only select the fatty tissue (HU -150 to -50) and it is corretly identified as green pixels on the attached image.<br>
I’ve also checked that this segmentation was correct looking at the label statistics. However, once I run the radiomics on this segment, I noticed that the first order minimum was -346 and the maximum was 73 (outside the range of my initial threshold).</p>
<p>Is this normal? What could cause this difference?<br>
Thank you<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ec4f619014f322b28b706d55d6b88e1e674de19.jpeg" data-download-href="/uploads/short-url/6FJWYSjNh70TH8Uc6SS9g8IU4zf.jpeg?dl=1" title="Imagem2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ec4f619014f322b28b706d55d6b88e1e674de19_2_690x276.jpeg" alt="Imagem2" data-base62-sha1="6FJWYSjNh70TH8Uc6SS9g8IU4zf" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ec4f619014f322b28b706d55d6b88e1e674de19_2_690x276.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ec4f619014f322b28b706d55d6b88e1e674de19_2_1035x414.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ec4f619014f322b28b706d55d6b88e1e674de19_2_1380x552.jpeg 2x" data-dominant-color="414449"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Imagem2</span><span class="informations">1920×768 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Fabio_Nunes (2021-10-26 23:43 UTC)

<p>Perhaps I’ve found the solution.<br>
I’ve been playing with the options and I’ve noticed that:</p>
<ul>
<li>when I resample with resampled voxel size 2,2,2 → the result is what is seen above</li>
<li>when I do not resample → the first order minimum and maximum are exactly -150 and -50</li>
</ul>

---

## Post #3 by @JoostJM (2022-01-11 12:17 UTC)

<p>Sounds like the issue indeed. A potential fix is enabling the resegmentationRange in PyRadiomcs this excludes voxels outside the specified range and works like thresholding, but is applied after resampling.</p>

---
