# Merging Segments from 3 different scans

**Topic ID**: 44862
**Date**: 2025-10-23
**URL**: https://discourse.slicer.org/t/merging-segments-from-3-different-scans/44862

---

## Post #1 by @Richard (2025-10-23 17:33 UTC)

<p>Hi!</p>
<p>New to 3D slicer so I hope the question is not too basic: I am working on a project where I segmented an implant from one patient from 3 different CT scans from 3 different time points. To visualize any deformation of the implant I would now like to fuse or merge the 3 different segments from the 3 different scans (basically creating a superimposition of the implant from the 3 scans). With each scan the patient positioning was slightly different and the scans seem to have a different geometry (if that makes sense?).<br>
Is that possible in 3D slicer and if so, any advice or instructions on how to do it? Thanks in advance!</p>

---

## Post #2 by @muratmaga (2025-10-23 17:58 UTC)

<p>You can use ANTs or General Registration modules to rigidly register two scans to the one you choose as the reference. One outcome of that registration is a transformation matrix. Apply that transform to the segmentations of the two scans, and now all six (three volumes, three segmentations) should be in the space of the scan you chose as reference in the first step.</p>

---
