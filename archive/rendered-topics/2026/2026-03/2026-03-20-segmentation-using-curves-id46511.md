---
topic_id: 46511
title: "Segmentation using curves"
date: 2026-03-20
url: https://discourse.slicer.org/t/46511
last_bumped: 2026-03-29T14:29:42.528Z
---

# Segmentation using curves

**Topic ID**: 46511
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/segmentation-using-curves/46511

---

## Post #1 by @mrrezaie (2026-03-20 13:38 UTC)

<p>Hello all.</p>
<p>I’m trying to do MRI segmentation on a very thin and round structure (knee cartilage). I was wondering if there is any to create a surface on a set of polynomial curves like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg" data-download-href="/uploads/short-url/8WPH6ss2vK25KijBDHDCO7tywag.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c_2_643x500.jpeg" alt="image" data-base62-sha1="8WPH6ss2vK25KijBDHDCO7tywag" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg 2x" data-dominant-color="403F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×615 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking forward to hearing from you.</p>
<p>Mohammadreza</p>

---

## Post #2 by @chir.set (2026-03-20 14:00 UTC)

<p>If you use a <code>closed curve</code> instead of an <code>open curve</code>, the <code>Baffle planner</code> module in the <code>SlicerHeart</code> extension can create a model out of it (not a segmentation).</p>

---

## Post #3 by @mrrezaie (2026-03-20 14:21 UTC)

<p>Thanks a lot for your response. I just tried Baffle planner, it could be definitely helpful in my workflow. One thing about it, I need to create a surface from multiple curves (on every slice). It apparently works with one curve only, and the knee cartilage is a complex geometry:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7cd6530d9b3b632b7f213ff554d66e8fd85198.jpeg" data-download-href="/uploads/short-url/8ufDg9rO9DLblJupMTmLa4lHdJ6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7cd6530d9b3b632b7f213ff554d66e8fd85198.jpeg" alt="image" data-base62-sha1="8ufDg9rO9DLblJupMTmLa4lHdJ6" width="474" height="264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">474×264 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2026-03-20 14:27 UTC)

<p>Do you really need the curve representation?  You might only need that if you are exporting to a CAD tool, and that’s a hard problem to do right.</p>
<p>You may be better off making a segmentation (binary labelmap) and reconstructing a surface from that.  You should definitely supersample the segmentation so that the thinnest structures are several voxels thick.  Then you can look at the wrapsolidify extension to get a smooth contour.  Search for similar work people do with thin temporal bones.</p>

---

## Post #5 by @mrrezaie (2026-03-20 14:54 UTC)

<p>Thanks a lot, this is a very thin structure on non-isotropic MRI. I had tried Wrap Solidify, but it was not successful. That’s why I ended up with this idea.</p>

---

## Post #6 by @pieper (2026-03-20 14:57 UTC)

<p>What is your overall goal and plan?  How will you use the surface?  I ask because lofting splines is a non-trivial operation whereas working with segmentations is well studies and you can make it work without developing new tools.</p>

---

## Post #7 by @mrrezaie (2026-03-20 15:09 UTC)

<p>My application is kind of Finite Element Analysis (not exactly; cartilages contact force analyses during physical activities using musculoskeletal modeling: <a href="https://github.com/clnsmith/opensim-jam/blob/master/opensim-jam-release/examples/walking/graphics/walking_contact.gif" class="inline-onebox" rel="noopener nofollow ugc">opensim-jam/opensim-jam-release/examples/walking/graphics/walking_contact.gif at master · clnsmith/opensim-jam · GitHub</a>).</p>
<p>So I need the cartilage surfaces accurate, and smoothed. But what I have already doesn’t allow me to use the common workflows in any medical imaging segmentation software.</p>
<p>Thanks for your help.</p>

---

## Post #8 by @pieper (2026-03-20 15:18 UTC)

<p>Okay, cool, yes, that helps.  I would definitely supersample the segmentation heavily.  Like use the crop volume to get just the cartilage are and the supersample as much as your computer can manage (or get a bigger computer) and then you may be able to paint with threshold and use smoothing to get a faithful surface.  (As an aside, joining curves manually draw slice-by-slice will always lead to bumpy surfaces so some kind of smoothing is needed here).</p>

---

## Post #9 by @mrrezaie (2026-03-20 16:06 UTC)

<p>Thanks again. There were two main issues in this approach: first, thresholding doesn’t work well for these kinds of MRI as this is not the best type for cartilage segmentation; second, the cartilages in children are so thin and narrow, the Brush or Draw tools were a nightmare. Overall, this approach is so boring for 60 patients <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=15" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">. I’ve been thinking about doing sth like this: <a href="https://superhivemarket.com/products/curves-to-mesh" rel="noopener nofollow ugc">https://superhivemarket.com/products/curves-to-mesh</a></p>

