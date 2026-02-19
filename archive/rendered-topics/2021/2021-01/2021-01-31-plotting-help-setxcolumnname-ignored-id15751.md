---
topic_id: 15751
title: "Plotting Help Setxcolumnname Ignored"
date: 2021-01-31
url: https://discourse.slicer.org/t/15751
---

# Plotting help? SetXColumnName ignored

**Topic ID**: 15751
**Date**: 2021-01-31
**URL**: https://discourse.slicer.org/t/plotting-help-setxcolumnname-ignored/15751

---

## Post #1 by @bloyl (2021-01-31 16:36 UTC)

<p>I am trying to work with slicer’s plotting nodes to use in an extension and I’m running into some issues</p>
<p>The main one is that calling <code>SetXColumnName('X')</code> on a <code>vtkMRMLPlotSeriesNode</code> seems to be ignored, and the x axis is always just the row index of the table.</p>
<p>here is the <a href="https://gist.github.com/bloyl/c3bf0dd584ed675c3e1d3e6c2129e1be" rel="noopener nofollow ugc">script</a> i’ve been testing with.</p>
<p>I would have expected the x axis to run from 1000-1100 as opposed to 0-100. calling <code>SetYColumnName</code> auto updates the Y values so the table seems correct.</p>
<p>Can you also point me to the api that shows how to turn on/set the x and y axis labels?</p>
<p>Thanks!<br>
Luke</p>

---

## Post #2 by @lassoan (2021-01-31 20:50 UTC)

<p>“X axis column” is only used by scatter plot types, such as “scatter” or “scatter bar”. If you just want to display labels for values in “Y axis column” then you can choose any string column as “Labels column”. To get familiar with how things work, you can get started with using Plots module GUI.</p>
<p>If you just need to plot a numpy array, you can use the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.plot"><code>slicer.util.plot</code></a> convenience function. For example:</p>
<pre><code class="lang-python">values = np.random.uniform(5, 25, [10,2])
chart = slicer.util.plot(values, xColumnIndex=0, columnNames=['x' ,'y'], title='My chart')
</code></pre>
<p>See more examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Slicer_plots_displayed_in_view_layout">here</a>.</p>

---
