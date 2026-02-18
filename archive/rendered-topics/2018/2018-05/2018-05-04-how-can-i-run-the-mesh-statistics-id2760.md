# How can I run the Mesh statistics?

**Topic ID**: 2760
**Date**: 2018-05-04
**URL**: https://discourse.slicer.org/t/how-can-i-run-the-mesh-statistics/2760

---

## Post #1 by @Pilar (2018-05-04 11:08 UTC)

<p>Hi 3Dslicer users,<br>
I am working on a University project and I need to get the statistics (the distance between all the points in a colormap file (.vtk file).<br>
This file was done with the two models of the hemimandibles which were firstly superimposed (voxel based registration) and then I used the Model to Model distance command to create it.<br>
It is posible to get the file with all the numbers. I mean, the distance between every correspondent point to analyze them?</p>
<p>Thank you in advance</p>

---

## Post #2 by @lassoan (2018-05-09 04:59 UTC)

<p>You can simply save the file in vtk or vtp file format and that will contain all the computed distances for each point.</p>
<p>Note that you can also access all the distance values in Python and compute statistics (histogram, etc). For example, this script shows how to compute and plot histogram:</p>
<pre><code>modelNode = getNode('VTK Output File')

# Get distances from model node (stored in point data array)
import vtk.util.numpy_support
distanceArrayVtk =modelNode.GetPolyData().GetPointData().GetArray('Signed')
distanceArray = vtk.util.numpy_support.vtk_to_numpy(distanceArrayVtk) 

# Compute histogram values
import numpy as np
histogram = np.histogram(distanceArray, bins=50)

# Save results to a new table node
tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
updateTableFromArray(tableNode, histogram)
tableNode.GetTable().GetColumn(0).SetName("Count")
tableNode.GetTable().GetColumn(1).SetName("Intensity")

# Create plot
plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", 'Distance histogram')
plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
plotSeriesNode.SetXColumnName("Intensity")
plotSeriesNode.SetYColumnName("Count")
plotSeriesNode.SetPlotType(plotSeriesNode.PlotTypeScatterBar)
plotSeriesNode.SetColor(0, 0.6, 1.0)

# Create chart and add plot
plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())
#plotChartNode.YAxisRangeAutoOff()
#plotChartNode.SetYAxisRange(0, 500000)

# Show plot in layout
slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b22e1f577b9207e6b67dc6a0054fd76f052648ff.png" data-download-href="/uploads/short-url/pqfO0wooH844QDaHuT2B6HLQImb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e1f577b9207e6b67dc6a0054fd76f052648ff_2_690x268.png" alt="image" data-base62-sha1="pqfO0wooH844QDaHuT2B6HLQImb" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e1f577b9207e6b67dc6a0054fd76f052648ff_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e1f577b9207e6b67dc6a0054fd76f052648ff_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b22e1f577b9207e6b67dc6a0054fd76f052648ff_2_1380x536.png 2x" data-dominant-color="8CACBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1580×615 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Pilar (2018-05-11 11:05 UTC)

<p>Andras, thank so much for your help.<br>
I will try to do this and let you know.</p>
<p>Regards</p>

---

## Post #4 by @antoniolch (2020-06-03 21:18 UTC)

<p>Hi,</p>
<p>I am trying to use your script to see the histogram of my vtk file but I am having some problems with the getNode(‘file.vtk’) instruction. I though that this method was inside the slicer.util package but when python3 raises me the error</p>
<blockquote>
<p>AttributeError: module ‘slicer.slicer’ has no attribute ‘util’</p>
</blockquote>
<p>I am using a simple python script outside the slider program. Should I use the python environment inside Slicer? Please, could do you help me?</p>

---

## Post #5 by @lassoan (2020-06-03 21:30 UTC)

<p>It seems that you are calling  <code>slicer.slicer.util.getNode()</code>. It should be <code>slicer.util.getNode()</code>.</p>

---

## Post #6 by @antoniolch (2020-06-04 07:12 UTC)

<p>Thanks but the problem still remain.<br>
I am trying to plot an histogram from the vtk saved file containing distances.<br>
So, how can I use a python script outside the slicer program to do it?</p>

---
