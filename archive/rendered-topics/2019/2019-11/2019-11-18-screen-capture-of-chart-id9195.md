---
topic_id: 9195
title: "Screen Capture Of Chart"
date: 2019-11-18
url: https://discourse.slicer.org/t/9195
---

# Screen capture of chart

**Topic ID**: 9195
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/screen-capture-of-chart/9195

---

## Post #1 by @dominicrushforth (2019-11-18 17:35 UTC)

<p>I want to screen capture a chart I’ve generated (using python) for inclusion in a report.</p>
<p>The following code works great for a 3D display…</p>
<p>view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(‘vtkMRMLViewNode1’))<br>
cap.captureImageFromView(view, latexFolder + ‘\’ + fileName + ‘3dImage.png’)</p>
<p>but I get just the same result if a chart is being displayed in the display window. I have tried looking for a chart specific view node such as ‘vtkMRMLPlotViewNodePlotView1’ but without any success .</p>
<p>Even with the screen capture widget I can’t figure out how to capture the chart on it’s own - although I can get the chart, with all the other windows, if I use the ‘capture all views’ option. The save button on the interactive chart also doesn’t seem to be working for me.</p>
<p>I am using the nightly build from 11/11 on windows.</p>

---

## Post #2 by @lassoan (2019-11-18 21:07 UTC)

<p>I’ve updated ScreenCapture module logic so that it can capture plot views. This script will work in Slicer rev28626 and later:</p>
<pre><code class="lang-python"># Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)
chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
chartNode.SetYAxisRangeAuto(False)
chartNode.SetYAxisRange(0, 4e5)

# Capture plot view
viewNodeID = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLPlotViewNode").GetID()
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))
cap.captureImageFromView(view,'c:/tmp/test.png')
</code></pre>

---

## Post #3 by @dominicrushforth (2019-11-22 15:20 UTC)

<p>That’s brilliant, thanks.</p>
<p>It’s now working exactly as I was expecting it to.</p>

---
