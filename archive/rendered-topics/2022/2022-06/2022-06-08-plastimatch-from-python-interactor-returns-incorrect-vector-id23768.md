# Plastimatch from Python Interactor returns incorrect vector field

**Topic ID**: 23768
**Date**: 2022-06-08
**URL**: https://discourse.slicer.org/t/plastimatch-from-python-interactor-returns-incorrect-vector-field/23768

---

## Post #1 by @Luca (2022-06-08 14:27 UTC)

<p>Dear Community,</p>
<p>I am working to a project about contrast-enhanced CT images registration using Slicer Pyhton Interactor to perform Plastimatch B-spline deformable registration. Following this <a href="https://groups.google.com/g/plastimatch/c/Muc24iX3X3I/m/PQoelmpkDAAJ" rel="noopener nofollow ugc">link</a>, I was able to write these lines to perform it:</p>
<pre><code class="lang-auto">import vtkSlicerPlastimatchPyModuleLogicPython

reg = vtkSlicerPlastimatchPyModuleLogicPython.vtkPlmpyRegistration()
reg.SetMRMLScene(slicer.mrmlScene)
reg.SetFixedImageID(getNode('Fixed_img').GetID())
reg.SetMovingImageID(getNode('Moving_img').GetID())

output = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', 'Output volume_PythonInteractor')
displayNode = slicer.vtkMRMLScalarVolumeDisplayNode()
slicer.mrmlScene.AddNode(displayNode)

output_VectorField = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLGridTransformNode', 'Output vector field_PythonInteractor')

reg.SetOutputVolumeID(output.GetID())
reg.SetOutputVectorFieldID(output_VectorField.GetID())

par = "[STAGE]\nxform = bspline"
reg.SetRegistrationParameters(par)
reg.RunRegistration()
</code></pre>
<p>Once I invert “Output vector field_PythonInteractor” and apply it to “Output volume_PythonInteractor”, I should obtain the original image “Moving_img”: however, the result is not correct.<br>
Then, I tried to perform the same steps (i.e. plastimatch b-spline deformable registration + inverse transform) from GUI and it worked as expected.<br>
Thus, I am supposing that the vector field obtained from Python Interactor is incorrect.</p>
<p>You can dowload from <a href="https://we.tl/t-Y0qfJUxkJq" rel="noopener nofollow ugc">here</a> the bundle file with the following nodes:</p>
<ul>
<li>Moving_img</li>
<li>Fixed_img</li>
<li>Output volume_GUI</li>
<li>Output vector field_GUI</li>
<li>Output volume_PythonInteractor</li>
</ul>
<p>“Output vector field_PythonInteractor” is not included because I cannot save the file if it is in the scene: the error is</p>
<blockquote>
<p>vtkITKTransformConverter::CreateITKTransformFromVTK failed: conversion of transform type vtkGridTransform is not supported.<br>
WriteTransform failed: cannot to convert VTK transform to ITK transform</p>
</blockquote>
<p>but you can get that variable by running the previous lines.</p>
<p>Furthermore, I find that the vector field from GUI contains a vtkOrientedGridTransform, while the one from Python Interactor includes a vtkGridTransform. I read about the LPS/IJK/RAS problem but I did not figure out if it is the correct hint and, in case, how to impement it.</p>
<p>Do you have any suggestion?</p>
<p>Thanks in advance,<br>
Luca</p>

---

## Post #2 by @mau_igna_06 (2022-06-08 14:38 UTC)

<p>I believe the vtOrientedGrid should just be a  vtkGrid with a vtkTransform</p>
<p>Slicer’s standard is RAS so the identityMatrixn matches that directions, first column is R and so on, forth column is the origin, forth row is 0s, but the last item can be a 1 if you want to transformna poikt, 0 otherwise for a vector</p>
<p>Hopenit helps</p>

---

## Post #3 by @Luca (2022-06-10 16:12 UTC)

<p>Thank you Mauro for the hint. However, I know basics of orientation matrices and reference systems but I cannot find out which matrix/matrices should I use in this case. For sure, It was my fault but I was not able to reach a solution yet.</p>
<p>Any other suggestions?</p>

---
