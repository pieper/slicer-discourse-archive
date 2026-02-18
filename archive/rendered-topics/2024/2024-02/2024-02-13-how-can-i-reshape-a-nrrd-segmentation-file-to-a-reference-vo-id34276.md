# How can I reshape a nrrd segmentation file to a reference volume shape?

**Topic ID**: 34276
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/how-can-i-reshape-a-nrrd-segmentation-file-to-a-reference-volume-shape/34276

---

## Post #1 by @binigoromillo (2024-02-13 03:05 UTC)

<p>Hi everyone! I have a big dataset that includes nifti files and their corresponding nrrd segmentation files. Most of the segmentations were exported with an older version of Slicer and without selecting a reference volume. Therefore, there’s a shape mismatch between the segmentations and the nifti volumes. I don’t want to export every case again one by one in Slicer. Is there a way that I can do this with python code?</p>

---

## Post #2 by @muratmaga (2024-02-13 04:51 UTC)

<p>check the relevant sections of the script repository. I believe everythign you need to build a python based workflow is explained there</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations</a></p>

---

## Post #3 by @binigoromillo (2024-02-14 19:50 UTC)

<p>Thank you! I’m now using the SlicerJupyter extension to run slicer code.<br>
However, I’m not able to load the segmentation.</p>
<p>seg = slicer.util.loadSegmentation(“Segmentation.seg.nrrd”)</p>
<p>RuntimeError: Failed to load node from file: Segmentation.seg.nrrd<br>
Error: Loading Segmentation.seg.nrrd -  load failed.</p>
<p>I’m able lo load it as a Volume though. But then, I can’t export the case with:<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, labelmapVolumeNode, ct)</p>
<p>because it’s expecting a vtkMRMLSegmentationNode.</p>
<p>Thank you.</p>

---

## Post #4 by @muratmaga (2024-02-14 19:59 UTC)

<p>It works for me:</p>
<p>Are you sure the filepath is correct, or indeed this is a segmentation file (as opposed to a labelmap?).</p>
<p>What happens when you drag and drop the same file in the Slicer? Does it load?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84332d89da3d6d43ef4f17ade17ff2b39c9c4fe6.png" data-download-href="/uploads/short-url/iRuFNFuPrVW6SO6sT2bYwmNdyTA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84332d89da3d6d43ef4f17ade17ff2b39c9c4fe6_2_603x500.png" alt="image" data-base62-sha1="iRuFNFuPrVW6SO6sT2bYwmNdyTA" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84332d89da3d6d43ef4f17ade17ff2b39c9c4fe6_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84332d89da3d6d43ef4f17ade17ff2b39c9c4fe6_2_904x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84332d89da3d6d43ef4f17ade17ff2b39c9c4fe6_2_1206x1000.png 2x" data-dominant-color="918B8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1472×1220 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
f</p>

---

## Post #5 by @binigoromillo (2024-02-14 20:06 UTC)

<p>yes. When I drag and drop the segmentation I get this log:</p>
<p>“Segmentation” Reader has successfully read the file “/home/blanca/Documents/3D-SAM-Slicer/Slicer-5.6.1-linux-amd64/Segmentation.seg.nrrd” “[0.07s]”</p>
<p>and my segmentation gets loaded.</p>

---

## Post #6 by @binigoromillo (2024-02-14 20:08 UTC)

<p>however, if I use the command to load the segmentation, then I get this log:</p>
<p>vtkMRMLSegmentationStorageNode::ReadDataInternal: Segmentation file ‘/home/blanca/Documents/Segmentation.seg.nrrd’ is not found while trying to read node (vtkMRMLSegmentationStorageNode1).</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node Segmentation (vtkMRMLSegmentationNode1) from filename=‘Segmentation.seg.nrrd’</p>
<p>LoadSegmentationFromFile: Error reading Segmentation.seg.nrrd</p>

---

## Post #7 by @muratmaga (2024-02-14 20:16 UTC)

<p>Path in your command line is not the same as what you have loaded when you drag and drop. Error is clear, it is not finding the file.</p>

---

## Post #8 by @binigoromillo (2024-02-14 20:29 UTC)

<p>That’s right. The current directory in my jupyter notebook with the slicer kernel is already ‘/home/blanca/Documents/3D-SAM-Slicer/Slicer-5.6.1-linux-amd64’ so I only have to give the file name (it works if I load it as a volume so it shouldn’t be a path issue).</p>

---

## Post #9 by @muratmaga (2024-02-14 20:34 UTC)

<p>I am not sure how the paths are intepreted through Jupyter Notebook, perhaps it doesn’t translate. I would suggest using the full path of the file and see it works.</p>

---

## Post #10 by @binigoromillo (2024-02-14 20:38 UTC)

<p>Thank you! I would’ve never said it wasn’t finding the path since I used the relative ct volume path and that worked…</p>

---