---

## Post #10 by @pieper (2026-03-20 16:09 UTC)

<p>Yes, that’s a classic CAD approach.  There’s some support for doing things like that in Slicer extensions (surface markups) but I haven’t used them myself.  Maybe someone else can chime in.  If you are willing / able to do some coding I’m sure it’s doable with vtk or some python packages.</p>

---

## Post #11 by @JASON (2026-03-22 01:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="46511">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>surface markups</p>
</blockquote>
</aside>
<p>I recall seeing NURBS surfaces in SurfaceMarkup extension.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="0_2ieNX3Flo" data-video-title="NURBS surface editing in 3D Slicer" data-video-start-time="70s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=0_2ieNX3Flo&amp;t=70s" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/0_2ieNX3Flo/maxresdefault.jpg" title="NURBS surface editing in 3D Slicer" width="690" height="388">
  </a>
</div>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerHeart/SlicerSurfaceMarkup">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/8bad88ae15577771d3a9781872cba5ac/SlicerHeart/SlicerSurfaceMarkup" class="thumbnail">

  <h3><a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid surface markup with</a></h3>

    <p><span class="github-repo-description">Extension to test the new grid surface markup with</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @cpinter (2026-03-23 10:25 UTC)

<p>Before I can chime in I’d like to understand. What you want to segment is this structure?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c093a219212efe69f5c31cf87ed9af2c97b6cad.jpeg" data-download-href="/uploads/short-url/hHgYsRTvTBNfIIKBTkCjF2FXCVf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c093a219212efe69f5c31cf87ed9af2c97b6cad.jpeg" alt="image" data-base62-sha1="hHgYsRTvTBNfIIKBTkCjF2FXCVf" width="643" height="497"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">643×497 81.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On how many slices does it appear in the MRI?</p>
<p>I really have a hard time imagining how NURBS would be useful to represent this thin structure.</p>
<p>Also, the problem with the NURBS in SurfaceMarkups is that</p>
<ul>
<li>It needs to be initialized programmatically, otherwise you need to start from a flat sheet</li>
<li>It is either a surface, or a “wrapped around” surface, like a cylinder</li>
<li>Conversion to segmentation is not conveniently solved</li>
</ul>

---

## Post #13 by @mrrezaie (2026-03-23 11:10 UTC)

<p>Thanks all;</p>
<blockquote>
<p>What you want to segment is this structure?</p>
</blockquote>
<p>Yes, exactly, but the surface would be enough for me, so I don’t have to have a volume. This is a non-isotropic MRI, I already have it in 31 slices.</p>
<p>I had some progress with curves and `vtkRuledSurfaceFilter`. This is not good yet, but the approach looks promising. Any idea?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11415e6a3c02f6c3ccdef27cdef537b2cc9c0262.jpeg" data-download-href="/uploads/short-url/2sEatJ8GwjW6lRzXvm0bk7aw9B8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11415e6a3c02f6c3ccdef27cdef537b2cc9c0262.jpeg" alt="image" data-base62-sha1="2sEatJ8GwjW6lRzXvm0bk7aw9B8" width="519" height="421"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">519×421 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your help.</p>

---

## Post #14 by @cpinter (2026-03-23 11:39 UTC)

<p>If you only want surface, then the SurfaceMarkup could be a way to go after all. What I could imagine is:</p>
<ul>
<li>Draw these open curves every few slices, in a way that they have the exact same number of control points</li>
<li>Use a Python script to create a NURBS surface from this NxM grid</li>
</ul>
<p>Something like this:</p>
<pre><code class="lang-auto">gridPoints = vtk.vtkPoints()
gridPoints.SetNumberOfPoints(numCurves * numPointsInCurve)
for u in range(numCurves):
  curveNode = pass  # Need to implement
  for v in range(numPointsInCurve):
    point = np.zeros(3)
    curveNode.GetNthControlPointPosition(v, point)
    gridPoints.SetPoint(u * numPointsInCurve + v, point[0], point[1], point[2])

nurbsSurfaceNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsGridSurfaceNode')
nurbsSurfaceNode.SetGridResolution(numCurves, numPointsInCurve)
nurbsSurfaceNode.SetControlPointPositionsWorld(gridPoints)
nurbsSurfaceNode.CreateDefaultDisplayNodes()

</code></pre>

---

## Post #15 by @mrrezaie (2026-03-23 11:47 UTC)

<p>Thanks a lot, I will try that. If I understood correctly, it fits a <em>plane</em> to the control points; Cool! Does it also handle the boundaries?</p>

---

