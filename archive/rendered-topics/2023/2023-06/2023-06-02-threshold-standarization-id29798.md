# Threshold standarization

**Topic ID**: 29798
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/threshold-standarization/29798

---

## Post #1 by @Juan (2023-06-02 12:23 UTC)

<p>Good afternoon,</p>
<p>My group is working with 3D slicer to evaluate adipose tissue with MRI (visceral and subcutaneous) and calculate volume. We are looking for changes over time in the same patients, with treatment response.</p>
<p>Maybe someone has encountered the same issue:</p>
<p>Regarding the use of threshold, The manual adjustment of the Threshold to highlight what is the adipose tissue may introduce some subjectivity and variability between studies (thus affecting volume results and impacting volume-change tracking).</p>
<p>Considering that MRI is not CT (it does not have Hounsfield units), could we use the same range of threshold in all patients to reduce variability or it needs to be manually adjusted for each study?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @pieper (2023-06-03 14:34 UTC)

<p>Yes, as you noted most MRI contrasts are non-quantitative and you cannot rely on the thresholds to identify tissue classes.  You may be better off training a model using MONAI Label or nnU-Net to segment the tissue.</p>

---
