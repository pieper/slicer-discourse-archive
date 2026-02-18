# What is the Algorithm and Theory of spin calibration?

**Topic ID**: 15434
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/what-is-the-algorithm-and-theory-of-spin-calibration/15434

---

## Post #1 by @timeanddoctor (2021-01-10 11:34 UTC)

<p>I am studing the calibration and  researched many publicatioins but get nothing about the spin calibration. I tend to know what is the Algorithm and Math Theory of spin calibration?</p>

---

## Post #2 by @ungi (2021-01-10 18:12 UTC)

<p><a class="mention" href="/u/mholden8">@mholden8</a> implemented it, but haven’t published the algorithm. You can find the implementation in the source code, here: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/PivotCalibration/Logic/vtkSlicerPivotCalibrationLogic.cxx" class="inline-onebox" rel="noopener nofollow ugc">SlicerIGT/vtkSlicerPivotCalibrationLogic.cxx at master · SlicerIGT/SlicerIGT · GitHub</a><br>
It is essentially looking for the axis with least variation in the tool motion during calibration. And adds a few heuristics, e.g. for direction in the axis, it assumes that the position sensor is behind the pointer, not in front.</p>
<p>To explain it to someone with no math background: Calculate the rotation of the tool between two time points. That rotation has an axis direction. Then, record a series of rotations of this tool, and take the average direction of the rotation axes. That will be the final axis of rotation. If you have already computed the tip point, then make sure the pointy tip is pointing away from the tracked position, so you may need to flip the direction in the end.</p>

---

## Post #3 by @mholden8 (2021-01-11 06:57 UTC)

<p>In case it helps, here are my notes on the “theory”: <a href="https://drive.google.com/file/d/1SUrL72-LJUD73rLYZaZOsJzf9qF0MNc8/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Holden_SpinCalibration.pdf - Google Drive</a>.</p>

---

## Post #4 by @timeanddoctor (2021-01-12 08:39 UTC)

<p>Thank you very much.</p>

---

## Post #5 by @timeanddoctor (2021-01-12 08:42 UTC)

<p>Thank you for helping me find the information I needed</p>

---

## Post #6 by @timeanddoctor (2021-01-13 11:51 UTC)

<p>I collected a stack of transform data(np.array([matrix][matrix][matrix]…)) and I tend to use this algorithm in 3d slicer to get the transform to calibrate the spin axis.I have tried this but seems not correct.<br>
calibrationSuccess = slicer.modules.pivotcalibration.logic().ComputeSpinCalibration()<br>
I donnot know how to set up the input data, or should I use ‘AddToolToReferenceMatrix(…)’ one by one?</p>

---
