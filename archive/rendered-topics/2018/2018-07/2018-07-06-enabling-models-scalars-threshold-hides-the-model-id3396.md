# Enabling models scalars threshold hides the model

**Topic ID**: 3396
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/enabling-models-scalars-threshold-hides-the-model/3396

---

## Post #1 by @Fernando (2018-07-06 11:11 UTC)

<p>Hi all,</p>
<p>I’m trying to use the scalars threshold of the Models module for the first time, but when I enable it, the model disappears. I might be doing something wrong. Can you please give me some advice? If you confirm that it’s a bug, I can report it in the issue tracker.</p>
<p>Here’s some code you can paste in the console to create some poly data with associated scalars:</p>
<pre><code class="lang-python">import numpy as np

points = vtk.vtkPoints()
vertices = vtk.vtkCellArray()

sizes = vtk.vtkFloatArray()
sizes.SetName('Sizes')

zMin, zMax = -50, 50
N = 1000
N += 1
b = 2
aMax = 20
z = np.linspace(zMin, zMax, N)
a = (zMax - z)/zMax * aMax
x = a * np.sin(z / b)
y = a * np.cos(z / b)
pointsArray = np.vstack((x, y, z)).T
indices = (z - zMin) / (zMax - zMin) * 300
indices = indices.clip(0, 255).astype(np.uint8)

for i in range(len(pointsArray - 1)):
    point = pointsArray[i]
    pointID = points.InsertNextPoint(point)
    cellID = vertices.InsertNextCell(1)
    vertices.InsertCellPoint(pointID)
    size = a[i]/20
    _ = sizes.InsertNextValue(size)

pointsPolyData = vtk.vtkPolyData()
pointsPolyData.SetPoints(points)
pointsPolyData.SetVerts(vertices)
pointsData = pointsPolyData.GetPointData()
_ = pointsData.SetScalars(sizes)


modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
modelNode.CreateDefaultDisplayNodes()
modelNode.SetAndObservePolyData(pointsPolyData)

modelDisplay = modelNode.GetDisplayNode()
modelDisplay.SetAndObserveColorNodeID('vtkMRMLColorTableNodeFileViridis.txt')
modelDisplay.SetScalarVisibility(True)
modelDisplay.SetActiveScalarName('Sizes')
modelDisplay.SetPointSize(3)

layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)

threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()
</code></pre>

---

## Post #2 by @lassoan (2018-07-06 18:30 UTC)

<p>Before going into the details, could you explain what you would like to achieve?</p>

---

## Post #3 by @Fernando (2018-07-07 09:50 UTC)

<p>I have a vessel network generated with VMTK, which has associated scalars representing vessel diameter. I want to use a threshold to interactively show vessels of a specific range of diameters.</p>

---

## Post #4 by @lassoan (2018-07-07 14:58 UTC)

<p>You can very easily and accurately cut polydata based on associated point or cell scalar values by using VTK thresholding filters, such as vtkThreshold.</p>

---

## Post #5 by @Fernando (2018-07-07 17:03 UTC)

<p>I know, but my understanding is that this feature is currently included in the Slicer core, and I think it doesn’t work.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/6e7af66c1567b05a05249dd149872568161a9e58/Libs/MRML/Core/vtkMRMLModelDisplayNode.cxx#L276-L284" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6e7af66c1567b05a05249dd149872568161a9e58/Libs/MRML/Core/vtkMRMLModelDisplayNode.cxx#L276-L284" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/6e7af66c1567b05a05249dd149872568161a9e58/Libs/MRML/Core/vtkMRMLModelDisplayNode.cxx#L276-L284</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="276" style="counter-reset: li-counter 275 ;">
<li>void vtkMRMLModelDisplayNode::SetThresholdRange(double min, double max)</li>
<li>{</li>
<li>vtkMTimeType mtime = this-&gt;ThresholdFilter-&gt;GetMTime();</li>
<li>this-&gt;ThresholdFilter-&gt;ThresholdBetween(min, max);</li>
<li>if (this-&gt;ThresholdFilter-&gt;GetMTime() &gt; mtime)</li>
<li>  {</li>
<li>  this-&gt;Modified();</li>
<li>  }</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2018-07-09 16:43 UTC)

<p>Settings in the display node are for display only (does not change the data stored in the model node), so you cannot use that to trim the data set.</p>
<p>However, if you only need to hide parts of your data set for display then you are right, model display settings should be usable.</p>
<p>Thresholding only worked correctly for unstructured grid models and point scalars. I’ve fixed this in r27270. It should be available in tomorrow’s nightly build.</p>

---

## Post #7 by @Fernando (2018-07-09 16:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="3396">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you only need to hide parts of your data set for display</p>
</blockquote>
</aside>
<p>Yes, this is what I wanted. I’ll try tomorrow and let you know. Thanks!</p>

---
