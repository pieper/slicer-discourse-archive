---
topic_id: 45968
title: "Nninteractive Fails To Export Segmentations"
date: 2026-01-28
url: https://discourse.slicer.org/t/45968
---

# NNInteractive fails to export segmentations

**Topic ID**: 45968
**Date**: 2026-01-28
**URL**: https://discourse.slicer.org/t/nninteractive-fails-to-export-segmentations/45968

---

## Post #1 by @doreenpa (2026-01-28 09:15 UTC)

<p>I am working with NNInteractive module in 3D slicer on 3D NRRD files (I converted from DICOM via 3D slicer itself). The module worked smoothly and nicely generated volume segmentations, but once I tried to export them through the ‘segmentations’ module, and the reference volume is assigned to the correct original image, I got the following error:<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: too many profiles<br>
[Qt] virtual double qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(vtkIdType) const : Input item is invalid<br>
[VTK] Warning: In vtkMRMLSubjectHierarchyNode.cxx, line 2156<br>
[VTK] vtkMRMLSubjectHierarchyNode (0x4ef0eb0): GetItemDataNode: Invalid item ID given</p>
<p>I would appreciate your help with this matter.</p>

---

## Post #2 by @pieper (2026-01-28 09:50 UTC)

<p>The subject hierarchy is probably getting confused.  You should be able to save using the regular Save dialog.</p>

---

## Post #3 by @doreenpa (2026-01-28 09:52 UTC)

<p>What do you mean by save using the regular Save dialog?</p>

---

## Post #4 by @pieper (2026-01-28 09:54 UTC)

<p>I mean File-&gt;Save Data</p>

---

## Post #5 by @doreenpa (2026-01-28 09:59 UTC)

<p>I will try!</p>
<p>Thanks,</p>
<p>Doreen</p>

---
