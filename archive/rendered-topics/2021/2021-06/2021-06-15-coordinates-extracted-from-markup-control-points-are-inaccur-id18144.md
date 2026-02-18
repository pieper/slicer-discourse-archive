# Coordinates extracted from markup control points are inaccurate

**Topic ID**: 18144
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/coordinates-extracted-from-markup-control-points-are-inaccurate/18144

---

## Post #1 by @mau_igna_06 (2021-06-15 15:33 UTC)

<p>Here is the code to reproduce the bug:</p>
<pre><code class="lang-auto">import numpy as np

lineNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsLineNode")
lineNode.SetName("screwLine")
slicer.mrmlScene.AddNode(lineNode)
#display node of the plane
displayNode = lineNode.GetDisplayNode()
displayNode.UseGlyphScaleOff()
displayNode.SetGlyphSize(8)
displayNode.SetOpacity(1)
displayNode.SetLineThickness(0)

lineNode.AddControlPoint(vtk.vtkVector3d(45.0,11.0,0.0))
lineNode.AddControlPoint(vtk.vtkVector3d(-26.0,-10.0,0.0))

def moveLineOnLineDirection():
  lineStartPoint = np.array([0,0,0])
  lineEndPoint = np.array([0,0,0])
  lineNode.GetNthControlPointPosition(0,lineStartPoint)
  lineNode.GetNthControlPointPosition(1,lineEndPoint)
  lineDirection = (lineEndPoint - lineStartPoint)/np.linalg.norm(lineEndPoint - lineStartPoint)
  stepmm = 5
  stepDirection = lineDirection
  lineTranslationTransform = vtk.vtkTransform()
  lineTranslationTransform.PostMultiply()
  lineTranslationTransform.Translate(stepmm*stepDirection)
  lineTranslationTransformNode = slicer.vtkMRMLLinearTransformNode()
  lineTranslationTransformNode.SetName("lineTranslationTransform")
  slicer.mrmlScene.AddNode(lineTranslationTransformNode)
  lineTranslationTransformNode = slicer.vtkMRMLLinearTransformNode()
  lineTranslationTransformNode.SetName("screwToScrewLineTransform")
  slicer.mrmlScene.AddNode(lineTranslationTransformNode)
  lineTranslationTransformNode.SetMatrixTransformToParent(
    lineTranslationTransform.GetMatrix())
  lineNode.SetAndObserveTransformNodeID(lineTranslationTransformNode.GetID())
  lineNode.HardenTransform()
  slicer.mrmlScene.RemoveNode(lineTranslationTransformNode)
  translatedLineStartPoint = np.array([0,0,0])
  translatedLineEndPoint = np.array([0,0,0])
  lineNode.GetNthControlPointPosition(0,translatedLineStartPoint)
  lineNode.GetNthControlPointPosition(1,translatedLineEndPoint)
  translatedLineDirection = (translatedLineEndPoint - translatedLineStartPoint)/np.linalg.norm(translatedLineEndPoint - translatedLineStartPoint)
  cosOfAngle = vtk.vtkMath.Dot(lineDirection,translatedLineDirection)
  import math
  angleDifference = math.degrees(math.acos(cosOfAngle))
  print(angleDifference)

moveLineOnLineDirection()

</code></pre>
<p>Open Slicer, open the python interactor, paste the code, see that the printed angle difference is near 1degree and it should be zero, (optional, move the line control points, execute moveLineOnLineDirection again and see the angle difference result: it’s not always zero)</p>

---

## Post #2 by @lassoan (2021-06-15 16:45 UTC)

<p>The problem is that you create an integer numpy array for storing the coordinates. This leads to loss of precision. For example:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a=np.array([0,0,0])
&gt;&gt;&gt; a[0]=1.2
&gt;&gt;&gt; a
array([1, 0, 0])
</code></pre>
<p>Example for markups:</p>
<pre><code class="lang-python">&gt;&gt;&gt; translatedLineStartPoint = np.array([0,0,0])  # this is an int32 array
&gt;&gt;&gt; lineNode.GetNthControlPointPosition(0,translatedLineStartPoint)
&gt;&gt;&gt; translatedLineStartPoint
array([40,  9,  0])

&gt;&gt;&gt; translatedLineStartPoint = np.zeros(3)
&gt;&gt;&gt; lineNode.GetNthControlPointPosition(0,translatedLineStartPoint)
&gt;&gt;&gt; translatedLineStartPoint
array([40.20532872,  9.58185779,  0.        ])
</code></pre>
<p><strong>Always use <code>np.zeros(3)</code> to create a numpy array initialized to zero.</strong> It is shorter and it correctly creates a float array.</p>

---

## Post #3 by @mau_igna_06 (2021-06-15 17:23 UTC)

<p>Yes Andras. Thank you very much!</p>

---
