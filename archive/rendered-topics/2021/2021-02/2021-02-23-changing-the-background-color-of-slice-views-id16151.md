# Changing the background color of slice views

**Topic ID**: 16151
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/changing-the-background-color-of-slice-views/16151

---

## Post #1 by @giovform (2021-02-23 02:18 UTC)

<p>I am not being able to change de slice views background colors. I am doing this:</p>
<pre><code>viewNode = slicer.app.layoutManager().sliceWidget('Red').mrmlSliceNode()
viewNode.SetBackgroundColor(1,1,1)
viewNode.SetBackgroundColor2(1,1,1)
</code></pre>
<p>But it has no effect. What should I do? I want to change to white. Thank you!</p>

---

## Post #2 by @jumbojing (2022-02-19 08:02 UTC)

<p>Try:<br>
<code>view = slicer.app.layoutManager().sliceWidget('Red').sliceView() view.setBackgroundColor(qt.QColor.fromRgbF(1,1,1))</code></p>
<ul>
<li>From <a href="https://github.com/Slicer/Slicer/blob/ed0fdbe71c5e98ef384a93d17850403aca8e685f/Docs/developer_guide/script_repository/screencapture.md#capture-3d-view-into-png-file-with-transparent-background" rel="noopener nofollow ugc">Slicer/screencapture.md at ed0fdbe71c5e98ef384a93d17850403aca8e685f · Slicer/Slicer (github.com)</a>
</li>
</ul>

---

## Post #3 by @Dwij_Mistry (2022-02-19 10:05 UTC)

<p><a class="mention" href="/u/jumbojing">@jumbojing</a> you forgot to add view.forceRender() to apply the modifications</p>
<p>For all slice view we can write like</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
  view = layoutManager.sliceWidget(sliceViewName).sliceView()
  view.setBackgroundColor(qt.QColor.fromRgbF(1,1,1))
  view.forceRender()
</code></pre>

---

## Post #4 by @jumbojing (2022-02-19 10:11 UTC)

<p><a class="mention" href="/u/dwij_mistry">@Dwij_Mistry</a>  Perfect! Thanks <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>但是, 如果每个slice有个边框就更好了</p>
<blockquote>
<p>However, it would be better if each slice had a balck border.</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fec429061630487d60912864a4237207bf21466.png" data-download-href="/uploads/short-url/dGzxKPEPYZvhwbHskJZPumqfZNI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fec429061630487d60912864a4237207bf21466_2_690x369.png" alt="image" data-base62-sha1="dGzxKPEPYZvhwbHskJZPumqfZNI" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fec429061630487d60912864a4237207bf21466_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fec429061630487d60912864a4237207bf21466_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fec429061630487d60912864a4237207bf21466_2_1380x738.png 2x" data-dominant-color="EBF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×1024 84.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Dwij_Mistry (2022-02-19 12:53 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="16151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>However, it would be better if each slice had a balck border.</p>
</blockquote>
</aside>
<p>If you are ok to use dark mode of slicer then we can get border which is nothing but a background color of central widget of MainWindow</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d719d534d14f8c7b0ae3fae13560ed92d233669c.png" data-download-href="/uploads/short-url/uGS0aycnoZJ2iwFNuG4Q752lS8Y.png?dl=1" title="Screenshot (110)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d719d534d14f8c7b0ae3fae13560ed92d233669c_2_690x381.png" alt="Screenshot (110)" data-base62-sha1="uGS0aycnoZJ2iwFNuG4Q752lS8Y" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d719d534d14f8c7b0ae3fae13560ed92d233669c_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d719d534d14f8c7b0ae3fae13560ed92d233669c_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d719d534d14f8c7b0ae3fae13560ed92d233669c_2_1380x762.png 2x" data-dominant-color="EEEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (110)</span><span class="informations">1441×797 13.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Dark mode can be activated from Menu → Edit → application settings → appearance → style → dark slicer</strong></p>

---

## Post #6 by @jumbojing (2022-02-19 12:57 UTC)

