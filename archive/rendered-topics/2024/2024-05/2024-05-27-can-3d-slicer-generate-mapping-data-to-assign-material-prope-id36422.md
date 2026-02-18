#  can 3D Slicer generate mapping data to assign material properties?

**Topic ID**: 36422
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/can-3d-slicer-generate-mapping-data-to-assign-material-properties/36422

---

## Post #1 by @jj_J (2024-05-27 15:58 UTC)

<p>Hello, I am a beginner who has recently started using 3D Slicer. I am trying to create a bone model for fatigue analysis in FEM, and I need to separate the cortical and cancellous bone to assign different material properties. Therefore, I need to implement them separately in STL files. Could you please let me know which method I should use for this?<br>
Additionally, can 3D Slicer generate mapping data to assign material properties?</p>

---

## Post #2 by @pieper (2024-05-27 17:42 UTC)

<p>You can use the Segment Editor to define the two regions, export them as models, and then save as STL.</p>
<p>Another option would be to use the Segment Mesher extension and export a single tetrahedral mesh with a separate label field to indicate which elements correspond with which segment.</p>

---
