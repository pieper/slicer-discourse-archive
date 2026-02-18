# How to calculate 2D Radiomics features for each slice of a 3D volume with a 3D mask

**Topic ID**: 12163
**Date**: 2020-06-22
**URL**: https://discourse.slicer.org/t/how-to-calculate-2d-radiomics-features-for-each-slice-of-a-3d-volume-with-a-3d-mask/12163

---

## Post #1 by @xlucox (2020-06-22 22:47 UTC)

<p>Hi!!!</p>
<p>I’m trying to calculate the radiomics features for each slice of a 3D volume with a 3D mask.</p>
<p>I’ve been reading but nothing is very clear.</p>
<p>I wonder if I will have to split the 3D volume and the 3D mask in 2D images and then calculate the features in each 2D image.</p>
<p>I’m using 2.2.0b1 pyradiomics.</p>
<p>Thank you very much!!!.</p>

---

## Post #2 by @JoostJM (2020-06-23 09:46 UTC)

<p>This is not supported directly in PyRadiomics, though something similar is mentioned in the IBSI work document, where features can be calculated per-slice, then averaged over slices. The reason this is not implemented in PyRadiomics is that we feel it places unreasonable high emphasis on voxels located on slices with few voxels segmented (as there they have a larger influence on the calculated feature value, which are weighted equally when averaging over slices).</p>
<p>If you want to calculate this, you can use the same 3D volume, but update your mask so, that the ROI has a different label value on each slice. Then calculate features for each slice by specifying the label value for each slice in consecutive calls to featureextractor.execute. In the SlicerRadiomics module, features are calculated automatically for all available label values I believe.</p>
<p>Finally, v3.0 has been released which implements important changes.</p>

---

## Post #3 by @xlucox (2020-06-23 12:06 UTC)

<p>Thank you very much,</p>
<p>Very clear.</p>

---
