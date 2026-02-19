---
topic_id: 4025
title: "Using Slicer Plot View Signal"
date: 2018-09-08
url: https://discourse.slicer.org/t/4025
---

# Using Slicer plot view signal

**Topic ID**: 4025
**Date**: 2018-09-08
**URL**: https://discourse.slicer.org/t/using-slicer-plot-view-signal/4025

---

## Post #1 by @Mateo_Lopez (2018-09-08 00:16 UTC)

<p>Hello,</p>
<p>I am not used to coding python scripts for Slicer and I am wondering how I can use the dataSelected signal provided by PlotViews.</p>
<p>I am creating some plots to visualize PCA data and I would like to detect when a point is selected on my projection plot.</p>
<p>I tried the following code to generate all the nodes I need and tried to create a  qMRMLPlotView object to connect the dataSelected signal but it doesn’t seem to be working.</p>
<p>Do you know a proper way to use this signal?</p>
<p>code:</p>
<pre><code>def generate2DVisualisationNodes(self):
    #clean previously created nodes
    self.delete2DVisualisationNodes()

    #generate PlotChartNodes to visualize the variance plot and the Projection plot
    variancePlotChartNode = self.generateVariancePlot()
    projectionPlotChartNode = self.generateProjectionPlot()

    # Switch to a layout that contains a plot view to create a plot widget
    layoutManager = slicer.app.layoutManager()
    layoutWithPlot = slicer.modules.plots.logic().GetLayoutWithPlot(layoutManager.layout)
    layoutManager.setLayout(layoutWithPlot)

    # Select chart in plot view
    plotWidget = layoutManager.plotWidget(0)
    plotViewNode = plotWidget.mrmlPlotViewNode()

    plotViewNode.SetPlotChartNodeID(projectionPlotChartNode.GetID())
    plotViewNode.SetPlotChartNodeID(variancePlotChartNode.GetID())

    plotView = slicer.qMRMLPlotView()
    plotView.setMRMLPlotViewNode(plotViewNode)
    plotView.connect("dataSelected(vtkStringArray, vtkCollection)", self.onDataSelected)

def generateProjectionPlot(self):
    projectionTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","PCA projection table")
    table = projectionTableNode.GetTable()

    pc1=vtk.vtkFloatArray()
    pc2=vtk.vtkFloatArray()

    pc1.SetName("pc1")
    pc2.SetName("pc2")

    table.AddColumn(pc1)
    table.AddColumn(pc2)

    #Projection plot serie
    projectionPlotSeries = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", "PCA projection")
    projectionPlotSeries.SetAndObserveTableNodeID(projectionTableNode.GetID())
    projectionPlotSeries.SetXColumnName("pc1")
    projectionPlotSeries.SetYColumnName("pc2")
    projectionPlotSeries.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeScatter)
    projectionPlotSeries.SetLineStyle(slicer.vtkMRMLPlotSeriesNode.LineStyleNone)
    projectionPlotSeries.SetUniqueColor()

    # Create projection plot chart node
    projectionPlotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode","PCA projection plot chart")
       projectionPlotChartNode.AddAndObservePlotSeriesNodeID(projectionPlotSeries.GetID())
    projectionPlotChartNode.SetTitle('Population projection')
    projectionPlotChartNode.SetXAxisTitle('pc1')
    projectionPlotChartNode.SetYAxisTitle('pc2')

    return projectionPlotChartNode
</code></pre>
<p>Thank you!</p>
<p>Mateo</p>

---

## Post #2 by @lassoan (2018-09-08 02:01 UTC)

<p>The correct syntax of creating the connection is:</p>
<pre><code>plotView.connect("dataSelected(vtkStringArray*, vtkCollection*)", self.onDataSelected)
</code></pre>
<p>If you try to connect a non-existing signal then you can see an error message in the application log.</p>

---

## Post #3 by @Mateo_Lopez (2018-09-08 21:51 UTC)

<p>Thank you for this quick answer, I have no more error in the application log but it’s still not working. Am I connecting the signal of the right object?<br>
I wonder if there is a way to directly get the qMRMLPlotView object of Slicer instead of creating one.</p>

---

## Post #4 by @Mateo_Lopez (2018-09-08 22:25 UTC)

<p>Now it’s working, I was not creating the qMRMLPlotView object the right way. using the plotWidget object to create it solved my problem.</p>
<p>Thank you for your help!</p>
<p>here is the code that worked for me</p>
<pre><code>    plotWidget = layoutManager.plotWidget(0)
    plotViewNode = plotWidget.mrmlPlotViewNode()

    plotViewNode.SetPlotChartNodeID(projectionPlotChartNode.GetID())
    plotViewNode.SetPlotChartNodeID(variancePlotChartNode.GetID())

    plotView = plotWidget.plotView()
    plotView.connect("dataSelected(vtkStringArray*, vtkCollection*)", self.onDataSelected)</code></pre>

---

## Post #5 by @Davide_Punzo (2018-09-10 09:34 UTC)

<p>Hi Mateo,</p>
<p>It will be great if you can add the example as documentation here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></p>
<p>in the <strong>Signal</strong> section</p>
<p>or/and</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>
<p>Thanks in advance,</p>
<p>Cheers,<br>
Davide.</p>

---

## Post #6 by @Mateo_Lopez (2018-09-10 14:03 UTC)

<p>Hi Davide,</p>
<p>Unfortunately, I don’t have the rights to modify the Slicer wiki, I will try to send a request to do so</p>
<p>Cheers,<br>
Mateo</p>

---

## Post #7 by @Davide_Punzo (2018-09-10 22:39 UTC)

<p>Ok thanks! In the case you don’t manage to get the rights, I can copy and paste the example script (if for you it is ok).</p>

---

## Post #8 by @Mateo_Lopez (2018-09-11 16:27 UTC)

<p>Sure, I have no problem with that, I let you do it, I think it will be easier like this.</p>
<p>Also, I find out that it could be useful to disconnect the signal before connecting it, I had Slicer crashes while reloading the module and using the signal.</p>

---
