---
topic_id: 1764
title: "Converting Mrtrix Connectome Model To Stl For 3D Printing"
date: 2018-01-05
url: https://discourse.slicer.org/t/1764
---

# Converting MRtrix connectome model to .stl for 3D printing

**Topic ID**: 1764
**Date**: 2018-01-05
**URL**: https://discourse.slicer.org/t/converting-mrtrix-connectome-model-to-stl-for-3d-printing/1764

---

## Post #1 by @Lena13 (2018-01-05 12:38 UTC)

<p>Hi, I created a whole brain connectome in MRtrix, which I converted to a .vtk file. I can open the file in Slicer,  but when I save it as an .stl file, that file seems to be corrupted as I can’t open it with any software (meshlab, paraview…). Is there an easy way to export fiber bundles as stl or obj files for 3D printing?</p>
<p>Cheers, Lena</p>

---

## Post #2 by @lassoan (2018-01-05 13:49 UTC)

<p>You may use these code snippets to export scene content to STL:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color</a></p>

---
