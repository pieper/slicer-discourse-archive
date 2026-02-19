---
topic_id: 503
title: "Bspline To Deformation Field Error"
date: 2017-06-14
url: https://discourse.slicer.org/t/503
---

# BSpline to deformation field Error

**Topic ID**: 503
**Date**: 2017-06-14
**URL**: https://discourse.slicer.org/t/bspline-to-deformation-field-error/503

---

## Post #1 by @eladam (2017-06-14 15:53 UTC)

<p>Hello,</p>
<p>I have been trying to work with the BSpline to deformation field module, but it doesn’t seem to work.</p>
<p>As an input I provided the transform that I acquired from the General Registration (BRAINS) module through the procedure of BSpline.</p>
<p>The error I am getting is:<br>
Can’t Create IO object for file /tmp/Slicer/DHCF_AxHfBfcEAABABA.mrml#vtkMRMLBSplineTransformNode1<br>
BSpline to deformation field terminated with an unknown exception.</p>
<p>The Slicer version I am using is 4.6.2. Is there a way to resolve this?</p>
<p>Thank you,<br>
Eleni</p>

---

## Post #2 by @ihnorton (2017-06-14 16:09 UTC)

<p>Please try a recent nightly. I believe this was caused by the <code>dynamic_cast</code> issues in ITK, which have been resolved.</p>

---

## Post #3 by @eladam (2017-06-14 17:38 UTC)

<p>Again, there is the error:</p>
<p>terminate called after throwing an instance of 'itk::ExceptionObject’<br>
what():  /home/kitware/Dashboards/Nightly/Slicer-0-build/ITKv4/Modules/IO/TransformBase/include/itkTransformFileReader.hxx:130:<br>
itk::ERROR: TransformFileReaderTemplate(0x20f6330):<br>
Could not create Transform IO object for reading file /tmp/Slicer/HJHD_AxHfdDeEAAJIdA.mrml#vtkMRMLBSplineTransformNode1<br>
File does not exists!  Tried to create one of the following:<br>
HDF5TransformIOTemplate<br>
HDF5TransformIOTemplate<br>
MatlabTransformIOTemplate<br>
MatlabTransformIOTemplate<br>
TxtTransformIOTemplate<br>
TxtTransformIOTemplate<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>I tried entering a transform with .h5 .tfm and .mat suffix, still the same error appears.</p>

---

## Post #4 by @lassoan (2017-06-14 18:04 UTC)

<p>BSpline to deformation field module only works for the old-style ITK bspline transform that we don’t use anymore.</p>
<p>Use Convert section in Transform module to convert any transform to displacement field.</p>

---

## Post #5 by @eladam (2017-06-14 18:15 UTC)

<p>Thank you, this worked!</p>
<p>Best,<br>
Eleni</p>

---

## Post #6 by @lassoan (2020-02-21 15:22 UTC)

<p>A post was split to a new topic: <a href="/t/general-registration-brains-error/10383">General Registration (BRAINS) error</a></p>

---
