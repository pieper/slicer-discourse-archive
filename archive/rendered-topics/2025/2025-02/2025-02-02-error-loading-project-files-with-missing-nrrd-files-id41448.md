---
topic_id: 41448
title: "Error Loading Project Files With Missing Nrrd Files"
date: 2025-02-02
url: https://discourse.slicer.org/t/41448
---

# Error Loading Project Files with Missing .NRRD Files

**Topic ID**: 41448
**Date**: 2025-02-02
**URL**: https://discourse.slicer.org/t/error-loading-project-files-with-missing-nrrd-files/41448

---

## Post #1 by @SLDT (2025-02-02 04:00 UTC)

<p>Hello Slicer Community,</p>
<p>I have recently encountered a problem loading a few sets of project files that I had a research assistant help me to prepare last year using Slicer 5.2.2. The problem is this: when I try to open the files, the segmentation and all of the project settings load, but none of the radiographic image data do, and I receive the following error message:</p>
<blockquote>
<p>ERROR: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLStorableNode.cxx, line 326</p>
<p>vtkMRMLScalarVolumeNode (000002B894FA8690): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Image00658 (vtkMRMLScalarVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode1.</p>
</blockquote>
<p>Notably, their are a few sets of project files that load without error, and the main difference in those sets is that they each contain two .NRRD files, one smaller one, and one much larger one. The project files that throw some variation of the above error are all missing the second, larger .NRRD file, so I suspect that the issue is probably that most of the radiographic image data would be stored in the second .NRRD file. Unfortunately, the research assistant who worked on the project files originally lost the original files and has not been able to find them, so I need to find a work around to repair the project files in case I need to make any further changes to each of the segmentations myself.</p>
<p>A partial workaround I have tried is reloading the original CT data in an instance of the 3D Slicer with the corresponding segmentation also loaded. However, because each segmentation was conducted using downsampled, cropped (using the Volume ROI), and often transformed CT data, getting the reloaded files to exactly match those that I used previously has proven challenging. Does anyone here have any suggestions of how I could get these replaced elements to match (some sort of transfer process for the Volume ROI and the transforms, for example)? Or does anyone here perhaps have a more elegant solution? Any advice or suggestions would certainly be very much appreciated.</p>

---
