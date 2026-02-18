# How to open .mat file in 3D Slicer

**Topic ID**: 29960
**Date**: 2023-06-10
**URL**: https://discourse.slicer.org/t/how-to-open-mat-file-in-3d-slicer/29960

---

## Post #1 by @akmal871026 (2023-06-10 06:45 UTC)

<p>Dear All,</p>
<p>I have the file attached (you can download it thru the link). the unit in every voxel is supposed Gray (Gy).</p>
<p>Anyone can help me how to open it in 3D Slicer so that when I put the cursor on my image’s voxel, the unit appears in the data probe?</p>
<p><a href="https://drive.google.com/file/d/1NACh6380x4ROc5nw6fNKxyxj8IB6VDDP/view?usp=sharing" rel="noopener nofollow ugc">data</a></p>

---

## Post #2 by @lassoan (2023-06-10 20:31 UTC)

<p>.mat is a general container file format. For storing images, please use a standard 3D image file format, such as NRRD. You can use <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a> to write a 3D matrix into an NRRD file.</p>

---
