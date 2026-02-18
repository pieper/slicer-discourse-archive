# How to read a volumetric mesh in python?

**Topic ID**: 18974
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/how-to-read-a-volumetric-mesh-in-python/18974

---

## Post #1 by @Matheus (2021-07-29 16:54 UTC)

<p>Hello everyone!</p>
<p>I segmented some DICOM files and turned the segmentation into a volumetric mesh. I want to read and plot this file correctly in python. Can you tell me how to do this the best way without losing information?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-07-29 22:10 UTC)

<p>You can use the VTK Python bindings to access the data in the mesh.</p>

---

## Post #3 by @Matheus (2021-08-02 18:17 UTC)

<p>Thank you Steve Piper!!</p>
<p>I’m having trouble to access the segment dimensions in the vtk file. Do you know how to do it?</p>

---
