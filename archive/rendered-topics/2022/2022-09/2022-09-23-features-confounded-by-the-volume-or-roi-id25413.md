---
topic_id: 25413
title: "Features Confounded By The Volume Or Roi"
date: 2022-09-23
url: https://discourse.slicer.org/t/25413
---

# Features confounded by the volume or ROI

**Topic ID**: 25413
**Date**: 2022-09-23
**URL**: https://discourse.slicer.org/t/features-confounded-by-the-volume-or-roi/25413

---

## Post #1 by @KLNU (2022-09-23 15:27 UTC)

<p>Currently, I use 3D slicer (pyradiomics plug in) to analyze myocardium of the heart (left ventricle). I draw ROI on myocardium of each time frames (total 25 frames on the same imaging plane) throughout a cardiac cycle. However, some features, such as “energy” in “first order” can be confounded by the volume. Therefore, it is not surprised that its level fluctuates within a cardiac cycle because the area of ROI keeps varies during systole and diastole. I am wondering if other features, like gray level nonuniformity, run length nonuniformity or coarseness, are also affected by the area or volume of the ROI? Are there any features that are totally independent from the area of ROI?</p>
<p>I think this issue is also important for other studies. For example, let’s say there is a feature of tumor can predict bad prognosis. If this feature is affected by tumor size, then the finding is almost meaningless because a larger tumor size is a strong predictor of bad prognosis.</p>
<p>Thanks!</p>

---

## Post #2 by @ebrahim (2022-09-25 01:21 UTC)

<p>To help the discussion, <a href="https://pyradiomics.readthedocs.io/en/latest/features.html" rel="noopener nofollow ugc">here is a link to pyradiomics feature documentation</a>; this contains the definitions of the features.</p>
<p>(Wish I could help but I’m not familiar with this library and I’m not quite understanding how the GLSZM features are defined. My only 2 cents: the definition of “energy” is straightforward and it looks like you could simply divide it by the number of voxels in the ROI in order to normalize it.)</p>

---
