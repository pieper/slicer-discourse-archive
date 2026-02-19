---
topic_id: 14925
title: "Smoothing Of Stl File"
date: 2020-12-07
url: https://discourse.slicer.org/t/14925
---

# Smoothing of STL file?

**Topic ID**: 14925
**Date**: 2020-12-07
**URL**: https://discourse.slicer.org/t/smoothing-of-stl-file/14925

---

## Post #1 by @Keegan_Selig (2020-12-07 10:26 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hi there,</p>
<p>I am wondering what type of smoothing is applied to a segmentation once it is exported using the “Export to files…” function when it is exported as a STL.</p>
<p>Thanks for the help!</p>
<p>Keegan</p>

---

## Post #2 by @lassoan (2020-12-07 22:11 UTC)

<p>Binary labelmap to closed surface representation conversion rule uses <a href="https://vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html">vtkWindowedSincPolyDataFilter</a> to create a smooth polydata.</p>
<p>There is no additional smoothing performed during export. Closed surface representation is exported to file as is.</p>

---
