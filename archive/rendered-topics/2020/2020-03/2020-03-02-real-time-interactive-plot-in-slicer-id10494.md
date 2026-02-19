---
topic_id: 10494
title: "Real Time Interactive Plot In Slicer"
date: 2020-03-02
url: https://discourse.slicer.org/t/10494
---

# Real time interactive plot in Slicer

**Topic ID**: 10494
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/real-time-interactive-plot-in-slicer/10494

---

## Post #1 by @fpsiddiqui91 (2020-03-02 15:11 UTC)

<p>Dear All,</p>
<p>I have been working with slicer for 5-6 months. I have managed to develop some useful modules. However, for the current task, I will be needing your help.</p>
<p>I have my data in NumPy array, which is kept on updating progressively. I need to plot a histogram real-time with an option that a user can interact with a histogram or make a rectangle or something to select a art of the data</p>
<p>something like this:</p><aside class="quote quote-modified" data-post="1" data-topic="9221">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-histogram-for-setting-threshold-range-in-segment-editor/9221">New feature: Histogram for setting threshold range in Segment Editor</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In the latest 3D Slicer 4.11.0 releases, the Threshold effect in the Segment Editor module now includes the option to specify the minimum and maximum thresholds based on the histogram of a region of interest in the slice view. 

  <a href="https://www.youtube.com/watch?v=pGVbhmsyXhY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    [Segment Editor: Local histogram in threshold effect]
  </a>


Clicking and dragging on a slice view will create a yellow border that encompasses the region of interest. Several different shapes can be used to draw the region of interest including: box, circle, freefo…
  </blockquote>
</aside>

<p>I cannot find the code for this, can you help me making this king of the histogram in the most efficient way?</p>

---

## Post #2 by @fpsiddiqui91 (2020-03-02 18:07 UTC)

<p>I went through several examples, like:</p>
<aside class="quote" data-post="1" data-topic="1559">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/area-of-segment-in-a-given-slice/1559">Area of segment in a given slice?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Is there a way to determine the area a segment takes up in a given slice? I’m interested in generating a plot from a CT scan, anterior to posterior, of the area taken up by a segment slice-by-slice (if that makes sense). 
If you were to do this on a sphere, for example, you’d wind up with a gaussian. (I think, I’d have to double-check the math on that…) 
Thanks! 
-Hollister
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="2" data-topic="2760">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-run-the-mesh-statistics/2760/2">How can I run the Mesh statistics?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can simply save the file in vtk or vtp file format and that will contain all the computed distances for each point. 
Note that you can also access all the distance values in Python and compute statistics (histogram, etc). For example, this script shows how to compute and plot histogram: 
modelNode = getNode('VTK Output File')

# Get distances from model node (stored in point data array)
import vtk.util.numpy_support
distanceArrayVtk =modelNode.GetPolyData().GetPointData().GetArray('Signed')
…
  </blockquote>
</aside>

<p>I managed to make a histogram with my Table Node, However, as I update the table Node with my new data, the chart just vanishes.   Here is my code for making a histogram:</p>
<pre><code>self.plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode", "Histogram")
histogram = np.histogram(self.my_DATA, bins=10)   # my_DATA is the numpy array containing the data
self.tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","Distance Histogram")
slicer.util.updateTableFromArray(self.tableNode,histogram)
self.tableNode.GetTable().GetColumn(0).SetName("Count")
self.tableNode.GetTable().GetColumn(1).SetName("Intensity")




# Create new plot data series node
self.plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", "Distance histogram")
self.plotSeriesNode.SetAndObserveTableNodeID(self.tableNode.GetID())
self.plotSeriesNode.SetXColumnName("Intensity")
self.plotSeriesNode.SetYColumnName("Count")
self.plotSeriesNode.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeScatterBar)
self.plotSeriesNode.SetMarkerStyle(slicer.vtkMRMLPlotSeriesNode.MarkerStyleNone)


# Add plot to chart
self.plotChartNode.AddAndObservePlotSeriesNodeID(self.plotSeriesNode.GetID())
#self.plotChartNode.AddAndObservePlotDataNodeID(self.DataNode.GetID())

layoutManager=slicer.app.layoutManager()
layoutManager.setLayout (slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)
self.plotWidget = layoutManager.plotWidget(0)


self.plotViewNode= self.plotWidget.mrmlPlotViewNode()
self.plotViewNode.SetPlotChartNodeID (self.plotChartNode.GetID())
</code></pre>
<p>This works fine. However as , my data gets updated, I make a new histogram and update the table node with a new histogram data as:</p>
<pre><code>histogram = np.histogram(self.my_DATA, bins=20)


slicer.util.updateTableFromArray(self.tableNode, histogram)
self.plotWidget.update()
</code></pre>
<p>As soon as my Table node gets updated, I cannot see anything in the chart.<br>
Can you help me with this?  <a class="mention" href="/u/lassoan">@lassoan</a> may be. Thanks.</p>
<p>Thanks in advance.</p>

---

## Post #3 by @lassoan (2020-03-03 02:08 UTC)

<p>The plot disappeared because you specified that the chart is built from columns “Intensity” and “Count”, but the table after calling <code>slicer.util.updateTableFromArray(tableNode, histogram)</code> had default column names (Column 1, Column 2). Since numpy arrays do not store column names, you need to manage them by yourself and pass it to the the converter function yourself:</p>
<pre><code>slicer.util.updateTableFromArray(tableNode, histogram, ["Count", "Intensity"])</code></pre>

---

## Post #4 by @fpsiddiqui91 (2020-03-03 07:41 UTC)

<p>Thank you so much for your response <a class="mention" href="/u/lassoan">@lassoan</a>, it worked like a charm.</p>
<p>According to your experience, what is the  most efficient way to make a real time interactive plot? Is there any better way other than this?</p>
<p>Thank you.</p>

---
