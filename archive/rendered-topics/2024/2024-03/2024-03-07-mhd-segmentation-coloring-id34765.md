# MHD segmentation coloring

**Topic ID**: 34765
**Date**: 2024-03-07
**URL**: https://discourse.slicer.org/t/mhd-segmentation-coloring/34765

---

## Post #1 by @Gokce_Guven (2024-03-07 13:22 UTC)

<p>Hi,</p>
<p>I have segmented body parts using totalsegmentator from dicom files. I have segmentation files as nii.gz files. I have created mhd files from dicom files without resampling. To explain what I would like to do with an example: Let’s assume I want to use clavicula_right.nii.gz file to recolor the clavicula right bone in the corresponding mhd file. I would like to change the inside of the bone to 3000 HU value and outside of the bone to -1024 . How can I do that? Would you show me the way to do that?</p>
<p>Thanks in advance<br>
Operating system: Ubuntu 22.04<br>
Slicer version: 5.3.0<br>
Expected behavior:  Recolor specific region in mhd using nii.gz segmentations<br>
Actual behavior: none</p>

---

## Post #2 by @pieper (2024-03-07 13:44 UTC)

<p>It sounds like you could use the ColorizeVolume module.  It creates an rgba volume for you and you can toggle the visibility of individual segments.</p>
<p><a href="https://github.com/Slicer/VTK/pull/43#issuecomment-1752104540">https://github.com/Slicer/VTK/pull/43#issuecomment-1752104540</a></p>
<p><a href="https://github.com/Slicer/VTK/pull/43">https://github.com/Slicer/VTK/pull/43</a></p>
<p><a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">https://discourse.slicer.org/t/new-colorize-volume-module/32254</a></p>

---

## Post #4 by @Gokce_Guven (2024-03-07 14:15 UTC)

<p>Hi Steve,<br>
thanks a lot for the fast response. I would like to use HU values as coloring, not want to use RGBA values. I will ask the same question in the links you have mentioned. Do you have any suggestion for the HU value change for segmentations?</p>
<p>Thanks in advance</p>

---

## Post #5 by @pieper (2024-03-07 14:27 UTC)

<aside class="quote no-group" data-username="Gokce_Guven" data-post="4" data-topic="34765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gokce_guven/48/66833_2.png" class="avatar"> Gokce_Guven:</div>
<blockquote>
<p>HU values as coloring</p>
</blockquote>
</aside>
<p>Maybe you can explain what you mean here.  It still sounds a lot like ColorizeVolume to me.  Maybe you also want to try the Mask effect i the Segment Editor.</p>

---

## Post #6 by @Gokce_Guven (2024-03-07 15:49 UTC)

<p>I believe the issue may be related to the mask effect. Currently, I’m working with an MHD file alongside its corresponding segmentation file in NII.GZ format. My objective is to preserve the HU values (pixel values) within the MHD file for the regions delineated by the bone segmentation, while setting the values outside of this segmentation to approximate air, which is around -1024 HU for pixels. I’m seeking assistance to accomplish this using the SimpleITK and Python libraries.</p>
<p>Any guidance on this matter would be greatly appreciated. Thank you in advance for your help.</p>

---

## Post #7 by @pieper (2024-03-07 18:49 UTC)

<p>This example shows how to get the coordinates in the CT for all voxels of a given label value.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-the-values-of-all-voxels-for-a-label-value">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-the-values-of-all-voxels-for-a-label-value</a></p>
<p>Between this operation and regular numpy array assignments you should have no problem emulating the mask operation.  There are other script examples showing how to do these operations.</p>

---
