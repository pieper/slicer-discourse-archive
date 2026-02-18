# VMTK extension : build fails with VTK9

**Topic ID**: 13840
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/vmtk-extension-build-fails-with-vtk9/13840

---

## Post #1 by @chir.set (2020-10-03 16:31 UTC)

<p>Slicer builds nicely with VTK9 on Arch Linux with gcc 10.2.</p>
<p>VMTK extension fails to build with these errors :</p>
<blockquote>
<p>[ 18%] Performing configure step for ‘VMTK’<br>
loading initial cache file /home/arc/src/SlicerExtension-VMTK-SuperBuild/SlicerVmtk-build/VMTK-prefix/tmp/VMTK-cache-Release.cmake<br>
CMake Error at CMake/CMakeOptions.cmake:75 (include):<br>
include could not find load file:</p>
<pre><code>/vtkWrapPython.cmake
</code></pre>
<p>Call Stack (most recent call first):<br>
vtkVmtk/CMakeLists.txt:25 (include)</p>
</blockquote>
<blockquote>
<p>CMake Error at /home/arc/src/Slicer-SuperBuild/VTK-build/lib/cmake/vtk-9.0/vtk-config.cmake:78 (message):<br>
The new name for the ‘vtkIOImage’ component is ‘IOImage’.  By requesting at<br>
least version 8.90, the new component names are now required.<br>
Call Stack (most recent call first):<br>
/home/arc/src/Slicer-SuperBuild/VTK-build/vtk-config.cmake:1 (include)<br>
vtkVmtk/Utilities/vtkvmtkITK/CMakeLists.txt:12 (find_package)</p>
</blockquote>
<p>Can’t workaround this one.</p>
<p>Thank you for looking into it.</p>

---
