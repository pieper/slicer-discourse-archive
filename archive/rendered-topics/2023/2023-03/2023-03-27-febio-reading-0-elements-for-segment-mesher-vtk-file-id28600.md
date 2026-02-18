# FEbio reading 0 elements for Segment Mesher vtk file

**Topic ID**: 28600
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/febio-reading-0-elements-for-segment-mesher-vtk-file/28600

---

## Post #1 by @fea_99 (2023-03-27 17:33 UTC)

<p>Apologies, this question may be better for the FEbio community, but I am currently awaiting approval to access their support forum.</p>
<p>Essentially I created a mesh using segment mesher (cleaver) of a vertebrae. I then exported this mesh as a vtk file (unchecked compress), and FEBio accepts in the file. However, FEbio registers the mesh as having 0 faces or elements, and is only able to read in the number of nodes.</p>
<p>Any idea on what may cause this to be the case?<br>
The vtk of the mesh can be found on drive <a href="https://drive.google.com/file/d/1ZUARVqyGUKIiwbzxXRZSbQsPw1kcI1XX/view?usp=sharing" rel="noopener nofollow ugc">here</a></p>

---

## Post #2 by @lassoan (2023-03-28 05:07 UTC)

<p>The file you linked to is corrupted. it only contains some point data. SegmentMesher with Cleaver generates an unstructured grid like <a href="https://1drv.ms/u/s!Arm_AFxB9yqHy4dnjUZ_kf9_-6xuTQ?e=9R8xp4">this one</a>.</p>

---

## Post #3 by @fea_99 (2023-03-29 15:09 UTC)

<p>Thank you, I wasn’t sure if it was my VTK file, or something else. If anyone else has a similar issue with a generated VTK, make sure you don’t export directly from the data module.</p>
<p>You have to use the save option in the top left, then in the window that pops up hit “show options”, and next to the file you want to save, turn off “compress”.</p>

---
