# About paintApply method in qSlicerSegmentEditorScissorsEffect.cxx

**Topic ID**: 28835
**Date**: 2023-04-11
**URL**: https://discourse.slicer.org/t/about-paintapply-method-in-qslicersegmenteditorscissorseffect-cxx/28835

---

## Post #1 by @dbtruong (2023-04-11 04:42 UTC)

<p>Hello<br>
What does qSlicerSegmentEditorScissorsEffectPrivate::paintApply method does in qSlicerSegmentEditorScissorsEffect.cxx ?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2023-04-11 04:44 UTC)

<p>The method adds the painted region to the current segment and removes it from all other segments (taking into account masking settings).</p>

---

## Post #3 by @dbtruong (2023-04-12 01:48 UTC)

<p>How to remove it from all other segments?</p>

---

## Post #4 by @lassoan (2023-04-12 16:29 UTC)

<p>You can attach a debugger and step through the code to see how it is done exactly. It is a very complex process because segments are stored in multiple layers in a 4D array and there are several masking options.</p>

---

## Post #5 by @dbtruong (2023-04-13 09:28 UTC)

<p>Can you for me some ideas when I crop by operation: fill inside, shape: free-form and slice cut: unlimited?</p>

---
