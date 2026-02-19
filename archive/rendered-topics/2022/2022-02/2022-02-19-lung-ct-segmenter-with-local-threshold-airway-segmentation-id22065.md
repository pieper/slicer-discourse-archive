---
topic_id: 22065
title: "Lung Ct Segmenter With Local Threshold Airway Segmentation"
date: 2022-02-19
url: https://discourse.slicer.org/t/22065
---

# Lung CT Segmenter with 'Local Threshold' airway segmentation

**Topic ID**: 22065
**Date**: 2022-02-19
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter-with-local-threshold-airway-segmentation/22065

---

## Post #1 by @rbumm (2022-02-19 11:43 UTC)

<p>The old CIP based airway segmentation has been removed from the Lung CT Segmenter extension (in Lung CT Analyzer Version 2.47) and a new airway segmentation technique based on the “Local Threshold” Segment Editor Extra Effect has been implemented.<br>
This results in increased speed and subsegmental airway precision in suitable data sets (1 mm slices recommended) with three levels of detail:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902e794ae361e5bdec8af98cc27d24e05763ebaa.jpeg" data-download-href="/uploads/short-url/kzukaPRsNDoPLnrHG3ZDizi3w6e.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902e794ae361e5bdec8af98cc27d24e05763ebaa_2_689x359.jpeg" alt="image" data-base62-sha1="kzukaPRsNDoPLnrHG3ZDizi3w6e" width="689" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902e794ae361e5bdec8af98cc27d24e05763ebaa_2_689x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/902e794ae361e5bdec8af98cc27d24e05763ebaa_2_1033x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902e794ae361e5bdec8af98cc27d24e05763ebaa.jpeg 2x" data-dominant-color="B6B7BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1231×642 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Airways are now overwriting the lung masks. No additional markups (one tracheal markup) are needed. Expect the update to become automatically available during the next few days.</p>

---

## Post #2 by @Eserval (2022-03-20 00:17 UTC)

<p>Hello everyone!</p>
<p>Is there any special configuration in the module to achieve a great result like that above? I’m having bad airway results like in the past module version.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7af9df9ac150cbda714c83946f9e4c79f6cd9f7.jpeg" data-download-href="/uploads/short-url/x3AyjRQtLgOm2Klw3slmIu9sRlt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7af9df9ac150cbda714c83946f9e4c79f6cd9f7_2_690x373.jpeg" alt="image" data-base62-sha1="x3AyjRQtLgOm2Klw3slmIu9sRlt" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7af9df9ac150cbda714c83946f9e4c79f6cd9f7_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7af9df9ac150cbda714c83946f9e4c79f6cd9f7_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7af9df9ac150cbda714c83946f9e4c79f6cd9f7_2_1380x746.jpeg 2x" data-dominant-color="A4A5A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regards</p>

---

## Post #3 by @rbumm (2022-03-20 10:24 UTC)

<p>You are showing the lung CT segmenter mask preview on your screenshot. The “lung intensity range” should be modified until you lose the “spikes” on the mask surface, probably set the minimum range to “-1500” and press “Update” until you are satisfied with the mask preview, then press “Apply” with “Airway segmentation” checked. The airway segmentation will only be generated after the “Apply” step. Maybe post the result you get after following this, thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66f8da111f7f5cfe774872b1b780d50a786ee5d1.jpeg" data-download-href="/uploads/short-url/eGVRBmH5ApZ4H6OBkbUOllddvSV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f8da111f7f5cfe774872b1b780d50a786ee5d1_2_690x374.jpeg" alt="image" data-base62-sha1="eGVRBmH5ApZ4H6OBkbUOllddvSV" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f8da111f7f5cfe774872b1b780d50a786ee5d1_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f8da111f7f5cfe774872b1b780d50a786ee5d1_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f8da111f7f5cfe774872b1b780d50a786ee5d1_2_1380x748.jpeg 2x" data-dominant-color="A4A4A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1583×860 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Eserval (2022-03-21 12:27 UTC)

<p>Thanks for the reply Rudolf !</p>
<p>That works fine. However I have poor airway dfinition. Maybe it is due to my slice thickness of 2mm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bece01592960670e0930ac2441c5cdc5b94a9162.jpeg" data-download-href="/uploads/short-url/rdW5bugOoJ9mu7UaaEnPy6fKAW6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bece01592960670e0930ac2441c5cdc5b94a9162_2_690x374.jpeg" alt="image" data-base62-sha1="rdW5bugOoJ9mu7UaaEnPy6fKAW6" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bece01592960670e0930ac2441c5cdc5b94a9162_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bece01592960670e0930ac2441c5cdc5b94a9162_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bece01592960670e0930ac2441c5cdc5b94a9162_2_1380x748.jpeg 2x" data-dominant-color="8B8D8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1041 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
