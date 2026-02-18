# Oral scan ply file, teeth segmentation

**Topic ID**: 45614
**Date**: 2025-12-27
**URL**: https://discourse.slicer.org/t/oral-scan-ply-file-teeth-segmentation/45614

---

## Post #1 by @saeed_46 (2025-12-27 02:43 UTC)

<p>Hello<br>
I have some oral scan files in ply format and I want to automatically segment and extract all the healthy and prepared teeth and save each one in a separate ply file. Is this possible in 3D Slicer software?<br>
If so, please explain the steps to do it.</p>

---

## Post #2 by @cpinter (2026-01-13 11:45 UTC)

<p>Here is this module, not sure if it still works<br>
<a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg">https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg</a></p>
<p>We tried to find reliable alternative methods for surface segmentation and also training our own models, but this segmenting surface meshes is a difficult topic.</p>

---
