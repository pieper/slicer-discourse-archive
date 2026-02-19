---
topic_id: 17134
title: "Intensity Resampling In Slicerradiomicc"
date: 2021-04-16
url: https://discourse.slicer.org/t/17134
---

# Intensity Resampling in SlicerRadiomicc

**Topic ID**: 17134
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/intensity-resampling-in-slicerradiomicc/17134

---

## Post #1 by @Giada_Fiore (2021-04-16 15:52 UTC)

<p>Hi, I’m working with CT images in Slicer Radiomics, but I have a doubt: is intensity resampling absolute or relative to ROI? I have set a fixed bin length. Thank you!</p>

---

## Post #2 by @JoostJM (2022-01-11 12:14 UTC)

<p>I assume you refer to normalization, this is relative to the image.</p>
<p>Still, you indicate you use a fixed bin length (fixed bin count). This normalizes the intensities to the ROI, but only for those features that use a discretized image (i.e. the texture features). There is much documentation on why this is not recommended.</p>

---
