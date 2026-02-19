---
topic_id: 19221
title: "How To Add A Border To 3D Widget"
date: 2021-08-17
url: https://discourse.slicer.org/t/19221
---

# How to add a border to 3d widget

**Topic ID**: 19221
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/how-to-add-a-border-to-3d-widget/19221

---

## Post #1 by @wycstar (2021-08-17 07:01 UTC)

<p>I want to add a border to 3d widget, but run the code below, nothing happened</p>
<pre><code class="lang-auto">slicer.app.layoutManager().threeDWidget(0).threeDView().setStyleSheet("border-bottom: 2px solid rgb(255, 0, 0)")
</code></pre>
<p>where am i wrong</p>

---

## Post #2 by @wycstar (2021-08-18 03:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> save me plz <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=10" title=":rofl:" class="emoji" alt=":rofl:"></p>

---

## Post #3 by @lassoan (2021-08-18 14:58 UTC)

<p>The VTK render window is painted by VTK, so style sheet will have no effect. You can draw the frame by using VTK by adding a 2D actor:</p>
<pre data-code-wrap="python"><code class="lang-python">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
color = [0.0, 1.0, 1.0]
lineThickness = 10.0

viewRenderer = view.renderWindow().GetRenderers().GetItemAsObject(0)

borderPoints = vtk.vtkPoints()
borderPoints.InsertNextPoint(  1e-4,   1e-4, 0)
borderPoints.InsertNextPoint(0.9999,   1e-4, 0)
borderPoints.InsertNextPoint(0.9999, 0.9999, 0)
borderPoints.InsertNextPoint(  1e-4, 0.9999, 0)

borderCells = vtk.vtkCellArray()
borderCells.InsertNextCell(5)
for i in range(5):
    borderCells.InsertCellPoint(i%5)

borderPolyData = vtk.vtkPolyData()
borderPolyData.SetPoints(borderPoints)
borderPolyData.SetLines(borderCells)

borderCoordinate = vtk.vtkCoordinate()
borderCoordinate.SetCoordinateSystemToNormalizedViewport()
borderCoordinate.SetViewport(viewRenderer)

borderPolyDataMapper = vtk.vtkPolyDataMapper2D()
borderPolyDataMapper.SetInputData(borderPolyData)
borderPolyDataMapper.SetTransformCoordinate(borderCoordinate)
borderPolyDataMapper.SetTransformCoordinateUseDouble(True)

highlightedBorderActor = vtk.vtkActor2D()
highlightedBorderActor.SetMapper(borderPolyDataMapper)
highlightedBorderActor.GetProperty().SetColor(color[0], color[1], color[2])
highlightedBorderActor.GetProperty().SetDisplayLocationToForeground()
highlightedBorderActor.GetProperty().SetLineWidth(lineThickness)
viewRenderer.AddActor2D(highlightedBorderActor)
view.renderWindow().Render()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292416681d0b0eeb772023fecb3cf32d7a8ad620.png" data-download-href="/uploads/short-url/5RWTorIPXcFxqph30h7EmjRh6pi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292416681d0b0eeb772023fecb3cf32d7a8ad620_2_550x500.png" alt="image" data-base62-sha1="5RWTorIPXcFxqph30h7EmjRh6pi" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/292416681d0b0eeb772023fecb3cf32d7a8ad620_2_550x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292416681d0b0eeb772023fecb3cf32d7a8ad620.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/292416681d0b0eeb772023fecb3cf32d7a8ad620.png 2x" data-dominant-color="41434B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">803×730 19.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @wycstar (2021-08-19 02:41 UTC)

<p>thanks <a class="mention" href="/u/lassoan">@lassoan</a>  it works!</p>

---

## Post #5 by @apparrilla (2022-01-04 23:33 UTC)

<p>What about to disable it?<br>
I´ve tried to repeat the process with lineThickness=0 but it doesn´t work for me. Is there any way to get this vtkActor2D to remove it?</p>
<p>Thanks on advance!</p>

---

## Post #6 by @apparrilla (2022-01-05 00:57 UTC)

<p>I answer to myself FYI:</p>
<pre><code class="lang-auto">for actor2D in viewRenderer.GetActors2D():
        viewRenderer.RemoveActor2D(actor2D)
</code></pre>

---
