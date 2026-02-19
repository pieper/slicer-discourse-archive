---
topic_id: 5228
title: "Dicom Image Intensity Rescaling Using Non Linear Regression"
date: 2018-12-30
url: https://discourse.slicer.org/t/5228
---

# DICOM image intensity rescaling using non-linear regression based fitting

**Topic ID**: 5228
**Date**: 2018-12-30
**URL**: https://discourse.slicer.org/t/dicom-image-intensity-rescaling-using-non-linear-regression-based-fitting/5228

---

## Post #1 by @michael (2018-12-30 14:02 UTC)

<p>Hi everybody !</p>
<p>I want to perform a value conversion on a DICOM image by solving an equation with 2 unknown variables (a and b) :<br>
output value = (a - input value) / (b + input value)</p>
<p>To do that we decided to perform least-square error minimization with non linear regression based on levenberg-marquardt model</p>
<p>To calibrate the model we have to use 2 segmentation volumes in the image were the value is fixed to calibrate the model.</p>
<p>Any advice for this? Thank for your help</p>

---

## Post #2 by @lassoan (2018-12-30 14:42 UTC)

<p>You can use arrayFromVolume and arrayFromSegment methods to get voxels as numpy arrays. You can find examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">script repository</a>.</p>
<p>You can implement the computation in Jupyter notebook using <a href="https://github.com/Slicer/SlicerJupyter/" rel="nofollow noopener">Slicer Jupyter notebook</a> or as scripted module.</p>

---

## Post #3 by @michael (2018-12-30 16:46 UTC)

<p>Hi thank for your help !</p>
<p>Do you think it is easier (for code) to use DICOM mask OR segmentation volume to identify “calibration volume”?</p>

---

## Post #4 by @lassoan (2018-12-30 17:24 UTC)

<p>What do you mean by DICOM mask and segmentation volume?</p>

---

## Post #5 by @michael (2018-12-30 17:32 UTC)

<p>i mean link the algorythm with DICOM mask=(image?) or link on segmentations (contours?)</p>

---

## Post #6 by @lassoan (2018-12-30 17:45 UTC)

<p>There are many ways to store segmentation in DICOM. Slicer can import DICOM RT Structure Set or DICOM Segmentation Object information objects.</p>

---

## Post #7 by @michael (2018-12-30 18:01 UTC)

<p>yes i can use all : RT structures Set, binary label map but is it better to use “masked image”</p>

---

## Post #8 by @lassoan (2018-12-30 18:29 UTC)

<p>RT structure set is somewhat less deterministic (due to complex rasterization procedure that includes contour interpolation, branching, end-capping, keyhole resolution), but in most cases they should give equivalent results.</p>

---

## Post #9 by @michael (2018-12-30 19:25 UTC)

<p>Ok i prefer to use RT STRUCTURE SET !</p>
<p>I ve found this function what to you think about?</p>
<p><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html" class="onebox" target="_blank" rel="nofollow noopener">https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html</a></p>

---

## Post #10 by @lassoan (2018-12-31 22:57 UTC)

<p>scipy.optimize.least_squares function is suitable for non-linear curve fitting.</p>

---

## Post #11 by @michael (2019-01-01 12:11 UTC)

<p>is is better than arrayFromVolume and arrayFromSegment methods you describe me previously?</p>

---

## Post #12 by @lassoan (2019-01-01 14:18 UTC)

<p>You first need to get data using arrayFrom* methods, probably apply some masking operation, and finally fit your model using least_squares or similar method.</p>

---
