---
topic_id: 5327
title: "Apply Transformation To A Model"
date: 2019-01-10
url: https://discourse.slicer.org/t/5327
---

# Apply Transformation to a model

**Topic ID**: 5327
**Date**: 2019-01-10
**URL**: https://discourse.slicer.org/t/apply-transformation-to-a-model/5327

---

## Post #1 by @siaeleni (2019-01-10 16:10 UTC)

<p>Hi,</p>
<p>I want to set and apply a transformation matrix using Python.<br>
Here is my code:</p>
<blockquote>
<pre><code>transform = slicer.vtkMRMLTransformNode()
transform.SetName('Transformation')
slicer.mrmlScene.AddNode(transform)
matrix = vtk.vtkMatrix4x4()
matrix.SetElement(0, 0, 0.67)
matrix.SetElement(0, 1, 0.45)
matrix.SetElement(0, 2, 1)
matrix.SetElement(0, 3, 23)

matrix.SetElement(1, 0, 0.34)
matrix.SetElement(1, 1, 1)
matrix.SetElement(1, 2, 0)
matrix.SetElement(1, 3, -11)

matrix.SetElement(2, 0, 0.5)
matrix.SetElement(2, 1, 0.1)
matrix.SetElement(2, 2, 1)
matrix.SetElement(2, 3, -33)

matrix.SetElement(3, 0, 0)
matrix.SetElement(3, 1, 0)
matrix.SetElement(3, 2, 0)
matrix.SetElement(3, 3, 1)

transform.SetMatrixTransformFromParent(matrix)
model = slicer.util.getNode('model')

model.SetAndObserveTransformNodeID(transform.GetName())
model.SetAndObserveTransformNodeID(transform.GetID())
</code></pre>
</blockquote>
<p>Unfortunately, I get some strange results when I check the output at Transformation module, why that is happening and what am I doing wrong here?</p>
<p>Thanks</p>

---

## Post #2 by @adamrankin (2019-01-10 16:51 UTC)

<p>This line is not needed:</p>
<blockquote>
<p>model.SetAndObserveTransformNodeID(transform.GetName())</p>
</blockquote>
<p>What is the strange results?</p>

---

## Post #3 by @siaeleni (2019-01-10 18:16 UTC)

<p>When I check the transformation matrix at <strong>Transforms</strong> module and pick the “Transformation”, the displayed matrix is not the same as I have set at the script, thus when I apply the transformation is not correct. Do you know why it is happening?</p>

---

## Post #4 by @lassoan (2019-01-10 18:18 UTC)

<p>You would normally set transform <strong>to</strong> parent and that is displayed on the GUI. In your example above, you set transform <strong>from</strong> parent, so on the GUI you saw inverse of that matrix.</p>
<pre><code class="lang-auto">matrix = vtk.vtkMatrix4x4()
matrix.SetElement(...)
transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', 'Transformation')
transformNode.SetMatrixTransformToParent(matrix)

modelNode = slicer.util.getNode('model')
modelNode.SetAndObserveTransformNodeID(transformNode.GetID())
</code></pre>

---