## Post #16 by @mrrezaie (2026-03-24 13:35 UTC)

<p>Hello all,</p>
<p>I managed to fit a grid surface to the control points. But, this is the output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61affbda651c96e18fcc55bf6dd8afd72aa09fbd.jpeg" data-download-href="/uploads/short-url/dWbmcSoGRCg5my0mfKirWKeL20d.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61affbda651c96e18fcc55bf6dd8afd72aa09fbd.jpeg" alt="image" data-base62-sha1="dWbmcSoGRCg5my0mfKirWKeL20d" width="365" height="362"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">365×362 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used the same snippet. Any idea?</p>

---

## Post #17 by @cpinter (2026-03-24 15:27 UTC)

<p>It seems twisted. Be very careful about the order and spacing of the control points of each curve so that they align in a more or less grid-like way.</p>

---

## Post #18 by @JASON (2026-03-24 16:17 UTC)

<p>I thought this was an interesting use-case so I’ve been playing along at home.<br>
Here is a way to turn curves into a Surface Mesh (vtkPolyData), with controllable subdivisions.</p>
<p>This isn’t as nice as a NURBS surface because it doesn’t subdivide between curves, but may be useful if distance between curves is much less than distance between control points.</p>
<p>This code will sort the curve order based on where the control points lie on the inferior / superior axis.  This way you can draw curves out of order and they get sorted during meshing.</p>
<p>This illustrates the importance of having the same number of control points per-curve, and doing your best to keep them relatively spaced the same proportions between curves.  This way the alignment of control points perpendicular to the curve are well aligned.  My example here could be improved for better flow lines (in yellow).</p>
<p>Its also critical to draw your curves the same direction each time (left-to-right or right-to-left)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b344e82d5f73e89960cfbf879cbaebc0b0e9d6ea.jpeg" data-download-href="/uploads/short-url/pzT6b4d06KIxcH5M9tUeVOXLZ34.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b344e82d5f73e89960cfbf879cbaebc0b0e9d6ea_2_690x215.jpeg" alt="image" data-base62-sha1="pzT6b4d06KIxcH5M9tUeVOXLZ34" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b344e82d5f73e89960cfbf879cbaebc0b0e9d6ea_2_690x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b344e82d5f73e89960cfbf879cbaebc0b0e9d6ea_2_1035x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b344e82d5f73e89960cfbf879cbaebc0b0e9d6ea_2_1380x430.jpeg 2x" data-dominant-color="855769"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×599 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>example code:</p>
<details>
<summary>
Summary</summary>
<pre><code class="lang-auto">import vtk
import slicer

def create_sorted_lofted_surface():
    # 1. Get all curve nodes
    allCurveNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsCurveNode")
    if len(allCurveNodes) &lt; 2:
        print("Need at least 2 curves to create a surface.")
        return

    # 2. Sort curves by their average 'S' (Superior/Inferior) coordinate
    # We calculate the mean S-value of all control points in the curve
    def get_average_s(node):
        s_values = []
        for i in range(node.GetNumberOfControlPoints()):
            p = [0, 0, 0]
            node.GetNthControlPointPositionWorld(i, p)
            s_values.append(p[2]) # RAS: R=0, A=1, S=2
        return sum(s_values) / len(s_values) if s_values else 0

    # Apply the sort
    curveNodes = sorted(allCurveNodes, key=get_average_s)

    numCurves = len(curveNodes)
    numPointsPerCurve = 50 
    points = vtk.vtkPoints()

    # 3. Extract and Resample Points
    for node in curveNodes:
        curvePoly = node.GetCurveWorld()
        if not curvePoly or curvePoly.GetNumberOfPoints() &lt; 2:
            continue

        resampler = vtk.vtkSplineFilter()
        resampler.SetInputData(curvePoly)
        resampler.SetSubdivideToSpecified()
        resampler.SetNumberOfSubdivisions(numPointsPerCurve - 1)
        resampler.Update()
        
        resampledPoly = resampler.GetOutput()

        for i in range(numPointsPerCurve):
            points.InsertNextPoint(resampledPoly.GetPoint(i))

    # 4. Create Mesh Topology (Triangles)
    cellArray = vtk.vtkCellArray()
    for i in range(numCurves - 1):
        for j in range(numPointsPerCurve - 1):
            p1 = i * numPointsPerCurve + j
            p2 = p1 + 1
            p3 = (i + 1) * numPointsPerCurve + j
            p4 = p3 + 1
            
            tri1 = vtk.vtkTriangle()
            tri1.GetPointIds().SetId(0, p1)
            tri1.GetPointIds().SetId(1, p2)
            tri1.GetPointIds().SetId(2, p3)
            
            tri2 = vtk.vtkTriangle()
            tri2.GetPointIds().SetId(0, p2)
            tri2.GetPointIds().SetId(1, p4)
            tri2.GetPointIds().SetId(2, p3)
            
            cellArray.InsertNextCell(tri1)
            cellArray.InsertNextCell(tri2)

    # 5. Finalize Model
    outputPolyData = vtk.vtkPolyData()
    outputPolyData.SetPoints(points)
    outputPolyData.SetPolys(cellArray)

    normals = vtk.vtkPolyDataNormals()
    normals.SetInputData(outputPolyData)
    normals.ConsistencyOn()
    normals.SplittingOff()
    normals.Update()

    modelName = "Lofted_S_Sorted_Surface"
    modelNode = slicer.util.getFirstNodeByName(modelName)
    if not modelNode:
        modelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", modelName)
    
    modelNode.SetAndObservePolyData(normals.GetOutput())
    modelNode.CreateDefaultDisplayNodes()
    modelNode.GetDisplayNode().SetBackfaceCulling(False) 
    modelNode.GetDisplayNode().SetColor(0.8, 0.2, 0.2) # Reddish
    
    print(f"Lofted {numCurves} curves sorted by Superior coordinate.")

