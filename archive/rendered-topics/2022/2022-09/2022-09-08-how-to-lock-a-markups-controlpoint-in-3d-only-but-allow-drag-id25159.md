---
topic_id: 25159
title: "How To Lock A Markups Controlpoint In 3D Only But Allow Drag"
date: 2022-09-08
url: https://discourse.slicer.org/t/25159
---

# How to lock a Markups ControlPoint in 3D only, but allow drag in 2D?

**Topic ID**: 25159
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/how-to-lock-a-markups-controlpoint-in-3d-only-but-allow-drag-in-2d/25159

---

## Post #1 by @sunshine (2022-09-08 15:02 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first extension module for annotation using module Markups.</p>
<p>Here is my case:<br>
I would like to add an annotation to a slicer showing in the Red slice (red window), and allow dragging the annotation (a ControlPoint) only in the 2D Red slice because dragging in 3D may go beyond the 2D red slice.</p>
<p>How can I lock the annotation (ControlPoint) only in 3D, but still allow dragging in 2D red slice?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2022-09-08 15:49 UTC)

<p>There are several ways to achieve this, depending on what behavior you would like exactly.<br>
Based on what you describe, it seems that you don’t want to lock the control point, just want to keep it on the slice. To do this, you can enable Markups module → Display → Advanced → 3D Display → Placement mode → snap to visible surface.</p>

---

## Post #3 by @sunshine (2022-09-08 16:08 UTC)

<p>Hi Andras,</p>
<p>Thank you so much for your reply!</p>
<p>I just tried following your instructions. However, the setting by default is “snap to visible surface”, and I may still accidentally move the ControlPoint from 3D scene, which means I may accidentally move the ControlPoint out of the 2D red scene.</p>
<p>Could you help please?</p>

---

## Post #4 by @lassoan (2022-09-08 16:31 UTC)

<p>If you show the slice view in 3D (by clicking the eye icon the the slice view’s controller at the top) then the point will remain on the slice view.</p>
<p>You can change left-click-and-drag to move a control point to Alt + left-click-and-drag in the 3D view by copy pasting this code snippet into the Python console:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
markupsDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLMarkupsDisplayableManager')

markupsDisplayNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsDisplayNode")
for markupsDisplayNode in markupsDisplayNodes:
    markupsWidget = markupsDisplayableManager.GetWidget(markupsDisplayNode)
    # Remove old mapping from left-click-and-drag
    markupsWidget.SetEventTranslationClickAndDrag(markupsWidget.WidgetStateOnWidget, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier,
        markupsWidget.WidgetStateTranslateControlPoint, vtk.vtkWidgetEvent.NoEvent, vtk.vtkWidgetEvent.NoEvent)
    # Keep responding to left-click event (for this we need to process left button press/release events)
    markupsWidget.SetEventTranslation(markupsWidget.WidgetStateOnWidget, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier, markupsWidget.WidgetEventReserved)
    markupsWidget.SetEventTranslation(markupsWidget.WidgetStateOnWidget, vtk.vtkCommand.LeftButtonReleaseEvent, vtk.vtkEvent.NoModifier, markupsWidget.WidgetEventReserved)
    # Make Alt + left-click-and-drag move a control point
    markupsWidget.SetEventTranslationClickAndDrag(markupsWidget.WidgetStateOnWidget, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.AltModifier,
        markupsWidget.WidgetStateTranslateControlPoint, markupsWidget.WidgetEventControlPointMoveStart, markupsWidget.WidgetEventControlPointMoveEnd)
</code></pre>

---
