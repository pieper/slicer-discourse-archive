---
topic_id: 17950
title: "Perform Cortical And Trabecular Bone Segmentation Of A Talus"
date: 2021-06-04
url: https://discourse.slicer.org/t/17950
---

# Perform cortical and  trabecular bone segmentation of a Talus bone to generate a 2body STL file

**Topic ID**: 17950
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/perform-cortical-and-trabecular-bone-segmentation-of-a-talus-bone-to-generate-a-2body-stl-file/17950

---

## Post #1 by @Manav_Kothari (2021-06-04 13:35 UTC)

<p>I apologise for being extremely naive in the field of biomechanics and radiology but I need to extract a 3D model of Talus bone from a CT scan of a foot. So far I have been successful in segmenting the outer structure of Talus bone from the DICOM file which has provided me with a 1 body 3D CAD model. However, as you might be aware, the Talus bone comprises the outer cortical bone with an inner Trabecular bone. So I would like to get a 3D CAD model containing 2 different bodies (one of each bone) with a considerable amount of accuracy. Kindly help me understand the steps that I need to follow in Slicer software to achieve the same.<br>
Thank You</p>

---

## Post #2 by @lassoan (2021-06-08 23:47 UTC)

<p>You can easily create a fixed-thickness segment to represent the cortical bone:</p>
<ul>
<li>create a new segment</li>
<li>click Logical operators effect, Copy operation, choose the first segment to copy from, and click Apply</li>
<li>click Margin effect, Shrink operation, type the thickness into Margin size, then click Apply</li>
</ul>
<p>An alternative approach is to create a volumetric mesh (using SegmentMesher extension), and set CT density values as point data in each point of the mesh (using Probe Volume with Model volume). I think FEBio Studio can load these meshes and use the CT density values to vary material properties across the mesh.</p>

---

## Post #3 by @lassoan (2021-07-18 03:15 UTC)

<p>You can use the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">“fill holes inside bones” Python script</a> to fill these holes fully automatically.</p>

---
