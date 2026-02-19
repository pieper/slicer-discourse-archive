---
topic_id: 42315
title: "Using Matplotlib For Voxel By Voxel Suv Plot"
date: 2025-03-26
url: https://discourse.slicer.org/t/42315
---

# Using matplotlib for voxel by voxel SUV plot

**Topic ID**: 42315
**Date**: 2025-03-26
**URL**: https://discourse.slicer.org/t/using-matplotlib-for-voxel-by-voxel-suv-plot/42315

---

## Post #1 by @CSalt (2025-03-26 14:27 UTC)

<p>I have a segmented PET scan for which I am trying to display voxel by voxel SUV data. I am using the Python console in Slicer and was able to code everything I need, but ran into the error:<br>
:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown</p>
<p>when I tried to use the command plt.show()<br>
Is is possible to generate plots like this in slicer? I am open to any other methods, I am just most familiar with matplotlib.</p>
<p>(aside, would this be easier to do with matlab?)</p>

---

## Post #2 by @lassoan (2025-03-26 14:47 UTC)

<p>For simple interactive plots, I would recommend Slicer’s built-in plotting infrastructure. See example here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#slicer-plots-displayed-in-view-layout" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>For more complex interactive plots you can use any of the web plotting toolkits.  This works, as you can access Slicer functions from JavaScript (by running Python code) and you can call JavaScript functions from Slicer. <a class="mention" href="/u/pieper">@pieper</a> has used this technique in some projects, probably you can find examples in his <a href="https://github.com/pieper">repositories on github</a>.</p>
<p>Matplotlib with the <code>agg</code> backend is still a simple option for generating static plots. For interactive plots, you can use other backends, but I’m not sure if it is worth the trouble.</p>
<p>Matlab’s cost is hard to justify considering the vast amount of free alternatives. Also, Matlab is just not popular in general (its <a href="https://www.tiobe.com/tiobe-index/">TIOBE popularity index</a> is around 1% and stagnating/declining in recent years), so if you want people to use your solution or eventually contribute to it then it is not a promising option.</p>

---

## Post #3 by @pieper (2025-03-26 16:15 UTC)

<p>Also, to show the voxelwise SUV you can make a scalar volume and set it in the foreground over the CT and then set a PET lookup table.  This will be more efficient than doing this in matplotlib.</p>
<p>If you really want to use matplotlib, then this approach should still work:</p>
<p><a href="https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality">https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality</a></p>
<p>(Almost 10 years old!).</p>
<p>For advanced plotting these days I have been experimenting with <a href="https://echarts.apache.org/en/index.html">Apache ECharts</a> in Slicer and it works well.  The examples I have are tied to some PHI so I can’t share but if there’s interest I could make some generic examples.</p>

---

## Post #4 by @pieper (2025-03-26 16:18 UTC)

<p>BTW, the animated demo of ECharts on their homepage is really cool.  I’ll be excited to use it next time I have some plotting to do.</p>

---
