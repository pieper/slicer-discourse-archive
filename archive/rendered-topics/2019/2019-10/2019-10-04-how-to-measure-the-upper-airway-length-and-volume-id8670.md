---
topic_id: 8670
title: "How To Measure The Upper Airway Length And Volume"
date: 2019-10-04
url: https://discourse.slicer.org/t/8670
---

# How to measure the upper airway length and volume?

**Topic ID**: 8670
**Date**: 2019-10-04
**URL**: https://discourse.slicer.org/t/how-to-measure-the-upper-airway-length-and-volume/8670

---

## Post #1 by @kwichuda (2019-10-04 04:34 UTC)

<p>I want to measure the upper airway (oropharynx) but I don’t know how to measure. How to calculate the airway length and volume from 3D slicer.</p>

---

## Post #2 by @Amine (2019-10-06 02:47 UTC)

<p>To calculate the volume you will need to segment it first, you can find many tutorials online, then you use Segmentstatistics module to get the volume of your segment.<br>
As for the lenght if it’s linear use the ruler tool and if it’s a curve use the curve tool (available in the Nightly version and use this script to get its lenght in mm (after renaming the curve adequately):</p>
<pre><code>curve = getNode("MarkupsCurve")
curve.GetCurveLengthWorld()</code></pre>

---
