# Custom axis values (vtkMRMLChartNode)

**Topic ID**: 2116
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/custom-axis-values-vtkmrmlchartnode/2116

---

## Post #1 by @fmarcano (2018-02-19 14:35 UTC)

<p>From python, is it possible to reverse the order of X axis (vtkMRMLChartNode, vtkMRMLChartViewNode object nodes) on a displayed chart? For example:<br>
original X axis view:    … -3   -2   -1   0    1    2    3 …<br>
required X axis view:    … 3    2    1   0   -1   -2   -3 …</p>

---

## Post #2 by @lassoan (2018-02-21 03:37 UTC)

<p>We don’t develop the old JavaScript-based plotting infrastructure anymore, but replacing it with VTK-based plots. It is faster and allows plotting directly from table nodes, and offers much more customization features.</p>
<p>I’ve just implemented today custom axis range, so you can have +3 on the left and -3 on the right side. This feature will be available in Slicer nightly version that you download tomorrow or later. See information and usage examples here:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume</a></li>
</ul>

---

## Post #3 by @fmarcano (2018-02-21 14:44 UTC)

<p>Thank you very much. I’ll follow your advice then  I’ll tell you how it went.</p>

---

## Post #4 by @fmarcano (2018-04-06 09:06 UTC)

<p>I’ve seen the plot example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a>, and neither there nor my own code examples, X axis values are shown properly.</p>
<p>For example, in the Nightly developer plot code figure, the table shows X values going from 0 to 7.5  in steps of 0.11 aprox., but in the chart points have a X value (abcise) having a step of 1. This means, i.e, point (0.110294, 0.993924)  becomes (1,0.993924) , which leads to misinterpretation of data.</p>
<p>Am I missing any function call in the code to show exact X axis values?</p>

---

## Post #5 by @lassoan (2018-04-06 13:47 UTC)

<p>Thanks for the feedback. I see that the example uses the default Line plot type, which uses sample index as X coordinates. You need to set the plot type using <code>SetPlotType</code> method to <code>slicer.vtkMRMLPlotSeriesNode.PlotTypeScatter</code> to see a scatter plot. I’ve updated the example code and screenshot.</p>

---
