---
topic_id: 32212
title: "From 3D Model To Sliced Image"
date: 2023-10-13
url: https://discourse.slicer.org/t/32212
---

# From 3D model to sliced image

**Topic ID**: 32212
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/from-3d-model-to-sliced-image/32212

---

## Post #1 by @elise (2023-10-13 13:52 UTC)

<p>Hello,<br>
I am trying to recreate the sliced image from a 3D (.cae). Indeed, I am first exporting a 3d from CT scans of a bone, then I drill holes in this bone and now I would like to recreate the CT scans from the altered 3d.<br>
I haven’t find any documentation to do this, do you know if it possible to do ? And where I could find documentation ?</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @tsehrhardt (2023-10-14 13:56 UTC)

<p>Did you drill the holes digitally? If so, you can import the new 3D model as a segment into your original segmentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a>).</p>

---
