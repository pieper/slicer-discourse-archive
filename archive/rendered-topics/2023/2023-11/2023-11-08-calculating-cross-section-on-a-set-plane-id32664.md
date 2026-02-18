# Calculating cross section on a set plane

**Topic ID**: 32664
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/calculating-cross-section-on-a-set-plane/32664

---

## Post #1 by @AKue (2023-11-08 09:54 UTC)

<p>Hello!</p>
<p>I have a segmentation (here in blue) and I would like to calculate the cross section with a preset plane.<br>
Is there a quick way to do so?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/823fc262855ca051093c6c42087b6ba7c633ec82.png" data-download-href="/uploads/short-url/iAeFQaCV2nDGz77Xnqu5Omrih3A.png?dl=1" title="Bildschirmfoto 2023-11-08 um 10.50.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/823fc262855ca051093c6c42087b6ba7c633ec82_2_530x500.png" alt="Bildschirmfoto 2023-11-08 um 10.50.10" data-base62-sha1="iAeFQaCV2nDGz77Xnqu5Omrih3A" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/823fc262855ca051093c6c42087b6ba7c633ec82_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/823fc262855ca051093c6c42087b6ba7c633ec82_2_795x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/823fc262855ca051093c6c42087b6ba7c633ec82_2_1060x1000.png 2x" data-dominant-color="8F8FC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-11-08 um 10.50.10</span><span class="informations">1171×1104 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @RafaelPalomar (2023-11-08 13:57 UTC)

<p><a class="mention" href="/u/akue">@AKue</a> a segmentation has different representations (most notably binary labelmap image and closed surface mesh).  Cross-section in different representations will typically be different and require different methods. For instance, the cross-section of a 3D surface mesh woud look like a contour and the cross-section of a binary image would look like a blob.  The output datatype will be also different in 3D mesh you will get a polydata where in a binary image you would get an image.</p>
<p>What is what you want to achieve?</p>

---

## Post #3 by @mau_igna_06 (2023-11-08 13:58 UTC)

<p>Maybe try this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/30ff1275fb4cbff0ae09ca0fdb8d4edb0569cd01/BoneReconstructionPlanner/BRPLib/helperFunctions.py#L8-L23">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/30ff1275fb4cbff0ae09ca0fdb8d4edb0569cd01/BoneReconstructionPlanner/BRPLib/helperFunctions.py#L8-L23" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/30ff1275fb4cbff0ae09ca0fdb8d4edb0569cd01/BoneReconstructionPlanner/BRPLib/helperFunctions.py#L8-L23" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/30ff1275fb4cbff0ae09ca0fdb8d4edb0569cd01/BoneReconstructionPlanner/BRPLib/helperFunctions.py#L8-L23</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="8" style="counter-reset: li-counter 7 ;">
          <li>def getIntersectionBetweenModelAnd1Plane(modelNode,planeNode,intersectionModel):</li>
          <li>  plane = vtk.vtkPlane()</li>
          <li>  origin = [0,0,0]</li>
          <li>  normal = [0,0,0]</li>
          <li>  planeNode.GetOrigin(origin)</li>
          <li>  planeNode.GetNormal(normal)</li>
          <li>  plane.SetOrigin(origin)</li>
          <li>  plane.SetNormal(normal)</li>
          <li></li>
          <li>  cutter = vtk.vtkCutter()</li>
          <li>  cutter.SetInputData(modelNode.GetPolyData())</li>
          <li>  cutter.SetCutFunction(plane)</li>
          <li>  cutter.Update()</li>
          <li></li>
          <li>  intersectionModel.SetAndObservePolyData(cutter.GetOutput())</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #4 by @RafaelPalomar (2023-11-08 14:00 UTC)

<p>That would be for cross-sections of 3D surfaces. Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>!</p>

---

## Post #5 by @lassoan (2023-11-08 14:58 UTC)

<p>You may also use the <a href="https://github.com/vmtk/SlicerExtension-VMTK/tree/master#the-vmtk-extension-for-3d-slicer">“Cross-Section Analysis” module</a> in VMTK extension. It does not just compute the cross-sectional area in two planes but many planes along a line or curve.</p>

---

## Post #6 by @AKue (2023-11-09 09:26 UTC)

<p>Thanks for all your input!!<br>
My aim is to get the exact size (square millimeter) of the cross section between plane and segmentation. For me it doesn’t matter if by 3D surface mesh or binary labelmap.<br>
It should be fast, accurate and reproducible.</p>
<p>Thanks for all your help!</p>

---

## Post #7 by @chir.set (2023-11-09 19:50 UTC)

<aside class="quote no-group" data-username="AKue" data-post="6" data-topic="32664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> AKue:</div>
<blockquote>
<p>3D surface mesh or binary labelmap.</p>
</blockquote>
</aside>
<p>You may install SlicerVMTK extension using the extension manager to use the '<a href="https://github.com/vmtk/SlicerExtension-VMTK/tree/master/StenosisMeasurement2D" rel="noopener nofollow ugc">Stenosis measurement: 2D’ module</a>. It can calculate the cut surface area of a segment using the orientation of a slice view that you specify. Of course, you should reformat the slice view to be that of your planes.</p>
<p>To help you quickly reformat a slice view to a plane, you may install <a href="https://gitlab.com/chir-set/RcHacks7" rel="noopener nofollow ugc">this</a> project. It’s a manual step, done once only. If you don’t know what is the ‘.slicerrc.py’ file, the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" rel="noopener nofollow ugc">online manual</a> will help you.</p>
<p>You must of course restart Slicer after the installations.</p>

---
