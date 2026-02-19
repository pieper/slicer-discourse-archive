---
topic_id: 44454
title: "Slicer Script Repository Module Name Logic Vs Slicer Module"
date: 2025-09-12
url: https://discourse.slicer.org/t/44454
---

# Slicer script repository: module_name.logic vs slicer.module_name.widgetRepresentation().self().logic() vs slicer.modules.logic()

**Topic ID**: 44454
**Date**: 2025-09-12
**URL**: https://discourse.slicer.org/t/slicer-script-repository-module-name-logic-vs-slicer-module-name-widgetrepresentation-self-logic-vs-slicer-modules-logic/44454

---

## Post #1 by @tas47 (2025-09-12 03:42 UTC)

<p>Slicer API explanation:</p>
<p>Hello all I have been trying to understand the Slicer API and I  am having a lot of trouble understanding exactly how the ecosystem works.</p>
<p>I want to specifically understand how the logic aspect of  modules works in Slicer.<br>
In the script repository, I have seen the logic() incorporated in 3 different ways:</p>
<p>Example 1:<br>
SegmentStatistics is often imported and accessed  like this:</p>
<pre><code class="lang-auto">import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic().Compute
</code></pre>
<p>However, I have seen other modules logic method accessed this way:<br>
Example 2:</p>
<pre><code class="lang-auto">slicer.modules.markups.logic().ExportControlPointsToCSV(markupsNode, "/path/to/MyControlPoints.csv")
</code></pre>
<p>so how come I cannot access  ComputeStatistics()  like this with the code below?</p>
<pre><code class="lang-auto">slicer.modules.segmentstatistics.logic()
</code></pre>
<p>I can also see that i can access ComputeStatistics() if I access it via widgetRepresentation<br>
Example 3:</p>
<pre><code class="lang-auto">slicer.modules.segmentstatistics.widgetRepresentation().self().logic.computeStatistics()
</code></pre>
<p>Overall what is the difference between the 3 ways? Which  one the correct way and the theory behind the code. I understand that widgetRepresentation handles the gui and by qt, but I cant wrap my head behind Slicer design pattern especially with all the vtk/qt bindings.<br>
Finally, whats the intuition  behind  accessing the self() in widget-representation from Slicer? Are the modules not already instantiated when slicer is loaded? I have seen this often used with segment editor example to access the different modes like pen, eraser and etc.</p>
<p>Thank you<br>
Tas</p>

---

## Post #2 by @lassoan (2025-09-13 15:14 UTC)

<p>Good question! To facilitate dynamic reloading, we don’t use <code>slicer.modules.segmentstatistics.logic()</code> in scripted modules. Instead, we usually let the widget create and own the logic in Python scripted modules. See more information in slide 11 in the <a href="https://training.slicer.org/#STC-DEV-101"> STC-DEV-101: Slicer Scripting and Module Development</a> tutorial.</p>

---

## Post #3 by @tas47 (2025-09-26 14:22 UTC)

<p>Thank you <span class="mention">@Iassoan</span><br>
Just  to make sure, if i want to access all the attributes and instance of logic modules, you always recommend accessing from the widget itself via <code>WidgetRepresenation()</code> instead of accessing it with  <code>slicer.modules.segmentstatistics</code> ?</p>

---

## Post #4 by @lassoan (2025-09-26 19:10 UTC)

<p>For a scripted module, you cannot reach module logic via the module object directly like <code>slicer.modules.segmentstatistics.logic()</code>, as this returns a placeholder object, not the real module logic object (that the widget instantiates and owns). This may change in the future, so the safest and most future-proof method is to use <code>slicer.util.getModuleLogic()</code> function.</p>

---

## Post #5 by @lassoan (2025-09-26 19:30 UTC)

<p>A small addition: <code>segStatLogic = SegmentStatistics.SegmentStatisticsLogic()</code> instantiates a new logic class. It does not access the logic class of the built-in module. This type of access is useful if you just want a temporary logic class that you use for some computations without affecting the state of the “Segment Statistics” module. You need to ensure that the logic is properly initialized. In many cases, no initialization is needed, but you can double-check by looking at how the module widget class does it.</p>

---
