---
topic_id: 1134
title: "Calculating Volume Of Ct Images"
date: 2017-09-27
url: https://discourse.slicer.org/t/1134
---

# Calculating volume of CT images

**Topic ID**: 1134
**Date**: 2017-09-27
**URL**: https://discourse.slicer.org/t/calculating-volume-of-ct-images/1134

---

## Post #1 by @mbura4 (2017-09-27 16:32 UTC)

<p>Operating system: Mac OS El Capitan<br>
Slicer version: 4.7</p>
<p>Hello, I am new to Slicer and I am trying to calculate volumes of maxillary sinuses. I have multiple axial slices, 1 mm each. Is there a simple way to calculate the volume of each slice of this irregularly shaped cavity and be able to add them up?</p>

---

## Post #2 by @lassoan (2017-09-29 00:32 UTC)

<p>Yes. You can use Segment Editor module to segment the structure and then use Segment statistics module to compute volume.</p>

---
