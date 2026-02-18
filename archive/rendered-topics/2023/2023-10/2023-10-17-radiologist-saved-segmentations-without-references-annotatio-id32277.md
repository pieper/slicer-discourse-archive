# Radiologist saved segmentations without references -> annotations come out cropped when loading as numpy arrays

**Topic ID**: 32277
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/radiologist-saved-segmentations-without-references-annotations-come-out-cropped-when-loading-as-numpy-arrays/32277

---

## Post #1 by @neuronflow (2023-10-17 15:30 UTC)

<p>Dear forum,</p>
<p>My dear radiologists saved all the segmentations they created without a reference as compressed niftis. Therefore, all the annotations appear cropped if I load them as numpy arrays using nibabel.</p>
<p>My image data is 240x240x192; however, when loading the images they appear with varying sizes cropped around the actual annotations.</p>
<p><strong>How can I load numpy arrays from the with the proper dimensions of the reference image and in the correct location?</strong></p>
<p>Probably, the necessary information is saved somewhere in the header because I can still open the images with slicer and they show up correctly.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @pieper (2023-10-18 14:21 UTC)

<p>You can write a script in Slicer to export the segmentations with respect to a reference geometry, e.g. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">like this</a>.</p>

---
