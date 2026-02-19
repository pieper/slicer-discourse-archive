---
topic_id: 22923
title: "Lung Ct Analyzer And Radiomic Features"
date: 2022-04-12
url: https://discourse.slicer.org/t/22923
---

# Lung CT Analyzer and Radiomic Features?

**Topic ID**: 22923
**Date**: 2022-04-12
**URL**: https://discourse.slicer.org/t/lung-ct-analyzer-and-radiomic-features/22923

---

## Post #1 by @wangxiaolan (2022-04-12 15:24 UTC)

<p>Can Features be extracted directly from Lung CT Analyzer 3D results using Radiomic Features?</p>

---

## Post #2 by @rbumm (2022-04-12 16:05 UTC)

<p>You would want to install the “Radiomics” extension in Slicer which you could then use to analyze the output (“Lung analysis segmentation”) of the “Lung CT Analyzer” module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f00fe3c02bb6675695f52dc5a06d1c5429d86b5d.png" data-download-href="/uploads/short-url/yfGDs2ObRd1qIIgRu1ftGRaWTX7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00fe3c02bb6675695f52dc5a06d1c5429d86b5d_2_690x357.png" alt="image" data-base62-sha1="yfGDs2ObRd1qIIgRu1ftGRaWTX7" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00fe3c02bb6675695f52dc5a06d1c5429d86b5d_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00fe3c02bb6675695f52dc5a06d1c5429d86b5d_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00fe3c02bb6675695f52dc5a06d1c5429d86b5d_2_1380x714.png 2x" data-dominant-color="C8C8CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×992 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @wangxiaolan (2022-04-13 09:14 UTC)

<p>So it can be. Thank you, teacher!</p>

---

## Post #4 by @wangxiaolan (2022-04-13 09:18 UTC)

<p>Excuse me teacher: is this operation only extracting the features of the lesion?</p>

---

## Post #5 by @rbumm (2022-04-13 12:03 UTC)

<p>Unfortunately, I have no experience with Radiomics and can only give limited advice here.<br>
I did not find Radiomics included in Slicer 4.13 so every guess from my side is based on a probably outdated program version.</p>
<p>Feeding the output of Lung CT Analyzer into Radiomics in Slicer 4.11 did not produce meaningful results. In the Radiomics result table, the feature columns for each output segment were identical.</p>

---

## Post #6 by @wangxiaolan (2022-04-13 12:18 UTC)

<p>Ok. Thank you, teacher.</p>

---
