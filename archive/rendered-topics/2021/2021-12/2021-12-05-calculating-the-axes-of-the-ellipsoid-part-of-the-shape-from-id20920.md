# Calculating the axes of the ellipsoid part of the shape from l=1 coefficients

**Topic ID**: 20920
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/calculating-the-axes-of-the-ellipsoid-part-of-the-shape-from-l-1-coefficients/20920

---

## Post #1 by @hcc (2021-12-05 22:04 UTC)

<p>Hi there, really enjoying using the great tools of SPHARM-PDM.</p>
<p>I just wanted to know how I could go about finding the 3 axes of the ellipsoid part of my shape in object space (not for alignment purposes, rather for some other downstream analysis). I have computed all of the coefficients using SPHARM-PDM (positive ‘m’ only, as I believe is the case for this package), but can’t find anywhere how I would then compute the ellipsoid axes from the l=1 coefficients. I’m thinking it must be possible, since each set of l=1 coefficients uniquely map to an ellipsoid shape. The eigenvectors of a matrix containing these coefficients seems intuitive, but I can’t find a formula in any of the papers I’ve searched through.</p>
<p>Thank you very much in advance.</p>

---

## Post #2 by @styner (2021-12-05 22:41 UTC)

<p>Took me down memory lane a bit:<br>
The corresponding code related to this is located in ParametricMeshToSPHARMSpatialObjectFilter.cxx  - RotateParametricMesh (here on GitHub <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Algorithms/ParametricMeshToSPHARMSpatialObjectFilter.cxx" class="inline-onebox" rel="noopener nofollow ugc">SPHARM-PDM/ParametricMeshToSPHARMSpatialObjectFilter.cxx at master · NIRALUser/SPHARM-PDM · GitHub</a> ). That function shows you how to set up the matrix from the l=1 coefficients. The eigenvectors &amp; eigenvalues of that matrix are the axes of the ellipsoid.<br>
see also:<br>
Brechbühler, Ch., Gerig, G. &amp; Kübler, O. Parametrization of Closed Surfaces for 3-D Shape Description. Comput Vis Image Und 61, 154–170 (1995).<br>
Look at page 162</p>
<p>Hope this helps<br>
Martin</p>

---

## Post #3 by @hcc (2021-12-07 11:54 UTC)

<p>Dear Dr Styner,</p>
<p>Good memories only I hope! Ah fantastic, that works perfectly. Thank you very much.</p>

---
