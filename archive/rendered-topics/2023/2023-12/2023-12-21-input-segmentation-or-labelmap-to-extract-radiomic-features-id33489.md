---
topic_id: 33489
title: "Input Segmentation Or Labelmap To Extract Radiomic Features"
date: 2023-12-21
url: https://discourse.slicer.org/t/33489
---

# Input segmentation or labelmap to extract radiomic features through 3D slicer

**Topic ID**: 33489
**Date**: 2023-12-21
**URL**: https://discourse.slicer.org/t/input-segmentation-or-labelmap-to-extract-radiomic-features-through-3d-slicer/33489

---

## Post #1 by @dazuidadatu (2023-12-21 14:09 UTC)

<p>Hi:<br>
I used the Radiomics in 3D slicer to extract radiomic features. When I write the input region, I don`t know choose the segmentation or the labelmap, and the their extract results of radiomics features were different. So, which region shoud I input?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cab692ad9e2c4715dad6f311c265cb4e2d0eb2bc.jpeg" data-download-href="/uploads/short-url/sVhBO3JkFTa1l58namqLxJ1BEte.jpeg?dl=1" title="微信图片_20231221195748" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cab692ad9e2c4715dad6f311c265cb4e2d0eb2bc_2_571x500.jpeg" alt="微信图片_20231221195748" data-base62-sha1="sVhBO3JkFTa1l58namqLxJ1BEte" width="571" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cab692ad9e2c4715dad6f311c265cb4e2d0eb2bc_2_571x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cab692ad9e2c4715dad6f311c265cb4e2d0eb2bc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cab692ad9e2c4715dad6f311c265cb4e2d0eb2bc.jpeg 2x" data-dominant-color="C8CAC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20231221195748</span><span class="informations">742×649 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-01-06 22:38 UTC)

<p>The radiomics results should be identical if the lablemap is the same as the segmentation.  I just tried that with the latest nightly build and radiomics extension and the tables matched.</p>

---
