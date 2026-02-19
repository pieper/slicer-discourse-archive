---
topic_id: 13529
title: "Probe Volume With Model Error"
date: 2020-09-17
url: https://discourse.slicer.org/t/13529
---

# "Probe volume with model" error

**Topic ID**: 13529
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/probe-volume-with-model-error/13529

---

## Post #1 by @janneke_slicer (2020-09-17 14:39 UTC)

<p>Hello,</p>
<p>I want to probe a displacement field (vector volume) with a model with the “Probe volume with model” module in Slicer 4.11.0. So I want that each point on the mesh/model contains the corresponding x-, y-, and z-value of the displacement field. I know it works in Slicer 4.10.2. However, when I try it in Slicer 4.11 it shows ‘Completed with errors’. It only works when I apply a volume with the vector magnitude (so not with distinct x-, y-, and z-values). Does someone know what the problem is?</p>
<p>Regards,</p>
<p>Janneke</p>

---

## Post #2 by @lassoan (2020-09-17 16:23 UTC)

<p>I was able to reproduce this. I’ll submit a fix today.</p>

---

## Post #3 by @lassoan (2020-09-17 17:51 UTC)

<p>The issue has been fixed, Slicer Preview Release that you download tomorrow or later will be able to probe a vector volume.</p>

---
