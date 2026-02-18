# Line widget text options

**Topic ID**: 12287
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/line-widget-text-options/12287

---

## Post #1 by @ungi (2020-06-30 06:37 UTC)

<p>I would like to customize the text displayed for line markups in the 3D viewer. It would be ideal to set any custom text, but if there was an option to only display the name of the node, that would be enough too. Currently, the length of the line is displayed after the node name, and I’m not sure how to hide only the distance. When the distance is important, I use a ruler. I think ruler and line look too similar now.<br>
Is there a way to customize markup text displayed in the views?</p>

---

## Post #2 by @lassoan (2020-06-30 12:27 UTC)

<p>Markups widgets now show the first measurement in their label. The plan is to make it configurable which measurment value(s) to display.</p>
<p>Ruler has several limitations and serious issues and will be removed soon.</p>

---

## Post #3 by @ungi (2020-06-30 15:30 UTC)

<p>That would be great. I tried to call RemoveAllMeasurements() on line markups, but it still displays the length. Additionally, when I set the text size to 0% on the line, I can still see the text as small as 2-3 pixels that pollute the view. I would replace the text with a fiducial label halfway between the line end-points. But if customizable text is coming soon, I’d rather wait for that.</p>

---
