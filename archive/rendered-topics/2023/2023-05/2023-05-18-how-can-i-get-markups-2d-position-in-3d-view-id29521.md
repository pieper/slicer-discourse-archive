# How can I get markup's 2D position in 3D view

**Topic ID**: 29521
**Date**: 2023-05-18
**URL**: https://discourse.slicer.org/t/how-can-i-get-markups-2d-position-in-3d-view/29521

---

## Post #1 by @nnzzll (2023-05-18 01:26 UTC)

<p>Is there a way to calculate the markup’s position in the 3D view? I mean the 2D position when capturing the 3D view into a 2D image, not the RAS coordinates.</p>

---

## Post #2 by @nnzzll (2023-05-18 04:00 UTC)

<p>For anyone who has the same question, I just figure it out.</p>
<p>First, get the <code>renderer</code> from the 3D view:</p>
<pre><code class="lang-auto">threeDWidget = slicer.app.layoutManager().threeDWidget(0)
threeDView = threeDWidget.threeDView()
renderWindow = threeDView.renderWindow()
renderer = renderWindow.GetRenderers().GetFirstRenderer() 
</code></pre>
<p>Then, set the markup’s homogeneous RAS position to renderer</p>
<pre><code class="lang-auto">worldPosition = [*markupNode.GetNthControlPointPosition(0), 1]
renderer.SetWorldPoint(worldPosition)
renderer.WorldToDisplay()
imagePosition = renderer.GetDisplayPoint()
</code></pre>
<p>Note that the projection is upsided-down, so we need another step to set up the right coordinates:</p>
<pre><code class="lang-auto">imagePosition[1] = threeDView.size.height() - imagePosition[1]
</code></pre>

---
