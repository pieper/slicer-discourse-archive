---
topic_id: 21803
title: "An Error Occurs During Installation Of Shapevariationanalyze"
date: 2022-02-04
url: https://discourse.slicer.org/t/21803
---

# An error occurs during installation of ShapeVariationAnalyzer extension

**Topic ID**: 21803
**Date**: 2022-02-04
**URL**: https://discourse.slicer.org/t/an-error-occurs-during-installation-of-shapevariationanalyzer-extension/21803

---

## Post #1 by @KIM_TY (2022-02-04 16:20 UTC)

<p>Slicer 4.13.0-2022-02-02 (windows)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17fd0b8a81a7505a40cc6058f0520637b95e33e8.png" alt="20220205_011328" data-base62-sha1="3qd7XBm9QRsvfR42w0DzV4Tfp5m" width="578" height="366"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c890b90fa8091fa7a1ceccacc71763a5aaa9dde6.png" alt="20220205_011409" data-base62-sha1="sChyOggKvuE9w4VmObeouYTzflY" width="543" height="499"></p>
<p>ShapeRegressionExtension &amp; ShapeVariationAnalyzer</p>
<p>Two extension program cannot be installed.</p>
<p>An error occurs during installation.</p>

---

## Post #2 by @lassoan (2022-02-04 18:59 UTC)

<p>Thanks for reporting this, I was able to reproduce and <a href="https://github.com/Slicer/Slicer/commit/068d5450ae3045ef7f4e853d1e2a1a5814eaa2fd">fix this issue</a>. You can download these extensions tomorrow.</p>
<p>The problem was that the extension developers did not provide a homepage and icon for their extension and there was a strict check during extension installation to abort the process if these fields are missing. I’ve now updated the check to be less strict (only log warning if non-essential fields are not found).</p>

---

## Post #3 by @KIM_TY (2022-02-04 19:43 UTC)

<p>I need an extension to use R-Vessel-X, but I haven’t been able to use it for weeks because it’s not ShapeRegression Extension…</p>
<p>Thank you for your quick response.</p>

---

## Post #4 by @lassoan (2022-02-09 22:54 UTC)

<p>R-Vessel-X extension <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation/blob/main/CMakeLists.txt#L13">depends on SlicerVMTK, MarkupsToModel, SegmentEditorExtraEffects, PyTorch extensions</a>. It is not related to ShapeRegression extension.</p>

---