create_sorted_lofted_surface()

</code></pre>
</details>

---

## Post #19 by @mrrezaie (2026-03-26 14:30 UTC)

<p><a class="mention" href="/u/jason">@JASON</a></p>
<p>Thanks a lot for the code. I had to sort the curves from right/left, and it worked.</p>
<pre data-code-wrap="python"><code class="lang-python">s_values.append(p[0]) # RAS: R=0, A=1, S=2
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/529b4222b12ff522576128acba764753f660d64d.jpeg" data-download-href="/uploads/short-url/bMLN6Blf8vHnmFH71tmj9OwYJNr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/529b4222b12ff522576128acba764753f660d64d.jpeg" alt="image" data-base62-sha1="bMLN6Blf8vHnmFH71tmj9OwYJNr" width="375" height="359"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">375×359 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, I need to take care of the points density on the curves, and the boundaries.</p>
<p>Thanks again.</p>

---

## Post #20 by @mikebind (2026-03-26 16:42 UTC)

<p>Just a quick comment.  You can also resample along individual curves easily, so that could be a way to address having different numbers of control points on different curves:  You just resample along the curve to have a specified matching number of control points (keeping the endpoints the same).  This would also handle having the points matching fractions of the way along the curve.</p>

---

## Post #21 by @chir.set (2026-03-26 20:20 UTC)

<p>The result below is obtained by this method:</p>
<ul>
<li>segment the femur</li>
<li>convert the segment to a model</li>
<li>outline the cartilage with a closed curve</li>
<li>use Curve cut in the Dynamic modeler module</li>
</ul>
<p>This has been done at the segmented bone’s surface. May be you could grow the segment by 1 mm at least, apply Joint smoothing before converting to a model. This would account for the thickness of the cartilage, which is itself an invisible structure on a CT scan.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3293e1c8ec7069069cfb0849bba8cc8d96bc91d.gif" alt="Cartilage" data-base62-sha1="rQtt3uvlJCYjW5OEKGu86aXmc6V" width="574" height="500" class="animated"></p>

---

## Post #22 by @mrrezaie (2026-03-27 08:33 UTC)

<p>This is an interesting approach; thanks for introducing the Dynamic Modeler module.</p>
<p>By any chance, is there any option to interpolate the segmentation? At the moment, I have 31 slices and interpolating the image doesn’t fix these steps, I have to do segmentation in all interpolated images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78fb0081197a2eb1f863a81416e30e86028556af.png" data-download-href="/uploads/short-url/hgf44wM7oWbeaT8rniAVLZRzTFd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78fb0081197a2eb1f863a81416e30e86028556af.png" alt="image" data-base62-sha1="hgf44wM7oWbeaT8rniAVLZRzTFd" width="275" height="267"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">275×267 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @chir.set (2026-03-27 11:35 UTC)

<p>Your best bet to segment the bone in this context is the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds" rel="noopener nofollow ugc">Grow from seeds</a> effect of the <code>Segment editor.</code></p>
<p>It’s not a one-click process. You’ll have to combine with many other effects.</p>

---

## Post #24 by @mrrezaie (2026-03-29 14:29 UTC)

<p>Thanks for the suggestion; I’m now trying the alternative approach in more details. Since this is a different topic, I created a new post for that: <a href="https://discourse.slicer.org/t/keep-the-hand-drawn-segmentation-after-interpolation/46605" class="inline-onebox">Keep the hand-drawn segmentation after interpolation</a></p>

---
