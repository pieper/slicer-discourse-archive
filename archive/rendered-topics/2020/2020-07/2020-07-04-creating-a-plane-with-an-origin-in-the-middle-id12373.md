# Creating a plane with an origin in the middle

**Topic ID**: 12373
**Date**: 2020-07-04
**URL**: https://discourse.slicer.org/t/creating-a-plane-with-an-origin-in-the-middle/12373

---

## Post #1 by @talmazov (2020-07-04 14:21 UTC)

<p>Hey,<br>
I am trying to create a plane with an origin/center set in the middle (ie. 0.5x_length, 0.5y_length).<br>
I don’t have a problem creating a plane, playing around with set center and origin yield weird results, the only predictable setup is having origin and center set to 0 then i get that origin/center to be at the edge of the plane. ive tried all kinds of combination of values but doesnt seem to work. any suggestions?</p>
<blockquote>
<p>tangential_plane = vtk.vtkPlaneSource()<br>
tangential_plane.SetCenter(0,0,0)<br>
tangential_plane.SetOrigin(0,0,0)<br>
tangential_plane.SetNormal(1,0,0)<br>
tangential_plane.SetPoint1(20.0, 0.0, 0.0)<br>
tangential_plane.SetPoint2(0.0,34.0, 0.0)<br>
tangential_plane.SetXResolution(1)<br>
tangential_plane.SetYResolution(1)<br>
tangential_plane_node = slicer.modules.models.logic().AddModel(tangential_plane.GetOutputPort())<br>
tangential_plane_node.SetName(“tangential_plane”)<br>
tangential_plane_node.GetDisplayNode().SetColor(255,255,0)<br>
<span class="hashtag-raw">#tangential_plane_node</span>.GetDisplayNode().SetOpacity(1.0)<br>
tangential_plane_node.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
tangential_plane_node.GetDisplayNode().SetSliceIntersectionThickness(2)</p>
<p>transform = slicer.vtkMRMLTransformNode()<br>
transform.SetName(“tangential_plane”+‘_trans’)<br>
slicer.mrmlScene.AddNode(transform)<br>
tangential_plane_node.SetAndObserveTransformNodeID(transform.GetID())</p>
</blockquote>
<p>thanks</p>

---

## Post #2 by @lassoan (2020-07-04 15:23 UTC)

<p>Yes, the VTK plane source has somewhat redundant parameterization and if you provide inconsistent input then the displayed plane is skewed.</p>
<p>I would recommended to use the markups plane node instead. It can be placed with more developer-friendly methods (and if you have any suggestions to improve its API then we can easily do that). Users can also move/rotate it interactively and it can be used as a cutting plane (in Dynamic modeler module) and will be used in more and more modules wherever an input or output plane is needed. It is available in recent Slicer Preview Releases.</p>

---
