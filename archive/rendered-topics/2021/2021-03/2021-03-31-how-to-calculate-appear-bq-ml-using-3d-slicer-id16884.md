---
topic_id: 16884
title: "How To Calculate Appear Bq Ml Using 3D Slicer"
date: 2021-03-31
url: https://discourse.slicer.org/t/16884
---

# How to Calculate/appear Bq/ml using 3D Slicer

**Topic ID**: 16884
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/how-to-calculate-appear-bq-ml-using-3d-slicer/16884

---

## Post #1 by @akmal871026 (2021-03-31 22:27 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior: Anyone knows how to calculate the Bq/ml using a 3D Slicer? Just now only can calculate SUV max, SUV min, SUV mean.</p>

---

## Post #2 by @lassoan (2021-04-14 05:45 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> as far as I remember, you have been working on PET related features recently. Do you have any suggestion for this?</p>

---

## Post #3 by @pieper (2021-04-14 14:13 UTC)

<p>If you have the PET-related extensions installed and the plugins are enabled, Slicer will apply the SUVbw by default.  But if you turn on Advanced mode you can select your desired interpretation after running the Examine step.  Then loading the scalar volume option on the attenuation corrected series should give you the Bq/ml volume (I’ve never used those raw values so let us know if they don’t load correctly for you - they do look correct to me).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5b9393f88c62fe32c45ff6ba6d0425c1eb0f3ec.png" data-download-href="/uploads/short-url/sd8TTeFqPi2E2XYywtW03KZi5iY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5b9393f88c62fe32c45ff6ba6d0425c1eb0f3ec_2_690x229.png" alt="image" data-base62-sha1="sd8TTeFqPi2E2XYywtW03KZi5iY" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5b9393f88c62fe32c45ff6ba6d0425c1eb0f3ec_2_690x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5b9393f88c62fe32c45ff6ba6d0425c1eb0f3ec_2_1035x343.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5b9393f88c62fe32c45ff6ba6d0425c1eb0f3ec_2_1380x458.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1736×578 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @akmal871026 (2021-04-20 00:07 UTC)

<p>yah… but the some extension that you screenshot like DICOMscalarvolume, MutivolumeImporter is not in Extensions Manager</p>

---

## Post #5 by @pieper (2021-04-20 22:28 UTC)

<p>Those are built-ins and don’t need to be installed via the extension manager.</p>

---
