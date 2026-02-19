---
topic_id: 12435
title: "How Via Python To Enable Data Labels On In Bar Chart"
date: 2020-07-08
url: https://discourse.slicer.org/t/12435
---

# How, via python, to enable "data labels" on in bar-chart?

**Topic ID**: 12435
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/how-via-python-to-enable-data-labels-on-in-bar-chart/12435

---

## Post #1 by @aiden.zhu (2020-07-08 10:39 UTC)

<p>Hi all,<br>
I am trying to have a bar chart using:<br>
ln = slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLLayoutNode’)<br>
ln.SetViewArrangement(24)</p>
<pre><code># Get the first ChartView node
cvn = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLChartViewNode')
# Create another data array
dn5 = slicer.mrmlScene.AddNode(slicer.vtkMRMLDoubleArrayNode())
a = dn5.GetArray()

a.SetNumberOfTuples(4)
a.SetComponent(0, 0, 6)
a.SetComponent(0, 1, 32)
a.SetComponent(1, 0, 3)
a.SetComponent(1, 1, 12)
a.SetComponent(2, 0, 4)
a.SetComponent(2, 1, 20)
a.SetComponent(3, 0, 5)
a.SetComponent(3, 1, 6)


# Create another ChartNode
cn = slicer.mrmlScene.AddNode(slicer.vtkMRMLChartNode())

# Add data to the chart
cn.AddArray('Volumes', dn5.GetID())

# Configure properties of the Chart
cn.SetProperty('default', 'title', 'A chart with labels')
cn.SetProperty('default', 'xAxisLabel', 'structure')
cn.SetProperty('default', 'xAxisType', 'categorical')
cn.SetProperty('default', 'yAxisLabel', 'size (cm)')
cn.SetProperty('default', 'type', 'Bar');
cn.SetProperty('Volumes', 'lookupTable', slicer.util.getNode('GenericAnatomyColors').GetID() )

# Set the chart to display
cvn.SetChartNodeID(cn.GetID())
self.delayDisplay('A chart with labels')
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d9328e418d1078d6dcddfea43bc41dbd43410bd.png" alt="image" data-base62-sha1="fDlkCjmj8HGzpNLdOCGTxDyUmO9" width="401" height="463"><br>
So how to enable those “data labels” in the bar circled in red?<br>
Thanks a lot,<br>
Aiden</p>

---

## Post #2 by @lassoan (2020-07-08 13:09 UTC)

<p>Can you show these labels using Slicer GUI?<br>
Can you show them using VTK API?</p>

---
