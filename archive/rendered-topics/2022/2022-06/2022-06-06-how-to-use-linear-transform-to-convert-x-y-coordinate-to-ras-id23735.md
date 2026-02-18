# How to use linear transform to convert X,Y Coordinate to RAS coordinates

**Topic ID**: 23735
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/how-to-use-linear-transform-to-convert-x-y-coordinate-to-ras-coordinates/23735

---

## Post #1 by @minhtan16 (2022-06-06 13:58 UTC)

<p>Hi everyone,</p>
<p>I have multiples 2D coordinates (X,Y). These coordinates are all mapped by a linear transform in which I have access. I’m wondering if there’s a way to convert a 2D coordinates using the linear transform matrix to RAS programatically using python.</p>
<p>For exemple, my 2D coordinate would look like this [220, 100] and my linear transform matrix :<br>
[-0.28146, 0.958297, 0.0494615, 142.429, 0.955756, 0.275374, 0.103442, 134.392, 0.0855075, 0.0763878, -0.993405, -37.0582, 0, 0, 0, 1]</p>
<p>I want to convert my coordinate to RAS so I can then programatically display <strong>segmentations</strong> in 3D.<br>
I’m new to slicer and is wondering if this is possible to do?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @cpinter (2022-06-07 10:43 UTC)

<p>You can get the xy to RAS transform for a given slice view from the slice node, using this function: <a href="https://github.com/Slicer/Slicer/blob/177f3b324247de4e77d4497cc9121fe37dd5b3f3/Libs/MRML/Core/vtkMRMLSliceNode.h#L319" class="inline-onebox">Slicer/vtkMRMLSliceNode.h at 177f3b324247de4e77d4497cc9121fe37dd5b3f3 · Slicer/Slicer · GitHub</a></p>
<p>You can get the slice node like this:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-slice-orientation" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-slice-orientation</a></p>

---
