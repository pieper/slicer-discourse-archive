---
topic_id: 11629
title: "Default Settings For Defying Glcm Rlm"
date: 2020-05-20
url: https://discourse.slicer.org/t/11629
---

# Default settings for defying GLCM, RLM

**Topic ID**: 11629
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/default-settings-for-defying-glcm-rlm/11629

---

## Post #1 by @Bassam (2020-05-20 03:46 UTC)

<p>Hi team.</p>
<p>Kindly, I am quite a little bit confused about the default settings used for defying the gray level co-occurrence matrix (GLCM) and run length matrix as well (RLM).</p>
<p>Does the GLCM, by default, study the occurrence of pixel pairs at distance =1 and angle =0 ? and same for RLM, which angle is used by default (is it 0 angle ?)</p>
<p>Kindly, if we would like to change the angle and distance between the pixel pairs in defying these matrices, how can we do that ?</p>
<p>Thanks</p>

---

## Post #2 by @JoostJM (2020-05-23 14:12 UTC)

<p>Distances used by default is [1], but multiple can be specified. As for angles, all possible angles are used, with the ultimate feature value being the mean across features values calculated per angle. It is possible to skip angles that define an offset between slices, using force2D. It is not possible to skip specific angles.</p>
<p>If you want to calculate features for angles separately, you’ll need to create a custom feature class based on the regular GLCM/GLRLM classes. See also <a href="https://discourse.slicer.org/t/features-extraction/11047/3">this</a> post.</p>
<p>All settings, and their default values, are listed in the PyRadiomics <a>online documentation</a>.</p>

---

## Post #3 by @Bassam (2020-05-23 20:49 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> Many thanks. I will go back and read the documentation carefully. Appreciated</p>

---
