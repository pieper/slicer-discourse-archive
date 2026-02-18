# Issue with 2D extraction and resampling

**Topic ID**: 9910
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/issue-with-2d-extraction-and-resampling/9910

---

## Post #1 by @rcuocolo (2020-01-22 20:37 UTC)

<p>Hello, I am havong an issue on PyRadiomics 2.2.0 using the terminal (Ubuntu 18.04) for batch extraction.<br>
I have images and masks in .nii.gz format, both with 1x1x3 mm voxels. I have drawn bidimensional ROIs on ITKSnap with 10x10x1 dimensions, which translate to 10x10x3 mm. Unfortunately some ROIs are also drawn on different planes (e.g. 10x1x10 mm).<br>
When extracting I tried to use force2D: true to enable shape2D features and true bidimensional extraction, only when paired with 1x1x1 resampling the process fails due to the ROI not having a z value of 1 anymore (e.g. after resampling it becomes 10x10x3). Reading the docs, it states that resampling in one of the planes should be left as 0 to keep original dimensions and only perform in-plane resampling which I suspect would solve my issue.<br>
I am not able to get the extraction to work, could someone give a parameter file example for the relevant settings to allow correct 2D extraction in a similar situation?</p>

---

## Post #2 by @fedorov (2020-01-27 20:20 UTC)

<p>Renato, can you accompany your question by a sample (de-identified) dataset?</p>

---

## Post #3 by @rcuocolo (2020-01-28 11:31 UTC)

<p>Thank you for the interest in my issue, I think it was solved.</p>
<p>The mistake was due to interpreting the orientation referred to in the documentation as “absolute” rather than relative to image acquisition orientation. Therefore, I was setting the force2Ddimension parameter wrongly in relation to the resampling. I made several tests checking the output of image and mask resegmentation to confirm my misunderstanding. Maybe this could be explained more clearly in the documentation as MRI acquisitions are often not aligned with the actual x, y and z axes of the patient, and the 2D dimensions refer to the acquisition volumes axes rather than the “true” axial, coronal and sagittal planes.</p>

---
