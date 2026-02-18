# Slicer 5.4.0 Sequence Loading Breaks

**Topic ID**: 32927
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/slicer-5-4-0-sequence-loading-breaks/32927

---

## Post #1 by @Liam_S (2023-11-21 12:14 UTC)

<p>Hi there</p>
<p>I have a 4D CT dataset, already saved as an NRRD sequence. I load it into slicer, save the case (incl. mrml file but excluding rewriting any image files) in the same working directory as the image and close slicer. When I try and load the case mrml file there is an error:</p>
<p>Error: Loading D:/seg tut/2023-11-21-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326</p>
<p>vtkMRMLScalarVolumeNode (000002654F042A40): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Image Sequences P02 (vtkMRMLScalarVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode2.</p>
<p>Is there a saving protocol I am missing? This is also happening with older cases that were previously working. In the older cases all of the segmentations and models load but just not the image sequence (all are in the same working directory).</p>
<p>Could you advise if this is a fixable problem?</p>
<p>Windows 10 Slicer v5.4.0</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2023-11-21 15:17 UTC)

<p>If you can reproduce the issue in the latest Slicer Preview Release and you can give step-by-step instructions that reproduce the issue (every click you make) then we’ll investigate.</p>

---
