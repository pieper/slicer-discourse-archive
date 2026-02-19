---
topic_id: 7362
title: "Create A Cube With The Certain Vertices"
date: 2019-06-30
url: https://discourse.slicer.org/t/7362
---

# Create a cube with the certain vertices

**Topic ID**: 7362
**Date**: 2019-06-30
**URL**: https://discourse.slicer.org/t/create-a-cube-with-the-certain-vertices/7362

---

## Post #1 by @shahrokh (2019-06-30 09:33 UTC)

<p>Hi Dears 3DSlicer developers</p>
<p>I want to create a cube with the certain vertices. For example, I have 8 points (vertices) with the following spatial coordinates in RAS.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Vertex</th>
<th>R</th>
<th>A</th>
<th>S</th>
</tr>
</thead>
<tbody>
<tr>
<td>superiorUpRight</td>
<td>-731.523242270663</td>
<td>-74.7326192431123</td>
<td>-1012.2</td>
</tr>
<tr>
<td>superiorUpLeft</td>
<td>-531.523242270663</td>
<td>-421.142780756888</td>
<td>-1012.2</td>
</tr>
<tr>
<td>superiorDownRight</td>
<td>-818.125782649107</td>
<td>-124.732619243112</td>
<td>-1012.2</td>
</tr>
<tr>
<td>superiorDownLeft</td>
<td>-618.125782649107</td>
<td>-471.142780756888</td>
<td>-1012.2</td>
</tr>
<tr>
<td>inferiorUpRight</td>
<td>-731.523242270663</td>
<td>-74.7326192431123</td>
<td>-1412.2</td>
</tr>
<tr>
<td>inferiorUpLeft</td>
<td>-531.523242270663</td>
<td>-421.142780756888</td>
<td>-1412.2</td>
</tr>
<tr>
<td>inferiorDownRight</td>
<td>-818.125782649107</td>
<td>-124.732619243112</td>
<td>-1412.2</td>
</tr>
<tr>
<td>inferiorDownLeft</td>
<td>-618.125782649107</td>
<td>-471.142780756888</td>
<td>-1412.2</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Min</td>
<td>-818.125782649107</td>
<td>-471.142780756888</td>
<td>-1412.2</td>
</tr>
<tr>
<td>Max</td>
<td>-531.523242270663</td>
<td>-74.7326192431123</td>
<td>-1012.2</td>
</tr>
</tbody>
</table>
</div><p>How can I define one cube with these points?<br>
I do not find the fuction about setting up vertices in vtk.vtkCubeSource(), then I used the function of vtk.vtkCubeSource().SetBounds (double xMin, double xMax, double yMin, double yMax, double zMin, double zMax) as following lines:</p>
<blockquote>
<p>EPID = vtk.vtkCubeSource()<br>
EPID.SetBounds(-818.125782649107, -531.523242270663, -471.142780756888, -74.7326192431123, -1412.2, -1012.2)<br>
modelsLogicEPID = slicer.modules.models.logic()<br>
modelEPID = modelsLogicEPID.AddModel(EPID.GetOutput())<br>
modelEPID.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
modelEPID.GetDisplayNode().SetColor(0,1,0)<br>
modelEPID.GetDisplayNode().SetSliceIntersectionThickness(3)<br>
EPID.Update()</p>
</blockquote>
<p>As seen in the following figure, the red cube is not correct. The vertices are specified with colored spheres.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68accae6fcac5238a1b9091df33ccbf8c7764f06.png" data-download-href="/uploads/short-url/eVZRwFpP6FlJ3MHx7nC8oPCLeKy.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68accae6fcac5238a1b9091df33ccbf8c7764f06_2_690x355.png" alt="Screenshot" data-base62-sha1="eVZRwFpP6FlJ3MHx7nC8oPCLeKy" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68accae6fcac5238a1b9091df33ccbf8c7764f06_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68accae6fcac5238a1b9091df33ccbf8c7764f06_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68accae6fcac5238a1b9091df33ccbf8c7764f06_2_1380x710.png 2x" data-dominant-color="9093C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1440×742 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2019-06-30 12:38 UTC)

