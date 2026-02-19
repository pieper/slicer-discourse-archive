---
topic_id: 38298
title: "Feature Extraction Depending On Image Type And Intensity Ran"
date: 2024-09-09
url: https://discourse.slicer.org/t/38298
---

# Feature Extraction depending on image type and intensity range

**Topic ID**: 38298
**Date**: 2024-09-09
**URL**: https://discourse.slicer.org/t/feature-extraction-depending-on-image-type-and-intensity-range/38298

---

## Post #1 by @AMM (2024-09-09 18:55 UTC)

<p>Hi,</p>
<p>I’m extracting features from MRI images. I do an initial feature extraction, followed by selection and binary classification with various machine learning models.<br>
My images are originally int16, the intensity across the dataset varies between -50 and 10000 and I set a bin width of 8. I get an AUC of 0.89.</p>
<p>However, if, for example, I do some rescaling to [0 1] and then multiply by 255 (double)  with a binwidth of 2.6 → AUC: 0.6.</p>
<p>Same data…with some alterations…</p>
<p>How can I solve this? What is the problem? I am using PyRadiomics.</p>

---
