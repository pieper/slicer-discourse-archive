---
topic_id: 48176
title: "Best practices for more complex plots in Slicer?"
date: 2026-09-15
url: https://discourse.slicer.org/t/48176
last_bumped: 2026-09-16T22:54:05.400Z
---

# Best practices for more complex plots in Slicer?

**Topic ID**: 48176
**Date**: 2026-09-15
**URL**: https://discourse.slicer.org/t/best-practices-for-more-complex-plots-in-slicer/48176

---

## Post #1 by @mikebind (2026-09-15 22:12 UTC)

<p>The slicer.util.plot() infrastructure is pretty limited. It’s OK for basic viewing of data that is already in MRML tables, but clunky for other data and incapable of nicer data visualizations.  It would be really nice to be able to use or display more complex plots in Slicer or at least from Slicer.  However, whenever I try to find nice solutions (using matplotlib, seaborn, etc.) I run into problems.  The default backend in matplotlib crashes Slicer.  wxPython is heavy but does provide a functional (but poorly styled) interactive plot window… until you try to close the plot, which hangs and crashes Slicer. The best option I found in the forum is this suggestion using pyqtgraph <a href="https://discourse.slicer.org/t/pythonqt-properties-shadowing-methods/16992/15" class="inline-onebox">PythonQt properties shadowing methods - #15 by fbordignon</a> , but it appears like it might require a manual patch to PythonQt, and PySide2, which appears to no longer be compatible with Slicer’s python version (it requires &lt;3.10), so is not really an option any more in recent Slicer versions.  It seems likely that some options will become available when Slicer fully shifts to Qt6 (it seems like this hasn’t happened in 5.12, but I’m not sure I’m understanding the release notes).  In the meantime, what do people use?  It sounds possible to save static plots to image files and then stretch those across a qt widget.  Is that the best current option for more advanced plots in Slicer?</p>

---

## Post #2 by @pieper (2026-09-16 22:54 UTC)

<p>A couple ideas:</p>
<ul>
<li>
<p>For the reasons you pointed out, trying to force some of these python plotting packages into Slicer can lead to dependency clashes and random crashes.  Another option is to write out the data and plot independently in a subshell with a different python interpreter (being careful with the paths in the environment).  You can use the web server (and the exec endpoint) to get any data you need out of Slicer and make any changes you want to slicer in response to interactions with the plot.</p>
</li>
<li>
<p>But my personal preference is to use <a href="https://echarts.apache.org/en/index.html">Apache ECharts</a> with the qSlicerWebWidget.  Here’s a project page that describes it: <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/">https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/</a>.  You have to feel comfortable using python and javascript together (or comfortable asking Claude to do it).</p>
</li>
</ul>
<p>Also, regarding Qt6, yes, it should be working everywhere now, we just haven’t made releases for it yet.</p>

---
