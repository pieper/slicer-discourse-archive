---
topic_id: 16027
title: "How To Get The Histogram And Area"
date: 2021-02-17
url: https://discourse.slicer.org/t/16027
---

# How to get the histogram and area

**Topic ID**: 16027
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/how-to-get-the-histogram-and-area/16027

---

## Post #1 by @BORIPHAT (2021-02-17 07:10 UTC)

<p>Hello,<br>
I would like to get the histogram and the area. In the beginning, I follow the  Calculating distance using Maurer distance map Topic. But when I copy and paste the script into the Python console. I got the below message. Could you please give me some advice? Thank you very much. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f58e35fef6978eabaccecedfeb07b508db048f02.png" data-download-href="/uploads/short-url/z2hFh9WxowftFp1ZfU4lDsFqRvI.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f58e35fef6978eabaccecedfeb07b508db048f02_2_690x375.png" alt="Picture1" data-base62-sha1="z2hFh9WxowftFp1ZfU4lDsFqRvI" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f58e35fef6978eabaccecedfeb07b508db048f02_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f58e35fef6978eabaccecedfeb07b508db048f02_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f58e35fef6978eabaccecedfeb07b508db048f02_2_1380x750.png 2x" data-dominant-color="9F9FA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1613×878 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">Python 2.7.13 (default, May 16 2019, 14:27:45) [MSC v.1900 64 bit (AMD64)] on win32
&gt;&gt;&gt; modelNode = getNode('VTK Output File')
DLL load failed: The specified module could not be found.
DLL load failed: The specified module could not be found.
DLL load failed: The specified module could not be found.
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py", line 710, in getNode
    raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (type(pattern) == str) else ""))
MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'VTK Output File'
&gt;&gt;&gt; distanceArrayName = "Signed"
&gt;&gt;&gt; 
&gt;&gt;&gt; # Get distances from point data
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; distances = vtk.util.numpy_support.vtk_to_numpy(modelNode.GetPolyData().GetPointData().GetArray(distanceArrayName))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'modelNode' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Print basic stats
&gt;&gt;&gt; print("Minimum distance: %f" % min(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; print("Maximum distance: %f" % max(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; print("Mean distance: %f" % np.mean(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Compute histogram
&gt;&gt;&gt; histogram = np.histogram(distances, bins=100)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Save results to a new table node
&gt;&gt;&gt; tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", modelNode.GetName() + " histogram")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'modelNode' is not defined
&gt;&gt;&gt; updateTableFromArray(tableNode, histogram)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; tableNode.GetTable().GetColumn(0).SetName("Count")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; tableNode.GetTable().GetColumn(1).SetName("Intensity")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Create plot
&gt;&gt;&gt; 
&gt;&gt;&gt; plotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")
&gt;&gt;&gt; plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetAndObserveTableNodeID'
&gt;&gt;&gt; plotDataNode.SetXColumnName("Intensity")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetXColumnName'
&gt;&gt;&gt; plotDataNode.SetYColumnName("Count")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetYColumnName'
&gt;&gt;&gt; 
&gt;&gt;&gt; plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
&gt;&gt;&gt; plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'MRMLCorePython.vtkMRMLPlotChartNode' object has no attribute 'AddAndObservePlotDataNodeID'
&gt;&gt;&gt; plotChartNode.SetAttribute("Type", "Bar") # delete this line for line plot
&gt;&gt;&gt; 
&gt;&gt;&gt; # Show plot in layout
&gt;&gt;&gt; 
&gt;&gt;&gt; layoutManager = slicer.app.layoutManager()
&gt;&gt;&gt; layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)
&gt;&gt;&gt; plotWidget = layoutManager.plotWidget(0)
&gt;&gt;&gt; 
&gt;&gt;&gt; plotViewNode = plotWidget.mrmlPlotViewNode()
&gt;&gt;&gt; plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
</code></pre>

---

## Post #2 by @lassoan (2021-02-17 11:39 UTC)

<p>This script is not compatible with Slicer 4.10. Let us know if you have any trouble with the latest stable version.</p>

---

## Post #3 by @BORIPHAT (2021-02-18 06:16 UTC)

<aside class="quote no-group" data-username="BORIPHAT" data-post="1" data-topic="16027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<p>Calculating distance using Maurer distance map</p>
</blockquote>
</aside>
<p>Thank you very much for your quick response. Now I use version 4.11 and I  found the error again and the software does not show the Histogram. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e4527b94a9a9bd8cc5c2fdce39a5a7b545ecf9.png" alt="Picture3" data-base62-sha1="kXsT6jpTQBzPNPB7ZUdq6t1vkYF" width="316" height="478"></p>

---

## Post #4 by @BORIPHAT (2021-02-18 06:17 UTC)

<pre><code class="lang-auto">Python 3.6.7 (default, Sep 30 2020, 16:13:32) [MSC v.1924 64 bit (AMD64)] on win32
&gt;&gt;&gt; modelNode = getNode('VTK Output File')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\Boriphat\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py", line 1137, in getNode
    raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (isinstance(pattern, str)) else ""))
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id 'VTK Output File'
&gt;&gt;&gt; distanceArrayName = "Signed"
&gt;&gt;&gt; 
&gt;&gt;&gt; # Get distances from point data
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; distances = vtk.util.numpy_support.vtk_to_numpy(modelNode.GetPolyData().GetPointData().GetArray(distanceArrayName))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'modelNode' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Print basic stats
&gt;&gt;&gt; print("Minimum distance: %f" % min(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; print("Maximum distance: %f" % max(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; print("Mean distance: %f" % np.mean(distances))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Compute histogram
&gt;&gt;&gt; histogram = np.histogram(distances, bins=100)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'distances' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Save results to a new table node
&gt;&gt;&gt; tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", modelNode.GetName() + " histogram")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'modelNode' is not defined
&gt;&gt;&gt; updateTableFromArray(tableNode, histogram)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; tableNode.GetTable().GetColumn(0).SetName("Count")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; tableNode.GetTable().GetColumn(1).SetName("Intensity")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'tableNode' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Create plot
&gt;&gt;&gt; 
&gt;&gt;&gt; plotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")
&gt;&gt;&gt; plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetAndObserveTableNodeID'
&gt;&gt;&gt; plotDataNode.SetXColumnName("Intensity")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetXColumnName'
&gt;&gt;&gt; plotDataNode.SetYColumnName("Count")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'SetYColumnName'
&gt;&gt;&gt; 
&gt;&gt;&gt; plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
&gt;&gt;&gt; plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: 'MRMLCorePython.vtkMRMLPlotChartNode' object has no attribute 'AddAndObservePlotDataNodeID'
&gt;&gt;&gt; plotChartNode.SetAttribute("Type", "Bar") # delete this line for line plot
&gt;&gt;&gt; 
&gt;&gt;&gt; # Show plot in layout
&gt;&gt;&gt; 
&gt;&gt;&gt; layoutManager = slicer.app.layoutManager()
&gt;&gt;&gt; layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)
&gt;&gt;&gt; plotWidget = layoutManager.plotWidget(0)
&gt;&gt;&gt; 
&gt;&gt;&gt; plotViewNode = plotWidget.mrmlPlotViewNode()
&gt;&gt;&gt; plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
&gt;&gt;&gt; 
&gt;&gt;&gt;
</code></pre>

---

## Post #5 by @lassoan (2021-02-18 13:15 UTC)

<aside class="quote no-group" data-username="BORIPHAT" data-post="4" data-topic="16027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<p><code>modelNode = getNode('VTK Output File')</code></p>
</blockquote>
</aside>
<p>Replace <code>VTK Output File</code> in the example with the actual name of your node.</p>

---

## Post #6 by @BORIPHAT (2021-02-19 05:51 UTC)

<p>I replace the VTK output File follow your recommendation and It shows the message. Could you please give me some advice again? Thank you very much for your kindness.</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Sep 30 2020, 16:13:32) [MSC v.1924 64 bit (AMD64)] on win32
&gt;&gt;&gt; modelNode = getNode('VTK Output File_6-0')distanceArrayName = "Signed"# Get distances from point dataimport numpy as npdistances = vtk.util.numpy_support.vtk_to_numpy(modelNode.GetPolyData().GetPointData().GetArray(distanceArrayName))# Print basic statsprint("Minimum distance: %f" % min(distances))print("Maximum distance: %f" % max(distances))print("Mean distance: %f" % np.mean(distances))# Compute histogramhistogram = np.histogram(distances, bins=100)# Save results to a new table nodetableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", modelNode.GetName() + " histogram")updateTableFromArray(tableNode, histogram)tableNode.GetTable().GetColumn(0).SetName("Count")tableNode.GetTable().GetColumn(1).SetName("Intensity")# Create plotplotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())plotDataNode.SetXColumnName("Intensity")plotDataNode.SetYColumnName("Count")plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())plotChartNode.SetAttribute("Type", "Bar") # delete this line for line plot# Show plot in layoutlayoutManager = slicer.app.layoutManager()layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)plotWidget = layoutManager.plotWidget(0)plotViewNode = plotWidget.mrmlPlotViewNode()plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
  File "&lt;console&gt;", line 1
    modelNode = getNode('VTK Output File_6-0')distanceArrayName = "Signed"# Get distances from point dataimport numpy as npdistances = vtk.util.numpy_support.vtk_to_numpy(modelNode.GetPolyData().GetPointData().GetArray(distanceArrayName))# Print basic statsprint("Minimum distance: %f" % min(distances))print("Maximum distance: %f" % max(distances))print("Mean distance: %f" % np.mean(distances))# Compute histogramhistogram = np.histogram(distances, bins=100)# Save results to a new table nodetableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", modelNode.GetName() + " histogram")updateTableFromArray(tableNode, histogram)tableNode.GetTable().GetColumn(0).SetName("Count")tableNode.GetTable().GetColumn(1).SetName("Intensity")# Create plotplotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())plotDataNode.SetXColumnName("Intensity")plotDataNode.SetYColumnName("Count")plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())plotChartNode.SetAttribute("Type", "Bar") # delete this line for line plot# Show plot in layoutlayoutManager = slicer.app.layoutManager()layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)plotWidget = layoutManager.plotWidget(0)plotViewNode = plotWidget.mrmlPlotViewNode()plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
                                                              ^
SyntaxError: invalid syntax
&gt;&gt;&gt;
</code></pre>

---

## Post #7 by @lassoan (2021-04-18 19:32 UTC)

<p>It seems that you have copied the text from somewhere so that the line breaks got lost and everything got into a single line. Use a programming editor, such as Visual Studio Code, for editing code snippets - it usually handles end-of-line character differences well.</p>

---
