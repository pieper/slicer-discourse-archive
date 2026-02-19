---
topic_id: 46047
title: "Calculating Difference In Dose Between Two Ct Scans"
date: 2026-02-03
url: https://discourse.slicer.org/t/46047
---

# Calculating difference in dose between two CT scans

**Topic ID**: 46047
**Date**: 2026-02-03
**URL**: https://discourse.slicer.org/t/calculating-difference-in-dose-between-two-ct-scans/46047

---

## Post #1 by @hanginghats (2026-02-03 15:34 UTC)

<p>I’m doing a project which requires me to analyse the difference in dose between two identical CT scans reconstructed with different algorithms. Is there any way for me to do this with slicer and slicerRT?</p>

---

## Post #2 by @cpinter (2026-02-05 09:25 UTC)

<p>We need more information. You don’t mention radiotherapy anywhere, so first question would be CT dose or RT dose? Please elaborate as much as possible, what kind of data do you have, what kind of comparison you want to do… Thanks.</p>

---

## Post #3 by @hanginghats (2026-02-13 06:22 UTC)

<p>I have RT dose, exported from varian eclipse TPS. I have the doses calculated using two different imaging systems and want to compare the obtained doses to ensure no big difference between them.</p>

---

## Post #4 by @lassoan (2026-02-14 05:11 UTC)

<p>After you install SlicerRT extension, you can load the dose volumes and compare them using Dose Comparison module.</p>

---
