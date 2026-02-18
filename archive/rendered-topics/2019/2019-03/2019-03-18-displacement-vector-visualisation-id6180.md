# Displacement Vector Visualisation

**Topic ID**: 6180
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/displacement-vector-visualisation/6180

---

## Post #1 by @GerryG (2019-03-18 03:14 UTC)

<p>I have a Model read in from a .vtu file in an unstructured grid format. Each point in this unstructured grid has its position data which visualises nicely but it also has a unique PointData Vector associated with it describing that point’s displacement from a previous time step. I’m wondering if there is a way to turn those vectors into a glyph. I’m aware that the Transformation module is designed to do this with Volumes but I can’t see how to make it work with a Model, especially given that the deformations cannot be summarised in a Transformation Matrix.<br>
Thank you!</p>

---

## Post #2 by @lassoan (2019-03-18 04:35 UTC)

<p>Slicer’s transforms module requires transforms that define displacements (and their inverse) everywhere, not just at specific sample points.</p>
<p>You can construct a transform from displacements known at random points by creating a <a href="https://vtk.org/doc/nightly/html/classvtkThinPlateSplineTransform.html" rel="nofollow noopener">thin-plate-spline transform</a>. It is probably 10-15 lines of Python code: use original point coordinates as source landmarks, use warp filter to compute displaced point coordinates, use those as target landmarks, then set the VTK transform to a new transform node.</p>
<p>If you had many thousands of points then evaluating the thin-plate-spline transform could take a long time. You can then use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ScatteredTransform" rel="nofollow noopener">ScatteredTransform extension</a> to create a regularly sampled b-spline displacement field from sparse samples, which may make the transform magnitudes faster to evaluate.</p>

---

## Post #3 by @Saima (2020-02-27 03:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>arp filter to compute displaced point coordinates,</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Would you please give me some information on how can i use warpbyvector filter in slicer for warping models.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @lassoan (2020-02-27 20:09 UTC)

<p>You can get the mesh from the model node, set it as input to a <a href="https://vtk.org/doc/nightly/html/classvtkWarpVector.html#details">vtkWarpVector</a>, and create a new model from the output of the filter.</p>

---

## Post #5 by @Saima (2020-03-05 05:54 UTC)

<p>Hi Andras,<br>
I tried it<br>
mesh =  model.GetMesh()<br>
warpvector = vtk.vtkWarpVector()<br>
warpvector.SetInputData(mesh)<br>
warpvector.Update()<br>
output = warpvector.GetUnstructuredGridOutput()</p>
<p>mesh2 = vtk.vtkUnstructuredGrid()<br>
mesh2.SetPoints(output.GetPoints())<br>
mesh2.SetCells(output.GetCellTypesArray(),output.GetCellLocationsArray(), output.GetCells())<br>
mesh2.UpdateCellGhostArrayCache()<br>
mesh2.UpdatePointGhostArrayCache()</p>
<p>modelNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’)<br>
modelNode.SetAndObserveMesh(mesh2)</p>
<p>but didnt get the warped model. Could you please see what am I missing in the code above.</p>
<p>It gives me the exact model as before.</p>
<p>Thanks alot</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @lassoan (2020-03-05 13:38 UTC)

<p>Probably you just miss active vector selection, warping mode setting, etc. Check out warp filter <a href="https://lorensen.github.io/VTKExamples/site">VTK examples</a> to see what exactly you need to set and how.</p>

---

## Post #7 by @Saima (2020-03-06 05:31 UTC)

<p>Thanks Andras. Yes I was missing the setactivevectors for the mesh grid.</p>
<p>Thanks a lot</p>

---

## Post #8 by @Saima (2020-05-01 06:12 UTC)

<p>Hi andras,<br>
Is it possible to show the coloring for the deformed mesh according to the displacements</p>

---

## Post #9 by @Saima (2021-01-29 05:47 UTC)

