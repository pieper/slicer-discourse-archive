---
topic_id: 46316
title: "Reimplementation Of 3D Slicer Cpr Using Pure Vtk"
date: 2026-02-26
url: https://discourse.slicer.org/t/46316
---

# Reimplementation of 3D slicer CPR using pure VTK

**Topic ID**: 46316
**Date**: 2026-02-26
**URL**: https://discourse.slicer.org/t/reimplementation-of-3d-slicer-cpr-using-pure-vtk/46316

---

## Post #1 by @S-Linh (2026-02-26 19:55 UTC)

<p>Hello everyone,</p>
<p>I’m trying to develop 3d Slicer Curve Planar Reformation in my own PACS Viewer, specifically OHIF:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430" target="_blank" rel="noopener nofollow ugc">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430" target="_blank" rel="noopener nofollow ugc">CurvedPlanarReformat/CurvedPlanarReformat.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430" rel="noopener nofollow ugc"><code>8235ee89a</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="395" style="counter-reset: li-counter 394 ;">
          <li>import SampleData</li>
          <li>volumeNode = SampleData.SampleDataLogic().downloadDentalSurgery()[1]</li>
          <li></li>
          <li># Define curve</li>
          <li>curveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode')</li>
          <li>curveNode.CreateDefaultDisplayNodes()</li>
          <li>curveNode.GetCurveGenerator().SetNumberOfPointsPerInterpolatingSegment(25) # add more curve points between control points than the default 10</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-45.85526315789473, -104.59210526315789, 74.67105263157896))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-50.9078947368421, -90.06578947368418, 66.4605263157895))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-62.27631578947368, -78.06578947368419, 60.7763157894737))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-71.86705891666716, -58.04403581456746, 57.84679891116521))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-74.73084356325877, -48.67611043794342, 57.00664267528636))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-88.17105263157895, -35.75, 55.092105263157904))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-99.53947368421052, -35.75, 55.092105263157904))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-107.75, -43.96052631578948, 55.092105263157904))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-112.80263157894736, -59.118421052631575, 56.355263157894754))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-115.32894736842104, -73.01315789473684, 60.144736842105274))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-125.43421052631578, -83.74999999999999, 60.7763157894737))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-132.3815789473684, -91.96052631578947, 63.934210526315795))</li>
          <li>curveNode.AddControlPoint(vtk.vtkVector3d(-137.43421052631578, -103.96052631578947, 67.72368421052633))</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m looking to use VTK Wasm to implement this. My question is:<br>
Since Slicer’s CPR extension is made specifically for Slicer, is it possible to translate those Slicer’s MRML abstractions to pure vtk/vtk.js code?<br>
How should I approach this?</p>

---
