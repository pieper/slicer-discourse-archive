---
topic_id: 46860
title: "I Want To Create A Closed Contour From Hdr Img Data"
date: 2026-04-28
url: https://discourse.slicer.org/t/46860
---

# I want to create a closed contour from hdr/img data

**Topic ID**: 46860
**Date**: 2026-04-28
**URL**: https://discourse.slicer.org/t/i-want-to-create-a-closed-contour-from-hdr-img-data/46860

---

## Post #1 by @PetrKryslUCSD (2026-04-28 15:33 UTC)

<p>Right now the contour runs into the boundary of the box, and it is then open. One thing that I could think of was to either surround the current volume with a layer of zero voxels (which would close the contour), or modify the volume itself by setting the voxels close to the boundary to zero.</p>
<p>Is this a good approach, hopefully supported by slicer. Or is there something better?</p>

---

## Post #2 by @lassoan (2026-04-28 16:08 UTC)

<p>If you load the image as segmentation then this boundary is automatically added for you.</p>
<p>However, for this first you need to convert the legacy hdr/img format to nrrd or nifti. You can do that by loading the hdr/img file into Slicer as a Volume and then saving it in the new format.</p>

---
