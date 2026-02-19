---
topic_id: 32264
title: "Recommended File Format For Saving Image And Segmentations"
date: 2023-10-17
url: https://discourse.slicer.org/t/32264
---

# Recommended file format for saving image and segmentations

**Topic ID**: 32264
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/recommended-file-format-for-saving-image-and-segmentations/32264

---

## Post #1 by @S_Arbabi (2023-10-17 06:32 UTC)

<p>I am working with CT images (DICOM) and the segmentation of bones. What file format you recommend to save the image and segmentations to follow standards, with going commercial in future in mind?</p>

---

## Post #2 by @pieper (2023-10-17 17:12 UTC)

<p>DICOM SEG is the standard you should probably follow, but it’s only going to be interoperable with a few systems currently.  Depending on how you want to use the results you may need to have custom proprietary interfaces.</p>

---
