---
topic_id: 30526
title: "Export 3D Stl File From Volume Rendering"
date: 2023-07-11
url: https://discourse.slicer.org/t/30526
---

# Export 3D stl file from Volume Rendering

**Topic ID**: 30526
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/export-3d-stl-file-from-volume-rendering/30526

---

## Post #1 by @thkarag (2023-07-11 17:29 UTC)

<p>Is there a way to export a stl file from volume rendering module ? I use volume rendering to make a 3D image of ultrasound scannings (ultrasound DICOM file load in 3D slicer) and I want to export this volume rendering image to stl file.<br>
I have tried to use total segmentator but, it produces a 3D model without the “details” of the image, only a colored 3D model.</p>
<p>Finally, is it possible to export a stl file of the exact same model produced using volume rendering ?</p>

---

## Post #2 by @rbumm (2023-07-11 19:31 UTC)

<p>No, that is not possible. <a href="https://discourse.slicer.org/t/how-to-export-the-volume-rendering-into-models/1019/5">Volume rendering is a display technique and no data are generated that could be exported to a model.</a></p>

---
