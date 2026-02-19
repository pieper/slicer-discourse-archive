---
topic_id: 10573
title: "Apply Bspline Transformation In Matlab"
date: 2020-03-06
url: https://discourse.slicer.org/t/10573
---

# Apply BSpline transformation in MATLAB

**Topic ID**: 10573
**Date**: 2020-03-06
**URL**: https://discourse.slicer.org/t/apply-bspline-transformation-in-matlab/10573

---

## Post #1 by @Farah (2020-03-06 02:02 UTC)

<p>Hi,<br>
I have registered two CT scans using non-rigid registration and got a bspline transform as .h5 file.<br>
I applied this transform on my segmented geometry using 3Dslicer but I want to apply this transform on point set using MATLAB.<br>
I have read the the transform components using MATLAB, it gave me two groups each group has 3 data sets: TranformFixedParameters, TranformParameters, and TransformType.<br>
could you tell me what each data set contain ?<br>
Many thanks,<br>
Farah</p>

---

## Post #2 by @lassoan (2020-03-06 02:45 UTC)

<p>This is an ITK transform, see its documentation <a href="https://itk.org/Doxygen/html/classitk_1_1BSplineTransform.html">here</a>. If you have further questions, then you can ask on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>
<p>Why would you consider using Matlab? Have you tried implementing the features you need in Python instead? FYI, Slicer has a built-in interactive Python environment (press Ctrl-3 to bring up the console), with a number of packages pre-installed and you can install any other package that you might need. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">here</a>.</p>

---
