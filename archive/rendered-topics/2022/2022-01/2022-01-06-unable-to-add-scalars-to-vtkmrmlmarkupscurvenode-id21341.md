# Unable to add scalars to `vtkMRMLMarkupsCurveNode`

**Topic ID**: 21341
**Date**: 2022-01-06
**URL**: https://discourse.slicer.org/t/unable-to-add-scalars-to-vtkmrmlmarkupscurvenode/21341

---

## Post #1 by @keri (2022-01-06 02:57 UTC)

<p>Hi,</p>
<p>I’m trying to create scalars and add it to the <code>vtkMRMLMarkupsCurveNode</code>. Then I go to the <code>Markups</code> module and I cant find any scalars except <code>PedigreeIDs</code>. Probably I do something wrong… here is the script I use:</p>
<pre><code class="lang-python"># Create random numpy array to use as input
import numpy as np
pointPositions = np.random.uniform(-10,10,size=[4,3])

# Create curve from numpy array
curveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.util.updateMarkupsControlPointsFromArray(curveNode, pointPositions)

# Create scalars
scalars = vtk.vtkDoubleArray()
scalars.SetName('MyScalars')
scalars.InsertNextValue(0)
scalars.InsertNextValue(1)
scalars.InsertNextValue(-1)
scalars.InsertNextValue(3)

# Add scalars to curve node
curveNode.GetCurve().GetPointData().SetScalars(scalars)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbc7f0596d855c4ecdbc34767d9b6ae88edf8380.jpeg" data-download-href="/uploads/short-url/qNbEy2fw73GzntBTu0bU7SpPmpy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbc7f0596d855c4ecdbc34767d9b6ae88edf8380_2_690x332.jpeg" alt="image" data-base62-sha1="qNbEy2fw73GzntBTu0bU7SpPmpy" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbc7f0596d855c4ecdbc34767d9b6ae88edf8380_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbc7f0596d855c4ecdbc34767d9b6ae88edf8380_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbc7f0596d855c4ecdbc34767d9b6ae88edf8380_2_1380x664.jpeg 2x" data-dominant-color="ABACB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1551×748 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @keri (2022-01-29 21:10 UTC)

<p>It seems that scalars in markups are prette tricky.</p>
<p>First of all the number of <code>ControlPoints</code> in markups doesn’t match the number of points of inner poly data object. For example in my case if I have only 4 <code>ControlPoints</code> then I can see that poly data has 31 points.</p>
<p>The next thing is that I was able to add scalars only after copying <code>PedigreeIDs</code> array to my array (using <code>ShallowCopy</code> or <code>DeepCopy</code>) and then adding my array to the polyData’s points data :</p>
<pre><code class="lang-auto"># Create random numpy array to use as input
import numpy as np
pointPositions = np.random.uniform(-10,10,size=[4,3])

# Create curve from numpy array
curveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.util.updateMarkupsControlPointsFromArray(curveNode, pointPositions)

# Get pedigree array
p=curveNode.GetCurve().GetPointData().GetArray('PedigreeIDs')

# Create scalars
np_scalars = np.random.uniform(-10,10,size=curveNode.GetCurve().GetNumberOfPoints())

scalars = vtk.vtkDoubleArray()
scalars.SetName('MyScalars')
scalars.SetVoidArray(np_scalars, np_scalars.size, 1)

# Copy from pedigree to scalars
p.ShallowCopy(scalars)	# or use DeppCopy()

# Add scalars to curve node
curveNode.GetCurve().GetPointData().SetScalars(scalars)
</code></pre>
<p>And the last thing is that my scalars are gone right after I do some manipulations with <code>ControlPoints</code> for example moving a single point. The <code>PedigreeIDs</code> array replaces my scalars then.</p>

---

## Post #3 by @keri (2022-02-05 15:34 UTC)

<p>It seems that even this solution doesn’t work anymore.<br>
If somebody knows a reason please share</p>

---

## Post #4 by @lassoan (2022-10-14 23:54 UTC)

<p>Curve scalars are managed by measurements (because in general you must update the scalars when the curve is modified). If you just add a scalar array then it will be automatically removed when the curve is updated.</p>
<p>If you don’t want to implement a new measurement then you can use the <code>vtkMRMLStaticMeasurement</code> class (see example <a href="https://github.com/Slicer/Slicer/blob/3a6d7b3d9a7e0f649fc6db40b360b798a79dfb57/Modules/Loadable/Markups/Testing/Python/MarkupsCurveMeasurementsTest.py#L130-L135">here</a>. You need to observe curve modified events and update the scalars in the measurement.</p>

---

## Post #5 by @keri (2022-10-15 12:45 UTC)

<p>Thank you very much!<br>
That should work.</p>

---
