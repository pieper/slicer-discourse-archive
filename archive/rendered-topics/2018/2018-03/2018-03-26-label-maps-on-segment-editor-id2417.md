---
topic_id: 2417
title: "Label Maps On Segment Editor"
date: 2018-03-26
url: https://discourse.slicer.org/t/2417
---

# Label maps on segment editor

**Topic ID**: 2417
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/label-maps-on-segment-editor/2417

---

## Post #1 by @mgastall (2018-03-26 00:09 UTC)

<p>Hello, I am drawing volumes of interest on masses on multiple different phases of contrast on MRIs. I am drawing the VOIs with segment editor and then performing texture measures with radiomics. After I have finished this, I am uploading the VOIs and mask saved in ANALYZE format to a different (non-3d slicer program) to perform a different kind of analysis. However, I am unsure what constitutes the VOIs–would it be the segmentations or the label maps?. Thank you very much.</p>

---

## Post #2 by @lassoan (2018-03-26 16:27 UTC)

<p>If you need good compatibility with other software and there are no overlapping segments then I would recommend to export your segmentation to labelmap (in Data module, right-click on your segmentation node and click “Export visible segments to binary labelmap”) and save the labelmap as a .nrrd, .mha, or, .nii file.</p>

---

## Post #3 by @feng (2018-12-29 07:55 UTC)

<p>Hi Lassoan, I was trying to save the labelmap, but after right clicking, there is only a choice of export as DICOM. how did you save it as other files?</p>

---

## Post #4 by @lassoan (2018-12-29 14:23 UTC)

<p>Use menu: File / Save to save data to files.</p>

---
