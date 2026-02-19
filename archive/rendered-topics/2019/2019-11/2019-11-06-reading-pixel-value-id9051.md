---
topic_id: 9051
title: "Reading Pixel Value"
date: 2019-11-06
url: https://discourse.slicer.org/t/9051
---

# reading pixel value 

**Topic ID**: 9051
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/reading-pixel-value/9051

---

## Post #1 by @abir_frad (2019-11-06 23:22 UTC)

<p>Hi everyone<br>
I am using an exemple of segmentation that need a seed point<br>
and I want to manually enter the value,is it possible to read pixel value from an image directly using 3D slicer</p>

---

## Post #2 by @lassoan (2019-11-06 23:45 UTC)

<p>These examples should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates</a></p>
<p>If you have a segmentation method then you can create a plugin for conveniently accessing it from the Segment Editor. See examples <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">here</a>. Most effects use painted seed as input, but some just take a user click, while others markup points.</p>

---
