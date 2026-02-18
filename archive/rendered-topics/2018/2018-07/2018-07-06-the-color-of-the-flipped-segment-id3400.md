# The color of the flipped segment

**Topic ID**: 3400
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/the-color-of-the-flipped-segment/3400

---

## Post #1 by @esurechao (2018-07-06 12:12 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.9.0</p>
<p>I am trying to flip the segment of an organ in the 3D viewer.<br>
These are my steps:<br>
Load CT DICOM file.<br>
Use segment editor module to visualize the organ structure in the 3D viewer.<br>
Open transform module, and replace 1 with -1 in the element box (1,1) in the transform matrix.</p>
<p>The segment did flip, but the segment become black.<br>
Could I change the color of the flipped segment?<br>
Thank you very much!</p>

---

## Post #2 by @pieper (2018-07-06 14:51 UTC)

<p>If you export to a model you can use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceToolbox">Surface Toolbox</a> module to flip the normals.</p>
<p>HTH</p>

---

## Post #3 by @lassoan (2018-07-06 14:58 UTC)

<p>You may also choose to flip the master volume only. Segmentation does not have to be transformed.</p>

---
