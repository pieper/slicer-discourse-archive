---
topic_id: 13372
title: "Using Mip Method In The Segmentation Extraction Vascular Sys"
date: 2020-09-07
url: https://discourse.slicer.org/t/13372
---

# Using MIP method in the segmentation/extraction vascular system

**Topic ID**: 13372
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/using-mip-method-in-the-segmentation-extraction-vascular-system/13372

---

## Post #1 by @shahrokh (2020-09-07 12:56 UTC)

<p>Hello Dear Developers and Users</p>
<p>Can I use the MIP method in 3D vascular extraction/segmentation?</p>
<p>For example, I have chest CT images that can be clearly seen the pulmonary vessels using <strong>MIP Viewer</strong> module. Now I want to use the MIP method to rough segment these vessels. Is this possible? Is this the correct way?</p>
<p>The only thing that comes to my mind is that increasing the “Slice Size MIP” parameter in this module improves the clarity of vessels in 3D. But this reduces the quality of the extracted vessels in 3D (jaggies in the vessel walls).</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2020-09-07 15:23 UTC)

<p>MIP method is just for visualization technique (show thick slices), but this does not help vessel extraction/segmentation methods, as they already take advantage of the full 3D volume.</p>
<p>To make segmented vessel edges smoother, increase the input image resolution (e.g., by reducing image spacing using Crop volume module).</p>

---
