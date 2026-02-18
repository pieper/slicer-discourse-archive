# Some loss for convert the stl model to the editable binary labelmap

**Topic ID**: 17987
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/some-loss-for-convert-the-stl-model-to-the-editable-binary-labelmap/17987

---

## Post #1 by @xiang_luo (2021-06-07 02:46 UTC)

<p>When i import a .stl file by the import data module, there is no anything unusual for the model visualization. But when i want to edit it for some fixed, i convert it to the binary label map and segmentation node, then set them as “master volume” and “segmentation node” separately in the segmentation node. And i find there some thin struture vessel disappear when i use the “Island-Keep largest island”. I don’t know why this happend, can you fix this?</p>

---

## Post #2 by @lassoan (2021-06-07 03:30 UTC)

<p>When a segmentation is edited, then it is converted to binary labelmap representation. By default this labelmap is converted to about 16 million voxels, which may or may not be enough to preserve all details that you are interested in. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">increase the binary labelmap resolution</a> to address this.</p>

---
