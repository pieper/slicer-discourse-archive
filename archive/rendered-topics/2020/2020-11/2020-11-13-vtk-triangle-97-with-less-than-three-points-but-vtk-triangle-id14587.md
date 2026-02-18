# VTK_TRIANGLE 97 with less than three points, but VTK_TRIANGLE needs at least three points

**Topic ID**: 14587
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/vtk-triangle-97-with-less-than-three-points-but-vtk-triangle-needs-at-least-three-points/14587

---

## Post #1 by @Anish_Basnet (2020-11-13 15:12 UTC)

<p>Hello everyone,<br>
I’d like to find intersection between two different sources. And later on apply it to a poly data that is extracted from a model node and a cube source.<br>
I was looking for a way to do it and I found a extension: <a href="https://github.com/zippy84/vtkbool" rel="noopener nofollow ugc">https://github.com/zippy84/vtkbool</a>.</p>
<p>I also found an example that uses the extension here: <a href="https://lorensen.github.io/VTKExamples/site/Cxx/PolyData/PolyDataBooleanOperationFilter/" rel="noopener nofollow ugc">https://lorensen.github.io/VTKExamples/site/Cxx/PolyData/PolyDataBooleanOperationFilter/</a></p>
<p>I am trying to test the intersection between two sphere sources, but I am getting a warning and the slicer crashes.</p>
<p>'Warning: In /home/anish/3D_Slicer_Code/Code_with_changes/Build/VTK/Common/DataModel/vtkPolyData.cxx, line 1021<br>
vtkPolyData (0x55ac4ab977d0): Building VTK_TRIANGLE 115 with less than three points, but VTK_TRIANGLE needs at least three points. Check the input.</p>
<p>error: [/home/anish/3D_Slicer_Code/Code_with_changes/Build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #2 by @lassoan (2020-11-13 16:14 UTC)

<p>It seems like the input polydata is corrupted. How did you generate it?<br>
Maybe you can fix it by using Cleaner option in Surface Toolbox module.</p>

---
