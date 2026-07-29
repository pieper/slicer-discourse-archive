---
topic_id: 45801
title: "Aligning CBCT & intraoral scan"
date: 2026-01-16
url: https://discourse.slicer.org/t/45801
last_bumped: 2026-07-28T19:47:30.392Z
---

# Aligning CBCT & intraoral scan

**Topic ID**: 45801
**Date**: 2026-01-16
**URL**: https://discourse.slicer.org/t/aligning-cbct-intraoral-scan/45801

---

## Post #1 by @Aiden (2026-01-16 21:47 UTC)

<p>I have a STL from an intraoral scan with 3shape, and a CBCT in dicom. How can I align these semi automatically using a few manual landmarks?</p>
<p>What I have:</p>
<p>1x Skull CBCT dicom (edit: I also have a segmentation of this from DentalSegmentator)</p>
<p>3x stl files from intraoral scan. 1 upper, 1 lower, 1 bite.</p>
<p>I want to align the upper intraoral scan to the upper jaw/teeth from the CBCT.</p>

---

## Post #2 by @abhijeet2410 (2026-07-23 01:24 UTC)

<p><strong>Have you found a solution? Thank  you</strong></p>

---

## Post #3 by @mikebind (2026-07-28 19:47 UTC)

<p>The easiest approach is fiducial registration.  Create two markups points nodes and place at least 3 landmark points on the CBCT in one points node, and then place the corresponding points (in the same order) on the STL.  Open the “Fiducial Registration” module, and select one landmark set as the fixed landmarks, the other as the moving landmarks, and create a new transform to hold the registration transform matrix, and then click Apply.  Lastly, apply the resulting transform to the CT or model associated with the “Moving” landmarks to view the alignment.</p>
<p>If you want a fully automated process, then you need to have a method of automatically choosing the points to align, which is much more complicated.</p>

---
