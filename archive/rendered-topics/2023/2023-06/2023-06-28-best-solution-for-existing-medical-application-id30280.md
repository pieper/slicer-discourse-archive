# Best solution for existing medical application

**Topic ID**: 30280
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/best-solution-for-existing-medical-application/30280

---

## Post #1 by @Elena_Chu (2023-06-28 14:07 UTC)

<p>Hi,<br>
I try to find the best solution for our application. This is medical application combining WPF (UI and flow logic) and core C++. I’m looking for engine that can accomplish the next tasks: window that can be inserted into existing application (preferable inside WPF), 3d and 2d views,  ability of DICOM reading, importing existing volume and mesh data,  registration, segmentation and editing on the point level even in  3d view. As well as a small features like RAS body orientation control, some useful widgets, etc.<br>
Up to now I was thinking only about VTK, but from some answers in VTK forums I understood that a lot of functionalities I’m looking for are already implemented in 3D Slicer.  And it looks like that 3D slicer is easier to implementation.<br>
My question is: Can the 3D slicer be used for my needs or I need to be stuck to VTK ?</p>
<p>Thanks,<br>
Elena</p>

---

## Post #2 by @lassoan (2023-06-28 14:10 UTC)

<p>3D Slicer is designed exactly for the purpose that you described. You can start from the <a href="https://github.com/KitwareMedical/SlicerCAT">custom application template</a> if you want to create an application with custom branding (your logos, colors, etc.) and/or you want to simplify the user interface (hide the features that you don’t think your users will need).</p>

---
