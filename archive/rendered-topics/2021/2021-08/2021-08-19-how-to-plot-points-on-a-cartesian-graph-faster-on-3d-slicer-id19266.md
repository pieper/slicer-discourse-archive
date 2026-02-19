---
topic_id: 19266
title: "How To Plot Points On A Cartesian Graph Faster On 3D Slicer"
date: 2021-08-19
url: https://discourse.slicer.org/t/19266
---

# How to plot points on a cartesian graph faster on 3D Slicer

**Topic ID**: 19266
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/how-to-plot-points-on-a-cartesian-graph-faster-on-3d-slicer/19266

---

## Post #1 by @armandanesh (2021-08-19 06:27 UTC)

<p>Hello,</p>
<p>As a part of my project, I need my graph on the interactive scene to update every 0.005 seconds. To do this, I used QTimer to recall the plot function every 0.005 seconds. To verify that it is, in fact, recalling this function every 0.005 seconds, I decided to print the time.clock() command at the end of the plot function, this allowing me to find the interval between each recall. What I found was that there was a lot of variability in regards to the time it took to recall the function, as some times the interval would be 0.02 seconds while other times it would be 0.001 seconds. I would need the interval to remain at 0.005 seconds or below, however. Would this be possible? Moreover, any tips on making the application plot faster in general? Because I would be fine if there was variability, so long as it is below 0.005 seconds. Thank you for your help in advance!</p>
<p>Arman</p>

---

## Post #2 by @pieper (2021-08-19 12:03 UTC)

<p>A couple suggestions:</p>
<ul>
<li>
<p>don’t use <code>print</code> to report the timing per-frame since that will introduce variability related to the logging system.  Instead, save timings to a pre-allocated array to minimize per-frame overhead.  If you save to a numpy array you can easily get mean, stddev, min, and max statistics.</p>
</li>
<li>
<p>write a simple stand-alone test that you can share here to use as the basis of discussions.  Perhaps even turn it into a Slicer test that can be contributed to the main repository so that it’s very easy for any developer to replicate.  This would also help ensure there are no graphing related regressions in the future.</p>
</li>
<li>
<p>use a profiler to identify where the time is being taken during your graphing</p>
</li>
</ul>

---

## Post #3 by @lassoan (2021-08-20 18:32 UTC)

<p>You don’t need to update the display at every 5ms. It would mean 200fps refresh rate.</p>
<p>Instead, you probably only want to <em>collect</em> data at a high sampling rate (potentially on a background thread, running at real-time priority) and display it on the GUI at the whatever frame rate is feasible (depending on your hardware you have and what software optimizations you implement based on <a class="mention" href="/u/pieper">@pieper</a>’s advice above).</p>
<p>Not that by default most systems limit rendering rate to the refresh rate of your monitor. You may be able to unlock this rendering/display rate synchronization in advanced settings of your GPU, but it will increase the overall load on your system and may introduce tearing.</p>

---

## Post #4 by @armandanesh (2021-08-24 22:10 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> for your help.</p>
<p>The current code I have for my project consists of the following:</p>
<pre><code>import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import numpy as np
import random as r

class GUI(ScriptedLoadableModule):
 def __init__(self,parent):
  ScriptedLoadableModule.__init__(self, parent)
  parent.title= "GUI"
  parent.categories = ["Research"]
  parent.dependencies = []
  parent.helpText = """Filler1"""
  parent.acknowledgementText = """Filler2"""
  self.parent = parent


elap = qt.QElapsedTimer()
elap.start()
x = []

