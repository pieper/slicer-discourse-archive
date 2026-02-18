# Change MarkupsCurve color programmatically

**Topic ID**: 11978
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/change-markupscurve-color-programmatically/11978

---

## Post #1 by @RafaelPalomar (2020-06-10 10:49 UTC)

<p>Hello.</p>
<p>I’m trying to change the color of curve markups programmatically. The following snippet does not seem to work (color remains unchanged) and does not produce any error:</p>
<pre><code class="lang-auto">markupNode = getNode('MarkupsCurve')
displayNode = markupNode.GetDisplayNode()
displayNode.SetColor([0,0,0])
</code></pre>
<p>From the UI I can see that colors are managed through terminologies. Does this means that setting the color from the display node does not apply to this case? Any example on how to use terminologies in this context?</p>
<p>Thank you in advance.</p>
<p>Rafael.</p>

---

## Post #2 by @lassoan (2020-06-10 12:45 UTC)

<p>Markups have <code>Color</code> and <code>SelectedColor</code> properties. <code>SelectedColor</code> is used if all control points are in “selected” state, which is the default. So, in most cases you want to use <code>SetSelectedColor</code>.</p>

---

## Post #3 by @RafaelPalomar (2020-06-10 15:55 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, that solves the problem!</p>

---
