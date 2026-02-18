# How to Debug? GDB Not Recognizing Source Files for 3D Slicer Debug Build

**Topic ID**: 35098
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/how-to-debug-gdb-not-recognizing-source-files-for-3d-slicer-debug-build/35098

---

## Post #1 by @Aram_Harutyunyan (2024-03-26 12:09 UTC)

<p>I’m using the debug build of 3D Slicer for enhanced debugging capabilities but face issues with GDB not recognizing some source files, hindering my debugging. Despite building 3D Slicer with debug flags and attempting to set breakpoints in specific files like <code>/slicer/Slicer/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsLineNode.cxx</code> , GDB fails to recognize these files, asking to make breakpoints pending on future shared library loads. This approach hasn’t resolved the issue. It’s confusing why GDB inconsistently recognizes source files despite being in debug mode. I’m using the <code>SlicerApp-real</code> binary for debugging, which differs from the regular release <code>Slicer</code> binary. I need an advice on debugging this project or at least understanding the cause of these issues. Attempts to debug with QT on Ubuntu 20.04 resulted in errors, preventing QT from running the project. What can I try to debug Slicer 3D to?</p>

---

## Post #2 by @RafaelPalomar (2024-03-26 13:29 UTC)

<p><a class="mention" href="/u/aram_harutyunyan">@Aram_Harutyunyan</a>, the bottom line is that Slicer uses a launcher that sets the environment and runs SlicerApp-real. There is a few ways one can go about debuggin Slicer in here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging on GNU/Linux systems — 3D Slicer documentation</a></p>

---
