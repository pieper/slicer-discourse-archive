---
topic_id: 40889
title: "Missing Image Loading In Dicom Files"
date: 2024-12-29
url: https://discourse.slicer.org/t/40889
---

# Missing image loading in dicom files

**Topic ID**: 40889
**Date**: 2024-12-29
**URL**: https://discourse.slicer.org/t/missing-image-loading-in-dicom-files/40889

---

## Post #1 by @Mehmet_Maruf_Aydin (2024-12-29 04:53 UTC)

<p>Hello everyone<br>
After uploading my dicom files to 3d slicer, I saw that all the images in the file content were not loaded, when I upload the same folder to Radiant, I can see complete images. When I examined a little, I realised that the missing images belonged to MR sequences. Even when I re-exported the files I opened via radiant as dicom, I saw that I could not overcome the problem. I could not understand where the problem originated. Thanks in advance for your support.</p>

---

## Post #2 by @pieper (2024-12-31 16:12 UTC)

<p>It’s not uncommon for MR sequences to have more than one image from the same physical location (same slice plane).  Slicer will try to compensate or warn you about this since it makes it impossible to make a single volume.  2D viewers my just show these images in sequence.</p>
<p>If you can replicate this issue with public data or data you can share please post that.</p>

---
