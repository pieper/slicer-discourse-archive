---
topic_id: 39461
title: "Problem With Uploading Jpeg Files Pc"
date: 2024-10-01
url: https://discourse.slicer.org/t/39461
---

# Problem with uploading .JPEG Files (PC)

**Topic ID**: 39461
**Date**: 2024-10-01
**URL**: https://discourse.slicer.org/t/problem-with-uploading-jpeg-files-pc/39461

---

## Post #1 by @caboj (2024-10-01 04:38 UTC)

<p>Operating system: PC<br>
Slicer version: 5.6.2<br>
Expected behavior: Uploading CT scans from .JPEG stacks<br>
Actual behavior: Unable to process</p>
<p>Hello,</p>
<p>I am a new 3D slicer user, attempting to use the program to measure volume of kidney stones from several CT scans. I am having problems being able to upload the CT scans into the 3D slicer program. Our imaging application at my institution allows export of CT slices in .JPEG format. I have perused several tutorials and have followed the basic guidance of selecting the first image in the series and making sure “Single Image” is unchecked. The upload process then slowly progresses (CT images, including axial, coronal, and sagittal images) are processed, but then once it hits 100%, it spits out an error message saying the images could not be uploaded. I am sure I am doing something incorrectly in processing the images, but I am not sure what that might be. I have also tried uploading just the axial images, but this yields the same error message.</p>
<p>Would appreciate any guidance or resources regarding uploading/processing CT scans with 3 series into 3D slicer. Thank you!</p>

---

## Post #2 by @lassoan (2024-10-01 04:48 UTC)

<p>Most likely some images in the series have different size. You can use <code>Image Stacks</code> module in <code>SlicerMorph</code> extension to get more information and faster loading.</p>
<p>If you want to measure volume then I would strongly recommend getting the DICOM images, not just these screenshots. For example, the jpegs use only 8-bit images, so you lose significant dynamic range compared to the original CT’s 16 bits per pixel. Also, you don’t know the spacing between pixels and slices, which are critical for volume computation. If you collect your data as part of a research study then you can request access to the DICOM data.</p>

---
