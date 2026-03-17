---
topic_id: 46471
title: "Using Getimagecropped Function In Pyautoscoper Getting Trunc"
date: 2026-03-16
url: https://discourse.slicer.org/t/46471
---

# Using getImageCropped function in PyAutoscoper. Getting truncated/empty data

**Topic ID**: 46471
**Date**: 2026-03-16
**URL**: https://discourse.slicer.org/t/using-getimagecropped-function-in-pyautoscoper-getting-truncated-empty-data/46471

---

## Post #1 by @Prabhroop_Singh (2026-03-16 19:09 UTC)

<p>I’m trying to use getImageCropped from PyAutoscoper to extract the cropped DRR image of a volume at a given pose. My setup works fine otherwise – getPose, getNCC, optimizeFrame, and trackingDialog all work correctly. This is the output i am getting:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/990caf8c94bc1592e79fccaeaf6ab7c8f8db1634.png" data-download-href="/uploads/short-url/lPWenZJx485bqJs5Udmx8oTqwHG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990caf8c94bc1592e79fccaeaf6ab7c8f8db1634_2_690x319.png" alt="image" data-base62-sha1="lPWenZJx485bqJs5Udmx8oTqwHG" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990caf8c94bc1592e79fccaeaf6ab7c8f8db1634_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990caf8c94bc1592e79fccaeaf6ab7c8f8db1634_2_1035x478.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990caf8c94bc1592e79fccaeaf6ab7c8f8db1634_2_1380x638.png 2x" data-dominant-color="383938"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2316×1072 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The width and height (1760x1760) look correct, but the byte array is only 1015 bytes long and entirely zeros. For a 1760x1760 image I’d expect significantly more data.</p>
<ol>
<li>What is getImageCropped supposed to return exactly? The docstring says list[float] but it actually returns [width, height, raw_bytes]. What format/dtype is the image data (float32, uint8, RGB, grayscale)?</li>
<li>Is there another recommended way to programmatically extract DRR or radiograph images from Autoscoper?</li>
</ol>
<p>Thanks for the help!</p>

---
