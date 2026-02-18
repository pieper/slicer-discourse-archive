# Exporting/Saving Transformed DICOM Volumes

**Topic ID**: 29087
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/exporting-saving-transformed-dicom-volumes/29087

---

## Post #1 by @18ilyasa (2023-04-24 11:12 UTC)

<p>Hi,<br>
I’m pretty green to Slicer, so apologies if this is a naive question. I’ve applied a transform to a DICOM volume, hardened it and then saved the file (both as a nrrd and as a new dicom folder). When I open these files in Slicer as a new scene, they are in the transformed state. However when I open it in other applications (imageJ for example) it shows up in its original untransformed state. Is there a step I’m missing?</p>

---

## Post #2 by @lassoan (2023-04-24 11:20 UTC)

<p>ImageJ ignores the 3D image geometry (maybe takes into account the image origin but ignores image origin and axis directions), so it cannot be used for verifying position or orientation of medical images.</p>
<p>When you apply a linear transform to an image then you can do it losslessly: by changing the image geometry information, without touching the voxel data. This is what Slicer does by default. If you want to keep the image geometry unchanged and modify the voxel data instead then you can use any of the image resample modules in Slicer (such as <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html">this</a>).</p>

---

## Post #3 by @18ilyasa (2023-04-24 12:16 UTC)

<p>Ah, interesting. I plan to use the transformed volumes in python to apply a deformation field that I created through other means. Would it be “safe” to assume that despite not appearing as transformed in imageJ, when reading it through a package such as simpleITK that the orientation is as I set it in Slicer (w/o having to resample the images)?</p>

---

## Post #4 by @lassoan (2023-04-24 13:09 UTC)

<p>Yes, SimpleITK generally performs image processing operations in physical space, properly taking image geometry into account.</p>

---