class GUIWidget(ScriptedLoadableModuleWidget):
 def __init__(self, parent = None):
  if not parent:
   self.parent = slicer.qMRMLWidget()
   self.parent.setLayout(qt.QVBoxLayout())
   self.parent.setMRMLScene(slicer.mrmlScene)
  else:
   self.parent = parent

  self.layout = self.parent.layout()
  if not parent:
   self.setup()
   self.parent.show()

  self.timer = qt.QTimer()
  self.timer.setInterval(5)
  self.timer.connect('timeout()', self.Plot)
  self.timer.start()

  self.cle = qt.QTimer()
  self.cle.setInterval(3000)
  self.cle.connect('timeout()', self.clear)
  self.cle.start()

  self.pri = qt.QTimer()
  self.pri.setInterval(10000)
  self.pri.connect('timeout()', self.print)
  self.pri.start()

 def setup(self):
  self.layoutManager = slicer.app.layoutManager()
  self.layoutWithPlot = slicer.modules.plots.logic().GetLayoutWithPlot(self.layoutManager.layout)
  self.layoutManager.setLayout(self.layoutWithPlot)

 def Plot(self):
  self.tableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
  table = self.tableNode.GetTable()

  arrX = vtk.vtkFloatArray()
  arrX.SetName("X")
  table.AddColumn(arrX)
  arrY1 = vtk.vtkFloatArray()
  arrY1.SetName("Y")
  table.AddColumn(arrY1)
  plotSeriesNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", "Example")
  plotSeriesNode1.SetAndObserveTableNodeID(self.tableNode.GetID())
  plotSeriesNode1.SetXColumnName("X")
  plotSeriesNode1.SetYColumnName("Y")
  plotSeriesNode1.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeScatter)

  plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
  plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode1.GetID())
  plotChartNode.SetTitle('Catheter Cartesian')
  plotChartNode.SetXAxisTitle('X-Axis')
  plotChartNode.SetYAxisTitle('Y-Axis')

  plotWidget = self.layoutManager.plotWidget(0)
  plotViewNode = plotWidget.mrmlPlotViewNode()
  plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())

  xpos = []
  xpos.append(r.random())
  ypos = []
  ypos.append(r.random())

  Number = len(xpos)
  Range = np.arange(Number)


  table.SetNumberOfRows(Number)
  for i in Range:
   table.SetValue(i, 0, xpos[i])
   table.SetValue(i, 1, ypos[I])

  x.append(elap.elapsed())

 def clear(self):
  slicer.mrmlScene.Clear()
  self.tableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
  table = self.tableNode.GetTable()

  arrX = vtk.vtkFloatArray()
  arrX.SetName("X")
  table.AddColumn(arrX)
  arrY1 = vtk.vtkFloatArray()
  arrY1.SetName("Y")
  table.AddColumn(arrY1)

  plotSeriesNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", "Example")
  plotSeriesNode1.SetAndObserveTableNodeID(self.tableNode.GetID())
  plotSeriesNode1.SetXColumnName("X")
  plotSeriesNode1.SetYColumnName("Y")
  plotSeriesNode1.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeScatter)

  plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
  plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode1.GetID())
  plotChartNode.SetTitle('Catheter Cartesian')
  plotChartNode.SetXAxisTitle('X-Axis')
  plotChartNode.SetYAxisTitle('Y-Axis')

  plotWidget = self.layoutManager.plotWidget(0)
  plotViewNode = plotWidget.mrmlPlotViewNode()
  plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())

  xpos = []
  xpos.append(r.random())
  ypos = []
  ypos.append(r.random())
   
  Number = len(xpos)
  Range = np.arange(Number)

  table.SetNumberOfRows(Number)
  for i in Range:
   table.SetValue(i, 0, xpos[i])
   table.SetValue(i, 1, ypos[I])

  x.append(elap.elapsed())


 def print(self):
  print(x)
</code></pre>
<p>Would you have any suggestions regarding how I could change my code to better fit what I am trying to achieve (faster and consistent plotting)? Also, I added a clear function which refreshes every 3 seconds because I noticed that when I didn’t, the plot speed would gradually decrease with time. Also, I would prefer that we update the display every 5ms if possible.</p>
<p>Thank you in advance for your help.</p>
<p>Arman</p>

---

## Post #5 by @pieper (2021-08-25 17:18 UTC)

<p>What are the current results in terms of min, mean, max elapsed time?</p>
<p>Did you try running a profiler to see where time is being spent?</p>

---

## Post #6 by @lassoan (2021-08-26 04:45 UTC)

<aside class="quote no-group" data-username="armandanesh" data-post="4" data-topic="19266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/67e7ee/48.png" class="avatar"> armandanesh:</div>
<blockquote>
<p>Also, I would prefer that we update the display every 5ms if possible</p>
</blockquote>
</aside>
<p>There is no such thing as a 200FPS GUI refresh rate, because if you rendered the everything at this rate then the whole application non-responsive (as it would become busy with all the re-renderings and would not have any time to process any events). It seems that you are mixing up rendering with data collection.</p>
<p>Where does this desire for a 200FPS refresh rate comes from? Do you have some hardware device that can acquire samples at this rate? Does it device interface offers buffered access, so that you can transfer all the collected readings since the last readout all at once? If that’s the case then you could then run a tight data collection loop at 30-60FPS in a real-time-priority background thread, and would put the acquired data into a thread-safe buffer shared with the main thread. When a rendering is due then the main thread processes the data accumulated in the shared buffer and updates the display.</p>
<p>In all the code that is called dozens of time per second, you should avoid very expensive operations, such as creating new nodes or reallocating large buffers. You should preferably avoid all operations that may reallocate heap memory (to avoid memory fragmentation), but the best is to not guess, but use a profiler to point out what takes too long time.</p>
<p>I noticed that you included Python code. Implementing sustained, predictable real-time data collection and display is not what Python was designed for. You have very little control over small details (memory allocations, threading, etc.) that matter in such an extremely demanding application. You may find that you need to implement performance-critical parts in C++.</p>

---
