---
topic_id: 21527
title: "Segmentation Of Ct Dicoms"
date: 2022-01-19
url: https://discourse.slicer.org/t/21527
---

# Segmentation of CT Dicoms

**Topic ID**: 21527
**Date**: 2022-01-19
**URL**: https://discourse.slicer.org/t/segmentation-of-ct-dicoms/21527

---

## Post #1 by @3Dslicerhelp (2022-01-19 15:09 UTC)

<p>I uploaded a CT dicom image set into Slicer and segmented a region of interest. Now, I would like to save both my input volume and segmentation into a single file (preferably .nrrd). Is there a way I am able to do this?</p>
<p>I have attempted to export my segmentation as a labelmap; however, this only saves the segmentation without the CT dicoms. I need the 3D CT volume with the segmentation included as my label.</p>
<p>My end goal is to use these .nrrd files as inputs for a deep learning model that requires labelled image sets.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2022-01-19 16:10 UTC)

<p>A post was merged into an existing topic: <a href="/t/saving-a-segmentation-and-input-volume-in-one-file/21506">Saving a segmentation and input volume in one file</a></p>

---

## Post #3 by @cpinter (2022-01-19 16:10 UTC)



---

## Post #4 by @pieper (2022-01-19 19:59 UTC)

<p>If by “included” you mean the segmentation overlayed in color on the CT, then the Screen Capture module can work.  But it will export png as 24 bit rgb that won’t be the best for learning.  Better to use nrrd files for the CT and segmentation individually at full bit depth – have a look at MONAI for deep learning tools that work with medical formats.</p>

---
