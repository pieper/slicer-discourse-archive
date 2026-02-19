---
topic_id: 10515
title: "How To Store The File After Performing Segmentation Using Nv"
date: 2020-03-03
url: https://discourse.slicer.org/t/10515
---

# How to store the file after performing segmentation using NVDIA AIAA

**Topic ID**: 10515
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/how-to-store-the-file-after-performing-segmentation-using-nvdia-aiaa/10515

---

## Post #1 by @Flash (2020-03-03 10:48 UTC)

<p>Hello,</p>
<p>I have performed segmentation using NVDIA AIAA segmentation models.<br>
It works well.<br>
However,I want to store the segmented file as nii file,as my main purpose is to use the annotated file to build an AI model using transfer learning and feeding annotated files is necessary here.</p>
<p>I am able to store the files but the files are coming in different formats after performing segmentation and one of the file which is saved as nii file is just like the input file I loaded without the segmentation parts mapped.</p>
<p>Kindly help me with this.</p>

---

## Post #2 by @lassoan (2020-03-05 02:06 UTC)

<p>First of all, do not use nifti (nii) file format, unless you work with brain imaging. Nifti is specifically developed for brain imaging, mostly for MRI, and it is <em>not</em> a general-purpose file format.</p>
<p>If you use a recent Slicer Preview Release then segmentation that does not have overlapping segments is saved into a simple 3D nrrd file, which you can read with any nrrd reader. Nrrd reader should be available in every environment where nifti reader is available.</p>
<p>If you work with brain images and you must use nifti format then you can convert the segmentation to labelmap volume by right-clicking on the segmentation in Data module. You can then save this labelmap volume in a wide variety of file formats, including nifti.</p>

---
