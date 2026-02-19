---
topic_id: 8755
title: "Save 3D Model As Dicom Format"
date: 2019-10-12
url: https://discourse.slicer.org/t/8755
---

# Save 3D model as dicom format

**Topic ID**: 8755
**Date**: 2019-10-12
**URL**: https://discourse.slicer.org/t/save-3d-model-as-dicom-format/8755

---

## Post #1 by @amirbahador (2019-10-12 13:37 UTC)

<p>Hi<br>
I load several Dicom and use volume rendering to create 3D model.how can I save 3D model as a dicom file or mhd and raw?</p>

---

## Post #2 by @lassoan (2019-10-12 14:10 UTC)

<p>Volume rendering is just a visualization mode, it does not create any model, segmentation, or labelmap. This has been discussed before on the forum, see for example: <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/21" class="inline-onebox">Save volume rendering as STL file</a>.</p>
<p>You can save the loaded DICOM volumes as mhd/raw file by using menu: File / Save.</p>
<p>To save as STL, you need to first segment the volume using Segment Editor module. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">here</a>.</p>

---
