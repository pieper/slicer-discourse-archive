---
topic_id: 12564
title: "Selecting And Interacting With Points In Plot"
date: 2020-07-15
url: https://discourse.slicer.org/t/12564
---

# Selecting and interacting with points in plot

**Topic ID**: 12564
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/selecting-and-interacting-with-points-in-plot/12564

---

## Post #1 by @sthirumal (2020-07-15 21:49 UTC)

<p>For my scatter plots in Slicer, I am using the interaction mode “select points” in order to select specific points on the plot. Once I’ve selected my points, however, I’m unsure how exactly to use my selection. I’ve used:</p>
<blockquote>
<p>plotView.connect(“dataSelected(vtkStringArray*, vtkCollection*)”, self.onDataSelected)</p>
</blockquote>
<p>but I’m not sure how to actually extract the data of the points I’ve selected from that. I haven’t been able to find documentation on what attributes can be used. I’d like to ultimately be able to create a new table and plot using just the data points from my selection.</p>

---

## Post #2 by @lassoan (2020-07-16 02:54 UTC)

<p>I’ve added an example of how to get selected point IDs in Python: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots#Signals">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots#Signals</a></p>

---
