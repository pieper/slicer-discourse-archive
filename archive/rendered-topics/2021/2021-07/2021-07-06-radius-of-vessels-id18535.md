---
topic_id: 18535
title: "Radius Of Vessels"
date: 2021-07-06
url: https://discourse.slicer.org/t/18535
---

# Radius of vessels

**Topic ID**: 18535
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/radius-of-vessels/18535

---

## Post #1 by @AshvinGupta (2021-07-06 16:39 UTC)

<p>Hello,<br>
I am using the VMTK extension to first find the centreline of a vessel from a dicom image. I then want to find the radius of the vessel at particular points, such as the control points. Is there any way to easily do this with the VMTK extension or will I need to download another package?<br>
Thanks</p>

---

## Post #2 by @lassoan (2021-07-06 16:45 UTC)

<p>Extract centerline module already computes the radius at every vessel point. You can get the results as a table (centerline position and radius values) and the radius values are also included in the output model node.</p>

---

## Post #3 by @AshvinGupta (2021-07-07 14:52 UTC)

<p>Thank you for your quick reply. So once I have the centrelines how do I actually find the radius because at the moment I can only see the RAS coordinates. Is it in edit properties?</p>

---

## Post #4 by @lassoan (2021-07-12 14:36 UTC)

<p>If you update to latest SlicerVMTK version then you should see the radius values in the table.</p>

---
