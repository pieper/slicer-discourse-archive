# How to change the background color of plot view

**Topic ID**: 28874
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/how-to-change-the-background-color-of-plot-view/28874

---

## Post #1 by @jay1987 (2023-04-13 02:05 UTC)

<p>my custom application has a dark color style , how to change the plot view background color to the dark color style<br>
the demo ui below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d3b0a6d473a1a001f6dc19112a6716e90522c46.png" alt="image" data-base62-sha1="diKTJuJJTBj9PPuhSX39LX92I0S" width="502" height="418"></p>

---

## Post #2 by @cpinter (2023-04-13 09:19 UTC)

<p>This worked for me:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
pw0 = lm.plotWidget(0)
pv = pw0.plotView()
ch = pv.chart()
bb = ch.GetBackgroundBrush()
bb.SetColor(0,0,128)
ch.SetBackgroundBrush(bb)
</code></pre>

---

## Post #3 by @jay1987 (2023-04-13 09:41 UTC)

<p>thank you cpinter<br>
this is the only code i find useful<br>
do you know how to change the color of the Coordinate axis?</p>

---

## Post #4 by @cpinter (2023-04-13 12:35 UTC)

<p>I’d look along the same lines. In the chart MRML node, the plot view (subclass of ctkVTKChartView), and the VTK chart class. If there is such a function in said classes use that, if there isn’t, then it is probably not supported.</p>

---

## Post #5 by @jay1987 (2023-04-13 12:36 UTC)

<p>thank you very much@cpinter</p>

---
