---
topic_id: 12765
title: "Pet Normalisation Before Radiomics"
date: 2020-07-29
url: https://discourse.slicer.org/t/12765
---

# PET normalisation before Radiomics

**Topic ID**: 12765
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/pet-normalisation-before-radiomics/12765

---

## Post #1 by @Nora (2020-07-29 11:24 UTC)

<p>Hello All,</p>
<p>I’ve been trying to calculate the bin width for fixed bin numbers. However, some PET data range were fluctuating. Example the minimum SUV = 3274.76, and the maximum = 14063.3.</p>
<p>I looked to pyradiomics recommendations and they mentioned that: “we still recommend a fixed bin width, but with additional pre-processing (e.g. normalization) to ensure better comparability of gray values”.</p>
<p>I tried ( PETDICOM) extenstion for PET normalisation, but i’m not sure what is their normalisation range?<br>
In slicer, this extension create two files: 1- standardised_uptake_value_body_weight 2- SUVBW.<br>
they look similar(not sure what’s the different).</p>
<p>After normalisation, I’ll calculate the bin width as (max-min)/ desired number of bins<br>
Do you think this way make sense?</p>
<p>Thanks for your help,</p>

---

## Post #2 by @JoostJM (2020-07-31 04:48 UTC)

<p>Visually they look the same, but the absolute values will most likely be different.<br>
As to determining bin width, your approach should be fine, so long as it’s not recalculated for each case separately, that would be equivalent to a fixed bin count.</p>
<p>Generally, I run the batch once with just first order, and use the Range feature to get a feel for what kind of bin width I want to use (a compromise so most cases have somewhere between 10-100 bins.</p>
<p>Finally, PyRadiomics also provides built in normalization, using mean and standard deviation of the image (not just the masked region). You can enable it using setting <code>normalize</code>.</p>

---
