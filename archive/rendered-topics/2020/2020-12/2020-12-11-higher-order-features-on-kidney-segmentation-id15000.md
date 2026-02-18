# Higher order features on kidney segmentation 

**Topic ID**: 15000
**Date**: 2020-12-11
**URL**: https://discourse.slicer.org/t/higher-order-features-on-kidney-segmentation/15000

---

## Post #1 by @lekremer (2020-12-11 04:14 UTC)

<p>I am using pyradiomics to look at the texture of segmented kidney images with many cysts masked out, therefore the value being 0 anywhere in the kidney that we deem are cysts. How will this affect the GLCM and features that are spatially dependent? I do not want the features to account for any relationships to the 0 value in the image due to cysts being removed.</p>
<p>Thank you!</p>

---

## Post #2 by @JoostJM (2020-12-17 12:48 UTC)

<p>PyRadiomics requires both an image and a mask. For normalization and filter purposes, it is best to keep the image as-is, without e.g. setting the cyst values to 0.</p>
<p>GLCM texture features are only calculated using the voxels marked as being part of the ROI, here you can mask-out anything you don’t want to influence your feature value, such as cysts and/or tissue outside the kidneys.</p>
<p>“Voxels marked as part of the ROI” means that in the mask, those voxels are asigned a certain non-0 value (often “1”), which is passed as the value for setting “label” (default 1). A ROI consists of all voxels in the mask assigned that specific values. Multiple ROIs can be defined by setting different groups of voxels to different label values, and passing those different values for the “label” parameter.</p>
<p>This does not support overlapping ROIs, those can be created using Segmentations, where each ROI is not identified by the value of a voxel, but where each voxel has a vector of values, with the ith value set to 1 marking that voxel as belonging to the ith ROI.</p>

---
