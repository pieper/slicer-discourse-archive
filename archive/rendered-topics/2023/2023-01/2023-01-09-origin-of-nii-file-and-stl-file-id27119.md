# Origin of nii file and STL file

**Topic ID**: 27119
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/origin-of-nii-file-and-stl-file/27119

---

## Post #1 by @fluidko (2023-01-09 01:29 UTC)

<p>I have to export my segmentation with forms of both nii file and STL file.<br>
But when I open nii file in Ansys Ensight and STL file in Spaceclaim,<br>
position of origin varies between them so it is hard to specify certatin position.<br>
How can I unify origin of nii file and STL file?<br>
Thank you~!</p>

---

## Post #2 by @pieper (2023-01-09 20:07 UTC)

<p>Both nii and stl formats are underspecified, which leads to interoperability issues like what you are seeing.  Probably it’s an issue with <a href="https://www.slicer.org/wiki/Coordinate_systems">LPS and RAS</a> which you can control in the model export step in the Segmentations module.  But it might also have to do with the units (mm vs meter) or something else.  The Slicer files will be well formed so you should talk with Ansys about what format they require.</p>

---
