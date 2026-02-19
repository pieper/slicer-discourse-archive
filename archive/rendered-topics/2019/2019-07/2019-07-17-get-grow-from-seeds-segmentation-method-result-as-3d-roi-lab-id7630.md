---
topic_id: 7630
title: "Get Grow From Seeds Segmentation Method Result As 3D Roi Lab"
date: 2019-07-17
url: https://discourse.slicer.org/t/7630
---

# Get grow from seeds segmentation method result as "3D ROI label" (segmentation-label.nrrd)

**Topic ID**: 7630
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/get-grow-from-seeds-segmentation-method-result-as-3d-roi-label-segmentation-label-nrrd/7630

---

## Post #1 by @Apex (2019-07-17 14:45 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
We are trying to mark a ROI inside the lung by uploading a DCM file, choosing Segment Editor Module. First we select respective Master volume and Source geometry. After which we Add required number of Segments_xx, paint and grow from seeds. To save the changes we then go to Segmentations module and choose “Export/import models and labelmaps”. There we select “Export and labelmap” and finally press “Export”. Then a new Output node (segmentation-label) is generated. We try to save the same Output node.nrrd (segmentation-label.nrrd) file to save the labels.</p>
<p>Actually, we require the labels of entire 3D ROI but when we are trying to save segmentation-label.nrrd we are getting only labels of seed points which we marked before growing from seeds. We also tried saving “segmentation.seg.nrrd” but it didn’t solve. Then we used “segmentation preview.seg.nrrd” the 3D region is shown but the image dimensions are different (from original 512x512) because of which we cannot overlay to get all the 3D label locations.<br>
Please let me know the proper procedure to get entire 3D ROI “segmentation-label.nrrd” file when we use grow from seeds technique.</p>

---

## Post #2 by @pieper (2019-07-17 15:01 UTC)

<p>Hi - it sounds like maybe you didn’t click “Apply” in the Grow From Seeds step?</p>

---

## Post #3 by @Apex (2019-07-18 07:07 UTC)

<p>It’s working now, thank you. Is there a way to correct previously marked files. I mean a possible way to “Apply” now in the previous files I saved. Or the only way is to redo the segmentation?</p>

---

## Post #4 by @pieper (2019-07-18 11:59 UTC)

<p>Great.  You can reload the seeds and use them, should be no problem.</p>

---
