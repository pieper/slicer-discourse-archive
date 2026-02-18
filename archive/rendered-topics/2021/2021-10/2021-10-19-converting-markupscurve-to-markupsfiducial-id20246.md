# Converting MarkupsCurve to MarkupsFiducial

**Topic ID**: 20246
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/converting-markupscurve-to-markupsfiducial/20246

---

## Post #1 by @kmalexander (2021-10-19 18:23 UTC)

<p>I’ve imported a brachytherapy treatment plan that includes a MarkupsCurve for each catheter.  I’m looking to convert each of these into models (ultimately, individual segments).</p>
<p>I can copy and paste all the control points in a MarkupsFiducial list, one catheter at a time, which allows me to create a model for each catheter.</p>
<p>I feel there must be an easier way!  Anyone have any ideas?  Perhaps I’m missing a set of tools that helps with this.</p>

---

## Post #2 by @muratmaga (2021-10-19 19:27 UTC)

<p>It is a hack, not a real solution, but you can save Markupcurves as fcsv (not JSON) and reload them into the slicer. That way they will be loaded as MarkupFiducials.</p>
<p>Or you use the import/export tab to export as a table and reimport as a markupFiducial, though I don’t think this will be less work than copy/pasting.</p>
<p>Probably scripting is the way to go.</p>

---

## Post #3 by @lassoan (2021-10-20 05:38 UTC)

<p>I guess we don’t have a module for this because it is so simple to get a model/segmentation using the Python console:</p>
<pre><code class="lang-python">curveNode = getNode('OC')
segmentationNode = getNode('Segmentation')

# Create mesh using tube filter
tube = vtk.vtkTubeFilter()
tube.SetInputData(curveNode.GetCurveWorld())
# Customize the tube parameters (optional)
tube.SetRadius(10)
tube.SetNumberOfSides(30)
tube.CappingOn()

# Add it to a new model node...
slicer.modules.models.logic().AddModel(tube.GetOutputPort())

# ...or add it to a segmentation as a new segment
tube.Update()
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(
  tube.GetOutput(), "catheter", [0.0,1.0,0.0])
</code></pre>
<p>This code could be quite easily added as a “Convert” or “Export/Import” section in Markups module. If you think this would help you then you can <a href="http://issues.slicer.org/">submit a feature request</a>.</p>

---
