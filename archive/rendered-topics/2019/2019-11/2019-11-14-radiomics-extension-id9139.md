# Radiomics extension

**Topic ID**: 9139
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/radiomics-extension/9139

---

## Post #1 by @tenzin_kunkyab (2019-11-14 03:01 UTC)

<p>Hi all,</p>
<p>I would like to ask what is the default slicer radiomics extension parameter settings for resampling? I mean to ask does it use sitkBspline or nearest neighbour or other ones cause I can’t specify that in the slicer but would like to know what it uses.</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @JoostJM (2019-11-14 13:06 UTC)

<p>By default, it uses sitkBSpline interpolation for the image. Interpolation for the mask is hardcoded to nearest-neighbor in PyRadiomics (and therefore also in SlicerRadiomics).</p>
<p>You can change this if you want, as SlicerRadiomics allows you to choose between manual (via the GUI, limited options) customization and customization via parameter file (the same one you use in PyRadiomics, exposes all customization options). So if you use option 2, you can set the interpolator for resampling.</p>

---

## Post #3 by @tenzin_kunkyab (2019-11-14 20:08 UTC)

<p>Hi Joost,</p>
<p>thank you so much, i would like to ask if any of the available function is bicupic interpolation function or bilinear interpolation function? I am not sure what name it corresponds to in the pyradiomics key words.</p>
<p>thanks so much,</p>
<p>best<br>
Tenzin</p>

---

## Post #4 by @JoostJM (2019-11-15 10:50 UTC)

<p>Bilinear is linear interpolation in 2 dimensions, with trilinear being in 3 dimensions. In SimpleITK (and hence, in PyRadiomics) no distinction is made in dimensionality (so it’s determined by dimensionality of input). For bi/trilinear, you’ll need ‘sitkLinear’. for bi/tricubic I think you are best off using the SimpleITK B-Spline interpolator: sitkBSpline. A full list of the possible interpolators is found <a href="https://itk.org/SimpleITKDoxygen/html/namespaceitk_1_1simple.html#a7cb1ef8bd02c669c02ea2f9f5aa374e5" rel="nofollow noopener">here</a>.</p>

---
