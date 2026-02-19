---
topic_id: 30782
title: "Get The Same Array Size After Transform"
date: 2023-07-25
url: https://discourse.slicer.org/t/30782
---

# Get the same array size after transform

**Topic ID**: 30782
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/get-the-same-array-size-after-transform/30782

---

## Post #1 by @Jakub_Mitura (2023-07-25 13:35 UTC)

<p>Hello, I use Fiducial registration to obtain linear transform. I saved markup points, transform, original 3d images, and transformed 3d image (checked apply transform when saving file).</p>
<p>After applying this transform, images appearing in the slicer are well registered<br>
However, after I load them by simple itk into python they have different array sizes (one has more slices than the other)</p>
<p>Is there a way to get a uniform size for both images ? - I assume it just requires some padding- but I have no idea how to get the correct padding in this scenario.</p>
<p>thanks for any suggestions !</p>

---

## Post #2 by @pieper (2023-07-27 17:54 UTC)

<p>You can specify a reference geometry using another volume to resample with <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html">this module</a> before exporting.</p>

---
