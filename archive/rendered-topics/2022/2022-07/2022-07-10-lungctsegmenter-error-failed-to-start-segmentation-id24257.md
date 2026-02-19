---
topic_id: 24257
title: "Lungctsegmenter Error Failed To Start Segmentation"
date: 2022-07-10
url: https://discourse.slicer.org/t/24257
---

# LungCTSegmenter error:Failed to start segmentation

**Topic ID**: 24257
**Date**: 2022-07-10
**URL**: https://discourse.slicer.org/t/lungctsegmenter-error-failed-to-start-segmentation/24257

---

## Post #1 by @Faraday_Caraway (2022-07-10 12:20 UTC)

<p>Hello, I am a novice user of 3D Slicer and trying to use version 5.1.0 of the software in windows 11.For a CT that I am looking at, I could not get segmentation done.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cdb21298e857d5800e8dab4fd047c71c937e6ba.jpeg" data-download-href="/uploads/short-url/6oOutC1uDEv3PoXxBvMik1AJyae.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cdb21298e857d5800e8dab4fd047c71c937e6ba_2_517x213.jpeg" alt="2" data-base62-sha1="6oOutC1uDEv3PoXxBvMik1AJyae" width="517" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cdb21298e857d5800e8dab4fd047c71c937e6ba_2_517x213.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cdb21298e857d5800e8dab4fd047c71c937e6ba_2_775x319.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cdb21298e857d5800e8dab4fd047c71c937e6ba_2_1034x426.jpeg 2x" data-dominant-color="4C4B4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1518×628 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It shows error message:Failed to start segmentation: ‘vtkSlicerSegmentationsModuleMRML.vtkMRMLSegmentEdi’ object has no attribute ‘SetMasterVolumeIntensityMask’.When I click the OK button on the message,I can place the control points successfully but nothing happens.What may be the reason?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf04a66b2ef28c04132967b720f0e755473322ee.jpeg" data-download-href="/uploads/short-url/rfP9Tt3bOsPy3NetMvYyO33c4Vw.jpeg?dl=1" title="1657415898799" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf04a66b2ef28c04132967b720f0e755473322ee_2_517x278.jpeg" alt="1657415898799" data-base62-sha1="rfP9Tt3bOsPy3NetMvYyO33c4Vw" width="517" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf04a66b2ef28c04132967b720f0e755473322ee_2_517x278.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf04a66b2ef28c04132967b720f0e755473322ee_2_775x417.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf04a66b2ef28c04132967b720f0e755473322ee_2_1034x556.jpeg 2x" data-dominant-color="515155"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1657415898799</span><span class="informations">1920×1034 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-07-10 12:21 UTC)

<p>There was a regression in Slicer-5.1 Preview Releases for a few days that have been fixed. Please use the latest Slicer Stable Release or the latest Slicer Preview Release.</p>

---

## Post #3 by @Faraday_Caraway (2022-07-10 16:11 UTC)

<p>Thank you! But when I use the latest Slicer Preview Release(slicer-5.1-7-8),I can’t find the "LungCTSegmenter " button in the "chest imaging platform(CIP) "as the slicer-5.1-7-6. What should I do to solve this problem.</p>

---

## Post #4 by @lassoan (2022-07-10 16:27 UTC)

<p>Have you installed the LungCTAnalyzer extension?</p>

---

## Post #5 by @Faraday_Caraway (2022-07-13 03:10 UTC)

<p>THANK YOU SO MUCH!!! I have successed to use the LungCTSegmenter! Sorry to not reply immediately.</p>

---
