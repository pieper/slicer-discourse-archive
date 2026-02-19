---
topic_id: 35037
title: "Converting Array Of Points To Segmentation Node"
date: 2024-03-24
url: https://discourse.slicer.org/t/35037
---

# Converting Array of Points to Segmentation Node

**Topic ID**: 35037
**Date**: 2024-03-24
**URL**: https://discourse.slicer.org/t/converting-array-of-points-to-segmentation-node/35037

---

## Post #1 by @THartman (2024-03-24 02:58 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.6.1<br>
Expected behavior: I am trying to programmatically create several segments within a file, to be passed into the Vascular Modelling Toolkit in order to extract the centerlines.<br>
Actual behavior: I currently can create arrays for each vessel containing the location of every voxel within that particular vessel, but have not figured out how to convert this to a segmentation.</p>
<p>I saw that I could use a labelMapNode to create a segmentation, but am having trouble finding the best way to do this.  Any advice on this matter would be greatly appreciated.</p>

---

## Post #2 by @THartman (2024-03-24 15:21 UTC)

<p>After a few hours of tinkering yesterday, I did manage to figure out how to achieve this.  I ended up making an array matching the shape of the original volume, but making each vessel have a unique id (1-numOfVessels).  After this, I created a new vtkMRMLLabelMapNode and used the method that updates the labelmap volume based on an array before porting that labelmap into a segmentation.  Now I just need to figure out exactly how to pass these segmentations into VMTK and I should be looking good.</p>

---
