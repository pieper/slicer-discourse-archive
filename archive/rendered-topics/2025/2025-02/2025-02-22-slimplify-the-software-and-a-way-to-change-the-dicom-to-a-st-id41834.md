# slimplify the software and a way to change the dicom to a stl file.

**Topic ID**: 41834
**Date**: 2025-02-22
**URL**: https://discourse.slicer.org/t/slimplify-the-software-and-a-way-to-change-the-dicom-to-a-stl-file/41834

---

## Post #1 by @forestiers (2025-02-22 21:07 UTC)

<p>Is there a way of making this software less complicated. I just want to be able to download my ct and mri files into the software and have a 3d image shown on the screen and then be able to convert the dicom images to a stl file so I can 3d print it.</p>
<p>Best regards<br>
Bruce</p>

---

## Post #2 by @muratmaga (2025-02-23 01:48 UTC)

<p>These are very doable and already quite simple. You need the dicom module to import the data, segment editor to create your model, and then segmentations modules to export your 3D model as an STL file. The total workflow of what you want to do is about 10-12 clicks.</p>
<p>Please find the relevant modules int the user manual: <a href="https://slicer.readthedocs.io" rel="noopener nofollow ugc">https://slicer.readthedocs.io</a></p>

---
