---
topic_id: 26761
title: "Closed Curves Centroid And Eplipse Long And Short Axis"
date: 2022-12-16
url: https://discourse.slicer.org/t/26761
---

# Closed curves - centroid and eplipse long and short axis

**Topic ID**: 26761
**Date**: 2022-12-16
**URL**: https://discourse.slicer.org/t/closed-curves-centroid-and-eplipse-long-and-short-axis/26761

---

## Post #1 by @Igor_S (2022-12-16 08:53 UTC)

<p>Hello,</p>
<p>I’ve drawn a closed curve on DICOM image. How do you calculate centroid of closed curve?<br>
Can you approximate ellipse from closed curve and calculate longest and short axis of this ellipse?<br>
I would like to implement this steps in a script, but haven’t found anything similar in script repository (there is and example of segment statistics, but I draw my closed curve on raw DICOM not on segmented images).</p>
<p>Thank you fro your help!</p>

---

## Post #2 by @pieper (2022-12-16 16:07 UTC)

<p>You can use something like <code>slicer.util.arrayFromMarkupsCurvePoints(slicer.util.getNode("CC"))</code> where “CC” is the default name of the closed curve.  With that array you can do whatever fitting and calculations you need.  Along with the examples in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">the script repository</a> you should have what you need.</p>

---

## Post #3 by @lassoan (2022-12-16 20:27 UTC)

<p>To fit an ellipse to the curve, you can slightly modify the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">sphere fitting example</a> in the script repository. Or, you can project all your curve points to a best-fit plane and then do a <a href="https://scipython.com/blog/direct-linear-least-squares-fitting-of-an-ellipse/">2D ellipse fitting</a>.</p>

---
