# N4 Bias Field Correction in sitk

**Topic ID**: 12837
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/n4-bias-field-correction-in-sitk/12837

---

## Post #1 by @xlucox (2020-08-03 19:03 UTC)

<p>Hi everyone,</p>
<p>I’ve been trying to automatize the application of N4 Bias Field Correction in python. I though it would be a good idea to use sitk. The fact is when I configure the class N4BiasFieldCorrectionImageFilter with the same parameters as it is programmed by default in the Slicer module “N4ITK MRI Bias correction”, the image output lose quality. Does anyone know how to get the same result in the same amount of time using python?</p>
<p>Here is the code I’m using:</p>
<p>shrinkFactor = 4<br>
inputImage = sitk.ReadImage(sys.argv[1])<br>
maskImage = sitk.OtsuThreshold(inputImage, 0, 1, 200)<br>
inputImage = sitk.Shrink(inputImage, [shrinkFactor] * inputImage.GetDimension())<br>
maskImage = sitk.Shrink(maskImage,[shrinkFactor] * inputImage.GetDimension())</p>
<p>inputImage = sitk.Cast(inputImage, sitk.sitkFloat32)<br>
corrector = sitk.N4BiasFieldCorrectionImageFilter()<br>
corrector.SetNumberOfControlPoints([4,4,4])<br>
corrector.SetConvergenceThreshold(0.0001)<br>
corrector.SetMaximumNumberOfIterations([50,40,30])<br>
inputImage = sitk.Cast(inputImage, sitk.sitkFloat32)<br>
output = corrector.Execute(inputImage, maskImage)<br>
sitk.WriteImage(output, name)</p>
<p>I know the shrinkFactor is making the quality poorer but if I turn it 1, then the algorithm takes to much time running.</p>

---

## Post #2 by @lassoan (2020-08-03 19:18 UTC)

<p>You can find the Slicer module’s source code here: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/N4ITKBiasFieldCorrection/N4ITKBiasFieldCorrection.cxx">https://github.com/Slicer/Slicer/blob/master/Modules/CLI/N4ITKBiasFieldCorrection/N4ITKBiasFieldCorrection.cxx</a></p>
<p>Based on this, you can reimplement the module in pure Python and SimpleITK, but you can save some time by using the Slicer CLI module from Python as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">here</a>.</p>

---
