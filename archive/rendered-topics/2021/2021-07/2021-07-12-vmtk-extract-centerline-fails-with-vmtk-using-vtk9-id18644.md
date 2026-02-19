---
topic_id: 18644
title: "Vmtk Extract Centerline Fails With Vmtk Using Vtk9"
date: 2021-07-12
url: https://discourse.slicer.org/t/18644
---

# VMTK extract centerline fails with VMTK using VTK9

**Topic ID**: 18644
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/vmtk-extract-centerline-fails-with-vmtk-using-vtk9/18644

---

## Post #1 by @chir.set (2021-07-12 16:38 UTC)

<p>Using 4.13.0-2021-07-11 r30039 / 27f99af factory built, and factory SlicerVMTK-Extension on Arch Linux.</p>
<p>Network models and curves are generated.<br>
—<br>
Tree model fails : 0 point, 0 cell. No errors in Python console. Application log reports :</p>
<pre><code class="lang-auto">Found CommandLine Module, target is  /home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation
ModuleType: CommandLineModule
Decimation command line: 

/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation --reductionFactor 0.925105 --method FastQuadric --deleteBoundary --aggressiveness 4 /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBG.obj /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBH.obj 

Decimation standard output:

Input: 66760 vertices,133472 triangles (target 9996)
Output: 8463 vertices,16920 triangles (0.873232 reduction)

Decimation completed without errors

ReadDataInternal (vtkMRMLModelStorageNode6): File /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBH.obj does not contain coordinate system information. Assuming LPS.


End of Centerline Computation..
vtkvmtkSimplifyVoronoiDiagram::RequestData is not functionnal when built against VTK &gt;= 9


Algorithm vtkvmtkSimplifyVoronoiDiagram(0x13e1ab70) returned failure for request: vtkInformation (0x13d1dd00)
  Debug: Off
  Modified Time: 32642077
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_DATA
  FROM_OUTPUT_PORT: 0
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Cost function array with name specified does not exist!


Cost function array with name specified does not exist!


Descent array with name specified does not exist!
</code></pre>
<p>—</p>
<p>Tree curve fails with the following errors  in Python console:</p>
<pre><code class="lang-auto">Failed to compute results: 'NoneType' object has no attribute 'GetValue'
Traceback (most recent call last):
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 318, in onApplyButton
    self.logic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode, curveSamplingDistance)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 914, in createCurveTreeFromCenterline
    self.addCenterlineCurves(mergedCenterlines, centerlineCurveNode)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 923, in addCenterlineCurves
    self._addCenterline(mergedCenterlines, replaceCurve=centerlineCurveNode)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 950, in _addCenterline
    groupId = mergedCenterlines.GetCellData().GetArray(self.groupIdsArrayName).GetValue(cellId)
AttributeError: 'NoneType' object has no attribute 'GetValue'
</code></pre>
<p>—<br>
And these in application log :</p>
<pre><code class="lang-auto">Found CommandLine Module, target is  /home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation
ModuleType: CommandLineModule
Decimation command line: 

/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/bin/../lib/Slicer-4.13/cli-modules/Decimation --reductionFactor 0.925105 --method FastQuadric --deleteBoundary --aggressiveness 4 /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBI.obj /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBJ.obj 

Decimation standard output:

Input: 66760 vertices,133472 triangles (target 9996)
Output: 8463 vertices,16920 triangles (0.873232 reduction)

Decimation completed without errors

ReadDataInternal (vtkMRMLModelStorageNode7): File /tmp/Slicer/CGCCEF_vtkMRMLModelNodeBJ.obj does not contain coordinate system information. Assuming LPS.


End of Centerline Computation..
vtkvmtkSimplifyVoronoiDiagram::RequestData is not functionnal when built against VTK &gt;= 9


Algorithm vtkvmtkSimplifyVoronoiDiagram(0xc3f9920) returned failure for request: vtkInformation (0x1a29ae40)
  Debug: Off
  Modified Time: 33443953
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_DATA
  FROM_OUTPUT_PORT: 0
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




Cost function array with name specified does not exist!


Cost function array with name specified does not exist!


Descent array with name specified does not exist!


Failed to compute results: 'NoneType' object has no attribute 'GetValue'
RadiusArray with name specified does not exist


RadiusArray with name specified does not exist


