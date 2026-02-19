---
topic_id: 31023
title: "Failed To Load Nifti File"
date: 2023-08-07
url: https://discourse.slicer.org/t/31023
---

# Failed to load nifti file

**Topic ID**: 31023
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/failed-to-load-nifti-file/31023

---

## Post #1 by @Zeynep_Erdogan (2023-08-07 09:52 UTC)

<p>Hi Mr. Lasso, I am trying to import some NIFTI files from the total segmentator dataset in Slicer 5.2.2. But some files are not open and give an error like this:“[VTK] ReadData: This is not a nrrd file<br>
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node ct (vtkMRMLVectorVolumeNode1) from filename=‘C:/Totalsegmentator_dataset/s0000/ct.nii.gz’<br>
[VTK] vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader<br>
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node ct (vtkMRMLVectorVolumeNode2) from filename=‘C:/Totalsegmentator_dataset/s0000/ct.nii.gz’<br>
[VTK] vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = C:/Totalsegmentator_dataset/s0000/ct.nii.gz]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of C:/Totalsegmentator_dataset/s0000/ct.nii.gz [reader 0th file name = C:/Totalsegmentator_dataset/s0000/ct.nii.gz].<br>
[VTK] vtkMRMLStorageNode::ReadData: Failed to read node ct (vtkMRMLScalarVolumeNode1) from filename=‘Totalsegmentator_dataset/s0000/ct.nii.gz’<br>
[Qt] void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: “Error: Loading C:/Totalsegmentator_dataset/s0000/ct.nii.gz -  load failed.\n”” I tried the volume, segmentation, and transform options, but they’re not helping. There are 1205 files in the total segmentator dataset, but I cannot open 131 of them.  Thanks in advice</p>

---
