---
topic_id: 4768
title: "Using The Invert Displacement Field Function"
date: 2018-11-15
url: https://discourse.slicer.org/t/4768
---

# Using the invert displacement field function

**Topic ID**: 4768
**Date**: 2018-11-15
**URL**: https://discourse.slicer.org/t/using-the-invert-displacement-field-function/4768

---

## Post #1 by @RuurdK (2018-11-15 18:35 UTC)

<p>Dear all,</p>
<p>I have been using the invert button in the Transforms module to invert displacement fields which I can regrettably only derive as a forward transform. Now I am trying to replicate this inversion using ITK or SimpleITK functions, such as InverseDisplacementField, InvertDisplacementField, FixedPointInverseDisplacementField and IterativeInverseDisplacementField. However, I am never able to replicate the results I get through Slicer. If someone could explain which algorithm Slicer uses I would be most grateful.</p>
<p>Thanks in advance,</p>
<p>RK</p>

---

## Post #2 by @lassoan (2018-11-15 18:41 UTC)

<p>Slicer uses <a href="https://www.vtk.org/doc/nightly/html/classvtkAbstractTransform.html">VTK’s transform classes</a>, which are far more versatile than ITK (SimpleITK):</p>
<ul>
<li>you can concatenate arbitrary chain of forward/inverse transforms and VTK can apply it to objects dynamically</li>
<li>VTK transforms provide transformation on the entire 3D space (while in ITK transforms, displacement drops to 0 outside the specified domain)</li>
<li>VTK ensures displacement is smoothly converging 0 or constant outside the specified domain, which allows robust inverse computation.</li>
</ul>
<p>If you need an inverse transform that ITK can use, you can convert the transform to a displacement field (in Transforms module / Convert section).</p>

---

## Post #3 by @RuurdK (2018-11-15 19:10 UTC)

<p>Thank you for your quick and comprehensive answer. I had been looking into the VTK classes but had some trouble loading the .nrrd files which my code outputs. I will look into this again and report back with the results.</p>
<p>R</p>

---

## Post #4 by @lassoan (2018-11-15 19:18 UTC)

<p>Slicer can load a vector field into a transform node (and inside it as a VTK grid transform) from .nrrd file: in the “Add data…” dialog, choose to load it as a “Transform” (in “Description” column).</p>

---
