# Segmentation of breast tumors

**Topic ID**: 43181
**Date**: 2025-06-01
**URL**: https://discourse.slicer.org/t/segmentation-of-breast-tumors/43181

---

## Post #1 by @Meltem (2025-06-01 11:45 UTC)

<p>Hello, I am Meltem. New here. I have downloaded 3d Slicer 5.8.1. I have chosen the second phase of dynamic contrasted breas MRI to segment, and I want to segment the tumor via threshold (it’s a very complex tumor, manually it would take eons!). But when I click on threshold, it includes whole imaging not only the region of tumor. How can I fix that?<br>
Thanks in advance,<br>
Best regards</p>

---

## Post #2 by @lassoan (2025-06-01 12:09 UTC)

<p>If the problem is that there are several areas with the same intensity as the tumor then you can use “Local threshold” effect (provided by SegmentEditorExtraEffects extension).</p>
<p>Note that you may not need a very accurate segmentation of breast tumors as they are removed by a wide margin (it is not a crucial to conserve surrounding tissues as in a brain surgery), but you may just need a simple, resectable shape that safely encompasses the tumor. If this is the case, then you can use the “Surface cut” effect. This effect allows your to draw a simple blob shape around the tumor by a couple of clicks in 1-2 minutes. We use this segmentation method on a touchscreen tablet on 3D tracked ultrasound images while the patient is on the table and it works very well.</p>

---

## Post #3 by @Meltem (2025-06-04 05:35 UTC)

<p>Hello, thank you very much.</p>

---
