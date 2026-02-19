---
topic_id: 7600
title: "Define Pyramid With Cross Section Of Polygon"
date: 2019-07-16
url: https://discourse.slicer.org/t/7600
---

# Define pyramid with cross-section of polygon

**Topic ID**: 7600
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/define-pyramid-with-cross-section-of-polygon/7600

---

## Post #1 by @shahrokh (2019-07-16 02:16 UTC)

<p>Hi Dear 3DSlicer developers</p>
<p>I want to define one pyramid with cross-section of polygon (for example polygon with 160  vertices) using VTK.<br>
I think that I must use vtkFrustumSource. Is it ok?<br>
How can I do it?<br>
Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2019-07-16 11:58 UTC)

<p>Yes, any vtkPolyData from vtk (either a source or the result of a pipeline) should be usable with a vtkMRMLModelNode.</p>
<p><a href="https://lorensen.github.io/VTKExamples/site/Python/#geometric-objects" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Python/#geometric-objects</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node</a></p>

---

## Post #3 by @lassoan (2019-07-16 12:12 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="7600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>pyramid with cross-section of polygon (for example polygon with 160 vertices)</p>
</blockquote>
</aside>
<p><code>vtkFrustumSource</code> can only create rectangular pyramid. If you need to extrude arbitrary polygons then you may use <a href="https://vtk.org/doc/nightly/html/classvtkLinearExtrusionFilter.html"><code>vtkLinearExtrusionFilter</code></a>.</p>

---

## Post #4 by @shahrokh (2019-07-22 03:57 UTC)

