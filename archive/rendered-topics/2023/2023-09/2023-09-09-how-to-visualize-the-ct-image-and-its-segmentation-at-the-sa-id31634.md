# How to visualize the CT image and its segmentation at the same time?

**Topic ID**: 31634
**Date**: 2023-09-09
**URL**: https://discourse.slicer.org/t/how-to-visualize-the-ct-image-and-its-segmentation-at-the-same-time/31634

---

## Post #1 by @Tony_Flystark (2023-09-09 14:11 UTC)

<p>Hello everyone,</p>
<p>I am seeking assistance in visualizing both a CT scan and its corresponding segmentation results simultaneously in 3D Slicer. I have successfully performed segmentation on a CT dataset (DICOM files) and saved the segmentation as an NRRD file. The purpose of this visualization is to allow others to examine and verify the accuracy of the segmentation.</p>
<p>I kindly request your guidance on how to load both the CT scan and segmentation file in 3D Slicer to achieve this concurrent visualization. Any step-by-step instructions, tips, or suggestions on the necessary tools and techniques within 3D Slicer would be highly appreciated.</p>
<p>Your help in enabling others to review the segmentation accuracy would be invaluable. Thank you in advance for your support and expertise.</p>
<p>Best regards,<br>
Kinny</p>

---

## Post #2 by @lassoan (2023-09-10 01:32 UTC)

<p>If you load both the segmentation and the CT scan they will be displayed at the same time, the segmentation overlaid on the image. You can find the description of basic visualization options on <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#using-slicer">this documentation page</a>.</p>

---
