---
topic_id: 40465
title: "Segmentation As Dicom Format"
date: 2024-12-01
url: https://discourse.slicer.org/t/40465
---

# Segmentation as dicom format

**Topic ID**: 40465
**Date**: 2024-12-01
**URL**: https://discourse.slicer.org/t/segmentation-as-dicom-format/40465

---

## Post #1 by @Nicolo_Tombini (2024-12-01 20:42 UTC)

<p>Good evening everyone. I’m using data from <a href="https://www.cancerimagingarchive.net" rel="noopener nofollow ugc">https://www.cancerimagingarchive.net</a> and I’m having trouble using the data. I notice that I have a single file for the segmentations in dicom format and when I import it into Python I have many more segmentation slices than the CT slices. How can this situation be managed and why does it happen? Thanks a lot</p>

---

## Post #2 by @lassoan (2024-12-01 20:54 UTC)

<p>As long as the segmentation is correct in physical space, everything is good. If you need the segmentation geometry (origin, spacing, axis directions, extents) to match any particular volume - for example because you want to process it with some software that ignores physical space - then you can resample the segmentation by a few clicks (Segmentations model, Export, Labelmap, choose a reference volume).</p>

---

## Post #3 by @Nicolo_Tombini (2024-12-03 21:10 UTC)

<p>Yes I converted them from dicom into nrrd and it works.<br>
Thank you.</p>

---
