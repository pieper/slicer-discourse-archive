---
topic_id: 9471
title: "Volume Rendering Transfer Function"
date: 2019-12-11
url: https://discourse.slicer.org/t/9471
---

# Volume rendering transfer function

**Topic ID**: 9471
**Date**: 2019-12-11
**URL**: https://discourse.slicer.org/t/volume-rendering-transfer-function/9471

---

## Post #1 by @Yingdi_Zhang (2019-12-11 10:57 UTC)

<p>I am new to Slicer.<br>
I want to achieve a module of spine CT image 3D visualization in which voxel values greater than a threshold are regarded as a class and given a color ，while other voxels given another color.  The two classes are visualized in a 3D manner.<br>
I think volume rendering module is needed according to my requirement but I do not know how to implement it.<br>
I have read the basic tutorial of python programing in Slicer. Are there any other document should I read or some similiar project I can reference？</p>

---

## Post #2 by @lassoan (2019-12-11 14:00 UTC)

<p>Don’t worry about programming first, just get to know Slicer and use the GUI to access functions. You can threshold the image using Segment Editor. If you want to modify the volume (blank out regions in the original image in a certain intensity range) then you can use Mask volume effect in Segment Editor (available if you install SegmentEditorExtraEffects extension).</p>

---
