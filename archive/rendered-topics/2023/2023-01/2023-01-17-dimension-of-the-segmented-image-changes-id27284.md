---
topic_id: 27284
title: "Dimension Of The Segmented Image Changes"
date: 2023-01-17
url: https://discourse.slicer.org/t/27284
---

# Dimension of the segmented image changes

**Topic ID**: 27284
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/dimension-of-the-segmented-image-changes/27284

---

## Post #1 by @Aditya_Kamath (2023-01-17 04:11 UTC)

<p>Version: 4.13.0</p>
<p>After I segment my images when I save the image the dimensions of the segmented image change.<br>
Say my imaging volume is (30,192,256) My segmented image becomes (11,56,65).<br>
Is there any chance I could retain the exact dimensions(30,192,356) of the segmented image?</p>

---

## Post #2 by @Aditya_Kamath (2023-01-17 04:52 UTC)

<p>I figured out how that could be rectified. While saving the segment make sure you save it as .nrrd instead of .seg.nrrd. By doing so the segmented image retains the dimensions of the image volume.</p>

---

## Post #3 by @lassoan (2023-01-17 05:33 UTC)

<p>Older Slicer versions crop segmentations to minimum necessary size during saving. We thought it made no sense to save empty image regions, since we expected that all medical image computing software do all processing in physical space anyway.</p>
<p>However, we later learned that there are just too many software (mostly prototype code, research software, etc.) that require exact match in voxel space (not just in physical space), so we changed the default and in current Slicer versions cropping is disabled by default.</p>
<p>The easiest solution is to use a current Slicer version (latest Slicer Stable Release or latest Slicer Preview Release).</p>

---
