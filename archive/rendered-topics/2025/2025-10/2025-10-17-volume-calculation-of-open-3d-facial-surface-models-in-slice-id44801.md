---
topic_id: 44801
title: "Volume Calculation Of Open 3D Facial Surface Models In Slice"
date: 2025-10-17
url: https://discourse.slicer.org/t/44801
---

# Volume calculation of open 3D facial surface models in Slicer

**Topic ID**: 44801
**Date**: 2025-10-17
**URL**: https://discourse.slicer.org/t/volume-calculation-of-open-3d-facial-surface-models-in-slicer/44801

---

## Post #1 by @Faisal_Alshaikh (2025-10-17 18:40 UTC)

<p>Hi,<br>
is there any module in 3D Slicer that can calculate the volume of 3D facial surface models (for example .obj files from the Vectra H2 system)?<br>
These models are not closed surfaces — for example, they are open at the eyes, neck, or mouth.</p>
<p>If no such module exists, is it possible to implement this using Python inside Slicer (e.g. with vtkMassProperties or voxelization)?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2025-10-17 18:50 UTC)

<p>Yes, sure you can compute volumes from such scans. When they are imported into a segmentation in Slicer they are automatically converted into a solid object. Depending on the size and orientation of the holes, this default conversion may work well. Otherwise you may need to implement shrinkwrapping or use other mesh hole filling method (they are very simple if you are not particularly concerned about filling the holes very nicely, smoothly).</p>
<p>If you want to measure volume changes between two scans then a good approach is to register them to each other and then subtract the same base segment from them.</p>
<p>We have implemented a complete workflow for volumetric fat resorption monitoring after breast lipofilling (see some more information and links in this post: <a href="https://discourse.slicer.org/t/stl-models-alignment-and-volume-measurement/8364/16" class="inline-onebox">STL models - Alignment and Volume measurement - #16 by lassoan</a>).</p>

---
