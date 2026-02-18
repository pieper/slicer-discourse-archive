# How to set the input transforms for calibration

**Topic ID**: 15533
**Date**: 2021-01-15
**URL**: https://discourse.slicer.org/t/how-to-set-the-input-transforms-for-calibration/15533

---

## Post #1 by @timeanddoctor (2021-01-15 01:37 UTC)

<p>I collected a stack of transform data(np.array([matrix][matrix][matrix]…)) in different times and I tend to use spin calibration in 3d slicer to get the transform to calculate the spin axis.I have tried this code but seems not correct.<br>
<code>calibrationSuccess = slicer.modules.pivotcalibration.logic().ComputeSpinCalibration()</code><br>
I donnot know how to set up the input datas, and I also tried ‘AddToolToReferenceMatrix(…)’ one by one, but the slicer was crashed.</p>

---

## Post #2 by @lassoan (2021-01-15 01:41 UTC)

<p>You need to convert the numpy array to VTK matrix using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.vtkMatrixFromArray">slicer.util.vtkMatrixFromArray</a>.</p>

---
