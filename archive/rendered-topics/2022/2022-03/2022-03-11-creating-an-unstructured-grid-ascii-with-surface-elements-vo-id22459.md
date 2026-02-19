---
topic_id: 22459
title: "Creating An Unstructured Grid Ascii With Surface Elements Vo"
date: 2022-03-11
url: https://discourse.slicer.org/t/22459
---

# creating an unstructured grid (ascii) with surface elements, volume and points

**Topic ID**: 22459
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/creating-an-unstructured-grid-ascii-with-surface-elements-volume-and-points/22459

---

## Post #1 by @oliver_gruhn (2022-03-11 16:33 UTC)

<p>Dear Slicer Team, dear Slicer community</p>
<p>i am working on a monte carlo simulation on soft tissue analysis including Slicer.<br>
For the last weeks I tried to find a solution for the upcoming issue that I hope you can help me with.</p>
<p>The MonteCarlo simulation software ValoMC needs *.vol data, including surface elements, volume elements and point data for running the analysis.</p>
<p>As far as I know the segment data exported by 3D-Slicer is saved as *.vtk (unstructured ascii grid). The meshgrid can be created by Cleaver, including volume and points, or TetGen, including surface and points.<br>
Combining single handedly isn’t possible as well, because the data doesn’t seem to have relatable bounds.</p>
<p>The conversion from *.vtk to *.vol is no problem, but with the surface elements or volume data missing ValoMC refuses to work.</p>
<p>Is this an already known problem you already know a workaround for, or would you have any suggestions that could help?</p>
<p>Thank you very much in advance!</p>
<p>greetings</p>
<p>Oliver Gruhn</p>

---

## Post #2 by @lassoan (2022-03-13 05:40 UTC)

<p>You can use “Probe Volume with Model” module to add a volume’s voxel values to a tetrahedral mesh (e.g., created by Segment Mesher), but I’m not sure if ValoMC can use that mesh.</p>
<p>ValoMC website has an example of how you can <a href="https://inverselight.github.io/ValoMC/voxeltest.html">use voxel data to create tetrahedral mesh</a> and then use it in ValoMC. If you have trouble following that then probably the best would be to contact the ValoMC community. Please let us know what you find out.</p>

---
