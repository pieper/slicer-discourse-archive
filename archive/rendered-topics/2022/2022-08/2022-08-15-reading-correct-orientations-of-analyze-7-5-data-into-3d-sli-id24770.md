---
topic_id: 24770
title: "Reading Correct Orientations Of Analyze 7 5 Data Into 3D Sli"
date: 2022-08-15
url: https://discourse.slicer.org/t/24770
---

# Reading correct orientations of Analyze 7.5 data into 3D Slicer

**Topic ID**: 24770
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/reading-correct-orientations-of-analyze-7-5-data-into-3d-slicer/24770

---

## Post #1 by @jsother (2022-08-15 19:18 UTC)

<p>Problem report for Slicer 5.0.2 win-amd64: [please describe expected and actual behavior]</p>
<p>When loading an axial Analyze 7.5 dataset (*.img, *.hdr), anterior/posterior directions are incorrectly flipped.  I know documentation says “Image orientation is specified ambiguously in this format, therefore its use is strongly discouraged,”  however this is a fairly easy fix for what is likely the most common orientation.  Can a patch be drafted or is there some global import setting I am overlooking?</p>
<p>JS</p>

---

## Post #2 by @muratmaga (2022-08-15 21:37 UTC)

<p>I highly suspect anyone would spend any time to create a patch for such old format.</p>
<p>If you are certain the flip is in A/P axis, you can create a transform matrix in which the third diagonal element is -1, assign your volume to it, harden the transform (right click in the data) and save it as nrrd.</p>

---
