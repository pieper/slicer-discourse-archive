---
topic_id: 17561
title: "Tips To Circumvent Not Having Pre Contrast Injection Images"
date: 2021-05-11
url: https://discourse.slicer.org/t/17561
---

# Tips to circumvent not having pre-contrast injection images for the purpose of bone subtraction

**Topic ID**: 17561
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/tips-to-circumvent-not-having-pre-contrast-injection-images-for-the-purpose-of-bone-subtraction/17561

---

## Post #1 by @KyleVanBeek (2021-05-11 05:44 UTC)

<p>Hello,</p>
<p>I have CTA brain data-sets for pre-operation and post operation of stroke patients and I want to segment the cerebral vessels to run some comparisons of geometry. I’ve been running into issues with other segmentation methods until I stumbled upon the subtraction method.</p>
<p>Unfortunately I don’t any pre-contrast injection images to use as my baseline. I was wondering if anyone knows a way of circumventing this by possibly changing the window/level of the CTA data set to mimic that of pre-contrast injection?</p>
<p>Any tips or tricks would be much appreciated</p>

---

## Post #2 by @lassoan (2021-05-13 13:54 UTC)

<p>You can try “Vesselness filtering” module in SlicerVMTK extension. It can make vessels (or other tubular structures) a bit brighter compared to the background, which may help with the segmentation.</p>
<p>It cannot do wonders, but if you tune the parameters well then it may help. See an example of thresholded vessel-enhanced image as red overlay in slice views; in 3D view: left is original volume, right is vessel-enhanced volume. The main difference is that small vessels are better visible and otherwise very bright bones are somewhat suppressed. You of course still need to segment the image to get the vasculature.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead75f6f62181d9dc90bd03460d82eeb10f8e691.jpeg" data-download-href="/uploads/short-url/xvva3mR417smaxf6pCzlXEsfR97.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ead75f6f62181d9dc90bd03460d82eeb10f8e691_2_690x420.jpeg" alt="image" data-base62-sha1="xvva3mR417smaxf6pCzlXEsfR97" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ead75f6f62181d9dc90bd03460d82eeb10f8e691_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ead75f6f62181d9dc90bd03460d82eeb10f8e691_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ead75f6f62181d9dc90bd03460d82eeb10f8e691_2_1380x840.jpeg 2x" data-dominant-color="B2A5A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2250×1370 770 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
f</p>

---
