---
topic_id: 5809
title: "Export Pixel Values For Specific Segmentation In Text File"
date: 2019-02-17
url: https://discourse.slicer.org/t/5809
---

# Export pixel values for specific segmentation in text file

**Topic ID**: 5809
**Date**: 2019-02-17
**URL**: https://discourse.slicer.org/t/export-pixel-values-for-specific-segmentation-in-text-file/5809

---

## Post #1 by @CostasP (2019-02-17 18:32 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.0</p>
<p>Hello, I am a new user and currently segmenting a ct dicom file. I am trying to export a .txt file with the pixel values of the segmented volume, in order to define spatially varying material properties in simulations. I wonder if such a feature is available. It may be something quite simple but I have not managed to resolve it yet. Thanks in advance for your input.</p>

---

## Post #2 by @lassoan (2019-02-17 18:51 UTC)

<p>Reading voxel values from text file would be 10-100x slower than reading from a binary file. Why would you like to write to text file instead the current binary format? What software will read the file?</p>

---

## Post #3 by @CostasP (2019-02-17 21:32 UTC)

<p>Thanks for the immediate response. I have segmented the CT data and exported the segmented volume in stl file. The stl was imported in comsol and now I need to define material properties as functions of spatial coordinates (within the same segment/domain). The property value for each spatial coordinate will be derived from the corresponding voxel value through a correlation function, so this is why I think that the text file is required. Of course maybe a better approach that I am not aware of is available.</p>

---
