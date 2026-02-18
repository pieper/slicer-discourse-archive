# Saving RTSTRUCT Nodes as Nifti Files

**Topic ID**: 24843
**Date**: 2022-08-20
**URL**: https://discourse.slicer.org/t/saving-rtstruct-nodes-as-nifti-files/24843

---

## Post #1 by @enamdar (2022-08-20 07:27 UTC)

<p>Hi everyone.<br>
I have loaded a patient volume, its segmentation, and the corresponding RTSTURCT.<br>
I need to save the components of the RTSTRUCT as separate nifti files using the python command line, but I have no idea how I can do that.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27357fb69cc330cb9dea27bba4f9d9fb587c2f51.png" alt="Screenshot from 2022-08-19 23-00-23" data-base62-sha1="5ARf0TOSKGqxE3LIenSDaYXiZbj" width="454" height="224"></p>

---

## Post #2 by @enamdar (2022-08-24 20:52 UTC)

<p>I figured it out.<br>
First, a for loop was needed over the visible segment ids.<br>
Then the following two commands to export the segments:</p>
<blockquote>
<p>slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segIds, labelmapVolumeNode, referenceVolumeNode)</p>
</blockquote>
<blockquote>
<p>slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(dst_patient_dir, segmentationNode, segIds, “seg.nii.gz”, True)</p>
</blockquote>
<p>Exporting the volume was the most straightforward part. slicer.util.exportNode does the job.</p>

---
