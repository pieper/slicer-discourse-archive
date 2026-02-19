---
topic_id: 24293
title: "Adding The Mouse Event To The Markup Does Not Take Effect"
date: 2022-07-13
url: https://discourse.slicer.org/t/24293
---

# Adding the mouse event to the markup does not take effect

**Topic ID**: 24293
**Date**: 2022-07-13
**URL**: https://discourse.slicer.org/t/adding-the-mouse-event-to-the-markup-does-not-take-effect/24293

---

## Post #1 by @1023185654 (2022-07-13 10:54 UTC)

<p>Operating system:18.04.1-Ubuntu<br>
Slicer version:Slicer-4.13.0<br>
Expected behavior:Add shortcut keys to the markup add curve node<br>
Actual behavior:There is no response after you customize the behavior according to the instructions</p>

---

## Post #2 by @lassoan (2022-07-13 10:57 UTC)

<p>Markups have changed a lot in recent years. If you use latest <code>main</code> documentation then you must use latest <code>main</code> Slicer version, which is currently 5.1 (not 4.13). If you find that any of the code snippets does not work even if you use the correct software version then let us know.</p>

---

## Post #3 by @1023185654 (2022-07-13 10:59 UTC)

<p>How can I generate a continuous markup controlpoint while dragging the mouse, When I set the left mouse click event to no event, I set the left mouse drag event, but when ENTERING slicer, clicking the left mouse button still generates a Markup node</p>
<pre><code class="lang-auto">markupsWidget.SetEventTranslation(markupsWidget.WidgetStateDefine, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier, vtk.vtkWidgetEvent.NoEvent)
        markupsWidget.SetEventTranslation(markupsWidget.WidgetStateDefine, vtk.vtkCommand.RightButtonPressEvent, vtk.vtkEvent.NoModifier, vtk.vtkWidgetEvent.NoEvent)
        markupsWidget.SetEventTranslationClickAndDrag(markupsWidget.WidgetStateDefine, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier, markupsWidget.WidgetStateTranslateControlPoint, markupsWidget.WidgetEventControlPointMoveStart, markupsWidget.WidgetEventControlPointMoveStart)
</code></pre>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---
