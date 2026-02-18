# NIFTI data batch pcocessing

**Topic ID**: 14698
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/nifti-data-batch-pcocessing/14698

---

## Post #1 by @Legendsevl (2020-11-20 02:09 UTC)

<p>3D slicer uses Slicer Radiology and NVIDIA AIAA extension to achieve good results in image feature extraction, image segmentation and other fields. However, these extensions usually deal with a single medical image ( nii.gz ）,When a large amount of data is used for feature extraction or segmentation, such as the data of 10000 patients(10000 nii .gz), is there a batch processing method that can process multiple data at a time instead of processing them one by one in 3D slicer extensions?</p>

---

## Post #2 by @lassoan (2020-11-20 04:56 UTC)

<p>3D Slicer does not add significant overhead to the segmentation and other processing, and you can use it to process tens of thousands of images using Python scripting. You can probably speed up the processing by running 5-10 Slicer instances in parallel (using Python subprocess or Qt QProcess; you can get Slicer executable path by calling <code>slicer.app.applicationFilePath()</code>).</p>

---

## Post #3 by @Legendsevl (2020-11-20 07:01 UTC)

<p>Thanks for your reply, but I’m not familiar with the operations you mentioned. Could you provide some references, such as documents or videos,  it would be very grateful</p>

---

## Post #4 by @muratmaga (2020-11-20 07:09 UTC)

<p>Slicer uses Python3, for which you can find tons of tutorials online.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">Here is slicer specific Python script examples</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="noopener nofollow ugc">And there is more in here</a></p>

---

## Post #5 by @Legendsevl (2020-11-20 07:22 UTC)

<p>Ok,thanks for your reply</p>

---
