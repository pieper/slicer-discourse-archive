---
topic_id: 18205
title: "Get New Fiducial Position After Transform"
date: 2021-06-18
url: https://discourse.slicer.org/t/18205
---

# Get new fiducial position after transform

**Topic ID**: 18205
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/get-new-fiducial-position-after-transform/18205

---

## Post #1 by @sandyaa0313 (2021-06-18 12:58 UTC)

<p>Operating system:Windows10<br>
Slicer version:4.11.20200930<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I want to do some functions similar to fiducial registeration wizard in SlicerIGT by my own python module.<br>
Now I can retrieve the transform matrix, but I don’t know how to get the new fiducial position of f1 node after transform.<br>
Thanks!</p>
<p>Here is my code:</p>
<pre><code class="lang-python">transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode")
transformNode.SetName("Registration Transform")
parameters = {}
f1 = slicer.util.getNode("Fiducials")
f2 = slicer.util.getNode("Fiducials2")

parameters["saveTransform"] = transformNode.GetID()
parameters["movingLandmarks"] = f1.GetID()  # fiducial points
parameters["fixedLandmarks"] = f2.GetID()  # fiducial points
fiduciaReg = slicer.modules.fiducialregistration
slicer.cli.runSync(fiduciaReg, None, parameters)

tmatrix = vtk.vtkMatrix4x4()
t1 = slicer.util.getNode(parameters["saveTransform"])
t2 = slicer.util.getNode(parameters["movingLandmarks"])
t1.GetMatrixTransformToParent(tmatrix) 
transformMatrix = slicer.util.arrayFromVTKMatrix(tmatrix)
</code></pre>

---

## Post #2 by @lassoan (2021-06-18 13:13 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsControlPoints"><code>slicer.util.arrayFromMarkupsControlPoints</code></a> function to get fiducial point positions as a numpy array. Specify <code>world=True</code> to get the transformed positions.</p>

---

## Post #3 by @sandyaa0313 (2021-06-24 06:45 UTC)

<p>Thank you ! I get it !</p>

---
