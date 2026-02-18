# How to Trigger an Event on Left-Click When Mouse Hovers Over a CurveNode?

**Topic ID**: 41209
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/how-to-trigger-an-event-on-left-click-when-mouse-hovers-over-a-curvenode/41209

---

## Post #1 by @park (2025-01-22 06:13 UTC)

<p>Hi all,</p>
<p>I have a MarkupsCurveNode and noticed that in the Slice view, the mouse cursor changes to a hand icon when hovering over the curve line. I would like to enhance this behavior with two specific features:</p>
<p><strong>Trigger Event on Left-Click During Mouse Hover</strong></p>
<ul>
<li>
<p>When the mouse hovers over the MarkupsCurveNode line and the cursor changes to a hand icon, I want to allow the user to left-click the line.</p>
</li>
<li>
<p>Upon clicking, the closest control point to the clicked position should be identified and moved to the mouse position. I have identified the GetClosestCurvePointIndexToPositionWorld function in CurveNode as useful for this purpose.</p>
</li>
<li>
<p><strong>Could you guide me on how to trigger an event when the cursor changes to a hand icon and the user left-clicks on the curve line?</strong></p>
</li>
</ul>
<p><strong>Limit Cursor Change Range in Slice View</strong></p>
<ul>
<li>
<p>Currently, the cursor changes to a hand icon whenever the mouse hovers over the MarkupsCurveNode line.</p>
</li>
<li>
<p><strong>I would like to restrict this behavior to a specific distance or region in the Slice view. For example, the cursor should only change when the mouse is within a defined range of the line</strong>.</p>
</li>
</ul>
<p>I would appreciate any guidance or code examples on implementing these features.<br>
Thank you for your time and support.</p>

---
