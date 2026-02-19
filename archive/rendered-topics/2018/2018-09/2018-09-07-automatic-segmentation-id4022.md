---
topic_id: 4022
title: "Automatic Segmentation"
date: 2018-09-07
url: https://discourse.slicer.org/t/4022
---

# Automatic Segmentation

**Topic ID**: 4022
**Date**: 2018-09-07
**URL**: https://discourse.slicer.org/t/automatic-segmentation/4022

---

## Post #1 by @oc34 (2018-09-07 20:31 UTC)

<p>Hi</p>
<p>I downloaded a nii file that has already segmentation. I don’t need to do segmentation. I want to see segmentations but I couldn’t. How can I open segmentation? After I open segmentation, I want to export STL files. I’d appreciate that if aynone helps me.</p>
<p>Thanks<br>
Ozan</p>
<p>Operating system: Windows<br>
Slicer version:4.9 Nightly<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-09-07 22:26 UTC)

<p>When you load the volume, in Add data dialog, check Labelmap option. After that import it into a segmentation node in Segmentations module.</p>
<p>If the volume is stored in NRRD format then you can load it directly as segmentation (in Add data dialog you can select “Segmentation” in the description column).</p>

---
