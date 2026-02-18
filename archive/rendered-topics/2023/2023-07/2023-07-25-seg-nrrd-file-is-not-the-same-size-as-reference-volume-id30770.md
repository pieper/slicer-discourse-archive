# .seg.nrrd file is not the same size as reference volume

**Topic ID**: 30770
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/seg-nrrd-file-is-not-the-same-size-as-reference-volume/30770

---

## Post #1 by @Limin (2023-07-25 01:03 UTC)

<p>Dear all,</p>
<p>I am using Slicer-4.11.20210226 on windows system. My segmentations (in seg.nrrd format) were created and linked to their reference volumes (in .nii format) automatically with a python script. The script ran fine, and manual ROI drawings could be performed and saved.</p>
<p>However, when saved among different systems and versions of 3D slicer, the size between .seg.nrrd file and reference volume doesn’t match. For example, my reference volume is always size of 512x512x35. But the saved seg.nrrd file can be 288x288x35 or 1024x1024x35, which causes a problem for ROI extraction.</p>
<p>Is there any way to solve this problem without redrawing all the ROIs? Really appreciate all your   inputs!</p>
<p>Thanks,<br>
Limin</p>

---

## Post #2 by @lassoan (2023-07-25 01:21 UTC)

<p>Slicer-4.11 automatically crops the segmentation to the minimum necessary size. It preserves the image content in physical space, but this may be a problem for applications that ignore image geometry and just operate on the voxels.</p>
<p>In later Slicer versions we changed the default so that the segmentation geometry is set to the same as the source image. You can also easily change the image geometry later.</p>
<p>I would recommend to use the current Slicer version, as it will work by default as you expect. For any existing segmentations, you can change the geometry to match the source image as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>.</p>

---

## Post #3 by @Limin (2023-07-25 15:26 UTC)

<p>Hi Andras,</p>
<p>Thank you for the kind reply! Will change slicer to the current version.</p>
<p>Best,<br>
Limin</p>

---