<p>Thanks a lot for your guidance.</p>
<p>To implement a polygon in Python interactor,  I wrote the code to run in 3DSlicer.<br>
In short, I mention to the geometry considered with me and it is shown in the following figures (IDs and spatial coordinates).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01dbf0a6c56b9e84a25ec7f83fab76506a2e3185.png" data-download-href="/uploads/short-url/grHcFcOA5H12c9lAW37FLNjyM5.png?dl=1" title="Picture16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01dbf0a6c56b9e84a25ec7f83fab76506a2e3185_2_618x500.png" alt="Picture16" data-base62-sha1="grHcFcOA5H12c9lAW37FLNjyM5" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01dbf0a6c56b9e84a25ec7f83fab76506a2e3185_2_618x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01dbf0a6c56b9e84a25ec7f83fab76506a2e3185_2_927x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01dbf0a6c56b9e84a25ec7f83fab76506a2e3185.png 2x" data-dominant-color="36506E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture16</span><span class="informations">1202×971 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d78c195be779bea028f5c7fdf29c54aec9aa0c.png" data-download-href="/uploads/short-url/hf16t3q7NqcHa4t8eDAbRVOVtvu.png?dl=1" title="Picture17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d78c195be779bea028f5c7fdf29c54aec9aa0c.png" alt="Picture17" data-base62-sha1="hf16t3q7NqcHa4t8eDAbRVOVtvu" width="645" height="500" data-dominant-color="25374C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture17</span><span class="informations">1254×971 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you see, I have 23 points in RAS coordinate system (RS plane). After doing it, I want to create a polygon model and access to it in Data module. The following figure is shown these points and the polygon.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/764a6441cb3cdb91f0622d4cec191e1eee4d8011.png" data-download-href="/uploads/short-url/gSrIWimrrDSC3hm4sB1XBYanWBb.png?dl=1" title="Picture18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764a6441cb3cdb91f0622d4cec191e1eee4d8011_2_580x500.png" alt="Picture18" data-base62-sha1="gSrIWimrrDSC3hm4sB1XBYanWBb" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764a6441cb3cdb91f0622d4cec191e1eee4d8011_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764a6441cb3cdb91f0622d4cec191e1eee4d8011_2_870x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/764a6441cb3cdb91f0622d4cec191e1eee4d8011.png 2x" data-dominant-color="B6C8E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture18</span><span class="informations">1127×971 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The following lines are the code I wrote.</p>
<blockquote>
<p>import vtk<br>
polygonPoints = vtk.vtkPoints()<br>
polygonPoints.SetNumberOfPoints(23)<br>
polygonPoints.InsertPoint(0,4,0,0)<br>
polygonPoints.InsertPoint(1,1,0,1)<br>
polygonPoints.InsertPoint(2,2,0,1.5)<br>
polygonPoints.InsertPoint(3,3,0,2.5)<br>
polygonPoints.InsertPoint(4,2,0,3.5)<br>
polygonPoints.InsertPoint(5,1,0,4.5)<br>
polygonPoints.InsertPoint(6,-1,0,5)<br>
polygonPoints.InsertPoint(7,-2,0,4)<br>
polygonPoints.InsertPoint(8,-3,0,3.5)<br>
polygonPoints.InsertPoint(9,-4,0,3)<br>
polygonPoints.InsertPoint(10,-4.5,0,2)<br>
polygonPoints.InsertPoint(11,-5,0,1)<br>
polygonPoints.InsertPoint(12,-5,0,0)<br>
polygonPoints.InsertPoint(13,-4.5,0,-1)<br>
polygonPoints.InsertPoint(14,-3,0,-2)<br>
polygonPoints.InsertPoint(15,-2,0,-2.5)<br>
polygonPoints.InsertPoint(16,-1,0,-3)<br>
polygonPoints.InsertPoint(17,0,0,-5)<br>
polygonPoints.InsertPoint(18,1,0,-5)<br>
polygonPoints.InsertPoint(19,2,0,-4.5)<br>
polygonPoints.InsertPoint(20,3,0,-3)<br>
polygonPoints.InsertPoint(21,3,0,-2)<br>
polygonPoints.InsertPoint(22,3,0,-1)<br>
polygonPolyData = vtk.vtkPolyData()<br>
polygonPolyData.SetPoints(polygonPoints)<br>
model = slicer.vtkMRMLModelNode()<br>
model.SetAndObservePolyData(polygonPolyData)<br>
modelDisplay = slicer.vtkMRMLModelDisplayNode()<br>
modelDisplay.SetColor(1, 1, 0)<br>
modelDisplay.BackfaceCullingOff()<br>
modelDisplay.SetOpacity(0.5)<br>
modelDisplay.SetPointSize(3)<br>
modelDisplay.SetSliceIntersectionVisibility(True)<br>
modelDisplay.SetVisibility(True)<br>
slicer.mrmlScene.AddNode(modelDisplay)<br>
model.SetAndObserveDisplayNodeID(modelDisplay.GetID())<br>
modelDisplay.SetInputPolyDataConnection(model.GetPolyDataConnection())<br>
slicer.mrmlScene.AddNode(model)</p>
</blockquote>
<p>When I enter this code in Python interactor of 3DSlicer, I see that a new node is created in Data module as is shown in the following figure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9942f0cfcec52f8041d7d2008e005c69cc5ad46.png" data-download-href="/uploads/short-url/ocaaPZwjz57Zy3LZ5Te92c5DfD0.png?dl=1" title="Screenshot%20from%202019-07-22%2008-20-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9942f0cfcec52f8041d7d2008e005c69cc5ad46_2_360x500.png" alt="Screenshot%20from%202019-07-22%2008-20-20" data-base62-sha1="ocaaPZwjz57Zy3LZ5Te92c5DfD0" width="360" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9942f0cfcec52f8041d7d2008e005c69cc5ad46_2_360x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9942f0cfcec52f8041d7d2008e005c69cc5ad46.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9942f0cfcec52f8041d7d2008e005c69cc5ad46.png 2x" data-dominant-color="F5F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-07-22%2008-20-20</span><span class="informations">535×742 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unfortunately, I do not see this model (polygon with 23 sides) in <strong>3D window</strong> and I can not change it (for example rotation and translation).<br>
Why?<br>
What’s wrong with me?<br>
Please guide me.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #5 by @lassoan (2019-07-22 04:32 UTC)

<p>You added points, but you’ve forgot to add a polygon cell. You need to do something like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/9d730b3ef2987b69d12689a084c5a0b420a6dacf/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L1419-L1428" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/9d730b3ef2987b69d12689a084c5a0b420a6dacf/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L1419-L1428" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/9d730b3ef2987b69d12689a084c5a0b420a6dacf/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.cxx#L1419-L1428</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1419" style="counter-reset: li-counter 1418 ;">
<li>vtkNew&lt;vtkPolyData&gt; inputSurface;</li>
<li>inputSurface-&gt;SetPoints(curvePoints);</li>
<li>vtkNew&lt;vtkCellArray&gt; polys;</li>
<li>polys-&gt;InsertNextCell(numberOfCurvePoints);</li>
<li>for (int i = 0; i &lt; numberOfCurvePoints; i++)</li>
<li>  {</li>
<li>  polys-&gt;InsertCellPoint(i);</li>
<li>  }</li>
<li>polys-&gt;Modified();</li>
<li>inputSurface-&gt;SetPolys(polys);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can find many examples of how to create polydata manually on <a href="https://lorensen.github.io/VTKExamples/site/" rel="nofollow noopener">VTK examples site</a>.</p>

