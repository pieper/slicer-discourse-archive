---
topic_id: 488
title: "Masking In General Registration"
date: 2017-06-13
url: https://discourse.slicer.org/t/488
---

# Masking in General Registration

**Topic ID**: 488
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/masking-in-general-registration/488

---

## Post #1 by @Ivan_Hidrovo (2017-06-13 02:35 UTC)

<p>Hello community,</p>
<p>Does anybody know how to input my own created 0-1 bit mask  for general registration (BRAINS) in 3D slicer?</p>
<p>Thank you,<br>
Ivan</p>

---

## Post #2 by @lassoan (2017-06-13 11:45 UTC)

<p>In the <code>Add data</code> dialog click <code>Show options</code> checkbox, in the <code>Options</code> column that appears on the right, click <code>LabelMap</code>. This will make the volume loaded as labelmap, which can be selected as mask in General Registration.</p>

---
