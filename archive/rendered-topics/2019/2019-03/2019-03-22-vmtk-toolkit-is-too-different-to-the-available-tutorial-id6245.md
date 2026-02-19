---
topic_id: 6245
title: "Vmtk Toolkit Is Too Different To The Available Tutorial"
date: 2019-03-22
url: https://discourse.slicer.org/t/6245
---

# VMTK toolkit is too different to the available tutorial

**Topic ID**: 6245
**Date**: 2019-03-22
**URL**: https://discourse.slicer.org/t/vmtk-toolkit-is-too-different-to-the-available-tutorial/6245

---

## Post #1 by @Nafis_Ebrahimi (2019-03-22 03:21 UTC)

<p>Operating system:  MacOS<br>
Slicer version:  4.10.1<br>
Expected behavior: filtering the vessels.<br>
Actual behavior:</p>
<p>hello All,<br>
I am new in Slicer and working with Slicer 4.10.1 and trying to go ahead with the example prepared in the available tutorial. For the Vesselness Filtering part, it is toooo different from the tutorial. I tried to filter the vessels by adjusting the variables but nothing happened. There is no “millimeter” option anymore and I do not have any clue about voxels. would you please direct me how to set all the parameters matter in this part of VMTK toolkit? I have attached the picture showing where I am.</p>

---

## Post #2 by @spujol (2019-03-22 10:39 UTC)

<p>The minimum vessel diameter and maximum vessel diameter parameters correspond to the min and max dimensions of the vascular structures that you want to enhance. You can access the voxel size information in mm (Image Spacing) in the module Volumes.</p>
<p>The Vessel Contrast parameter corresponds to the contrast between the vascular structures and the background. The Suppress Plates and Suppress Blobs parameters let you choose the geometric shape of the vascular structures that you want to filter out (e.g. vessels vs aneurysms).</p>

---

## Post #3 by @lassoan (2019-03-22 13:50 UTC)

<p>Note that by default you don’t need to specify vessel diameter manually. If you specify a seed point and the “Compute vessel diameters and contrast from seed point” button is depressed then vessel diameters and contrast are computed automatically from the seed point that you have specified.</p>
<p>Automatic diameter detection only works reliably when there are no other structures of similar intensity nearby, so you may want to adjust the values manually. You can either compute the value as Sonia described above, or try different values and click Preview to see if it improved the results.</p>

---

## Post #4 by @Nafis_Ebrahimi (2019-03-22 16:28 UTC)

<p>Thank you for your response. I am trying to filter vessels of the whole aorta (from the top to the bottom) using a CT Scan for a patient. Applying the contrast liquid for the patient the aorta and bones have the same contrast. So, what is your suggestion to do that? when I filter it, it also highlights the vertebral column and pelvis as well. I cannot find any information on diameter seed. would you please guide me how to use it to exclude bones? will support plates and suppress blobs help? how?</p>

---

## Post #5 by @spujol (2019-03-23 13:13 UTC)

<p>To specify a seed point in the aorta, click on the arrow next to the Slicer GUI icon in the top bar menu and place the fiducial in the lumen of the aorta on a 2D slice. To measure the vessel diameter manually, select the ruler mode of the fiducial control.<br>
If you are trying to segment the abdominal and thoracic aorta, the Draw tool of the Segment Editor can be used to segment the structure in a few slices and the Fit Between Slices tool to interpolate between the segmented slices. Both tools are available in the Segment Editor.</p>

---

## Post #6 by @lassoan (2019-03-23 17:38 UTC)

<p>Vesselness enhancement is just a first (optional) step of vessel segmentation.</p>
<p>Segmenting the aorta on contrast-enhanced CT scans is not a difficult task and it should be doable without prior vessel enhancement. You can use Segment Editor directly on the CT image using Fast marching or masked Grow from seeds methods as described in the two aorta segmentation recipes available here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" rel="nofollow noopener">https://lassoan.github.io/SlicerSegmentationRecipes/</a></p>

---

## Post #7 by @Nafis_Ebrahimi (2019-03-26 20:08 UTC)

<p>Thank you Iassoan for helpful recipes. Just one more question. Will I be able to use VMTK toolkit (centerline computation) after completing aorta segmentation with this method?</p>

---

## Post #8 by @lassoan (2019-03-27 13:19 UTC)

<p>Yes, you can detect centerline on manually segmented data sets. Go to Data module, right-click on the Segmentation node, and choose “Export visible segments to models” to create a model node that “Centerline computation” module can use as input. After export is complete, hide the segmentation node so that it does interfere with further visualizations (opaque visualization of the segment would prevent you from seeing the generated centerline).</p>

---

## Post #9 by @Nafis_Ebrahimi (2019-03-28 04:51 UTC)

<p>Dear Iassoan,<br>
I have tried both recipes for aorta segmentation (fast and high-accuracy methods) with my CT data. I also cropped the volume to reduce the calculation and tried several times. However, it does not show anything. after clicking show 3D nothing happened. would you please let me know what do you think about it?</p>

---
