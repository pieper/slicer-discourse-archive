# PET/CT Standardized_uptake_value_body_weight series

**Topic ID**: 14898
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/pet-ct-standardized-uptake-value-body-weight-series/14898

---

## Post #1 by @Jakub_Mitura (2020-12-05 15:45 UTC)

<p>Hello When I upload the PET/CT dicom data (exported from syngo via) I get Standardized_uptake_value_body_weight series  that is not in the series i imported - so I presume it is genereted by slicer - so just to be sure each voxel is standardized in such view - given activity, atenuation and body weigths are taken into account? Can I interpolate it with CT and export interpolated file? Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ccc0b55a9c2720b9c9170e2b332af9160cd3280.png" data-download-href="/uploads/short-url/mn5EbOwZJCQBqpNi8YR58dzqm7S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccc0b55a9c2720b9c9170e2b332af9160cd3280_2_690x290.png" alt="image" data-base62-sha1="mn5EbOwZJCQBqpNi8YR58dzqm7S" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccc0b55a9c2720b9c9170e2b332af9160cd3280_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccc0b55a9c2720b9c9170e2b332af9160cd3280_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccc0b55a9c2720b9c9170e2b332af9160cd3280_2_1380x580.png 2x" data-dominant-color="EAEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1923×811 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
on the left series that I am talking about on the right names of important series for reference here is a<br>
link to the study that I am analyzing if needed<br>
<a href="https://drive.google.com/drive/folders/1leE7X9US0j5ZZcVO0GIa8y6MCOQE7fau?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1leE7X9US0j5ZZcVO0GIa8y6MCOQE7fau?usp=sharing</a><br>
Slicer - 4.11.20200930<br>
Extensions - AnglePlanes; dcmqi; petPhantom; PETDICOMExtension;PetSpectAnalysis; PETTumorSegmentation; QuantitativeReporting; SlicerDevelopmentToolbox;SlicerVMTK<br>
System - clear Linux</p>

---

## Post #2 by @pieper (2020-12-05 17:25 UTC)

<p>Hi -</p>
<p>The PET calculations are documented here: <a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/PETDICOM">https://www.slicer.org/wiki/Documentation/4.10/Extensions/PETDICOM</a></p>
<p>When you say “interpolate and export” what are you trying to accomplish?</p>

---

## Post #3 by @Jakub_Mitura (2020-12-05 17:34 UTC)

<p>Thanks! Ok now IT is clear frankly i was unsure what part of slider is responsible to get IT, i AM thinking about weather there is any anatomic interpolation that will correct slight movements of patient between pet and ct ? And is IT possible to visualize joined PET CT? (I AM afraid that IT is possible only with longitudinal pet plugin which seems to no konger exist in extension card) so then i can export IT for futher processing</p>

---

## Post #4 by @lassoan (2020-12-05 18:43 UTC)

<p>You can show PET/CT volumes blended together by <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">choosing one as foreground volume and the other as background volume in the slice viewer</a>.</p>

---
