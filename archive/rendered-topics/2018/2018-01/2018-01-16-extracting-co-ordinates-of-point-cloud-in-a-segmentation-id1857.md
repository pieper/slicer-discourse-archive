# Extracting co-ordinates of point cloud in a segmentation

**Topic ID**: 1857
**Date**: 2018-01-16
**URL**: https://discourse.slicer.org/t/extracting-co-ordinates-of-point-cloud-in-a-segmentation/1857

---

## Post #1 by @HarishRRao (2018-01-16 16:30 UTC)

<p>I want to extract <em>xyz</em> co-ordinates of point cloud of a segment created in Slicer. I have tried saving a segment as a .ply file and then opened the same in Meshlab and saved it as a .xyz file to get the physical co-ordinates of all the points. That works. I wanted to know if there is a direct way to get the co-ordinates of points directly from 3D Slicer?</p>

---

## Post #2 by @lassoan (2018-01-16 16:59 UTC)

<p>Yes, you can access the coordinates directly. For example, this code snippet gives you point coordinates in a numpy array:</p>
<pre><code>segmentationNode=getNode('Segmentation')
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)
segmentPolyData=segmentationNode.GetClosedSurfaceRepresentation(segmentId)
import vtk.util.numpy_support
pointData = segmentPolyData.GetPoints().GetData()
pointCoordinates = vtk.util.numpy_support.vtk_to_numpy(pointData)
</code></pre>
<p>Connectivity between points is very important, as often it is very difficult to accurately reconstruct a surface from just the point cloud. So, in general, I would recommend to export the full mesh (triangle cell point IDs as well), and not just points coordinates.</p>

---

## Post #3 by @mrrezaie (2022-10-24 10:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>GetClosedSurfaceRepresentation</code></p>
</blockquote>
</aside>
<p>GetClosedSurfaceInternalRepresentation</p>

---

## Post #4 by @lassoan (2022-10-24 13:13 UTC)

<p>Indeed, the API slightly changed since how it worked 5 years ago. <code>GetClosedSurfaceInternalRepresentation</code> returns what the segmentation node stores internally, which is for advanced use (because for example in the future one polydata may be used for multiple segments and you would need to extract mesh of a specific segment with an additional step). It is generally recommended to use <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a981a64425627037c55d418c36981e371">GetClosedSurfaceRepresentation()</a> method instead, because it will always return the mesh of the selected segment, regardless how internal implementation may change in the future.</p>

---

## Post #5 by @mrrezaie (2022-10-24 14:09 UTC)

<p>Dear Andras,</p>
<p>Thanks for your guidance. What would be the second argument of <code>GetClosedSurfaceRepresentation()</code> in this example?</p>
<p>Also, I’m trying to fit a sphere to a point cloud.<br>
Instead of creating 3-4 markup points, I prefer to use point clouds in order to enhance accuracy. If I use the SurfaceWrapSolidify extension, I can close the segment and get the outer point cloud. Does API has any function to get the external points and ignore the internal points?</p>
<p>Thnak you</p>

---

## Post #6 by @lassoan (2022-10-24 17:33 UTC)

<aside class="quote no-group" data-username="mrrezaie" data-post="5" data-topic="1857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrrezaie/48/17032_2.png" class="avatar"> mrrezaie:</div>
<blockquote>
<p>Thanks for your guidance. What would be the second argument of <code>GetClosedSurfaceRepresentation()</code> in this example?</p>
</blockquote>
</aside>
<p>It is a <code>vtkPolyData</code> object. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-representation-of-a-segment">script repository</a>.</p>
<aside class="quote no-group" data-username="mrrezaie" data-post="5" data-topic="1857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrrezaie/48/17032_2.png" class="avatar"> mrrezaie:</div>
<blockquote>
<p>Also, I’m trying to fit a sphere to a point cloud.<br>
Instead of creating 3-4 markup points, I prefer to use point clouds in order to enhance accuracy.</p>
</blockquote>
</aside>
<p>You can use all the mesh points to fit a sphere. See a complete implementation in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">script repository</a>. The only change you need to make is to call <code>slicer.util.arrayFromModelPoints()</code> for an input model node instead of <code>slicer.util.arrayFromMarkupsControlPoints()</code> for an input markup node.</p>
<aside class="quote no-group" data-username="mrrezaie" data-post="5" data-topic="1857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrrezaie/48/17032_2.png" class="avatar"> mrrezaie:</div>
<blockquote>
<p>If I use the SurfaceWrapSolidify extension, I can close the segment and get the outer point cloud. Does API has any function to get the external points and ignore the internal points?</p>
</blockquote>
</aside>
<p>There is no need for any special API, as SurfaceWrapSolidify extension removes all internal points. If you find that after solidify operation only cells are removed but orphan points are still there then you can remove them using Surface toolbox module’s Clean option (or vtkCleanPolyData filter).</p>

---

## Post #7 by @mrrezaie (2022-10-24 21:57 UTC)

<p>Thank you so much for your help. Fixed.</p>

---
