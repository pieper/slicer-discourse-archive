# Markups line projection on a model

**Topic ID**: 28205
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/markups-line-projection-on-a-model/28205

---

## Post #1 by @soukup.la (2023-03-07 07:56 UTC)

<p>Hello,<br>
I have markups line which passes through the surface of the model. I’d like to shift endpoint to the model surface using python. Could you help me please?</p>
<p>Ladislav</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d0e4807430b988531452af0180cbd31b47a30d0.png" data-download-href="/uploads/short-url/aZFmuYZrTuVe069GNncERW7qFva.png?dl=1" title="point_on_surface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d0e4807430b988531452af0180cbd31b47a30d0_2_687x500.png" alt="point_on_surface" data-base62-sha1="aZFmuYZrTuVe069GNncERW7qFva" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d0e4807430b988531452af0180cbd31b47a30d0_2_687x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d0e4807430b988531452af0180cbd31b47a30d0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d0e4807430b988531452af0180cbd31b47a30d0.png 2x" data-dominant-color="35073F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">point_on_surface</span><span class="informations">891×648 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @soukup.la (2023-03-09 10:43 UTC)

<p>This works fine:</p>
<pre><code>obbTree = vtk.vtkOBBTree()
obbTree.SetDataSet(modelNode.GetPolyData())
obbTree.BuildLocator()
pointsVTKintersection = vtk.vtkPoints()
code = obbTree.IntersectWithLine(startPoin, endPoint, pointsVTKintersection, None)
pointsVTKIntersectionData = pointsVTKintersection.GetData()
pointsIntersection = pointsVTKIntersectionData.GetTuple3(0)
</code></pre>

---
