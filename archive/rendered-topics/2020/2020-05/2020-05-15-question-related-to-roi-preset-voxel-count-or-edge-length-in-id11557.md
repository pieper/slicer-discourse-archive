# Question related to ROI: preset voxel count or edge length in a square(rectangle effect) roi

**Topic ID**: 11557
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/question-related-to-roi-preset-voxel-count-or-edge-length-in-a-square-rectangle-effect-roi/11557

---

## Post #1 by @kowloon (2020-05-15 13:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
My problem is about drawing a rectangular ROI into a computed tomography. I have already drawn round ROIs, now I want to draw the same voxelcount as rectangular ROIs. With the HeterogeneityCAD I have already determined the voxel count of the round ROIs. I want to know where I can preset the edge lengths or the voxelcount for a rectangular ROI, if this is possible at all.<br>
Since I  believe that my question is very specific, I address in particular <span class="mention">@Iassoan</span> and <span class="mention">@federov</span>.<br>
Many thanks in advance!!</p>

---

## Post #2 by @lassoan (2020-05-18 18:08 UTC)

<p>If you want to specify a region of interest by a segment programmatically, then a good option is to create one using a VTK source (for example, vtkCubeSource) and import it into a segmentation (as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_histogram_of_a_segmented_region">this example</a>).</p>

---