<p>vtkCubeSource creates cube with non-rotated axes. I would recommend to create a cube with the right size, centered around the origin. Then position and orient the node by <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples" rel="nofollow noopener">specifying a parent transform</a>.</p>

---

## Post #3 by @shahrokh (2019-07-01 13:45 UTC)

<p>Hi Dear Andras</p>
<p>Thanks a lot for your gudance. I create a cube model as mentioned you in the center of coordinate system with the following commands:</p>
<blockquote>
<p>EPIDmodel = vtk.vtkCubeSource()<br>
EPIDmodel.SetXLength(400)<br>
EPIDmodel.SetYLength(50)<br>
EPIDmodel.SetZLength(400)<br>
modelsLogic = slicer.modules.models.logic()<br>
modelEPID = modelsLogic.AddModel(EPIDmodel.GetOutput())<br>
modelEPID.SetName(‘EPIDmodel’)<br>
modelEPID.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
modelEPID.GetDisplayNode().SetSliceIntersectionThickness(3)<br>
modelEPID.GetDisplayNode().SetColor(0,1,0)<br>
EPIDmodel.Update()</p>
</blockquote>
<p>I really want to apologize. Unfortunately I did not find a simple example in moving a model (vtkMRMLModelNode) including as Translation + Rotation.<br>
In the link you mentioned, Unfortunately, I did not see about the transformation of model node.<br>
Using the file of procrustesAlignment.py in VTK, I enter the following commands:</p>
<blockquote>
<p>transform1 = vtk.vtkTransform()<br>
transform1.Translate(200, 100, 400)<br>
transform1.RotateX(45)</p>
<p>transformer1 = vtk.vtkTransformPolyDataFilter()<br>
transformer1.SetInputConnection(EPIDmodel.GetOutputPort())<br>
transformer1.SetTransform(transform1)<br>
EPIDmodel.Update()</p>
</blockquote>
<p>I do not see any changes in the 3D window. Why?<br>
I must mention that after creating the model, I can transfer it to any direction using Transforms module, but I would like to learn this from Python Interactor. Please guide me to do it from command line of Python.</p>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #4 by @lassoan (2019-07-01 15:33 UTC)

<p>No need to apply transform polydata filter manually. Instead, you can set a parent transform node for the model node and then call <code>SetMatrixTransformToParent</code> to set a transformation matrix.</p>

---

## Post #5 by @shahrokh (2019-07-04 17:11 UTC)

<p>Thank you very much for guidance. I do as you mentioned. Unfortunately, the cube model is not transfered with the following commands.</p>
<blockquote>
<p>transform = slicer.vtkMRMLTransformNode()<br>
transform.SetName(‘Transformation’)<br>
slicer.mrmlScene.AddNode(transform)<br>
matrix = vtk.vtkMatrix4x4()<br>
matrix.SetElement(0, 0, 1)<br>
matrix.SetElement(0, 1, 0)<br>
matrix.SetElement(0, 2, 0)<br>
matrix.SetElement(0, 3, 0)<br>
matrix.SetElement(1, 0, 0)<br>
matrix.SetElement(1, 1, 1)<br>
matrix.SetElement(1, 2, 0)<br>
matrix.SetElement(1, 3, 0)<br>
matrix.SetElement(2, 0, 0)<br>
matrix.SetElement(2, 1, 0)<br>
matrix.SetElement(2, 2, -1212.200)<br>
matrix.SetElement(2, 3, 0)<br>
matrix.SetElement(3, 0, 0)<br>
matrix.SetElement(3, 1, 0)<br>
matrix.SetElement(3, 2, 0)<br>
matrix.SetElement(3, 3, 0)<br>
transform.SetMatrixTransformToParent(matrix)<br>
modelNode = slicer.util.getNode(‘EPIDmodel’)</p>
<p>modelNode.SetAndObserveTransformNodeID(transform.GetName())<br>
modelNode.SetAndObserveTransformNodeID(transform.GetID())</p>
</blockquote>
<p>Where else are I wrong?<br>
Please guide me.<br>
Thanks a lot.</p>
<p>Shahrokh.</p>

