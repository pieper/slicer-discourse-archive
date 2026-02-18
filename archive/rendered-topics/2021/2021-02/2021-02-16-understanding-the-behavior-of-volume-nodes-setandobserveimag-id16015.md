# Understanding the behavior of volume node's SetAndObserveImageData method

**Topic ID**: 16015
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/understanding-the-behavior-of-volume-nodes-setandobserveimagedata-method/16015

---

## Post #1 by @marianaslicer (2021-02-16 17:55 UTC)

<p>Hi everyone,</p>
<p>Slicer: 4.13</p>
<p>My question might be stupid…<br>
I am not understanding the behavior of these lines of code:</p>
<pre><code>mathMultiply = vtk.vtkImageMathematics()
mathMultiply.RemoveAllInputs()
CT_before.SetAndObserveImageData(ctNode.GetImageData())
mathMultiply.SetInputData(ctNode.GetImageData())
mathMultiply.Modified()
mathMultiply.Update()
CT_after.SetAndObserveImageData(mathMultiply.GetOutput())
</code></pre>
<p>I was expecting that CT_before and CT_after to be exactly the same, but I’m having a shift in the voxel values. Any idea why?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e4368c46dfdbca55b92be1cd8dbbcf806b9e26.png" alt="image" data-base62-sha1="seD0mQnGU66Y8SMelUHwCGbEykm" width="245" height="106"></p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2021-02-16 18:38 UTC)

<p>Did you get any error messages?  The default operation of <code>vtkImageMathematics</code> is Add, which requires two inputs.  Also you would typically use the <code>SetInput1Data</code> and optionally <code>SetInput2Data</code> depending on the selected operation.</p>

---

## Post #3 by @lassoan (2021-02-16 20:15 UTC)

<p>Note that it is not enough to copy the image data, you also need to copy image origin, spacing, and axis directions (for example, by copying the IJKToRAS matrix). Although in this case the difference is not cause by this, because you seem to have origin=(0,0,0), spacing=(1,1,1), directions=<code>np.diag([1,1,1])</code>. By the way, it is rare to have isotropic spacing of 1.0mm/pixel along all axes and directions is most commonly is <code>np.diag([-1,-1,1])</code>), so maybe you have lost your image geometry during some previous preprocessing step.</p>
<p>Where did you get your inputs from? What are you trying to achieve?</p>

---

## Post #4 by @marianaslicer (2021-02-16 21:40 UTC)

<p>Hi Pieper,</p>
<p>Thanks for your response.<br>
Yes, I am getting several VTK errors:</p>
<pre><code>Bad component index 1
Bad component index 2
Bad component index 2

Execute: input2 ScalarType, 4, must match output ScalarType 6
Execute: input2 ScalarType, 6, must match output ScalarType 4
</code></pre>
<p>I changed the code as you can see in the following answer but I am getting the same errors.</p>

---

## Post #5 by @marianaslicer (2021-02-16 21:41 UTC)

<p>Hi Andras Lasso,</p>
<p>Thank you for your response.<br>
I am trying to calculate the average CT of 10 CT and I have the following code:</p>
<pre><code>ctImageData = vtk.vtkImageData()
mathMultiply = vtk.vtkImageMathematics()
mathAddCT = vtk.vtkImageMathematics()
mathAddCT.RemoveAllInputs()

if firstRun:
  ctImageData.SetSpacing(ctNode.GetSpacing())
  ctImageData.SetOrigin(ctNode.GetOrigin())
  ctImageData.DeepCopy(ctNode.GetImageData())
  firstRun = False

else:
  mathAddCT.SetOperationToAdd()
  mathAddCT.SetInput1Data(ctNode.GetImageData())
  mathAddCT.SetInput2Data(ctImageData)
  mathAddCT.Modified()
  mathAddCT.Update()
  ctImageData.DeepCopy(mathAddCT.GetOutput())

after adding 10 CT, calculate the mean:

mathMultiply.RemoveAllInputs()
mathMultiply.SetOperationToMultiplyByK()
mathMultiply.SetConstantK(0.1)
mathMultiply.SetInput1Data(ctImageData)
mathMultiply.Modified()
mathMultiply.Update()
ctImageData.DeepCopy(mathMultiply.GetOutput())
</code></pre>
<p>I am not understanding why I have this shift in voxel values after applying mathematical operations.The input medical images have  origin = (300, 157, 24)mm , spacing = (1.171875, 1.171875, 2)mm and size of 512x512x89 mm.</p>

---

## Post #6 by @lassoan (2021-02-16 22:52 UTC)

<p>Instead of using VTK filters, it is much easier to add values using numpy operations. You can get the voxels as a numpy array by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume"><code>arrayFromVolume</code></a>.</p>
<p>Before you can compute average, you need to ensure that all arrays have the same geometry (origin, spacing, axis directions, and extents). You can achieve that by registering them to a common template and resampling them using the same reference geometry.</p>

---

## Post #7 by @marianaslicer (2021-02-16 23:56 UTC)

<p>Thank you for your useful suggestion. It solved my problem!</p>

---
