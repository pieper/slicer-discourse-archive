---
topic_id: 17518
title: "How To Display A Line With Projection In 2Dslicer By Python"
date: 2021-05-08
url: https://discourse.slicer.org/t/17518
---

# How to display a line with projection in 2Dslicer by python?

**Topic ID**: 17518
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/how-to-display-a-line-with-projection-in-2dslicer-by-python/17518

---

## Post #1 by @jumbojing (2021-05-08 11:22 UTC)

<pre><code class="lang-auto">def p2pline(P0, P1, width=1,modelName="Line",color = "blue"):
    points = vtk.vtkPoints()
    points.SetNumberOfPoints(2)
    points.SetPoint(0,   P0[0], P0[1], P0[2])
    points.SetPoint(1,   P1[0], P1[1], P1[2])
    line = vtk.vtkLineSource()
    line.SetPoints(points)
    lineNode = slicer.modules.models.logic().AddModel(line.GetOutputPort())
    lineNode.SetName(modelName)
    modelDisplay = lineNode.GetDisplayNode()
    modelDisplay.SetColor(myColor(color)) # yellow
    modelDisplay.SetLineWidth(width)
    modelDisplay.SetOpacity(1)
    modelDisplay.SetVisibility2D(1)
</code></pre>
<p>以上的代码想用2点画一条直线,可不知道为啥在2D视图里看不到,我发现用projection可以看到,我该怎么实现呢?</p>
<p>The above code wants to draw a straight line with 2 points, but I don’t know why I can’t see it in 2D view, but I found that I can see it with projection, how can I achieve it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8087794ae2d35ada211ec083c48cdbe8201bea1.jpeg" data-download-href="/uploads/short-url/sxzDm9jjrrNBZCu0gsQKKkukv7P.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8087794ae2d35ada211ec083c48cdbe8201bea1_2_690x278.jpeg" alt="image" data-base62-sha1="sxzDm9jjrrNBZCu0gsQKKkukv7P" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8087794ae2d35ada211ec083c48cdbe8201bea1_2_690x278.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8087794ae2d35ada211ec083c48cdbe8201bea1_2_1035x417.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8087794ae2d35ada211ec083c48cdbe8201bea1_2_1380x556.jpeg 2x" data-dominant-color="B6B7B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1642×662 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a673aba214546279024829829c96488d5466bc8.jpeg" data-download-href="/uploads/short-url/fbhMlIlEtsuJwT6rPkcTEM5tYwM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a673aba214546279024829829c96488d5466bc8_2_690x286.jpeg" alt="image" data-base62-sha1="fbhMlIlEtsuJwT6rPkcTEM5tYwM" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a673aba214546279024829829c96488d5466bc8_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a673aba214546279024829829c96488d5466bc8_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a673aba214546279024829829c96488d5466bc8_2_1380x572.jpeg 2x" data-dominant-color="B6B7B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1630×676 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-05-10 04:55 UTC)

<p>You can set slice display mode to projection by this call:</p>
<pre><code class="lang-python">modelDisplay.SetSliceDisplayModeToProjection()
</code></pre>
<p>See documentation of the display node <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html">here</a>.</p>
<p>To display pedicle screw trajectory with label, interactively editable line endpoints, and many other display options, etc. you can use markups line instead of model.</p>
<p>You may also find the <a href="https://github.com/lassoan/PedicleScrewSimulator">Pedicle Screw Simulator extension</a> interesting:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="XN3Tp8jaYdQ" data-video-title="3D Slicer - Pedicle Screw Surgical Simulator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=XN3Tp8jaYdQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/XN3Tp8jaYdQ/maxresdefault.jpg" title="3D Slicer - Pedicle Screw Surgical Simulator" width="" height="">
  </a>
</div>


---

## Post #3 by @jumbojing (2021-05-10 14:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf57de67e4a0775ac79ad94cf6d1272637a8f9b6.jpeg" data-download-href="/uploads/short-url/riHscnut7aBOT7DBwzNIXZxkYtM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf57de67e4a0775ac79ad94cf6d1272637a8f9b6_2_543x500.jpeg" alt="image" data-base62-sha1="riHscnut7aBOT7DBwzNIXZxkYtM" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf57de67e4a0775ac79ad94cf6d1272637a8f9b6_2_543x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf57de67e4a0775ac79ad94cf6d1272637a8f9b6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf57de67e4a0775ac79ad94cf6d1272637a8f9b6.jpeg 2x" data-dominant-color="B5B1B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×640 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
谢谢老师!你太好了!!</p>

---
