---
topic_id: 12869
title: "How To Setup A Chart Range Of X Y Axies Via Python Scripts"
date: 2020-08-06
url: https://discourse.slicer.org/t/12869
---

# How to setup a chart range of X/Y axies, via python scripts?

**Topic ID**: 12869
**Date**: 2020-08-06
**URL**: https://discourse.slicer.org/t/how-to-setup-a-chart-range-of-x-y-axies-via-python-scripts/12869

---

## Post #1 by @aiden.zhu (2020-08-06 09:06 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0<br>
Expected behavior: change X/Y axes minimum and maximum in charts<br>
Actual behavior:</p>
<p>Hi all,<br>
I am still trying to use a Chart (slicer.vtkMRMLChartNode()) but I am stuck at the settings of its properties such as: how to reset up the minimum and maximum in a chart? Say, by default I have a range of x-axis from 8 to 10, now I would like to set it up as from 0 to 11.</p>
<p>Thanks a lot.</p>

---

## Post #2 by @aiden.zhu (2020-08-06 13:25 UTC)

<p>Hahha, forget about this:<br>
chartNode.SetYAxisRangeAuto(False)<br>
chartNode.SetYAxisRange(0, 4e5)</p>

---

## Post #3 by @lassoan (2020-08-06 13:48 UTC)

<p>Thanks for sharing the solution. You can find further information and examples here:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plotting">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plotting</a></li>
</ul>

---
