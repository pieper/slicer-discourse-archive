---
topic_id: 19163
title: "How To Save Labelmap Information In A Volumetric Mesh"
date: 2021-08-11
url: https://discourse.slicer.org/t/19163
---

# How to save labelmap information in a volumetric mesh?

**Topic ID**: 19163
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/how-to-save-labelmap-information-in-a-volumetric-mesh/19163

---

## Post #1 by @Matheus (2021-08-11 22:57 UTC)

<p>Hello everyone!</p>
<p>I segmented some DICOM files and turned the segmentation into a volumetric mesh. I have different segments for different biological tissues and I want to store the segment ID information after transforming it into a volumetric mesh. It seems that when the .vtk file is created this information is somehow lost. I say this because when I read the file in python the mesh volume appears as just one segment. Does anyone know how to help?</p>
<p>In short: How to save labelmap information in a volumetric mesh?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-08-12 03:42 UTC)

<p>Segment ID is stored as a cell data in the mesh and it is saved into .vtk/.vtu files. If you load the mesh file and you want to see the different materials then you need to enable scalar display in Models module (and may need to cut into the mesh to see different segments).</p>

---

## Post #3 by @Matheus (2021-08-12 15:57 UTC)

<p>Thanks Andreas!<br>
That worked!</p>
<p>I still need to extract the node, face and element information (uchar format) from .vtk file. Do you know how I can do this in python? (I’m trying to use meshio or pymesh)</p>

---

## Post #4 by @lassoan (2021-08-12 17:12 UTC)

<p>You can get point (node) positions as numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">arrayFromModelPoints</a>, material ID from cell data using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelCellData">arrayFromModelCellData</a>, etc. If you want to access more mesh properties, cell connectivity, etc. then you can do it by a few lines of Python code - see examples <a href="https://github.com/Slicer/Slicer/blob/1a692bf36e9c99c47661fbf5fdba0fd3c3e72f95/Base/Python/slicer/util.py#L1494-L1507">here</a>.</p>

---

## Post #5 by @Matheus (2021-08-17 12:52 UTC)

<p>Thanks Andreas!</p>
<p>I still need one more thing: where do I get the modelNode information?</p>

---

## Post #6 by @lassoan (2021-08-17 18:01 UTC)

<p>For testing, you can get modelNode by node name, for example <code>modelNode = getNode('MyNodeName')</code>. In a module typically users choose input/output nodes using node selector widgets.</p>

---
