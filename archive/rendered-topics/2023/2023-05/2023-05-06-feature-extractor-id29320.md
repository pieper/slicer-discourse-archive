---
topic_id: 29320
title: "Feature Extractor"
date: 2023-05-06
url: https://discourse.slicer.org/t/29320
---

# Feature extractor

**Topic ID**: 29320
**Date**: 2023-05-06
**URL**: https://discourse.slicer.org/t/feature-extractor/29320

---

## Post #1 by @Benji (2023-05-06 18:37 UTC)

<p>Dear community,</p>
<p>I have little experience in coding and I am using radiomics for the first time. I tried to find the solution in the documentation, websearch etc. but was not able to.</p>
<pre><code class="lang-auto">import radiomics
from radiomics import featureextractor
from radiomics import getFeatureClasses
import SimpleITK as sitk
import numpy as np 
from matplotlib import pyplot as plt

extractor = radiomics.featureextractor.RadiomicsFeatureExtractor()

#load numpy array with a CT image of a benign and malignant tumor and corresponding image masks
image_benign = np.load('case_00044_slice_33.npy')
mask_benign = np.load('case_00044_slice_33_segmentation.npy')
image_malig = np.load('case_00202_slice_137.npy')
mask_malig = np.load('case_00202_slice_137_segmentation.npy')

#transform arrays into sitk format
sitk_benign = sitk.GetImageFromArray(image_benign)
sitk_seg_benign = sitk.GetImageFromArray(mask_benign)
sitk_malig = sitk.GetImageFromArray(image_malig)
sitk_seg_malig = sitk.GetImageFromArray(mask_malig)

#extract tumor area
new_mask = (mask_benign == 2)*mask_benign
result = extractor.getSphericityFeatureValue(sitk_benign, new_mask)
</code></pre>
<p>AttributeError: ‘RadiomicsFeatureExtractor’ object has no attribute ‘getSphericityFeatureValue’<br>
is the error I receive…</p>
<p>I tried a couple other things, but that wasn’t working either. This might be a pretty basic question, nevertheless I’d be super happy for any help!</p>
<p>Cheers,<br>
Ben</p>

---
