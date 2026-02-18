# Export Mask as binary tiff file 

**Topic ID**: 2329
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/export-mask-as-binary-tiff-file/2329

---

## Post #1 by @LisaWies (2018-03-15 15:51 UTC)

<p>Hi everyone,</p>
<p>I’m trying to export my generated mask as a set of binary files for each slice. How can I achieve this in Slicer?<br>
Thanks a lot for your help.</p>
<p>Best wishes,</p>
<p>Lisa</p>

---

## Post #2 by @lassoan (2018-03-15 20:59 UTC)

<p>Tiff files are not well suited for medical image computing, as they lack standard way of storing essential metadata (slice spacing, anatomical orientation, etc.), slice ordering is based on file names, which is error-prone, etc. Therefore, no software should expect to get a 3D image mask as a sequence of Tiff files.</p>
<p>If you need a set of image files for presentations (image series or video animation), then you can use Screen Capture module: Master view -&gt; one of the slice views, Animation mode -&gt; slice sweep.</p>
<p>For further image processing or analysis, I would recommend to use a standard research file format, such as nrrd or metaimage (mhd/mha). Readers are available for most programming languages and development environments. Let us know if you cannot find one.</p>

---

## Post #3 by @LisaWies (2018-04-19 07:01 UTC)

<p>Thank you very much for your help. Slice caputre was exactly what I was looking for. I need the data for the validation of an edge detection code for automatic segmentation. In this way I can comare the results obtained from the code with my manual segmentation.</p>

---
