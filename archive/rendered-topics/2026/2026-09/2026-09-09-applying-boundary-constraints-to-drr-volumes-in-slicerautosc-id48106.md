---
topic_id: 48106
title: "Applying boundary constraints to DRR volumes in SlicerAutoscoperM"
date: 2026-09-09
url: https://discourse.slicer.org/t/48106
last_bumped: 2026-09-10T07:22:41.896Z
---

# Applying boundary constraints to DRR volumes in SlicerAutoscoperM

**Topic ID**: 48106
**Date**: 2026-09-09
**URL**: https://discourse.slicer.org/t/applying-boundary-constraints-to-drr-volumes-in-slicerautoscoperm/48106

---

## Post #1 by @Dorte (2026-09-09 14:20 UTC)

<p>Hello Slicer team and Slicer community,</p>
<p>I’m working with monoplanar videoradiography, and I’m trying to reduce depth ambiguity during bone tracking.<br>
I was wondering whether SlicerAutoscoperM allows applying geometric or anatomical boundary constraints to DRR volumes.<br>
For example, is it possible to define a condition where the femur must remain between two other volumes (or within a predefined 3D region) during registration, so that the solution space is restricted and out‑of‑plane drift is reduced?</p>
<p>Any insights, existing functionality, or potential workarounds would be greatly appreciated.</p>
<p>Thanks in advance for all your input!</p>

---

## Post #2 by @HelenMarsh (2026-09-10 07:22 UTC)

<p>I’m not sure AutoscoperM exposes a hard anatomical constraint directly, but a practical workaround is to separate the problem into initialization and registration. First place the femur and the bounding volumes with landmarks or a manual transform, then run registration only in a small translation/rotation window around that pose. A cropped DRR/volume ROI can also keep unrelated anatomy from driving the metric.</p>
<p>For a true “must stay between these surfaces” rule, I’d log the candidate transform after each optimization step and reject or penalize poses whose transformed femur leaves the allowed region. Even a coarse parameter sweep with that test can show whether the ambiguity is a local-minimum problem or an underconstrained view. Recording the accepted pose and the boundary margins would make the result reproducible.</p>

---
