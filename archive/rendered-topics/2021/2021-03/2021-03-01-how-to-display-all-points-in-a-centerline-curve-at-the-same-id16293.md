---
topic_id: 16293
title: "How To Display All Points In A Centerline Curve At The Same"
date: 2021-03-01
url: https://discourse.slicer.org/t/16293
---

# How to display all points in a centerline curve at the same time in sagittal view? And how to display them?

**Topic ID**: 16293
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/how-to-display-all-points-in-a-centerline-curve-at-the-same-time-in-sagittal-view-and-how-to-display-them/16293

---

## Post #1 by @akshay_pillai (2021-03-01 17:55 UTC)

<p>Operating system: windows 10<br>
This is a 2 part question:</p>
<ol>
<li>
<p>First, I want to display the points in a centerline curve at all times programmatically. So I have a centerline curve and it has n number of control points. I want to display all n control points on the centerline curve in the sagittal view. I can manually click on view and jump to control points using the markups module but I want to display them automatically (or display control points of curve at all times)through code.</p>
</li>
<li>
<p>Second, I am using the endoscopy module to go through using the centerline curve. Is there any way I can change the color of displayed centerline curve control points as I pass it in the endoscopy view on the 2d views.</p>
</li>
</ol>

---

## Post #2 by @lassoan (2021-03-01 18:04 UTC)

<aside class="quote no-group" data-username="akshay_pillai" data-post="1" data-topic="16293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>So I have a centerline curve and it has n number of control points. I want to display all n control points on the centerline curve in the sagittal view</p>
</blockquote>
</aside>
<p>You can make all control points appear in a slice view by enabling Markups module / Display / 2D Display / Projection visibility. If you want to show them in a selected view only then specify the view node (Display / Advanced / View).</p>
<aside class="quote no-group" data-username="akshay_pillai" data-post="1" data-topic="16293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar"> akshay_pillai:</div>
<blockquote>
<p>Second, I am using the endoscopy module to go through using the centerline curve. Is there any way I can change the color of displayed centerline curve control points as I pass it in the endoscopy view on the 2d views.</p>
</blockquote>
</aside>
<p>You can change the curve color using Markups module / Display / Advanced.</p>
<p>All these properties are also accessible in Python, via the display node of the curve node. You can get the display node by calling <code>curveNode-&gt;GetDisplayNode()</code>.</p>

---
