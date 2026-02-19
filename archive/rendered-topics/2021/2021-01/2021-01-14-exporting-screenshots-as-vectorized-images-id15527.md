---
topic_id: 15527
title: "Exporting Screenshots As Vectorized Images"
date: 2021-01-14
url: https://discourse.slicer.org/t/15527
---

# Exporting screenshots as vectorized images

**Topic ID**: 15527
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/exporting-screenshots-as-vectorized-images/15527

---

## Post #1 by @FatihSogukpinar (2021-01-14 15:27 UTC)

<p>Hi all,</p>
<p>Is it possible to export screenshots from Slicer as vectorized PDFs rather than PNGs ? As far as I know the only way to take screenshots is to use the screenshot icon but it only gives .png image.</p>
<p>Thank you and best regards.</p>

---

## Post #2 by @pieper (2021-01-14 15:48 UTC)

<p>That’s not currently an option, but someone could implement it using <a href="https://vtk.org/doc/nightly/html/.html#details"><code>vtkPDFExporter</code></a>.  It wouldn’t be too much work.</p>

---

## Post #3 by @lassoan (2021-01-14 16:33 UTC)

<p>Screenshots are always bitmaps - that’s what screens can display. PDF export of a screenshots would be a 2D image in a PDF file, which is probably not what you need.</p>
<p>vtkPDFExporter can be used to export 2D device contexts (such as plots).</p>
<p>For 3D graphics, you would not normally use PDF (it is terrible, it uses an ancient 3D mesh file format, and there has been no improvement in 3D support in PDF in the last decade), instead OBJ, PLY, STL, VTK, etc. formats are commonly used. There are desktop, mobile, web viewers for these formats.</p>
<p>What would you like to achieve?</p>

---
