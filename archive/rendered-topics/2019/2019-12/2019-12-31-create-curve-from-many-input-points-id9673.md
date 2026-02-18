# Create curve from many input points

**Topic ID**: 9673
**Date**: 2019-12-31
**URL**: https://discourse.slicer.org/t/create-curve-from-many-input-points/9673

---

## Post #1 by @RayCui (2019-12-31 10:32 UTC)

<p>Hi, Andras<br>
I have a numpy array that contains some points. I want to create a vtkMRMLMarkupsCurveNode. So, I call the function curveNode.AddControlPoint() to add every point coordinate. But that’s too slow. What’s the better way to do this?<br>
Thank you.</p>
<pre><code>for pointIndex in range(len(centerlinePoints)):
    centerlineCurveNode.AddControlPoint(vtk.vtkVector3d(centerlinePoints[pointIndex][0], centerlinePoints[pointIndex][1], centerlinePoints[pointIndex][2]))</code></pre>

---

## Post #2 by @lassoan (2019-12-31 15:07 UTC)

<p>How many control points are you trying to add?</p>
<p>You may speed up node updates if you call <code>wasModify=centerlineCurveNode.StartModify()</code> before starting to add points and call <code>centerlineCurveNode.EndModify(wasModify)</code> when you are done.</p>
<p>If you have hundreds or thousands of points then you can update them all at once using<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#ab0146489b4bc1beef9760f73cce7ad4d">SetControlPointPositionsWorld</a> (if you have your inputs as a numpy array then you need to convert the array to vtkPoints object first).</p>
<p>If you have thousands of points then probably you also want to reduce number of interpolated points using <code>SetNumberOfPointsPerInterpolatingSegment()</code>.</p>

---

## Post #3 by @RayCui (2020-01-02 02:31 UTC)

<p>Hundreds of  control points.<br>
I adopt your sencond solution: <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#ab0146489b4bc1beef9760f73cce7ad4d" rel="nofollow noopener">SetControlPointPositionsWorld</a>, That’s run fast. Thank you Andras.<br>
Some code:</p>
<pre><code>points = vtk.vtkPoints()
vtkpointsData = vtk.util.numpy_support.numpy_to_vtk(centerlinePoints, deep=1)
points.SetNumberOfPoints(len(centerlinePoints))
points.SetData(vtkpointsData)
centerlineCurveNode.SetControlPointPositionsWorld(points)</code></pre>

---

## Post #4 by @yee_lu (2020-12-21 17:02 UTC)

<p>Hello! When I input your code in the python interrupter , I get “name ‘centerlineCurveNode’ is not defined”. Can you tell me how to import centerlineCurveNode? Thank you in advance.</p>

---

## Post #5 by @lassoan (2020-12-21 17:45 UTC)

<p>Replace <code>centerlineCurveNode</code> with your curve node. You can get a curve node from its name by calling:</p>
<pre><code>centerlineCurveNode = getNode('NameOfMyCurveNode')</code></pre>

---

## Post #6 by @yee_lu (2021-03-01 06:10 UTC)

<p>Hello！ I run the code above , but I didn’t see anything in 3Dslicer， how to show the curve?  Thank you in advance!</p>

---

## Post #7 by @lassoan (2021-03-01 14:47 UTC)

<p>Here is a complete example that works fine in recent Slicer versions:</p>
<pre data-code-wrap="python"><code class="lang-python"># Create random numpy array to use as input
import numpy as np
pointPositions = np.random.uniform(-50,50,size=[15,3])

# Create curve from numpy array
curveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.util.updateMarkupsControlPointsFromArray(curveNode, pointPositions)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df86fb0cfa10c10371018afa410d866bccea5699.png" alt="image" data-base62-sha1="vTpFzZQspHvy4ZCHIYifwvcbyNH" width="421" height="328"></p>

---

## Post #8 by @Greydon_Gilmore (2021-03-16 05:20 UTC)

<p>How would you then assign labels to the points? Would you iterate through each Nth point to add  the label (via <code>SetNthControlPointLabel</code>)?</p>
<p>I have hundreds of points but also need to label each one.</p>
<p>Greydon</p>
<pre><code class="lang-auto"></code></pre>

---
