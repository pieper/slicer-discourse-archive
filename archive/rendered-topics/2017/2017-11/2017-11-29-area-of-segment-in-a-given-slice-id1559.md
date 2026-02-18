# Area of segment in a given slice?

**Topic ID**: 1559
**Date**: 2017-11-29
**URL**: https://discourse.slicer.org/t/area-of-segment-in-a-given-slice/1559

---

## Post #1 by @hherhold (2017-11-29 21:00 UTC)

<p>Is there a way to determine the area a segment takes up in a given slice? I’m interested in generating a plot from a CT scan, anterior to posterior, of the area taken up by a segment slice-by-slice (if that makes sense).</p>
<p>If you were to do this on a sphere, for example, you’d wind up with a gaussian. (I think, I’d have to double-check the math on that…)</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2017-11-30 14:08 UTC)

<p>There’s nothing built-in to do that, but it would be possible with a little python scripting.  Are you interested in trying that?  We could give some pointers.</p>

---

## Post #3 by @lassoan (2017-11-30 14:52 UTC)

<p>This should do what you need (this script puts results in a table but you can easily create a plot from the vtkDoubleArray):</p>
<pre><code>segmentationNode = getNode('Segmentation')
segmentId = 'Segment_1'

# Get segment as a numpy array
import vtk.util.numpy_support
import numpy as np
vimage = segmentationNode.GetBinaryLabelmapRepresentation(segmentId)
narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars())
vshape = vimage.GetDimensions()

# Reshape the segment volume to have an array of slices
narrayBySlice = narray.reshape([-1,vshape[1]*vshape[2]])

# Count number of &gt;0 voxels for each slice
narrayBySlicePositive = narrayBySlice[:]&gt;0
areaBySliceInVoxels = np.count_nonzero(narrayBySlicePositive, axis=1)

# Convert number of voxels to area in mm2
areaOfPixelMm2 = vimage.GetSpacing()[0] * vimage.GetSpacing()[1]
areaBySliceInMm2 = areaBySliceInVoxels * areaOfPixelMm2

# Save results to a new table node
tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", "Segment quantification")
updateTableFromArray(tableNode, areaBySliceInMm2)
tableNode.GetTable().GetColumn(0).SetName("Segment Area")</code></pre>

---

## Post #4 by @hherhold (2017-11-30 17:57 UTC)

<p>You guys are awesome! Thanks!!</p>
<p>-Hollister</p>

---

## Post #5 by @lassoan (2017-11-30 19:32 UTC)

<p>This code snipped will create a plot:</p>
<pre><code>plotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")
plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())
plotDataNode.SetXColumnName("Indexes")
plotDataNode.SetYColumnName(tableNode.GetTable().GetColumn(0).GetName())

plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())

layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)
plotWidget = layoutManager.plotWidget(0)

plotViewNode = plotWidget.mrmlPlotViewNode()
plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
</code></pre>
<p>It’ll work with tomorrow’s nightly build (I had to make some fixes in the Slicer core).</p>

---
