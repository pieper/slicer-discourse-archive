# Stairs line style, vertical lines in charts/plots

**Topic ID**: 1507
**Date**: 2017-11-22
**URL**: https://discourse.slicer.org/t/stairs-line-style-vertical-lines-in-charts-plots/1507

---

## Post #1 by @mschumaker (2017-11-22 20:05 UTC)

<p>I’d like to request “stairs” as a chart and/or plot type. The Step Chart in jqPlot would be a good starting point:<br>
<a href="http://www.jqplot.com/examples/step-charts.php" class="onebox" target="_blank" rel="noopener nofollow ugc">http://www.jqplot.com/examples/step-charts.php</a><br>
The plot creation system Grace (either Qtgrace or xmgrace) has options for “left stairs” and “right stairs”, depending if the x-axis value is to the right or left of the flat portion. Ideally, I’d like to see those options replicated. The reason for this is to make it possible to display histograms well. Bar charts don’t work, because the sides of the bars don’t meet.</p>
<p>I’d also like to request the ability to place vertical lines as markers in charts and/or plots. My intention is to use a slider widget to move the vertical lines on the chart.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2017-11-22 20:54 UTC)

<p>Hi Michael -</p>
<p>I don’t think anyone is actively working on the jqplot based plotting in Slicer right now.  In general features from jqpolot are mapped pretty directly, so if you don’t mind a little a little C++ and javascript it might be a very mechanical translation to make this work (exposing some features by following the pattern of the existing code).</p>
<p>But as described here [1] slicer also supports vtkPlots [2] which may have better support for what you are looking for.</p>
<p>Not sure what will work best for you.</p>
<p>Cheers,<br>
Steve</p>
<p>[1] <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_difference_between_Slicer_Plot_and_Chart_.3F">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_difference_between_Slicer_Plot_and_Chart_.3F</a></p>
<p>[2] <a href="https://www.vtk.org/features-2d-plots-and-charts/">https://www.vtk.org/features-2d-plots-and-charts/</a></p>

---

## Post #3 by @mschumaker (2017-11-22 22:13 UTC)

<p>Thanks, I’ll investigate this.</p>

---
