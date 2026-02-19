---
topic_id: 15103
title: "Peritumoral Volume Segmentation"
date: 2020-12-17
url: https://discourse.slicer.org/t/15103
---

# Peritumoral volume segmentation

**Topic ID**: 15103
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/peritumoral-volume-segmentation/15103

---

## Post #1 by @jianyuan (2020-12-17 00:45 UTC)

<p>Hi,<br>
I want to delineate peritumoral volume using my 3D-slicer.</p>
<p>The segmentation of tumor has been conducted  along the boundary of pulmonary nodules (the gray area in the picture). Now I wonder whether the volume can be dilated 10 mm (or 20mm) (the blue area in the picture) in three dimensions uniformly based on the tumor boundary? And then I intend to save tumor volume and peritumoral volume respectively.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d0a0e0e2fc5380d8c20ff3a5771074518cc368b.png" alt="image" data-base62-sha1="aZwj516y8oQc7dc6cIi0XKIksB5" width="319" height="242"></p>

---

## Post #2 by @lassoan (2020-12-17 00:51 UTC)

<p>Yes, you can use Margin effect to dilate a segment by a margin. You probably want to make a copy of the GTV before you grow it, and set Masking/Modify other segments to “Allow overlap” to allow the GTV and PTV segments to overlap.</p>
<p>If you want to restrict margin growing to be inside the lungs, you can segment the lungs using Lung CT segmenter module (provided by <a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">LungCTAnalyzer extension</a>), import the lung segment into your segmentation, and choose it as Editable area in Masking section when you use the Margin effect.</p>

---

## Post #3 by @jianyuan (2020-12-17 01:19 UTC)

<p>I could not find Margin effect and LungCTAnalyzer extension in my 3D slicer (version 4.10.2). should I update a latest version?</p>

---

## Post #4 by @lassoan (2020-12-17 02:18 UTC)

<p>Yes, you always need to use the latest stable or latest preview release.</p>

---
