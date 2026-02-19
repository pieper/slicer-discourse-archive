---
topic_id: 10245
title: "Cannot Store Multivolumeexplorer Chart To Svg"
date: 2020-02-13
url: https://discourse.slicer.org/t/10245
---

# Cannot store MultiVolumeExplorer chart to .svg

**Topic ID**: 10245
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/cannot-store-multivolumeexplorer-chart-to-svg/10245

---

## Post #1 by @nwschurink (2020-02-13 16:21 UTC)

<p>Operating system: Windows 7 Enterprise 64-bit (6.1, Build 7601)<br>
Slicer version: version 4.10.2 revision 28257 built 2019-05-22</p>
<p>Expected behavior:<br>
I am using the MultiVolumeExporer to extract a time intensity curve of a DCE MRI scan. To do this, I made a segmentation of the tumor and created a chart of the signal intensity over time.</p>
<p>There are actually 2 features that I would like.</p>
<ol>
<li>to access the raw extracted data values (i.e. the mean signal intensity over time)</li>
<li>to save the chart that was created as an SVG such that I can use it in full resolution.</li>
</ol>
<p>Actual behavior:</p>
<ol>
<li>the raw values are stored in a node that I am not able to access.</li>
<li>I am not able to save the chart other than saving it a snapshot.</li>
</ol>
<p>I found the following topic on exporting plots from slicer <a href="https://discourse.slicer.org/t/exporting-plots-from-slicer/5711" class="inline-onebox">Exporting plots from Slicer</a></p>
<p>Using the information there, combined with the information provided in this commit: <a href="https://github.com/Slicer/Slicer/commit/54ba5e0b4212b5cb477e478f552e86fa6eb7ac02" class="inline-onebox" rel="noopener nofollow ugc">ENH: add option to save plot contents as svg · Slicer/Slicer@54ba5e0 · GitHub</a></p>
<p>I tried to save the chart in the following manner:</p>
<blockquote>
<p>e = vtk.vtkGL2PSExporter()<br>
e.SetFileFormatToSVG()<br>
lm = slicer.app.layoutManager()<br>
e.SetRenderWindow(lm.plotWidget(1).plotView())<br>
e.SetFilePrefix(‘D:/pre’)<br>
e.Update()</p>
</blockquote>
<p>When I do this I get the following error message:<br>
“TypeError: SetRenderWindow argument 1: method requires a VTK object”</p>
<p>I understand from this that the plotView apparently isn’t a VTK object. However I have no clue about how to change this or why it did seem to work in the above mentioned topic on chart exporting.</p>
<p>Also I tried to use the saveAsSVG function that war implemented in the above mentioned commit, however it does not seem to be available in slicer 4.10.2. I tried to use the slicer nightly build instead, however the MultiVolumeExplorer in the nightly doesn’t work as expected and doesn’t provide a chart.</p>
<p>Can you help me out here?</p>

---

## Post #2 by @nwschurink (2020-02-14 10:45 UTC)

<p>Ah, okay I obviously don’t need the plotWidget but need to access the chartWidget and get it’s renderer.<br>
However unlike the sliceWidget, the chartWidget doesn’t have a lm.chartWidget(1).chartView().renderWindow()…</p>
<p>How do I access the renderer to pass it onto the exporter??</p>

---

## Post #3 by @nwschurink (2020-02-18 09:52 UTC)

<p>Ok, I didn’t know this but apparently you need to access the mrmlScene nodes and not the layoutManager nodes. I got the data out in the following manner:</p>
<pre><code># My goal is to get the datapoints from 'Chart_6'
n = slicer.mrmlScene.GetNodesByName('Chart_6')
for nn in n:
  print(nn) # Apparently only one node available

# Get the names of the data series in this node
for i in range(nn.GetArrayNames().GetNumberOfValues()):
  print(nn.GetArrayNames().GetValue(i))

# I want to have the series that is named 'tissue'
a_node_name = nn.GetArray('tissue')

a_MRML_node = slicer.mrmlScene.GetNodeByID(a_node_name)

a_vtk_node = a_MRML_node.GetArray()
data = [a_vtk_node.GetValue(e) for e in range(a_vtk_node.GetNumberOfValues())]
</code></pre>
<p>So I got the chart data which allows me to plot the graph myself. But still I think it should be possible to get the actual render itself. Can someone help me do this?</p>

---

## Post #4 by @lassoan (2020-02-18 13:53 UTC)

<p>You can get numpy array from a volume node using a single command: <code>slicer.util.arrayFromVolume</code>.</p>
<p>VTK plotting is extremely fast and allows rich interactions. VTK should be able to produce SVG plots, too, but probably it is simpler to just use matplotlib.</p>
<p>A complete example that gets voxels of an MRI volume as numpy array, computes histogram, draws a plot, saves as svg, and display it in a web view:</p>
<pre><code class="lang-python"># Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
volumeVoxels = slicer.util.arrayFromVolume(volumeNode)
histogram = np.histogram(volumeVoxels, bins=50)

# Make sure matplotlib is installed
try:
  import matplotlib
except ModuleNotFoundError:
  pip_install('matplotlib')
  import matplotlib

matplotlib.use('Agg')

# Show a plot using matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(histogram[1][1:], histogram[0].astype(float))
ax.grid(True)
ax.set_ylim((0, 4e5))
outputFilePath = slicer.app.temporaryPath+'/test.svg'
plt.savefig(outputFilePath)

# Show the saved svg file in a web view window
webView = slicer.qSlicerWebWidget()
webView.url = qt.QUrl().fromLocalFile(outputFilePath)
webView.show()
</code></pre>

---