---

## Post #6 by @lassoan (2019-07-04 17:22 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="5" data-topic="7362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>matrix.SetElement(3, 3, 0)</p>
</blockquote>
</aside>
<p>You must leave the row 3 of the matrix as is: <code>(0,0,0,1)</code>. Calling <code>matrix.SetElement(3, 3, 0)</code> makes the transform invalid.</p>
<p>vtkMatrix4x4 is already initialized to identity, so there is no need to set the orientation (top-left 3x3 matrix) to identity again, just leave it as is.</p>
<p>Translation part of the transform is in column 3, not column 2, so this is incorrect: <code>matrix.SetElement(2, 2, -1212.200)</code> (it would ruin your model by scaling it by a factor of 1000 and turning it inside out). Use <code>matrix.SetElement(..., 3, ...)</code> instead.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="5" data-topic="7362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>modelNode.SetAndObserveTransformNodeID(transform.GetName())</p>
</blockquote>
</aside>
<p>Delete this line. <code>SetAndObserveTransformNodeID</code> method requires a node ID, not a node name and you set the node ID correctly in the line below.</p>

---

## Post #7 by @shahrokh (2019-07-07 05:43 UTC)

<p>Dear Andras</p>
<p>At now, I can define transform matrix, including as Translation and Rotation, with the following commands.</p>
<blockquote>
<p>…<br>
<span class="hashtag-raw">#Define</span> transformation matrix (Translation and Rotation)<br>
transform = slicer.vtkMRMLTransformNode()<br>
transform.SetName(‘Transformation’)<br>
<span class="hashtag-raw">#Add</span> node Transormation to “Data” module<br>
slicer.mrmlScene.AddNode(transform)<br>
matrix = vtk.vtkMatrix4x4()<br>
<span class="hashtag-raw">#Translation</span><br>
<span class="hashtag-raw">#Shifting</span> along the axis LR<br>
matrix.SetElement(0, 3, translateLR)<br>
<span class="hashtag-raw">#Shifting</span> along the axis PA<br>
matrix.SetElement(1, 3, translatePA)<br>
<span class="hashtag-raw">#Shifting</span> along the axis IS<br>
matrix.SetElement(2, 3, translateIS)<br>
<span class="hashtag-raw">#Rotation</span><br>
<span class="hashtag-raw">#Rotation</span> around IS (-60 degree)<br>
matrix.SetElement(0, 0, math.cos(math.radians(300-360)))<br>
matrix.SetElement(0, 1, -math.sin(math.radians(300-360)))<br>
matrix.SetElement(1, 0, math.sin(math.radians(300-360)))<br>
matrix.SetElement(1, 1, math.cos(math.radians(300-360)))</p>
<p><span class="hashtag-raw">#Set</span> IS parameter in “Transforms” module<br>
transform.SetMatrixTransformToParent(matrix)</p>
<p><span class="hashtag-raw">#Move</span> “EPIDmodel” from “Transformable” to “Transormed” table in “Transforms” module and then apply to it.<br>
modelNode = slicer.util.getNode(‘EPIDmodel’)<br>
modelNode.SetAndObserveTransformNodeID(transform.GetID())</p>
</blockquote>
<p>Thanks a lot for your guidance.<br>
Shahrokh.</p>

---

## Post #8 by @lassoan (2019-07-07 12:01 UTC)

<p>It is great to hear this. Note that you can compute transformation matrix by using translate and rotate methods of vtkTransform and retrieve the matrix by calling <code>GetMatrix()</code>.</p>

---
