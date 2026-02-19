---
topic_id: 16146
title: "Export Of Binary Masks Not Working"
date: 2021-02-22
url: https://discourse.slicer.org/t/16146
---

# Export of binary masks not working

**Topic ID**: 16146
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/export-of-binary-masks-not-working/16146

---

## Post #1 by @lekremer (2021-02-22 23:16 UTC)

<p>I have created multiple segmentations on a 3D MR volume of coronal images. when creating a binary label map of the segmentation and then exporting as dicom, the number of the sequence of images correlate to the pixel value e.g. the binary mask is no longer 0 and 1’s after the 1st image, but 0 and 2 for the second image, 0 and 3 for the third image, and so onto the last segmentation number of the last image. is this a bug in exporting binary masks? it should be consistently between 0 and 1 for any DICOM export of a binary label map, but it keeps changing.</p>

---

## Post #2 by @lassoan (2021-02-22 23:23 UTC)

<p>Did you export the segmentation as fake CT/MRI volume, DICOM Segmentation object, or DICOM RT Structure Set?</p>

---

## Post #3 by @lekremer (2021-02-22 23:34 UTC)

<p>I exported the segmentation as a DICOM.</p>

---

## Post #4 by @lassoan (2021-02-22 23:42 UTC)

<p>This generates a fake CT/MRI/PET (depending on what imaging modality you choose), which has voxels that are not actually correspond to image intensity but to discrete labels.</p>
<p>Clinical imaging software will probably not like these images very much (as their content is not an actual CT/MRI/PET). For clinical software, it is better to export the segmentation as DICOM segmentation object. If you want to inject the segmentation as a CT into a surgical planning or radiation therapy treatment software then it is better if you rescale the images to have values that are expected in CT images (air=-1000, soft tissue 200-500, bones 1000-3000) before exporting to DICOM.</p>
<p>Most research software will prefer to get the segmentation in a research file format, such as NRRD or NIFTI. In this case, no DICOM export is needed.</p>

---

## Post #5 by @lekremer (2021-02-22 23:49 UTC)

<p>ok. I am using these segmentations for binary masks for texture analysis, and need each separate segmentation as a binary mask to put with its respective MRI DICOM image.</p>

---

## Post #6 by @lassoan (2021-02-23 02:52 UTC)

<p>The currently recommended way of storing segmentations (binary masks) in DICOM is Segmentation Object. If you want to make your software DICOM compliant then use DICOM segmentation objects, instead of trying to store binary masks in as MR images. While I like DICOM very much, because it allows very rich and accurate description and cross-referencing of data, DICOM is also very complex, so you need to learn a lot to be able to use it correctly. If you are not in the final stage of clinical translation but still working on development and validation of a new analysis method, then I would recommend you to defer DICOM import/export until a later time.</p>
<p>For now, you can convert DICOM to widely used research file formats, such NRRD (for general use) or NIFTI (for brain imaging only; also check out <a href="https://bids.neuroimaging.io/">BIDS</a>).</p>

---
