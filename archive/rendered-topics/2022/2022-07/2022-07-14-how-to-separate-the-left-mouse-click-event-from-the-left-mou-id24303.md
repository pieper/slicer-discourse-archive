---
topic_id: 24303
title: "How To Separate The Left Mouse Click Event From The Left Mou"
date: 2022-07-14
url: https://discourse.slicer.org/t/24303
---

# How to separate the left mouse click event from the left mouse drag time when operating a Markup node

**Topic ID**: 24303
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/how-to-separate-the-left-mouse-click-event-from-the-left-mouse-drag-time-when-operating-a-markup-node/24303

---

## Post #1 by @1023185654 (2022-07-14 06:44 UTC)

<p>Operating system: unbuntu 18.04<br>
Slicer version: Slicer-4.13.0-2022-01-16-linux-amd64<br>
Expected behavior:add the control point when I press the left button,and Rotate the 3D model while holding and dragging the left mouse button<br>
Actual behavior:I set Leftbuttonpressevent to no event and SetEventTranslationClickAndDrag to add rotating 3d view event.but There is no effective on left button press event.</p>
<pre><code class="lang-auto">markupsWidget.SetEventTranslationClickAndDrag(markupsWidget.WidgetStateIdle, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier, markupsWidget.WidgetStateRotate, markupsWidget.WidgetEventRotateStart, markupsWidget.WidgetEventRotateEnd)
</code></pre>

---
