# Create Parallel Coordinates Chart

**Topic ID**: 27995
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/create-parallel-coordinates-chart/27995

---

## Post #1 by @spyridon97 (2023-02-22 22:30 UTC)

<p>Hello!</p>
<p>I would like to know how i can create Parallel Coordinates chat?</p>
<p>i have some paths that have various metrics and for each metrics i save the min.max in a column of a table, which i connect to a vtkMRMLTableNode.</p>
<p>What do i need to do afterwards to create a Parallel Coordinates Chart?</p>

---

## Post #2 by @jcfr (2023-02-22 23:36 UTC)

<p>The plot type currently supported in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/plots.html">Plots module</a> are:</p>
<ul>
<li><code>line</code></li>
<li><code>bar</code></li>
<li><code>scatter</code></li>
<li><code>scatter-bar</code></li>
</ul>
<p>It could be extended to also include <code>parallel-coordinates</code> by leveraging the <code>vtkPlotParallelCoordinates</code> VTK class.</p>
<p>If you would like to help improve the code base, we can provide additional guidance.</p>
<p>As a starting point, you could look at <a href="https://github.com/Slicer/Slicer/blob/4f3d97c612b417cb8fe1c5688910f71d23a35852/Libs/MRML/Widgets/qMRMLPlotView.cxx#L238">qMRMLPlotViewPrivate::updatePlotFromPlotSeriesNode</a></p>
<p>References:</p>
<ul>
<li><a href="https://vtk.org/doc/nightly/html/classvtkPlotParallelCoordinates.html">https://vtk.org/doc/nightly/html/classvtkPlotParallelCoordinates.html</a></li>
<li><a href="https://kitware.github.io/vtk-examples/site/Cxx/Plotting/ParallelCoordinates/">https://kitware.github.io/vtk-examples/site/Cxx/Plotting/ParallelCoordinates/</a></li>
</ul>

---

## Post #3 by @spyridon97 (2023-03-06 21:29 UTC)

<p>Thanks for the answer <a class="mention" href="/u/jcfr">@jcfr</a>. I will work on it an submit a PR on Slicer’s Github.</p>

---

## Post #4 by @spyridon97 (2023-03-06 23:09 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Could i change the API of the following in the ctk library?</p>
<pre><code class="lang-auto">class CTK_VISUALIZATION_VTK_WIDGETS_EXPORT ctkVTKChartView : public ctkVTKOpenGLNativeWidget
{
  Q_INVOKABLE vtkChartXY* chart()const;
</code></pre>
<p>chart() to return a vtkChart object instead of vtkChartXY?<br>
I wanna do that because i need vtkChartParallelCoordinates instead of vtkChartXY.<br>
Also this will enable us to be able to add other subclasses of vtkChart such as, vtkChartBox, vtkChartPie. vtkHistogram2D.</p>

---

## Post #5 by @lassoan (2023-03-09 05:55 UTC)

<p>Adding support for more chart types would be great!</p>
<p>Adding an API to get/set vtkChart* is certainly necessary for this, but simply changing the return type would be a breaking change (could cause compilation errors) that would be nice to avoid. For example we could simply add a new method (<code>abstractChart()</code>, <code>generalChart()</code>, …).</p>
<p>We would need to see all the necessary API changes for making a final decision on whether we should make any breaking changes.</p>

---
