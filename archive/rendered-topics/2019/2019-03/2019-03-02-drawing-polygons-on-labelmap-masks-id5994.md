---
topic_id: 5994
title: "Drawing Polygons On Labelmap Masks"
date: 2019-03-02
url: https://discourse.slicer.org/t/5994
---

# Drawing Polygons on Labelmap Masks

**Topic ID**: 5994
**Date**: 2019-03-02
**URL**: https://discourse.slicer.org/t/drawing-polygons-on-labelmap-masks/5994

---

## Post #1 by @gleman (2019-03-02 19:03 UTC)

<p>I’ve got a function that produces a list of vtkPolygons (that I put together into a vtkPolyData) that I’d like to “draw” on a labelmap mask.  It looks like</p>
<pre><code>EditorLib.LabelEffect.slicer.SegmentEditorDrawEffect.scriptedEffect.appendPolyMask(label_map, polyData, sliceWidget )
</code></pre>
<p>will do the trick.  The problem is that when I call that I get:</p>
<pre><code>MemoryError: std::bad_alloc: bad allocation
</code></pre>
<p>It looks like the label map I get inside my effect on an empty segment has zero dimensions:</p>
<pre><code>label_map = self.scriptedEffect.maskLabelmap()
</code></pre>
<p>I assume that would be the case even if there were something in the segment already and I was drawing outside of the bounds of that mask?</p>
<p>Is there a way to create a mask that isn’t zero length from an empty segment?  Or how should I be going about the task of drawing these vtkPolygons into a segment?  I’d like to be able to have the system draw these in and then let the user clean them up a bit in one workflow.</p>

---

## Post #2 by @gleman (2019-03-06 22:43 UTC)

<p>I wasn’t able to make this work but came up with a different approach.  I figured I’d post this for the next person that is tearing their hair out over this.</p>
<p>First, get the points out of the vtkPolygons:</p>
<pre><code>def get_points_from_vtk_polygon(vtk_polygon):
        return [list(vtk_polygon.GetPoints().GetPoint(i)) for i in  
               xrange(vtk_polygon.GetPoints().GetNumberOfPoints())]
</code></pre>
<p>Then save those points as Markups:</p>
<pre><code>def save_markup_points(markup_name, points):
     markupsNode = slicer.mrmlScene.GetFirstNodeByName(markup_name)
     if markupsNode is None:
         markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
         markupsNode.SetName(markup_name)
     for pt in points:
         markupsNode.AddFiducial(*pt)
</code></pre>
<p>Then just convert the markups to a segment:</p>
<pre><code>markupsToModelNode = slicer.vtkMRMLMarkupsToModelNode()
slicer.mrmlScene.AddNode(markupsToModelNode)
fiducial_node = slicer.util.getNode(fiducial_name)
slicer.modules.markupstomodel.logic().SetMarkupsNode(fiducial_node, markupsToModelNode)
outputModelNode = slicer.vtkMRMLModelNode()
slicer.mrmlScene.AddNode(outputModelNode)
outputModelNode.SetName(model_name)
markupsToModelNode.SetAndObserveModelNodeID(outputModelNode.GetID())
markupsToModelNode.SetModelType(0)
mesh = outputModelNode.GetMesh()
color_list = [51.0, 221.0, 255.0]
segment_id = segmentation.GetSegmentIdBySegmentName(segment_name)
segmentation_node.AddSegmentFromClosedSurfaceRepresentation(mesh, segment_name, color_list, segment_id)
slicer.mrmlScene.RemoveNode(markupsToModelNode)
slicer.mrmlScene.RemoveNode(outputModelNode)
</code></pre>
<p>It takes a bit of time to run with large polygons, but can be sped up by just skipping some of the markup points:</p>
<pre><code>save_markup_points('test', pts[0::3])</code></pre>

---

## Post #3 by @lassoan (2019-03-07 03:52 UTC)

<aside class="quote no-group" data-username="gleman" data-post="1" data-topic="5994">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/85e7bf/48.png" class="avatar"> gleman:</div>
<blockquote>
<p>EditorLib.LabelEffect</p>
</blockquote>
</aside>
<p>This indicates that you might have tried to use the legacy Editor module. It will be probably removed from Slicer5, so I would recommend not to rely on it anymore.</p>
<p>The approach that you described should work nicely for convex (or slightly concave) shapes. You don’t need to create a temporary markups module, you can use a lower level API - vtkSlicerMarkupsToModelClosedSurfaceGeneration - to generate vtkPolyData from vtkPoints.</p>
<p>If you need to work with concave shapes then you can save your planar contours in a polydata and set it in a segmentation node as “planar contour” representation. Segmentation infrastructure automatically converts it to all other representations (binary labelmap, closed surface, ribbon, etc.) as needed. The converters are provided by SlicerRT extension (since this planar contour representation is still quite commonly used for radiotherapy and not used much elsewhere), so you will need to install this extension.</p>

---
