---
topic_id: 13157
title: "Can Not Create Midbrain Surface Mesh"
date: 2020-08-25
url: https://discourse.slicer.org/t/13157
---

# can not create midbrain surface mesh

**Topic ID**: 13157
**Date**: 2020-08-25
**URL**: https://discourse.slicer.org/t/can-not-create-midbrain-surface-mesh/13157

---

## Post #1 by @Jacqueline_Zhang (2020-08-25 13:20 UTC)

<p>Operating system: WIN 10<br>
Slicer version: 4.8.1<br>
Expected behavior: Create a mesh from freesurfer segmented data<br>
Actual behavior: error message: Model Maker standard error:</p>
<p>Model scene file doesn’t exist yet: C:/Users/JACQUE~1/AppData/Local/Temp/Slicer/BHDDG_AAAAABAIFDCCJBBA.mrml<br>
Error: no model hierarchy node at ID “vtkMRMLModelHierarchyNode1”, creating one<br>
ERROR: cannot open input volume file C:/Users/JACQUE~1/AppData/Local/Temp/Slicer/BHDDG_vtkMRMLLabelMapVolumeNodeB.nrrd</p>
<p>I tried to use the 3D slicer to create a surface mesh of the midbrain. The label data is from the freesufer. and use the model maker function, the input model is the label map. and I got the error message as followed. Model Maker standard error:</p>
<p>Model scene file doesn’t exist yet: C:/Users/JACQUE~1/AppData/Local/Temp/Slicer/BHDDG_AAAAABAIFDCCJBBA.mrml<br>
Error: no model hierarchy node at ID “vtkMRMLModelHierarchyNode1”, creating one<br>
ERROR: cannot open input volume file C:/Users/JACQUE~1/AppData/Local/Temp/Slicer/BHDDG_vtkMRMLLabelMapVolumeNodeB.nrrd</p>

---

## Post #2 by @pieper (2020-08-25 13:33 UTC)

<p>Hi -</p>
<p>4.8.1 is very old and we don’t support it anymore.  Try the latest preview version from <a href="http://download.slicer.org">download.slicer.org</a> and the <a href="https://github.com/PerkLab/SlicerFreeSurfer">SlicerFreeSurfer</a> extension.</p>

---
