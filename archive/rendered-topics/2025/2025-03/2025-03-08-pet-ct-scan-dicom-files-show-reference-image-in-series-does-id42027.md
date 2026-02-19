---
topic_id: 42027
title: "Pet Ct Scan Dicom Files Show Reference Image In Series Does"
date: 2025-03-08
url: https://discourse.slicer.org/t/42027
---

# Pet/CT Scan DICOM files show "Reference image in series does not contain geometry information" error

**Topic ID**: 42027
**Date**: 2025-03-08
**URL**: https://discourse.slicer.org/t/pet-ct-scan-dicom-files-show-reference-image-in-series-does-not-contain-geometry-information-error/42027

---

## Post #1 by @neutronstar (2025-03-08 00:48 UTC)

<p>Hi! I’m sorry I’m very new to 3d Slicer. I’m trying to 3d print one of my organs from my pet/ct scan. When I upload it to 3d slicer I can see the results, but I can’t see the 3d model.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a401d01804292d51a5b865c685a0cd82cb7be37.png" alt="image" data-base62-sha1="3KdM8iuH77JV9PUXNGVWpJsteLB" width="645" height="95"></p>
<p>What should I do to fix this issue?</p>

---

## Post #2 by @lassoan (2025-03-08 00:50 UTC)

<p>Often fused PET/CT images are saved as a series of secondary capture images. These are not suitable for further analysis or 3D reconstruction, only for viewing as a set of 2D images.</p>
<p>If you want to 3D print then you can load and segment the CT image.</p>

---
