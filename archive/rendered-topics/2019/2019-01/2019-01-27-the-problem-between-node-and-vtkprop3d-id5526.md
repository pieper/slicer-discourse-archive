---
topic_id: 5526
title: "The Problem Between Node And Vtkprop3D"
date: 2019-01-27
url: https://discourse.slicer.org/t/5526
---

# The problem between Node and vtkProp3D

**Topic ID**: 5526
**Date**: 2019-01-27
**URL**: https://discourse.slicer.org/t/the-problem-between-node-and-vtkprop3d/5526

---

## Post #1 by @timeanddoctor (2019-01-27 06:23 UTC)

<p>I want to use a vtkAssembly in slicer. I am not clear there is any relationship between modelNode and vtkProp3D. How to use a model as vtkProp3D in slicer script.<br>
<code>Assembly.AddPart(NeedleModel)</code><br>
Traceback (most recent call last):   File “”, line 1, in  TypeError: AddPart argument 1: method requires a vtkProp3D, a vtkMRMLModelNode was provided.<br>
And another problem is how to rotate a model(or transform)  setting a origin(x,y,z) myself.<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2019-01-27 14:57 UTC)

<p>Each model node is displayed using a prop in each view. You should not need assembly, as you can build your own model transform hierarchy using transform and model nodes.</p>

---

## Post #3 by @timeanddoctor (2019-01-27 15:30 UTC)

<p>Thank you Professor Lassoan.<br>
I need add two parts into a Transform, and then I need set a Origin for this transform. Are there any example similar what I am doing.<br>
Thanks.</p>

---

## Post #4 by @lassoan (2019-01-27 16:44 UTC)

<p>You just need to create transform nodes and apply it to model and transform nodes below. <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a> may help - see for example U-04.</p>

---

## Post #5 by @timeanddoctor (2019-01-28 02:15 UTC)

<p>Thank you for your quick reply.<br>
I can do it through manu now. In order to run it through script, I found some code from here, but I could not distinguish the different between them.<br>
First:</p>
<pre><code>vTransform = vtk.vtkTransform()
vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
vTransform.RotateZ(10)  # The angle is in degrees
vTransform.Translate(0.88, -35.4, -5.65)
imageNode.ApplyTransform(vTransform)
</code></pre>
<p>Second:</p>
<pre><code>transform = slicer.vtkMRMLLinearTransformNode()
scene = slicer.mrmlScene
scene.AddNode(transform) 
imageNode.SetAndObserveTransformNodeID(transform.GetID())
vTransform = vtk.vtkTransform()
vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
vTransform.RotateZ(10)  # The angle is in degrees
vTransform.Translate(0.88, -35.4, -5.65)
transform.SetAndObserveMatrixTransformToParent(vTransform.GetMatrix())
#transform.SetMatrixTransformToParent(vTransform.GetMatrix())</code></pre>

---

## Post #6 by @lassoan (2019-01-31 00:27 UTC)

<p>First example changes the image position/orientation permanently.</p>
<p>Second example applies a transform to the image. You can remove the transform to get back the image to its original pose or harden the transform to change the image pose permanently.</p>
<p>Simplified and more up-to-date version of the second example:</p>
<pre><code class="lang-auto">transform = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
imageNode.SetAndObserveTransformNodeID(transform.GetID())
vTransform = vtk.vtkTransform()
vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
vTransform.RotateZ(10)  # The angle is in degrees
vTransform.Translate(0.88, -35.4, -5.65)
transform.SetMatrixTransformToParent(vTransform.GetMatrix())
</code></pre>

---
