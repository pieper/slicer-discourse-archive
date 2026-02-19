---
topic_id: 28042
title: "Save Overlapping Segments In Binary Labelmaps Nrrd"
date: 2023-02-25
url: https://discourse.slicer.org/t/28042
---

# Save overlapping segments in binary labelmaps - Nrrd

**Topic ID**: 28042
**Date**: 2023-02-25
**URL**: https://discourse.slicer.org/t/save-overlapping-segments-in-binary-labelmaps-nrrd/28042

---

## Post #1 by @bmendes (2023-02-25 00:36 UTC)

<p>Hello everyone.<br>
What a great software Slicer is and what a great community it has. I have been using Slicer for a while for visualization and registration. But currently, I am performing a radiomic study where I believe the most efficient strategy would be to convert the structures in the RT_STRUCT file to an NRRD (I have multiple patients and would like to perform the features extraction from all at once). In radiotherapy, some structures overlap, such as the CTV and PTV. Converting the visible segments to a binary label map saves only the intersection (as expected since it is binary). Is it possible to save the structures of the RT_STRUCT file to a single NRRD volume with overlaps? The idea is to open it with SimpleITK and select the desired label.<br>
Thank you</p>

---

## Post #2 by @lassoan (2023-02-25 00:44 UTC)

<p>Segmentation (with or without overlapping segments) is always saved into a single nrrd file. When segments overlap then Slicer automatically adds a 4th dimension (“layer”) to the volume. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html#segmentation-labelmap-file-format-seg-nrrd">here</a>.</p>
<p>You can conveniently get segments from such 4D nrrd files conveniently with the <a href="https://github.com/lassoan/slicerio">slicerio Python package</a>. The package can look up label value and layer index for a specific segment and get the segment as a numpy array.</p>

---

## Post #3 by @bmendes (2023-02-25 18:37 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you for your quick reply. I did follow your recommendation in a previous post, <a href="https://discourse.slicer.org/t/how-can-i-convert-an-rtstruct-to-an-nrrd/539/2">https://discourse.slicer.org/t/how-can-i-convert-an-rtstruct-to-an-nrrd/539/2</a>, and I was able to save a 4D volume. The problem is we can’t reference the CT volume, and the number of images doesn’t match the number of masks, a necessary condition for PyRadiomics. Exporting to a file in the segmentations module does not save overlapping segments but provides the ability to reference a volume. I will try the slicerio Python package as you recommended since it seems very promising.</p>

---

## Post #4 by @lassoan (2023-02-25 18:43 UTC)

<p>If your segmentation’s geometry does not match the CT geometry then you can click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">“Specify geometry” button</a> in Segment Editor and choose the CT as source geometry.</p>

---

## Post #5 by @bmendes (2023-02-25 19:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you so much for your support. It did the trick. And the slicerio package is a very useful utility. Highly recommended it.</p>

---

## Post #6 by @bmendes (2023-02-27 16:09 UTC)

<p>For future reference and for someone with the same issue, to align the geometries of both volumes (CT + label map), we need to do the following:</p>
<blockquote>
<p>image_vol = sitk.ReadImage(ct_nrrd_file_path)<br>
origin = image_vol.GetOrigin()<br>
spacing = image_vol.GetSpacing()<br>
direction = image_vol.GetDirection()<br>
segmentation_info = slicerio.read_segmentation_info(label_nrrd_path)<br>
voxels, header = nrrd.read(label_path)<br>
extracted_voxels, extracted_header = slicerio.extract_segments(voxels, header, segmentation_info, [(‘label_name’, label_value)])<br>
label_map = sitk.GetImageFromArray(np.swapaxes(extracted_voxels.astype(np.uint16),0,2))<br>
label_map.SetOrigin((origin[0], origin[1], origin[2]))<br>
label_map.SetSpacing((spacing[0], spacing[1], spacing[2]))<br>
label_map.SetDirection(direction)</p>
</blockquote>

---
