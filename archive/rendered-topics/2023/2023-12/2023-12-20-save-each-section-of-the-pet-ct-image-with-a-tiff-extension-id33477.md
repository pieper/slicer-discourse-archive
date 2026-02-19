---
topic_id: 33477
title: "Save Each Section Of The Pet Ct Image With A Tiff Extension"
date: 2023-12-20
url: https://discourse.slicer.org/t/33477
---

# Save each section of the pet/ct image with a tiff extension

**Topic ID**: 33477
**Date**: 2023-12-20
**URL**: https://discourse.slicer.org/t/save-each-section-of-the-pet-ct-image-with-a-tiff-extension/33477

---

## Post #1 by @Bahadir_Emekli (2023-12-20 20:36 UTC)

<p>I uploaded a file consisting of 336 tiff-extended PET/CT images to the 3d slicer application. I processed these 336 slices on the application and I want to download these 336 tiff-extended images from the 3d slicer application to a folder on my desktop, how can I do that? (I wanted to do the segmentation and download it, but it downloaded the segmented region as a 3D model. I don’t want that. So I want to save these 336 tiff extension data again).</p>

---

## Post #2 by @pieper (2023-12-20 21:49 UTC)

<p>We don’t support saving in tiff since there’s no standard for saving metadata like 3D geometry.  You can easily write a small python script to convert data to match your tiff format either directly from Slicer or by saving to a format like nrrd and then converting.</p>

---
