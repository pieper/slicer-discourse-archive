---
topic_id: 2133
title: "Can I Have A Boolean Operarion For Stls Directly"
date: 2018-02-21
url: https://discourse.slicer.org/t/2133
---

# Can I have a boolean operarion for STLs directly?

**Topic ID**: 2133
**Date**: 2018-02-21
**URL**: https://discourse.slicer.org/t/can-i-have-a-boolean-operarion-for-stls-directly/2133

---

## Post #1 by @timeanddoctor (2018-02-21 01:09 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
I have established two cubes by  points with the same axis.After changed into segments , this cubes can be boolean operation but there are many losed informations. I don’t know there are any way maybe some codes to bool-operate just stay in stl file?</p>

---

## Post #2 by @lassoan (2018-02-21 02:03 UTC)

<p>Boolean operations directly on meshes is one of the most complicated problems in computer graphics and in Slicer we opted to have a solution that is very robust and quite fast. The method includes a step where the mesh is rasterized into a binary labelmap, therefore you have to make sure the binary labelmap representation of the segmentation has sufficiently small spacing so that all relevant details are preserved. You can use the <code>Crop volume</code> module to create a volume with sufficiently small spacing and use the resulting volume as master volume in the segmentation.</p>

---

## Post #3 by @cpinter (2018-02-21 15:11 UTC)

<p>There are two ways you can do this easily in Slicer:</p>
<ul>
<li>Segment Morphology module in SlicerRT extension (a good choice if you want to script it and not as part of a segmentation workflow)</li>
<li>Logical operators effect in Segment Editor (I recommend this if you want to do this while segmenting, or if you want to script without relying on an extension)</li>
</ul>

---