<p>Great! Thanks <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e9da3762dc3bbcb25615b60c861915d3145112c.png" data-download-href="/uploads/short-url/dv0CvSSg2vjQcpJ0RtOXYJJISRK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e9da3762dc3bbcb25615b60c861915d3145112c_2_690x289.png" alt="image" data-base62-sha1="dv0CvSSg2vjQcpJ0RtOXYJJISRK" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e9da3762dc3bbcb25615b60c861915d3145112c_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e9da3762dc3bbcb25615b60c861915d3145112c_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e9da3762dc3bbcb25615b60c861915d3145112c_2_1380x578.png 2x" data-dominant-color="F6F1EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1976×828 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Dwij_Mistry (2022-02-25 16:45 UTC)

<p><a class="mention" href="/u/jumbojing">@jumbojing</a></p>
<p>Finally I found a way by which we can have border without changing the slicer color mode.</p>
<pre><code class="lang-auto">
def paint_border(view):
  color = [0.0, 0.0, 0.0] #change color for border 
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



#calling 
paint_border(slicer.app.layoutManager().threeDWidget(0).threeDView())
for sliceViewName in slicer.app.layoutManager().sliceViewNames():
    paint_border(slicer.app.layoutManager().sliceWidget(sliceViewName).sliceView())
</code></pre>
<p>OutPut<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76fa84c76af6f5279f03bcdf2bf93320d4cc0d65.png" data-download-href="/uploads/short-url/gYx4FoaAouUCuO3iN5cv3Ywwk1n.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fa84c76af6f5279f03bcdf2bf93320d4cc0d65_2_690x437.png" alt="Capture" data-base62-sha1="gYx4FoaAouUCuO3iN5cv3Ywwk1n" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fa84c76af6f5279f03bcdf2bf93320d4cc0d65_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fa84c76af6f5279f03bcdf2bf93320d4cc0d65_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fa84c76af6f5279f03bcdf2bf93320d4cc0d65_2_1380x874.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1452×920 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @jumbojing (2022-03-01 13:13 UTC)

<aside class="quote no-group" data-username="Dwij_Mistry" data-post="7" data-topic="16151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dwij_mistry/48/15265_2.png" class="avatar"> Dwij_Mistry:</div>
<blockquote>
<pre><code class="lang-auto">def paint_border(view):
  color = [0.0, 0.0, 0.0] #change color for border 
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



#calling 
paint_border(slicer.app.layoutManager().threeDWidget(0).threeDView())
for sliceViewName in slicer.app.layoutManager().sliceViewNames():
    paint_border(slicer.app.layoutManager().sliceWidget(sliceViewName).sliceView())
</code></pre>
<p>OutPut</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/636a1933151b40f654a11c4db87a9b0db079fe60.png" data-download-href="/uploads/short-url/ebsAewK8F09RsA57gRTCRGX9lHW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/636a1933151b40f654a11c4db87a9b0db079fe60_2_580x500.png" alt="image" data-base62-sha1="ebsAewK8F09RsA57gRTCRGX9lHW" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/636a1933151b40f654a11c4db87a9b0db079fe60_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/636a1933151b40f654a11c4db87a9b0db079fe60_2_870x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/636a1933151b40f654a11c4db87a9b0db079fe60_2_1160x1000.png 2x" data-dominant-color="C9C9DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1838×1582 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/dwij_mistry">@Dwij_Mistry</a> what’s wrong? a black line</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d29aeab760acb98de11a2209a0fd18661c62c16.png" data-download-href="/uploads/short-url/hReZePKkK7L7adhXiA6QU0tJ1Ma.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d29aeab760acb98de11a2209a0fd18661c62c16_2_578x500.png" alt="image" data-base62-sha1="hReZePKkK7L7adhXiA6QU0tJ1Ma" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d29aeab760acb98de11a2209a0fd18661c62c16_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d29aeab760acb98de11a2209a0fd18661c62c16_2_867x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d29aeab760acb98de11a2209a0fd18661c62c16_2_1156x1000.png 2x" data-dominant-color="DDDDE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1882×1628 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Dwij_Mistry (2022-05-12 11:05 UTC)

<p>I am also facing the same issue, Can any one please share why it is happening? or any alternative solution?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #10 by @lassoan (2022-05-12 12:54 UTC)

<p>I cannot reproduce this, so I cannot tell what’s wrong, but maybe you need to tweak the <code>1e-4</code> and <code>0.9999</code> constants.</p>

---
