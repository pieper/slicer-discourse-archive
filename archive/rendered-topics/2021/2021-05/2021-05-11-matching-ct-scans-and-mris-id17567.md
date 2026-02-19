---
topic_id: 17567
title: "Matching Ct Scans And Mris"
date: 2021-05-11
url: https://discourse.slicer.org/t/17567
---

# Matching CT scans and MRIs

**Topic ID**: 17567
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/matching-ct-scans-and-mris/17567

---

## Post #1 by @Vincebisca (2021-05-11 10:24 UTC)

<p>Hello everyone,</p>
<p>I have been wondering : is there a way to match IRM and CT scans sequences in 3D Slicer?<br>
I explain : I have been working for a few weeks on 3D Slicer and I am exploring the possibility of using two sequences in parallel for segmentation. For example, to segment a bone tumor, using a CT scan to model the bone, and an MRI for the tumor and soft tissues.</p>
<p>Are they dedicated features to use 2 sequences? If the CT and MRI sequences are not well aligned, is there a procedure to match them well for segmentation?</p>
<p>Thanks !</p>

---

## Post #2 by @lassoan (2021-05-13 06:19 UTC)

<p>You can align MR and CT scans fully automatically using intensity-based registration as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">here</a>.</p>

---
