# How to see the version of vtk in slicer

**Topic ID**: 9822
**Date**: 2020-01-15
**URL**: https://discourse.slicer.org/t/how-to-see-the-version-of-vtk-in-slicer/9822

---

## Post #1 by @timeanddoctor (2020-01-15 10:23 UTC)

<p>I tried to ‘import vtk’ and then used the help(vtk), but the slicer crashed. So where can I find the vtk version of my slicer based on</p>

---

## Post #2 by @lassoan (2020-01-15 13:15 UTC)

<p><code>help(VTK) </code> prints hundreds of thousands of lines of text on the console (all documentation of all its classes), so it takes a good while to complete.</p>
<p>You can get VTK version from from <code>vtk.vtkVersion()</code>, for example: <code>vtk.vtkVersion().GetVTKMajorVersion()</code>.</p>

---
