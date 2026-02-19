---
topic_id: 7253
title: "How To Match Mri From Different Series"
date: 2019-06-20
url: https://discourse.slicer.org/t/7253
---

# How to match MRI from different series?

**Topic ID**: 7253
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/how-to-match-mri-from-different-series/7253

---

## Post #1 by @Tangtangyinghuochong (2019-06-20 02:00 UTC)

<p>Hi Dear developers and users.</p>
<p>I am delineating the ROI（Tumor） in abdominal MRIs and then extract the radiomics features for further search.</p>
<p>The tumor boundary is very clear in some series(for example, T2 TRA) but blurry on other series(DWI etc).So I wish I can segment the ROI in “clear” series, and then “copy” the segmentation to the other series then finish the feature extraction . But different MRI series cannot match very well. After “copy” of ’segmentation, the new segmentation cannot cover the real tumor area in “blurry” series. How to match MRI from different series?</p>

---

## Post #2 by @pieper (2019-06-20 19:28 UTC)

<p>If the series are part of the same study then they should have the same Frame of Reference UID at the dicom level, meaning they are in the same space.  But if the patient moved then yes, the tumor can shift too and you may be able to compensate for the motion with registration.  Have a look at the examples here to get some ideas:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary</a></p>

---
