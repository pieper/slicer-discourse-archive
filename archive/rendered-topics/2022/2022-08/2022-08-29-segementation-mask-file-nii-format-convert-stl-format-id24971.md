---
topic_id: 24971
title: "Segementation Mask File Nii Format Convert Stl Format"
date: 2022-08-29
url: https://discourse.slicer.org/t/24971
---

# Segementation mask file (.nii format) convert .stl format

**Topic ID**: 24971
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/segementation-mask-file-nii-format-convert-stl-format/24971

---

## Post #1 by @wawa (2022-08-29 07:02 UTC)

<p>Hi,<br>
I am able to convert my data ‘.nii’ Segementation mask files to Model ‘.stl’ files.<br>
Segementation mask files is for 3D medical images,which consists of multiple 2D slices.<br>
My Code</p>
<pre><code class="lang-auto">nii_pathname =  ...   
seg = slicer.util.loadSegmentation(nii_pathname)
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(out, segmentationNode, None, "STL")

</code></pre>
<p>I think the conversion of mask to stl is a 3D reconstruction process, I would like to know what went through in the process and what functions were used?<br>
Looking forward to your reply.</p>

---
