---
topic_id: 6221
title: "Anisotropic Gaussian Filtering For Python Module"
date: 2019-03-20
url: https://discourse.slicer.org/t/6221
---

# Anisotropic Gaussian Filtering for Python Module

**Topic ID**: 6221
**Date**: 2019-03-20
**URL**: https://discourse.slicer.org/t/anisotropic-gaussian-filtering-for-python-module/6221

---

## Post #1 by @Prashant_Pandey (2019-03-20 23:49 UTC)

<p>OS: Windows 10<br>
Slicer 4.8.1</p>
<p>Hi, I’m developing a python module consisting of some simple image processing. I want to implement an anisotropic 3D Gaussian filter to smooth an ultrasound sweep, but the only (already implemented) option I can is using the simpletITK and sitkUtils libraries, and these only seem to implement isotropic smoothing (same sigma in all 3 dimensions using sitk.SmoothRecursiveGaussian()). Is there an alternative function?</p>
<p>Side question, what are the units of sigma are for SmoothRecrusiveGaussian()? Are these mm or pixels? Thanks!</p>

---

## Post #2 by @lassoan (2019-03-21 03:12 UTC)

<p>Anisotropic noise filters typically adjust smoothing factor depending on image content (e.g., smoothing is applied within homogeneous regions but not at high-gradient areas, to preserve contours) and not just use a fixed smoothing factor along each image axis.</p>
<p>Since properly implemented image processing filters always operate in physical space, you can easily tune smoothing factor differently along each image axes by temporarily changing the image spacing (change the image spacing, run the smoothing filter, and revert to the original image spacing).</p>

---

## Post #3 by @Prashant_Pandey (2019-03-22 02:47 UTC)

<p>Thanks. It does seem however that SimpleITK’s Gaussian smoothing filter should accept different sigmas for different axes: <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.1.0" rel="nofollow noopener">https://github.com/SimpleITK/SimpleITK/releases/tag/v1.1.0</a> but I can’t seem to make this work.</p>

---

## Post #4 by @lassoan (2019-03-22 03:19 UTC)

<p>You can follow this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK</a></p>

---
