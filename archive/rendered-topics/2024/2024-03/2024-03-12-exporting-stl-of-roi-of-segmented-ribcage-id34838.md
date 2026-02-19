---
topic_id: 34838
title: "Exporting Stl Of Roi Of Segmented Ribcage"
date: 2024-03-12
url: https://discourse.slicer.org/t/34838
---

# Exporting stl of ROI of segmented ribcage

**Topic ID**: 34838
**Date**: 2024-03-12
**URL**: https://discourse.slicer.org/t/exporting-stl-of-roi-of-segmented-ribcage/34838

---

## Post #1 by @Marthe (2024-03-12 01:27 UTC)

<p>Dear all</p>
<p>After segmenting the ribcage from the CTACardio data, I wondered how I can export an STL file only containing the part of the 3D ribcage structure indicated by the ROI? See attached screenshot to understand my question. Thank you in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8950844d981720494433d977c172f0c3f1702ca.png" data-download-href="/uploads/short-url/xbw4y3rAXCDT6SDH7mDN5okIFaq.png?dl=1" title="Schermopname (329)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8950844d981720494433d977c172f0c3f1702ca_2_690x388.png" alt="Schermopname (329)" data-base62-sha1="xbw4y3rAXCDT6SDH7mDN5okIFaq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8950844d981720494433d977c172f0c3f1702ca_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8950844d981720494433d977c172f0c3f1702ca_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8950844d981720494433d977c172f0c3f1702ca_2_1380x776.png 2x" data-dominant-color="8B8C90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermopname (329)</span><span class="informations">1920×1080 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-03-12 02:52 UTC)

<p>You can use the Dynamic Modeler module to crop your segmentation model with this ROI, and then export the resultant model as an STL by right clicking and choosing “Export File” in the Data module.</p>

---

## Post #3 by @Marthe (2024-03-12 08:44 UTC)

<p>Thank you very much for your reply! I tried doing that, however, I cannot input my segmented ribcage in order to do the ROI cut as can be seen from my screenshot. Did I do something wrong?</p>
<p>Kind regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfced877818485fad471e8c8d1baae76f63c0d8b.png" data-download-href="/uploads/short-url/rmOmpqpxoaLifBkhWWOK1ySj2A3.png?dl=1" title="Schermopname (330)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfced877818485fad471e8c8d1baae76f63c0d8b_2_690x388.png" alt="Schermopname (330)" data-base62-sha1="rmOmpqpxoaLifBkhWWOK1ySj2A3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfced877818485fad471e8c8d1baae76f63c0d8b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfced877818485fad471e8c8d1baae76f63c0d8b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfced877818485fad471e8c8d1baae76f63c0d8b_2_1380x776.png 2x" data-dominant-color="898B90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermopname (330)</span><span class="informations">1920×1080 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Sunderlandkyl (2024-03-12 14:43 UTC)

<p>You’ll need to export your segmentation to a model node.</p>

---

## Post #5 by @Marthe (2024-03-13 09:54 UTC)

<p>Thank you very much!!</p>

---