Failed to compute results: 'NoneType' object has no attribute 'GetValue'
Traceback (most recent call last):
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 318, in onApplyButton
    self.logic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode, curveSamplingDistance)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 914, in createCurveTreeFromCenterline
    self.addCenterlineCurves(mergedCenterlines, centerlineCurveNode)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 923, in addCenterlineCurves
    self._addCenterline(mergedCenterlines, replaceCurve=centerlineCurveNode)
  File "/home/user/programs/Test/Slicer-4.13.0-2021-07-11-linux-amd64/NA-MIC/Extensions-30039/SlicerVMTK/lib/Slicer-4.13/qt-scripted-modules/ExtractCenterline.py", line 950, in _addCenterline
    groupId = mergedCenterlines.GetCellData().GetArray(self.groupIdsArrayName).GetValue(cellId)
AttributeError: 'NoneType' object has no attribute 'GetValue'
</code></pre>
<p>—</p>
<p>Same observations with home built Slicer and SlicerVMTK-Extension.</p>
<p>That’s since SlicerVMTK-Extension built with VTK9.</p>
<p>My last VTK8 builds were fine.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-07-12 17:34 UTC)

<p>Unfortunately, Voronoi smoothing is currently broken (VTK API drastically changed, which requires update of the filter). For now, you need to disable this feature by setting <code>centerlineFilter.SetSimplifyVoronoi(0)</code> here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/d47d8ce70b3222ca08ea40ac27ce1f56e1ef9137/ExtractCenterline/ExtractCenterline.py#L705">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/d47d8ce70b3222ca08ea40ac27ce1f56e1ef9137/ExtractCenterline/ExtractCenterline.py#L705" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/d47d8ce70b3222ca08ea40ac27ce1f56e1ef9137/ExtractCenterline/ExtractCenterline.py#L705" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/d47d8ce70b3222ca08ea40ac27ce1f56e1ef9137/ExtractCenterline/ExtractCenterline.py#L705</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="695" style="counter-reset: li-counter 694 ;">
          <li>slicer.tubePolyData = tubePolyData
</li>
          <li>
</li>
          <li>centerlineFilter = vtkvmtkComputationalGeometry.vtkvmtkPolyDataCenterlines()
</li>
          <li>centerlineFilter.SetInputData(tubePolyData)
</li>
          <li>centerlineFilter.SetSourceSeedIds(sourceIdList)
</li>
          <li>centerlineFilter.SetTargetSeedIds(targetIdList)
</li>
          <li>centerlineFilter.SetRadiusArrayName(self.radiusArrayName)
</li>
          <li>centerlineFilter.SetCostFunction('1/R')  # this makes path search prefer go through points with large radius
</li>
          <li>centerlineFilter.SetFlipNormals(False)
</li>
          <li>centerlineFilter.SetAppendEndPointsToCenterlines(0)
</li>
          <li class="selected">centerlineFilter.SetSimplifyVoronoi(1)  # this slightly improves connectivity
</li>
          <li>centerlineFilter.SetCenterlineResampling(0)
</li>
          <li>centerlineFilter.SetResamplingStepLength(curveSamplingDistance)
</li>
          <li>centerlineFilter.Update()
</li>
          <li>
</li>
          <li>centerlinePolyData = vtk.vtkPolyData()
</li>
          <li>centerlinePolyData.DeepCopy(centerlineFilter.GetOutput())
</li>
          <li>
</li>
          <li>voronoiDiagramPolyData = vtk.vtkPolyData()
</li>
          <li>voronoiDiagramPolyData.DeepCopy(centerlineFilter.GetVoronoiDiagram())
</li>
          <li>
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It would be great if you could test this and if everything works well then submit a pull request with this change.</p>

---

## Post #3 by @chir.set (2021-07-12 18:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For now, you need to disable this feature</p>
</blockquote>
</aside>
<p>Setting SetSimplifyVoronoi(0) does allow the centerline model and curve to be created.</p>
<p>I pushed the change, but it is merged in the <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/32" rel="noopener nofollow ugc">PR</a> already open for Centerline metrics. Though I clicked ‘New pull request’ in my fork. Is it a problem ? How should I do otherwise ?</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2021-07-12 19:29 UTC)

<p>Thank you, I’ve cherry-picked your commit (and added a version check so that the smoothing is still performed in older Slicer versions).</p>
<p>You pushed the change into the same branch, probably that’s why it is included in the same open pull request that you have for that branch.</p>

---
