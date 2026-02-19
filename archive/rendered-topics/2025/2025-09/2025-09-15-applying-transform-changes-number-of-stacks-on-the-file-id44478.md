---
topic_id: 44478
title: "Applying Transform Changes Number Of Stacks On The File"
date: 2025-09-15
url: https://discourse.slicer.org/t/44478
---

# Applying Transform Changes number of stacks on the file

**Topic ID**: 44478
**Date**: 2025-09-15
**URL**: https://discourse.slicer.org/t/applying-transform-changes-number-of-stacks-on-the-file/44478

---

## Post #1 by @ylcnkzy (2025-09-15 09:44 UTC)

<p><strong>Dear Colleagues,</strong></p>
<p>I am registering the <em>Fixed.tiff</em> image to the <em>Moving.tiff</em> image using the Elastix module within 3D Slicer. Both images are 512 × 512 × 381. The registration works well, and after I apply the transform, everything looks perfect in Slicer — I can see the high-precision alignment.</p>
<p>However, when I export and save the transformed moving image as a .tiff file, the number of slices in the Z-dimension increases to 384, and it no longer aligns with the fixed image in ImageJ.</p>
<p>Does anyone have any idea how to fix this problem?</p>
<p>Best regards,</p>

---

## Post #2 by @pieper (2025-09-15 15:14 UTC)

<p>You probably need to resample the Moving volume in the space of the Fixed (use the Resample module)</p>

---

## Post #3 by @ylcnkzy (2025-09-24 12:37 UTC)

<p>Hi Steve,</p>
<p>I have managed it via <strong>Resample Scalar/Vector/DWI Volume</strong> option within the Slicer.</p>
<p>Thanks for the info.</p>

---
