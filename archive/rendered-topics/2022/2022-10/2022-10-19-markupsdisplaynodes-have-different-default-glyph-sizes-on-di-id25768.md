---
topic_id: 25768
title: "Markupsdisplaynodes Have Different Default Glyph Sizes On Di"
date: 2022-10-19
url: https://discourse.slicer.org/t/25768
---

# MarkupsDisplayNodes have different default glyph sizes on different computers

**Topic ID**: 25768
**Date**: 2022-10-19
**URL**: https://discourse.slicer.org/t/markupsdisplaynodes-have-different-default-glyph-sizes-on-different-computers/25768

---

## Post #1 by @wrc (2022-10-19 02:48 UTC)

<p>Hello. When I am using<br>
vtkMRMLMarkupsCurveNode.CreateDefaultDisplayNodes()<br>
slicer.util.updateMarkupsControlPointsFromArray(vtkMRMLMarkupsCurveNode, Node)</p>
<p>The default glyph size is 1% on PC and 3% on Mac.<br>
It looks good on PC but too thick on Mac. I have to change it to 1% on Mac manually. I think they should have the same value. Thanks.</p>

---

## Post #2 by @lassoan (2022-10-19 04:56 UTC)

<p>This issue of different glyph sizes on HiDPI screens has been resolved some time ago. Can you still reproduce inconsistent sizes if you use the current Slicer version (Slicer-5.0.3 and latest Slicer-5.1.x)?</p>

---

## Post #3 by @wrc (2022-10-19 05:12 UTC)

<p>The version on both PC and Mac (with HiDPI screen) are 5.0.3. They have inconsistent sizes.</p>

---

## Post #4 by @lassoan (2022-10-19 05:18 UTC)

<p>If you load the same scene in both computers then the sizes should be the same (I don’t remember if it is relative to the application window or the screen size).</p>
<p>If you create a new markup then the default markup size is used, which may not be the same. The size is stored in application settings and you can set it in Markups module → Display → Save to Defaults.</p>

---
