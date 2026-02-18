# load surface in 3dSlicer 4.10.2

**Topic ID**: 12257
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/load-surface-in-3dslicer-4-10-2/12257

---

## Post #1 by @Patricia_Pais (2020-06-28 19:02 UTC)

<p>Operating system: Ubuntu 18.04.4<br>
Slicer version: 4.10.2<br>
Expected behavior: I would like to load a surface generated with freesurfer (e.g., lh.pial) and apply an overlay to it (e.g., overlayInPial.mgh).<br>
Actual behavior: I cannot find the option to load the surface (in a tutorial of 3dSlicer 3.4, I’ve seen that the corresponding module is “models”, but I don’t see any option to load a new model or surface in 4.10.2).<br>
Thanks!</p>

---

## Post #2 by @lassoan (2020-07-01 00:44 UTC)

<p>FreeSurfer support has been hugely improved in Slicer-4.11, so install this version and SlicerFreeSurfer extension. You can find file import tutorial on the extension’s webpage: <a href="https://github.com/PerkLab/SlicerFreeSurfer/wiki/Tutorials">https://github.com/PerkLab/SlicerFreeSurfer/wiki/Tutorials</a></p>

---

## Post #3 by @Patricia_Pais (2020-07-02 11:37 UTC)

<p>Thanks! Also I realized I can just drag the files in 4.10.2, but they must be converted to .vtk.<br>
Best,</p>

---

## Post #4 by @lassoan (2020-07-02 13:52 UTC)

<p>Yes, you can load surface meshes in vtk, vtp, vtu, stl, ply, obj formats by simple drag-and-drop.</p>
<p>Unfortunately, FreeSurfer chose to encode mesh coordinates in a way that it is not possible to recover the true mesh point positions without also having access to the corresponding image. So, if you want to get surfaces and image in the same coordinate system then you need to use the FreeSurfer importer in Slicer-4.11. The importer also makes is easier to load many overlays.</p>

---
