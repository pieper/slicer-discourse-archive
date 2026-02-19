---
topic_id: 22933
title: "Reproducibility Of Radiomics Results With Pyradiomics And Pa"
date: 2022-04-13
url: https://discourse.slicer.org/t/22933
---

# Reproducibility of Radiomics Results with Pyradiomics and Parenchymal Analysis

**Topic ID**: 22933
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/reproducibility-of-radiomics-results-with-pyradiomics-and-parenchymal-analysis/22933

---

## Post #1 by @chuawm (2022-04-13 12:03 UTC)

<p>Hi there,</p>
<p>I am trying to see if the Radiomics module analysis for the lung segmentation I performed using CIP is consistent with that derived from Parenchymal Analysis. This is partly because the Parenchymal Analysis is no longer available on the later versions of 3D Slicer. Thus far, most of the parameters are the same but I keep getting different values for kurtosis. Just wondering what went wrong?</p>
<p>Here is an example<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ede23bd8693ac90e927eca627902df59d6f73ec1.jpeg" data-download-href="/uploads/short-url/xWpRzEQrHOVenggKFTX9JcOqCU9.jpeg?dl=1" title="segmented example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ede23bd8693ac90e927eca627902df59d6f73ec1_2_575x500.jpeg" alt="segmented example" data-base62-sha1="xWpRzEQrHOVenggKFTX9JcOqCU9" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ede23bd8693ac90e927eca627902df59d6f73ec1_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ede23bd8693ac90e927eca627902df59d6f73ec1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ede23bd8693ac90e927eca627902df59d6f73ec1.jpeg 2x" data-dominant-color="625E58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmented example</span><span class="informations">775×673 77.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbb5d82906776dee2ff1ef2907542379166c875e.jpeg" data-download-href="/uploads/short-url/zUJrA2WwQ8ZX7XYNTuypQxM0NGe.jpeg?dl=1" title="radiomics sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbb5d82906776dee2ff1ef2907542379166c875e_2_558x500.jpeg" alt="radiomics sample" data-base62-sha1="zUJrA2WwQ8ZX7XYNTuypQxM0NGe" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbb5d82906776dee2ff1ef2907542379166c875e_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbb5d82906776dee2ff1ef2907542379166c875e_2_837x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbb5d82906776dee2ff1ef2907542379166c875e_2_1116x1000.jpeg 2x" data-dominant-color="F5F5F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">radiomics sample</span><span class="informations">1462×1308 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d1c595b6b2741a15245ff4a037f4bc47b844fd2.jpeg" data-download-href="/uploads/short-url/fzeMtoBfoiiTCLoFlIXotzeK2qK.jpeg?dl=1" title="parenchymal analysis sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d1c595b6b2741a15245ff4a037f4bc47b844fd2_2_690x177.jpeg" alt="parenchymal analysis sample" data-base62-sha1="fzeMtoBfoiiTCLoFlIXotzeK2qK" width="690" height="177" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d1c595b6b2741a15245ff4a037f4bc47b844fd2_2_690x177.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d1c595b6b2741a15245ff4a037f4bc47b844fd2_2_1035x265.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d1c595b6b2741a15245ff4a037f4bc47b844fd2_2_1380x354.jpeg 2x" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">parenchymal analysis sample</span><span class="informations">1755×452 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, all of the matching parameters have same values except for kurtosis. Perhaps the formulas used for the modules are different?</p>

---

## Post #2 by @JoostJM (2022-05-03 07:40 UTC)

<p>This is a known confusion. What happens is that parenchymal analysis gives you the <em>excess</em> kurtosis, while pyradiomics gives you the true kurtosis. It’s a static difference of 3 (derived from the normal distribution, where kurtosis = 3, and excess kurtosis = 0).</p>

---
