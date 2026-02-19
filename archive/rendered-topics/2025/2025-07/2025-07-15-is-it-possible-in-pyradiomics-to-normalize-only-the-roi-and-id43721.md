---
topic_id: 43721
title: "Is It Possible In Pyradiomics To Normalize Only The Roi And"
date: 2025-07-15
url: https://discourse.slicer.org/t/43721
---

# Is it possible in pyradiomics to normalize only the ROI and not the entire image?

**Topic ID**: 43721
**Date**: 2025-07-15
**URL**: https://discourse.slicer.org/t/is-it-possible-in-pyradiomics-to-normalize-only-the-roi-and-not-the-entire-image/43721

---

## Post #1 by @Alessandro_Ghilardi (2025-07-15 04:26 UTC)

<p>I need to know if there’s a standard way to normalize only the ROI. I tried to create a function to do so but in this case filtered versions of the image would be calculated only after the ROI normalization (which means generate filtered version of the image processing the result of image*mask, the one with black pixels out of the ROI)</p>
<p>I think PyRadiomics follows this logic:<br>
Image → Normalization of the entire image (optional) → Apply filters → Calculate features in the ROI</p>
<p>But I need this:<br>
Apply filters → Normalize only the ROI → Calculate features in the ROI</p>

---