<p>Hi Andras,<br>
I am trying to offset a mesh using warpvector by setting the setscalarfactor. But dont know what is missing . could you please see the attached code.</p>
<p>Thank you or is there any other way to get one or two layers of extranodes around the existing mesh.</p>
<p>Thank you<br>
modelNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’)</p>
<pre><code>  model = slicer.util.getNode(inputModel.GetID())
  mesh =  model.GetMesh()
  mesh.GetPointData().SetActiveVectors("Displacements")
  warpvector = vtk.vtkWarpVector()
  warpvector.SetInputData(mesh)
  warpvector.SetInputArrayToProcess(0,0,0,"vtkDataObject::FIELD_ASSOCIATION_POINTS", "Displacements")

  warpvector.SetScaleFactor(1.0)
  warpvector.Update()
  output = warpvector.GetUnstructuredGridOutput()
  
  mesh2 = vtk.vtkUnstructuredGrid()
  mesh2.SetPoints(output.GetPoints())
  mesh2.SetCells(output.GetCellTypesArray(),output.GetCellLocationsArray(), output.GetCells())
  mesh2.UpdateCellGhostArrayCache()
  mesh2.UpdatePointGhostArrayCache()
  modelNode.SetAndObserveMesh(mesh2)   
</code></pre>
<p>Regards,<br>
Saima sAfdar</p>

---

## Post #10 by @lassoan (2021-01-29 05:55 UTC)

<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="6180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p><code>warpvector.SetInputArrayToProcess(0,0,0,"vtkDataObject::FIELD_ASSOCIATION_POINTS", "Displacements")</code></p>
</blockquote>
</aside>
<p>This syntax does not look familiar. Normally we use something like this:</p>
<pre><code>threshold.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "Distance")
</code></pre>
<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="6180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p><code>  output = warpvector.GetUnstructuredGridOutput()</code></p>
</blockquote>
</aside>
<p>We usually simply use <code>output = warpvector.GetOutput()</code>.</p>

---

## Post #11 by @Saima (2021-01-29 05:59 UTC)

<p>Hi Andras.<br>
I am getting the output mesh but with no scalar factor. THe code I pasted is without errors but I dont get desired output.</p>
<p>I do not understand threshold line …</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #12 by @lassoan (2021-01-29 06:02 UTC)

<aside class="quote no-group" data-username="Saima" data-post="11" data-topic="6180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I am getting the output mesh but with no scalar factor.</p>
</blockquote>
</aside>
<p>I don’t understand what you mean by this.</p>
<p>You can check our VTK examples website for complete examples of using the warp filter. One you get an example working, modify it step by step so that it does exactly what you need.</p>

---

## Post #13 by @Saima (2022-02-01 05:16 UTC)

<p>Dear Andras,<br>
I am trying to visualise the electric potential within 3D slicer. In paraview, I can use select potentail from a drop down window and then apply rescale to visible data range and it shoes me a coloured vtk mesh. Mesh is a hexahedral mesh.</p>
<p>How can I do something like below in paraview in 3D slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9100f22de705ce47c06d5e472f1d18f46a318ef.jpeg" data-download-href="/uploads/short-url/xfLEK1bRfeZtakliWIV2rT0X6ML.jpeg?dl=1" title="eeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9100f22de705ce47c06d5e472f1d18f46a318ef_2_475x500.jpeg" alt="eeg" data-base62-sha1="xfLEK1bRfeZtakliWIV2rT0X6ML" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9100f22de705ce47c06d5e472f1d18f46a318ef_2_475x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9100f22de705ce47c06d5e472f1d18f46a318ef.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9100f22de705ce47c06d5e472f1d18f46a318ef.jpeg 2x" data-dominant-color="865C61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">eeg</span><span class="informations">603×634 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @lassoan (2022-02-01 05:35 UTC)

<p>In Slicer you can configure how a scalar array colors a model in Models module / Display / Scalars section.</p>

---

## Post #15 by @Saima (2022-02-04 06:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="6180">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ow a scalar array colors a mod</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I can see all variable in active scalar under scalar section, but when i select variable it does not show it on the model.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/433700bd28dfa8b5f0755038e8056a34f77ec84a.jpeg" alt="pic" data-base62-sha1="9ABPGAF7zZzQ0iVxiQXbOeUfhA6" width="548" height="204"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ef05e3d4fcc3dd5ef78236db5c01a947bc77f1e.jpeg" alt="pic2" data-base62-sha1="6HeWTGfQkm0x1M6qvNNtRESW9f8" width="384" height="371"></p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #16 by @lassoan (2022-02-08 20:03 UTC)

<p>You have set a very large display range for <code>potential</code>, therefore all your valid values have very similar color. Reduce the displayed range manually or switch to <code>Scalar range mode</code> → <code>Data scalar range (auto)</code>.</p>

---