---

## Post #6 by @shahrokh (2019-07-23 06:28 UTC)

<p>Thanks a lot for your help.<br>
As mentioned you, I add the following lines</p>
<blockquote>
<p>…<br>
polygonPolyData = vtk.vtkPolyData()<br>
polygonPolyData.SetPoints(polygonPoints)</p>
<p><strong><span class="hashtag-raw">#Create</span> Cell</strong><br>
<strong>polygons = vtk.vtkCellArray()</strong><br>
<strong>polygons.InsertNextCell(23)</strong><br>
<strong>for i in range(0,22):</strong><br>
<strong>polygons.InsertCellPoint(i)</strong><br>
<strong>polygons.Modified()</strong><br>
<strong>polygonPolyData.SetPolys(polygons)</strong></p>
<p>model = slicer.vtkMRMLModelNode()<br>
model.SetAndObservePolyData(polygonPolyData)<br>
…</p>
</blockquote>
<p>At now, I can see my polygon model in <em>Wireframe Representation</em> as following figure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b93b4356b00771e51f4fee0f1b4d17f83fc45158.png" data-download-href="/uploads/short-url/qqDiKRx4oo5Ap6GXOnTu48sFUco.png?dl=1" title="ScreenshotWireFrame" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b93b4356b00771e51f4fee0f1b4d17f83fc45158.png" alt="ScreenshotWireFrame" data-base62-sha1="qqDiKRx4oo5Ap6GXOnTu48sFUco" width="585" height="500" data-dominant-color="9C9FD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotWireFrame</span><span class="informations">852×727 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is ok.</p>
<p>Unfortunately, this varies slightly when I see it in <em>Surface</em> with <em>WireFrame</em> representations as following figures:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c3169b6489bf76a658534be7fcbac0f0a09ba30.png" data-download-href="/uploads/short-url/hIF4wRLJYm5rGNHi0BpcSWnr0CA.png?dl=1" title="ScreenshotSurface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c3169b6489bf76a658534be7fcbac0f0a09ba30_2_585x500.png" alt="ScreenshotSurface" data-base62-sha1="hIF4wRLJYm5rGNHi0BpcSWnr0CA" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c3169b6489bf76a658534be7fcbac0f0a09ba30_2_585x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c3169b6489bf76a658534be7fcbac0f0a09ba30.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c3169b6489bf76a658534be7fcbac0f0a09ba30.png 2x" data-dominant-color="C1C382"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotSurface</span><span class="informations">852×727 9.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68a89f39a7a8f3f2945e89394159aaf2f4215cae.png" data-download-href="/uploads/short-url/eVQVwBX7aAjaXgY60JHlJC0OFLU.png?dl=1" title="ScreenshotSurfaceWithEdges" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68a89f39a7a8f3f2945e89394159aaf2f4215cae_2_585x500.png" alt="ScreenshotSurfaceWithEdges" data-base62-sha1="eVQVwBX7aAjaXgY60JHlJC0OFLU" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/68a89f39a7a8f3f2945e89394159aaf2f4215cae_2_585x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68a89f39a7a8f3f2945e89394159aaf2f4215cae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68a89f39a7a8f3f2945e89394159aaf2f4215cae.png 2x" data-dominant-color="C0C281"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotSurfaceWithEdges</span><span class="informations">852×727 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As see you, Why do not they match (edges (black color wireframe) with the edges of polygon surface (yellow surface))?</p>
<p>Is this a visual error or I made a mistake again?<br>
Thanks a lot for your support.<br>
Shahrokh.</p>

---

## Post #7 by @lassoan (2019-07-23 12:32 UTC)

<p>OpenGL can only render <em>convex</em> filled polygons. If you need to display non-convex polygon then you can triangulate it using vtkTriangleFilter.</p>

---
