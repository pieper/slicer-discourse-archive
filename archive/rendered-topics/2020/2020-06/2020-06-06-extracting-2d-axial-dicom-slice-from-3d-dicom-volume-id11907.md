---
topic_id: 11907
title: "Extracting 2D Axial Dicom Slice From 3D Dicom Volume"
date: 2020-06-06
url: https://discourse.slicer.org/t/11907
---

# Extracting 2D axial DICOM slice from 3D DICOM volume

**Topic ID**: 11907
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/extracting-2d-axial-dicom-slice-from-3d-dicom-volume/11907

---

## Post #1 by @Vincent_C (2020-06-06 19:50 UTC)

<p>Hi all,</p>
<p>I want to extract a single 2D axial DICOM slice from a 3D DICOM volume as a separate node. It seems this topic was covered before here <a href="https://discourse.slicer.org/t/extraction-of-2d-image-from-3d-volume/7674" class="inline-onebox">Extraction of 2D Image from 3D Volume</a>. Indeed this method works, but I am wondering if it is possible to “split” the volume to achieve a single 2D slice without having a segment define where the volume will split. Can I extract a single slice as a scalar volume?</p>
<p>Thanks</p>

---

## Post #2 by @Vincent_C (2020-06-06 20:13 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array</a> - this seems to be the answer!</p>

---

## Post #3 by @lassoan (2020-06-06 20:46 UTC)

<p>Also note that if you don’t need reformatted slices then you can simply use numpy indexing to retrieve a slice, as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_axial_slice_as_numpy_array">example</a>.</p>

---
