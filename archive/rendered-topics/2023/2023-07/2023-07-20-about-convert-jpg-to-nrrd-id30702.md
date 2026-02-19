---
topic_id: 30702
title: "About Convert Jpg To Nrrd"
date: 2023-07-20
url: https://discourse.slicer.org/t/30702
---

# About convert jpg to nrrd

**Topic ID**: 30702
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/about-convert-jpg-to-nrrd/30702

---

## Post #1 by @Matt8268 (2023-07-20 12:56 UTC)

<p>Dear PyRadiomics / 3DSlicer community,<br>
When importing JPEG images into 3D Slicer and converting them to the NRRD format, they may not be recognized by the Radiomics module. However, by converting them to a scalar volume, they can be recognized by the Radiomics module, although the image becomes grayscale. Is there a way to convert the images to a scalar volume while preserving the color information, or are there other methods to make them recognizable by the Radiomics module?<br>
Could you please guide me on how to accomplish this task.<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2023-07-21 14:15 UTC)

<p>There may not be any metric of PyRadiomics that is computed from multichannel images (such as RGB color images). You can use one color channel, a combined channel (e.g., average), or compute features for each color channel and combine the features.</p>

---
