---
topic_id: 10406
title: "Matching Volume Size With Linear Transformation"
date: 2020-02-23
url: https://discourse.slicer.org/t/10406
---

# Matching volume size with linear transformation

**Topic ID**: 10406
**Date**: 2020-02-23
**URL**: https://discourse.slicer.org/t/matching-volume-size-with-linear-transformation/10406

---

## Post #1 by @mbutler808 (2020-02-23 22:12 UTC)

<p>I have uCTscans of small frogs and we are trying to segment the hindlimb muscles for a study on locomotion.  They were scanned in arbitrary orientations, which make it hard to identify the muscles. I would like to transform and save the volume in a standard orientation.</p>
<p>I have been able to apply a linear transform, however, when I try to resample the original volume with <em>Resample scalar/vector/DWI volume</em> while applying the linear transform,  the resulting volume is now cropped.</p>
<p>It looks like I transformed the long, medium, and short axes of the volume but the volume remained defined in its original coordinate space, clipping part of the specimen. How do I rotate and resample the volume preserving the volume needed to capture the entire specimen?  I tried entering Manual:size values (I assumed it was pixel numbers), but it did not make a difference. I did not change the spacing leaving it as 0,0,0.</p>
<p>Thank you for your help!<br>
Marguerite</p>

---

## Post #2 by @lassoan (2020-02-24 03:30 UTC)

<p>I would recommend to use “Crop volume” module for this. You can translate either the ROI node or the volume.</p>

---
