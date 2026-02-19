---
topic_id: 7007
title: "How Save Segmentation Data"
date: 2019-06-03
url: https://discourse.slicer.org/t/7007
---

# How save segmentation data?

**Topic ID**: 7007
**Date**: 2019-06-03
**URL**: https://discourse.slicer.org/t/how-save-segmentation-data/7007

---

## Post #1 by @kscript (2019-06-03 10:44 UTC)

<p>Hi</p>
<p>How i segmentation data with dicom</p>
<p>i want to make one file(seg data+dicom)</p>
<p>help me plz</p>

---

## Post #2 by @lassoan (2019-06-03 10:52 UTC)

<p>Would you like to create a single file that contain both segmentation and the input volume? Or two files (one for the segmentation, one for the volume)?</p>
<p>What format you would like to save to? What software do you plan to use to read the files?</p>

---

## Post #3 by @kscript (2019-06-03 12:15 UTC)

<p>Thanks for reply</p>
<p>i want to create single file</p>
<p>now i making a Dee Learning model used annotation data.</p>
<p>Can we make a dcm format?</p>

---

## Post #4 by @lassoan (2019-06-03 13:16 UTC)

<p>For deep learning, you typically need input input and output images separately. DICOM format is generally not supported directly by deep learning frameworks.</p>
<p>For preliminary tests, you may export data using “Screen Capture” module. For more controller data export, you can study the <a href="https://github.com/SlicerIGT/UsAnnotationExport/" rel="nofollow noopener">helper scripts for creating inputs for deep learning from Slicer scenes</a>.</p>

---

## Post #5 by @kscript (2019-06-03 23:41 UTC)

<p>Then. If i use for deep learning.<br>
i should change image type. jpg, bmp like this?</p>

---

## Post #6 by @lassoan (2019-06-04 02:22 UTC)

<p>Many deep learning examples use jpg, bmp, … files as input, so you may find it easier to quickly try these examples if you export data in the same format. However, since most medical images are 3D, they use more than 8 bits per channel, and usually single-channel, consumer file formats, such as jpg and bmp are too limited. So, for anything else than quick tests, I would recommend to save metaimage (mha), nrrd, or maybe nifti format. You can find Python readers for all these formats (e.g., in <a href="https://itk.org/" rel="nofollow noopener">ITK</a>).</p>

---
