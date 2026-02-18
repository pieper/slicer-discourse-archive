# How does Slicer distinguish different series?

**Topic ID**: 24338
**Date**: 2022-07-16
**URL**: https://discourse.slicer.org/t/how-does-slicer-distinguish-different-series/24338

---

## Post #1 by @kaizhao (2022-07-16 08:14 UTC)

<p>I’m developing an automatic algorithm to generate 3 different parametric maps.</p>
<p>Specifically, I generate 3 different maps named <code>ktrans</code>, <code>t0</code> and <code>kep</code> maps. The generated maps are written into dicom files with <code>pydicom</code> package.<br>
I give these maps 3 different <code>SeriesDescription</code> and <code>SeriesNumber</code> fields when writing into dicom files.<br>
However, when loading these files into slicer, only the <code>ktrans</code> maps are loaded.</p>
<p>These maps can be successfully loaded with Osirix. So, is there some other fields I have to fill when writing into dicom? Which field does slicer use to identify different series?</p>

---

## Post #2 by @lassoan (2022-07-16 14:42 UTC)

<p>Do you create distinct series instance UID for each series; and distinct SOP instance UID for each file?</p>

---

## Post #3 by @kaizhao (2022-08-05 01:53 UTC)

<p>Thank you Andras!</p>
<p>After giving different values for <code>SeriesInstanceUID</code>, Slicer is able to load all the series. It seems that Slicer identifies different slices according to <code>SeriesInstanceUID</code>, not <code>SeriesNumber</code> or <code>SeriesDescription</code>.</p>

---
