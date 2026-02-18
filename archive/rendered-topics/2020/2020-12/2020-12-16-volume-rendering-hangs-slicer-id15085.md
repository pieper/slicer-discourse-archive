# Volume rendering hangs Slicer

**Topic ID**: 15085
**Date**: 2020-12-16
**URL**: https://discourse.slicer.org/t/volume-rendering-hangs-slicer/15085

---

## Post #1 by @manjula (2020-12-16 09:35 UTC)

<p>System - Manjaro Linux<br>
Slicer versions - Current stable and current preview release</p>
<blockquote>
<p>[DEBUG][Qt] 16.12.2020 09:53:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “VolumeRendering”<br>
[WARNING][VTK] 16.12.2020 09:56:05 [vtkObject (0xad73ab0)] (/work/Preview/Slicer-0-build/VTK/Rendering/VolumeOpenGL2/vtkOpenGLVolumeOpacityTable.h:191) - This OpenGL implementation does not support the required texture size of 65536. Falling back to maximum allowed, 16384.This may cause an incorrect color table mapping.<br>
[WARNING][VTK] 16.12.2020 09:56:05 [vtkObject (0xa110260)] (/work/Preview/Slicer-0-build/VTK/Rendering/VolumeOpenGL2/vtkOpenGLVolumeRGBTable.h:144) - This OpenGL implementation does not support the required texture size of 65536, falling back to maximum allowed, 16384.This may cause an incorrect color table mapping.</p>
</blockquote>
<p>When I try to volume render, Slicer hangs and becomes unresponsive.  How do I fix this problem?</p>
<p>thanks</p>

---

## Post #2 by @manjula (2020-12-16 10:05 UTC)

<p>Figure that out.</p>
<p>Needed to rescale.</p>

---
