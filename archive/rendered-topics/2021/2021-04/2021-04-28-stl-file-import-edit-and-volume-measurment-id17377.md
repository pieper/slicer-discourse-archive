---
topic_id: 17377
title: "Stl File Import Edit And Volume Measurment"
date: 2021-04-28
url: https://discourse.slicer.org/t/17377
---

# STL file import, edit and volume measurment

**Topic ID**: 17377
**Date**: 2021-04-28
**URL**: https://discourse.slicer.org/t/stl-file-import-edit-and-volume-measurment/17377

---

## Post #1 by @ashkansh (2021-04-28 23:05 UTC)

<p>Hi all,</p>
<p>I imported a .STL file as segmentation and I tried to cut a piece of the part and measure the volume of the rest.<br>
When I tried to use segment editor to use scissors, I had to define the volume as I defined it in the Specify Geometry section. Then I tried to use the scissor and faced this:</p>
<p>“Editing requires binary labelmap master representation, but currently the master representation is Closed surface. Changing the master representation requires conversion. Some details may be lost during conversion process.<br>
Change master representation to binary labelmap?”</p>
<p>when I accepted this the resulted shape kind of shrunk and I didn’t want this. Does anyone know how the segmentation could be as close as possible to the original .STL file I imported during the editing?</p>
<p>I appreciate your responses in advance.</p>

---

## Post #2 by @lassoan (2021-09-07 18:59 UTC)

<p>You can either <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">specify a sufficiently accurate labelmap geometry</a> or edit the surface mesh using Dynamic modeler module (you can do simple plane cuts) or using Combine models module (in Sandbox extensions; you can modify the mesh by subtracting or intersecting with another mesh of arbitrary shape).</p>

---
