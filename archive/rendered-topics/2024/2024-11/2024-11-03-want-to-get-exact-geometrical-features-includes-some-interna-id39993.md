# Want to get exact geometrical features (includes some internal voids in the CT-scanned volume) with mesh for FE analysis via Abaqus.

**Topic ID**: 39993
**Date**: 2024-11-03
**URL**: https://discourse.slicer.org/t/want-to-get-exact-geometrical-features-includes-some-internal-voids-in-the-ct-scanned-volume-with-mesh-for-fe-analysis-via-abaqus/39993

---

## Post #1 by @SKarmakar (2024-11-03 02:55 UTC)

<p>Hello everyone,<br>
By using a 3D slicer, I only have a surface mesh of a CT-scanned structure. However, The structure includes some internal defects like voids; hence, those details should be included in the structure while imported for FE analysis (using Abaqus). How the volumetric mesh data can be imported in Abaqus compatible format for FE analysis?<br>
Kindly support me with the required steps for doing the same and suggest the name of the required plug-in to the 3D slicer or any external software.</p>
<p>Best Regards,<br>
Souvik</p>

---

## Post #2 by @pieper (2024-11-03 16:30 UTC)

<p>Have a look at this extension: <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a></p>

---
