---
topic_id: 6130
title: "Cannot Set Slice Intersection Thickness On Display Node"
date: 2019-03-13
url: https://discourse.slicer.org/t/6130
---

# Cannot set slice intersection thickness on display node

**Topic ID**: 6130
**Date**: 2019-03-13
**URL**: https://discourse.slicer.org/t/cannot-set-slice-intersection-thickness-on-display-node/6130

---

## Post #1 by @michalikthomas (2019-03-13 12:09 UTC)

<p>Hello,</p>
<p>I am trying to set slice intersection thickness of simple poly data line.</p>
<pre><code>modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(track)
model.GetDisplayNode().SetSliceIntersectionVisibility(True)
model.GetDisplayNode().SetSliceIntersectionThickness(10)
</code></pre>
<p>In the slice view, I can see line intersection with a slice as a small square (probably just one pixel). I expected the function <strong>SetSliceIntersectionThickness()</strong> will set this intersection “indicator” larger.</p>
<p>The same goal I tried to achieve via Models module GUI by setting <strong>Slice Display &gt; Line Width</strong> to 10px. After this, the result is still the same.</p>
<p>Am I checking the correct function for this, or this feature is just currently not working properly?</p>
<p>Slicer version: Slicer-4.10.1-win-amd64.exe</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82daa940d9dd17ec1ff222a78d4fb59bc7d23a31.jpeg" alt="New%20Project" data-base62-sha1="iFAy88c42IZgXO0w9lkkZhjq5eV" width="261" height="318"></p>

---

## Post #2 by @pieper (2019-03-13 12:25 UTC)

<p>The intersections will need a surface not just a line to control the thickness.  You should be able to use the curvemaker or similar method to make a surface from your line.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker</a></p>

---

## Post #3 by @lassoan (2019-03-13 12:34 UTC)

<p>You can use “Markups to Model” extension to convert your line to a tube model. You may also try Models / Display / Slice Display / Mode / Distance encoded projection to show a certain length of the line near the slice plane (you can specify coloring scheme and length of displayed part by editing the color node).</p>
<p>We have recently added support for curves to the nightly version. Currently, you can only create, displaty, edit, and delete them, but we’ll add many more features in the coming months (various projection options, coloring schemes, compute of metrics, reslice volume along the line, etc.). Let us know what features you would need.</p>

---

## Post #4 by @michalikthomas (2019-03-13 13:48 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> for your answers.</p>
<p>I ended up with using <strong>vtk.vtkTubeFilter</strong> to create needed surfaces.</p>

---
