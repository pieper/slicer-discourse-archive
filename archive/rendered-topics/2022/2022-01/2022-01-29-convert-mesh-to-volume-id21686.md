# Convert mesh to volume

**Topic ID**: 21686
**Date**: 2022-01-29
**URL**: https://discourse.slicer.org/t/convert-mesh-to-volume/21686

---

## Post #1 by @Artur_V (2022-01-29 00:54 UTC)

<p>Thank you for this information, but i ran into some problems with the code and the model is not displayed.<br>
I’m trying to convert a .VTK file from an atlas (unstructured grid) into a mesh or volume to create a .nrrd or nifti file for a medical project.<br>
Here is a link to the VTK - <a href="https://drive.google.com/file/d/107T-ZeqlZIl22GMbxN_bKGPGcKWfI_4M/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">M1_cf_face.1k.vtk - Google Drive</a></p>
<p>These are the errors im running into:</p>
<pre><code class="lang-auto">'[success, modelNode] = slicer.util.loadModel(sampleModelFile, returnNode=True)'
Error: loadNodeFromFile `returnNode` argument is deprecated. Loaded node is now returned directly if `returnNode` is not specified.

'modelNode.GetBounds(bounds)'
Error: Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'GetBounds'

'transformer.SetInputConnection(modelNode.GetMeshConnection())'
Error: Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'GetMeshConnection'

'modelNode.GetDisplayNode().BackfaceCullingOff()'
Error: Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'GetDisplayNode'

'display()'
Error: Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'display' is not defined
</code></pre>

---

## Post #2 by @lassoan (2022-01-29 02:50 UTC)

<p>The file that you linked above is not an unstructured grid but a polydata containing 1000 line cells.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fef30819e532af6bd36cc3a4b66907182b403cb9.png" data-download-href="/uploads/short-url/AnnYabFj4g3eqPCRuiZdW0ddiVX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef30819e532af6bd36cc3a4b66907182b403cb9_2_584x500.png" alt="image" data-base62-sha1="AnnYabFj4g3eqPCRuiZdW0ddiVX" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef30819e532af6bd36cc3a4b66907182b403cb9_2_584x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef30819e532af6bd36cc3a4b66907182b403cb9_2_876x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef30819e532af6bd36cc3a4b66907182b403cb9_2_1168x1000.png 2x" data-dominant-color="A4A6C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1394×1192 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since lines are one-dimensional objects (have zero volume), before you can convert this to a labelmap, you need to give it some thickness. You can use vtkTubeFilter or vtkImplicitModeller+vtkContourFilter or Delaunay triangulation for this.</p>
<p>For example:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode('M1*')
outputModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
outputModelNode.CreateDefaultDisplayNodes()

decimate = vtk.vtkDecimatePolylineFilter()
decimate.SetInputData(modelNode.GetPolyData())
decimate.SetTargetReduction(0.9)

delaunay = vtk.vtkDelaunay3D()
delaunay.SetInputConnection(decimate.GetOutputPort())
delaunay.SetAlpha(5.0)
delaunay.BoundingTriangulationOn()
delaunay.AlphaTetsOn()
delaunay.AlphaLinesOff()
delaunay.AlphaTrisOff()

geometry = vtk.vtkDataSetSurfaceFilter()
geometry.SetInputConnection(delaunay.GetOutputPort())

normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(geometry.GetOutputPort())
outputModelNode.SetPolyDataConnection(normals.GetOutputPort())
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6ceabc50d7f4ed5cbe6973743793f09a4af54aa.png" data-download-href="/uploads/short-url/q5bGMUNL8mukLROXVfhZqHPeWL0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6ceabc50d7f4ed5cbe6973743793f09a4af54aa_2_656x500.png" alt="image" data-base62-sha1="q5bGMUNL8mukLROXVfhZqHPeWL0" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6ceabc50d7f4ed5cbe6973743793f09a4af54aa_2_656x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6ceabc50d7f4ed5cbe6973743793f09a4af54aa_2_984x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6ceabc50d7f4ed5cbe6973743793f09a4af54aa_2_1312x1000.png 2x" data-dominant-color="A09DC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1564×1192 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can then convert this model to a segmentation node and get a binary labelmap representation.</p>

---

## Post #3 by @Artur_V (2022-10-11 02:32 UTC)

<p>Thanks for the help!</p>

---

## Post #4 by @tuncerms (2023-08-09 10:24 UTC)

<p>Hi!</p>
<p>First of all, thanks a lot for the helpful comments regarding this issue. I found this topic recently as I actually have exactly the same issue with the same vtk files.</p>
<p>I tried out your code, but I get this error “NameError: name ‘normals’ is not defined” referring to the last command “outputModelNode.SetPolyDataConnection(normals.GetOutputPort())”. The Model is not displayed like in the second image you showed.</p>
<p>Since it worked for you, it has to be an issue with my setup. Is there a solution for this?</p>
<p>Thanks a lot in advance!</p>
<p>Best,<br>
Mehmet</p>

---

## Post #5 by @Sunderlandkyl (2023-08-09 14:39 UTC)

<p>You can change ‘normals’ to ‘geometry’.</p>
<pre><code class="lang-auto">outputModelNode.SetPolyDataConnection(geometry.GetOutputPort())
</code></pre>
<p>Or, you can add a normal filter, which would create a smoother looking surface:</p>
<pre><code class="lang-auto">modelNode = getNode('M1*')
outputModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
outputModelNode.CreateDefaultDisplayNodes()

decimate = vtk.vtkDecimatePolylineFilter()
decimate.SetInputData(modelNode.GetPolyData())
decimate.SetTargetReduction(0.9)

delaunay = vtk.vtkDelaunay3D()
delaunay.SetInputConnection(decimate.GetOutputPort())
delaunay.SetAlpha(5.0)
delaunay.BoundingTriangulationOn()
delaunay.AlphaTetsOn()
delaunay.AlphaLinesOff()
delaunay.AlphaTrisOff()

geometry = vtk.vtkDataSetSurfaceFilter()
geometry.SetInputConnection(delaunay.GetOutputPort())

normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(geometry.GetOutputPort())
outputModelNode.SetPolyDataConnection(normals.GetOutputPort())
</code></pre>

---

## Post #6 by @tuncerms (2023-08-09 15:16 UTC)

<p>works! Thanks a lot!</p>

---
