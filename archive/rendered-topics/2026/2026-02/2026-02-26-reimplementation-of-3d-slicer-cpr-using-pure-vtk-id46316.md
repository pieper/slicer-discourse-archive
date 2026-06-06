---
topic_id: 46316
title: "Reimplementation of 3D slicer CPR using pure VTK"
date: 2026-02-26
url: https://discourse.slicer.org/t/46316
last_bumped: 2026-06-05T16:10:02.510Z
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

## Post #2 by @Thibault_Pelletier (2026-03-03 07:33 UTC)

<p>Hi <a class="mention" href="/u/s-linh">@S-Linh</a>,</p>
<p>VTK js already has a CPR implementation : <a href="https://kitware.github.io/vtk-js/api/Rendering_Core_ImageCPRMapper.html" class="inline-onebox" rel="noopener nofollow ugc">ImageCPRMapper | VTK.js</a></p>
<p>There is also a pure VTK CPR implementation available through the <a href="https://vtk.org/doc/nightly/html/classvtkOpenGLSurfaceProbeVolumeMapper.html" rel="noopener nofollow ugc">vtkOpenGLSurfaceProbeVolumeMapper</a></p>
<p>For the C++ implementation, you can have a look at the <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/v9.6.0/Rendering/VolumeOpenGL2/Testing/Cxx/TestSurfaceProbeVolumeMapper.cxx" rel="noopener nofollow ugc">tests</a> for an example on how to use the mapper.</p>
<p>For VTK js, you also have an <a href="https://github.com/Kitware/vtk-js/blob/3b54de3b9a8a338aa9dad237efe24045dfb6e8b1/Sources/Rendering/Core/ImageCPRMapper/example/index.js#L18" rel="noopener nofollow ugc">example available</a></p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @S_G (2026-04-17 19:03 UTC)

<p>Hi <a class="mention" href="/u/s-linh">@S-Linh</a>,</p>
<p>You don’t need to translate Slicer MRML. A more direct approach is to use <strong>VTK.js ImageCPRMapper</strong> and integrate it within OHIF.</p>
<p>I implemented a CPR prototype using:</p>
<ul>
<li>
<p>VTK.js ImageCPRMapper for CPR rendering</p>
</li>
<li>
<p>Custom Cornerstone3D CPR viewports, fully supporting native Cornerstone3D tools and interaction</p>
</li>
<li>
<p>OHIF Viewer as the integration layer</p>
</li>
</ul>
<p>It demonstrates:</p>
<ul>
<li>
<p>Curved planar reformation viewport and cross-sectional viewports with custom tooling</p>
</li>
<li>
<p>Real-time centerline editing with live CPR re-rendering</p>
</li>
<li>
<p>Segmentation rendering pipeline integration</p>
</li>
</ul>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eb406b4b6ae099ccfee8430a1a6d2e35efcf152.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/317b5a41d807e5cf52457ba7eb7cb8e90dc05408.jpeg" data-video-base62-sha1="i4RRFrAHD3c5HpCYE5kwMqwzA0q.mp4">
  </div><p></p>

---

## Post #4 by @S-Linh (2026-04-20 02:59 UTC)

<p><a class="mention" href="/u/s_g">@S_G</a> Hi Gaber, Can you share the source code of your CPR prototype?</p>

---

## Post #5 by @S-Linh (2026-04-20 03:19 UTC)

<p><a class="mention" href="/u/s_g">@S_G</a> I have questions, as I am new to all these:</p>
<ul>
<li>What are the 3 viewports on the right of the CPR viewport result? how do they work?</li>
<li>How do you calculate the orientation of each centerline?</li>
<li>Are you generating centerlines based on coronal/sagittal/axial view of the original CT dicom images?</li>
</ul>

---

## Post #6 by @heart_project (2026-06-03 12:44 UTC)

<p><a class="mention" href="/u/s_g">@S_G</a></p>
<p>Amazing results!</p>
<p>I’m building something similar with OHIF and vtkImageCPRMapper and I’m particularly interested in the step before CPR generation: obtaining the coronary centerline from the axial CT images.</p>
<p>Did you implement any vessel tracking / centerline extraction algorithm, or is the current prototype based on manually placed centerline control points?</p>
<p>If coronary extraction is not part of this prototype, would you recommend starting with a simple Draw Centerline Tool based on seed points placed on the axial view and then generating a spline for the CPR?</p>
<p>Any insight into the strategy you used (or would recommend) would be greatly appreciated.</p>

---

## Post #7 by @mikebind (2026-06-05 16:10 UTC)

<p>I’m not the original poster, but <a href="http://www.vmtk.org/" rel="noopener nofollow ugc">VMTK (Vessel Modeling Tool Kit)</a> is a great option for finding vessel centerlines, and is easy to use from Slicer via the VMTK Slicer extension (installable via the extension manager).</p>

---
