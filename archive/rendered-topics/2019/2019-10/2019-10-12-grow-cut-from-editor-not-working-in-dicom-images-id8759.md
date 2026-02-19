---
topic_id: 8759
title: "Grow Cut From Editor Not Working In Dicom Images"
date: 2019-10-12
url: https://discourse.slicer.org/t/8759
---

# Grow cut from editor not working in dicom images

**Topic ID**: 8759
**Date**: 2019-10-12
**URL**: https://discourse.slicer.org/t/grow-cut-from-editor-not-working-in-dicom-images/8759

---

## Post #1 by @tenzin_kunkyab (2019-10-12 21:09 UTC)

<p>Hi Lasso,</p>
<p>I hope you are doing very well, I was trying to segment a dicom with editor (GrowCut effect) not the grow from seed effect. However I get the following error.</p>
<p>GrowCut is attempted with image type ‘int’ and labelmap type ‘short’. GrowCut only works robustly with ‘short’ image and labelmap types.</p>
<p>How can I use the growcut effect from editor to work on dicom images?</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @lassoan (2019-10-13 01:52 UTC)

<p>We have fixed many issues in the old GrowCut effect (including the one that you described above), made several improvements (speed, memory usage, masking, live preview, etc) and the result is the Grow from seeds effect  Segment Editor. There is no reason to still use the legacy Editor module or the old GrowCut effect.</p>

---
