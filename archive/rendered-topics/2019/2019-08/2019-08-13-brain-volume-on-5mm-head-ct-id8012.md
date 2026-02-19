---
topic_id: 8012
title: "Brain Volume On 5Mm Head Ct"
date: 2019-08-13
url: https://discourse.slicer.org/t/8012
---

# Brain Volume on 5mm Head CT

**Topic ID**: 8012
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/brain-volume-on-5mm-head-ct/8012

---

## Post #1 by @Caleb_Price (2019-08-13 18:55 UTC)

<p>Hello!</p>
<p>I’ve been struggling with finding a method to infer brain volume on clinically obtained head CTs. We have tried to segment brain tissue with the intensity tool in the editor but there is significant overlap between white matter and CSF. We have also given the Robust Statistics Segment tool a run but I’m afraid that the variation in intensity between white and gray matter may be too much for the tool to get a relatively precise segmentation.</p>
<p>Our end goal is to measure changes in brain volume across longitudinal head CTs.</p>
<p>Thanks,</p>
<p>Caleb</p>

---

## Post #2 by @lassoan (2019-08-15 16:37 UTC)

<p>I would recommend using “Grow from seeds” effect in Segment Editor module. You can find several tutorials for the Segment editor <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">here</a>.</p>

---
