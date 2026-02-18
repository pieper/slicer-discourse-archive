# Projection of interpolated points on open curve markup

**Topic ID**: 22566
**Date**: 2022-03-17
**URL**: https://discourse.slicer.org/t/projection-of-interpolated-points-on-open-curve-markup/22566

---

## Post #1 by @rhodesdante22 (2022-03-17 15:33 UTC)

<p>I am developing a module where I use the open curve markups with spline interpolation to plot points. I have SetSliceProjection(True) so that the projected control points show up on the 2D slice viewers. However, I cannot find a means to get the whole curve (including the interpolated points between the control points) to project onto the slice viewer and create a smooth curve. Is there a simple way to achieve this effect? Thank you very much.</p>

---

## Post #2 by @rhodesdante22 (2022-03-23 19:09 UTC)

<p>Hi Slicer Support community,</p>
<p>Please let me know if there is any additional information I should post to receive guidance on this issue. I am new to the forum and want to make sure I provide adequate information so I can receive support!</p>
<p>Thank you very much.</p>

---

## Post #3 by @ebrahim (2022-03-23 19:54 UTC)

<p>There’s probably a better answer from someone who knows how the markups display manager works, but here’s a hacky and not great idea that I’ll throw out: resample the curve to produce lots of control points, and then adjust the display properties of the control points to make their display area cover the curve in a connected way.</p>

---

## Post #4 by @lassoan (2022-04-01 04:57 UTC)

<p>You can configure the fade-out distance of the curve in slice views (distance from slice at the curve starts to fade and distance at the curve completely disappears). If you set these distances to a large value (e.g., 1000mm) then the entire curve will be visible in the slice.</p>
<pre><code class="lang-python">curveNode.GetDisplayNode().SetLineColorFadingStart(1000.0)
curveNode.GetDisplayNode().SetLineColorFadingEnd(1001.0)
</code></pre>

---

## Post #5 by @rhodesdante22 (2022-04-02 21:40 UTC)

<p>Great, this is fantastic. Thank you both for the suggestions.</p>

---
