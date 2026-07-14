---
topic_id: 47587
title: "Write 3D model to CT images"
date: 2026-07-10
url: https://discourse.slicer.org/t/47587
last_bumped: 2026-07-13T11:13:03.867Z
---

# Write 3D model to CT images

**Topic ID**: 47587
**Date**: 2026-07-10
**URL**: https://discourse.slicer.org/t/write-3d-model-to-ct-images/47587

---

## Post #1 by @KarelPenicka (2026-07-10 07:41 UTC)

<p>Hello gentlemen. I have a 3D model of a mirrored healthy femur proximally aligned to the operated femur. In the 3D slicer I can see the difference and how they are superimposed. But I would like to write the 3D model into a CT, upload it to the hospital system as a CT so that doctors can review it. Do you have a tip on how to write this segmentation into individual layers? I will make a label map from the model, I need to write it into each layer and export it as DICOM.</p>

---

## Post #2 by @lassoan (2026-07-12 02:47 UTC)

<p>You can export to standard DICOM Segmentation Object by following these steps in Slicer-5.12 and later:</p>
<ul>
<li>Go to <code>Data</code> module</li>
<li>Right-click on the segmentation node and select <code>Export to DICOM...</code> → by default, the export type will be <code>DICOMSegmentation</code> (if it is not, then make sure you use Slicer-5.12 or later)</li>
<li>Check the <code>Export to folder</code> checkbox and select a folder for the DICOM segmentation files</li>
<li>Click <code>Export</code></li>
</ul>
<p>If you want to push the DICOM Segmentation objects directly to the PACS then leave <code>Export to folder</code> checkbox unchecked, which will export the segmentation into the DICOM database. You can then push the segmentation directly to the PACS in the DICOM module.</p>

---

## Post #3 by @KarelPenicka (2026-07-13 07:18 UTC)

<p>Thanks for the information. This works when I want to convert the Object to DICOM. But I need to burn the Object directly into the CT. So that it is just a set of images.<br>
I tried exporting it as a Data Bundle but PACS won’t show it together.</p>

---

## Post #4 by @lassoan (2026-07-13 11:13 UTC)

<p>You can use “Mask volume” effect on Segment Editor module to burn a segment into voxels of a CT image.</p>

---
