# MIRD or ORNL phantom

**Topic ID**: 22888
**Date**: 2022-04-09
**URL**: https://discourse.slicer.org/t/mird-or-ornl-phantom/22888

---

## Post #1 by @naninano1 (2022-04-09 23:55 UTC)

<p>Hi,</p>
<p>Does somebody have a phantom similar to MIRD to be used in 3D Slicer that has pre-segmented organs?</p>

---

## Post #2 by @lassoan (2022-04-12 20:54 UTC)

<p>I’m not sure if these kind of very rough geometric phantoms are still in use.</p>
<p>There are more accurate segmentations available along with the corresponding CT/MRI image, such as the <a href="https://www.openanatomy.org/atlas-pages/atlas-spl-abdomen.html">SPL abdominal atlas</a>. If you don’t need an accompanying 3D image then there are a number of mesh atlases, such as the full-body <a href="https://www.z-anatomy.com/">z-anatomy phantom</a>. There are also many thousands of CT images on TCIA and on various image segmentation challenge websites that you can use as voxel-based phantoms.</p>

---

## Post #3 by @naninano1 (2022-04-12 22:03 UTC)

<p>Thank you Andras.</p>
<p>Actually, I need a phantom for Pancras treatment planning. I want to do some changes or contouring on images and then convert them as DICOM series to be able to plan in a TPS.<br>
The mentioned resources seem don’t have the export capability, to be used in 3DSlicer</p>

---

## Post #4 by @lassoan (2022-04-12 23:33 UTC)

<p>You can load all these atlases into 3D Slicer. Let us know if you have trouble using any of them in Slicer (describe what you did, what you expected to happen, and what happened instead).</p>
<p>However, probably you would be much better off asking for a set of an anonymized data sets (CT + corresponding RT structure set) from your clinical collaborators, because those data sets will more accurately represent the kind of image and segmentation quality that you can expect in clinical practice.</p>

---
