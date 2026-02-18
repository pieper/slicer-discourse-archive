# MRI image segmentation and export

**Topic ID**: 31460
**Date**: 2023-08-31
**URL**: https://discourse.slicer.org/t/mri-image-segmentation-and-export/31460

---

## Post #1 by @Kelly_Lee (2023-08-31 07:50 UTC)

<p>I have an image, and I’ve already used the segment editor to outline the ROI. How can I remove the image outside the ROI and export the MRI image within the ROI (in JPG, DICOM, or JSON format)?</p>

---

## Post #2 by @lassoan (2023-08-31 07:52 UTC)

<p>You can blank out the region inside or outside a segment using the Mask Volume effect.</p>
<p>If you want to do skull stripping then there are several Slicer extensions that do that automatically.</p>

---

## Post #3 by @Kelly_Lee (2023-09-01 01:32 UTC)

<p>I’m sincerely grateful for your response. I have successfully completed the segmentation and exported it in DICOM format.</p>

---
