---
topic_id: 8379
title: "Single Point Placement For Vtkmrmlmarkupslinenode"
date: 2019-09-11
url: https://discourse.slicer.org/t/8379
---

# Single point placement for vtkMRMLMarkupsLineNode?

**Topic ID**: 8379
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/single-point-placement-for-vtkmrmlmarkupslinenode/8379

---

## Post #1 by @Greydon_Gilmore (2019-09-11 01:58 UTC)

<p>Hello,</p>
<p>I am wondering if it is possible to place one fiducial point at a time when using <code>MarkupsLineNode</code>. I would like the user to place one point, without having to place the second point to complete the line.</p>
<p>I’d like the line to be displayed following placement of the second fiducial. I am using the <code>MarkupsLineNode</code> to plot a planned trajectory.</p>
<p>I have tried applying the following to each fiducial point but it doesn’t seem to work:</p>
<pre><code class="lang-auto">self.Point = slicer.qSlicerMarkupsPlaceWidget()
self.Point.placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
</code></pre>
<p>Thanks!<br>
Greydon</p>

---

## Post #2 by @lassoan (2019-09-11 04:12 UTC)

<p>You can hide the line until you want to show it by calling <code>SetLineThickness(0.0)</code> on the markup’s display node.</p>
<p>One markup is a line, so forcing a single placement will deactivate place mode after the two line points are placed. To disable place mode after one point is placed, you can call <code>self.Poin.placeModeEnabled = False</code>.</p>
<p>Alternatively, you can use markup fiducial points to get user input (they can be placed one by one and they are not connected by a line) and when you have the two points, create a markup line using these point positions.</p>

---
