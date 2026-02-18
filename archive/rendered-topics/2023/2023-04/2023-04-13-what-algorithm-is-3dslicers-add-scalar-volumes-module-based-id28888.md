# what algorithm is 3Dslicer's Add Scalar Volumes module based on for image fusion?

**Topic ID**: 28888
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/what-algorithm-is-3dslicers-add-scalar-volumes-module-based-on-for-image-fusion/28888

---

## Post #1 by @ending (2023-04-13 14:08 UTC)

<p>I have a question for everyone<br>
what algorithm is 3Dslicer’s Add Scalar Volumes module based on for image fusion?</p>

---

## Post #2 by @Sam_Horvath (2023-04-13 14:12 UTC)

<p>The code for the module can be found here:<br>
<a href="https://github.com/Slicer/Slicer/blob/fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64/Modules/CLI/AddScalarVolumes/AddScalarVolumes.cxx#L34" class="inline-onebox">Slicer/AddScalarVolumes.cxx at fd7b4f3cceba976aabeb2e1cdda9ecc685fc0c64 · Slicer/Slicer · GitHub</a>.</p>
<p>It uses an ITK filter to add the images. The specific ITK filter used is the <a href="https://itk.org/Doxygen/html/classitk_1_1ConstrainedValueAdditionImageFilter.html">ConstrainedValueAdditionImageFilter</a>.</p>

---

## Post #3 by @ending (2023-04-13 14:18 UTC)

<p>Thank you for your timely answer, your answer solved the problem I encountered during the research.<br>
In addition, can I extract features in the image of PET and CT fusion, is this feasible in research?<br>
Looking forward to your reply！</p>

---

## Post #4 by @Sam_Horvath (2023-04-13 14:30 UTC)

<p>For PET/CT feature extraction, I think the starting point would by <a href="https://github.com/AIM-Harvard/SlicerRadiomics">SlicerRadiomics / pyradiomics</a>.  It should be available in the current preview build (except for macOS).</p>

---

## Post #5 by @ending (2023-04-13 14:34 UTC)

<p>Thanks！<br>
sorry, maybe I didn’t make the question clear, I mean can I extract features separately in the three images of PET, CT, PET/CT fusion images?<br>
Looking forward to your reply！</p>

---
