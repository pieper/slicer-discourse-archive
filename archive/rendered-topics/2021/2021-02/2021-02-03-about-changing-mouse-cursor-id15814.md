# About changing mouse cursor

**Topic ID**: 15814
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/about-changing-mouse-cursor/15814

---

## Post #1 by @forfullstack (2021-02-03 14:21 UTC)

<p>I want to change shape of mouse cursor when mouse crosses MPR lines<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b485012b501dc1c6e408f7bd6ed04550bf141633.png" alt="Capture" data-base62-sha1="pKWU9kafFQQulWjm7Lmuqoog8iT" width="269" height="201"><br>
I’ve added function in the vtkMRMLSliceIntersectionWidget.cxx to check crossing with MPR lines.<br>
But how can I change cursor in that time? I think I have to add setCursor to the qMRMLSliceView.cxx.<br>
How can I send event from the vtkMRML to the qMRML? Is there anything sample doing such an action?</p>
<p>Thanks.</p>

---

## Post #2 by @forfullstack (2021-02-03 14:32 UTC)

<p>Just I found a way to do it. Hope it will help everyone who wants to implement similar logic.<br>
// Sender<br>
vtkMRMLSliceIntersectionWidget::MyFunc()<br>
{<br>
crosshairNode-&gt;InvokeEvent(vtkMRMLCrosshairNode::MyEvent, nullptr);<br>
}</p>
<p>// Handler<br>
void qMRMLSliceControllerWidgetPrivate::setAndObserveCrosshairNode()<br>
{<br>
this-&gt;qvtkReconnect(nullptr, crosshairNode, vtkMRMLCrosshairNode::MyEvent,<br>
q, SLOT(MyHandler()));<br>
}</p>

---

## Post #3 by @lassoan (2021-02-03 15:38 UTC)

<p>It is great that you are adding this feature. We have created the slice intersection widget to allow exactly this and also to make it easier to customize the behavior (e.g., drag-and-drop slice intersection line to move/rotate slice intersection instead of Shift+MouseMove and Ctrl+Alt+Left-click-and-drag).</p>
<p>To change the mouse cursor, please update the displayable manager’s <a><code>GetMouseCursor()</code></a> method. Since the crosshair is already a widget, all you need to do is to ask the widget what is the desired cursor shape, similarly how it is done in <a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Modules/Loadable/Markups/MRMLDM/vtkMRMLMarkupsDisplayableManager.cxx#L925-L931">markups displayable manager</a>.</p>

---

## Post #4 by @forfullstack (2021-02-05 03:11 UTC)

<p>Hello Andras,<br>
Thanks for your reply.<br>
Just I was become known there already exists virtual function named GetMouseCursor().<br>
vtkMRMLAbstractDisplayableManager and his child class vtkMRMLMarkupsDisplayableManager have this function.<br>
Also vtkMRMLAbstractWidget and his child class vtkSlicerMarkupsWidget have that one.<br>
I added logging function in the above all GetMouseCursor() and found only vtkMRMLAbstractDisplayableManager’s GetMouseCursor() is working.<br>
I think displayable manager’s GetMouseCursor() should call its widget’s GetMouseCursor() then my logic is able to work.<br>
Unfortunately vtkMRMLAbstractDisplayableManager does not have widget member as vtkMRMLMarkupsDisplayableManager has LastActiveWidget.<br>
So currently there’s no way to call widget’s GetMouseCursor() from the displayable manager.</p>

---

## Post #5 by @lassoan (2021-02-05 03:17 UTC)

<aside class="quote no-group" data-username="forfullstack" data-post="4" data-topic="15814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/forfullstack/48/9751_2.png" class="avatar"> forfullstack:</div>
<blockquote>
<p>Unfortunately vtkMRMLAbstractDisplayableManager does not have widget member as vtkMRMLMarkupsDisplayableManager has LastActiveWidget.</p>
</blockquote>
</aside>
<p>vtkMRMLCrosshairDisplayableManager has the SliceIntersectionWidget widget. You can ask that widget what cursor shape it wants and set that in the renderer, similarly how it is done in markups.</p>

---

## Post #6 by @forfullstack (2021-02-05 09:52 UTC)

<p>I added GetMouseCursor() on the vtkMRMLCrosshairDisplayableManager and let it to call vtkMRMLSliceIntersectionWidget::GetMouseCursor() and it’s working.<br>
But really mouse cursor isn’t changed despite of GetMouseCursor() returns VTK_CURSOR_CROSSHAIR.<br>
I think somewhere it hooks mouse cursor.<br>
Anyway thanks for your answer and I have learned some event handlings more.<br>
I have more issues and will ask you.</p>

---
