# Event on double right click in a given view

**Topic ID**: 27486
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/event-on-double-right-click-in-a-given-view/27486

---

## Post #1 by @rhodesdante (2023-01-26 17:16 UTC)

<p>Is it possible to trigger a custom event when double-right clicking on a slice viewer? I saw that it was possible to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view" rel="noopener nofollow ugc">observe the crosshair node</a>, but this is not exactly what I’m after. I know right clicking and double clicking trigger their own events (i.e. maximize/restore view) but I’m not sure how this functionality is implemented. Any advice would be greatly appreciated.</p>

---

## Post #2 by @rhodesdante (2023-01-26 21:22 UTC)

<p>After doing some digging in the script repository &amp; on the forum, I found some helpful answers (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures" rel="noopener nofollow ugc">here</a> and <a href="https://discourse.slicer.org/t/mouse-click-over-slice/24967/2">here</a>). However, much of what I found advises that one use the markups module for interactions with the slice viewer. I’m sure this might work, but it seems a little roundabout for what I actually need to do. Is there no way to:</p>
<ol>
<li>
<p>set an event translation via something like:<br>
sliceViewWidget = slicer.app.layoutManager().sliceWidget(“Red”)<br>
displayableManager = sliceViewWidget.sliceView().displayableManagerByClassName(“vtkMRMLCrosshairDisplayableManager”)<br>
widget = displayableManager.GetSliceIntersectionWidget()<br>
widget.SetEventTranslation(widget.WidgetStateAny, vtk.vtkCommand.RightButtonDoubleClickEvent, vtk.vtkEvent.NoModifier, widget.WidgetEventCustomAction1)</p>
</li>
<li>
<p>Take the translation and set an observer on a vtkMRMLsliceNode or a vtkMRMLcrosshairNode?<br>
i.e. sliceNode.AddObserver(sliceNode.CustomActionEvent1 (DOES NOT EXIST), GenericCallbackFn)</p>
</li>
</ol>

---

## Post #3 by @lassoan (2023-01-26 22:03 UTC)

<p>Event handling in the viewers is very complex, because there are lots of interactive widgets in the viewer, each having several internal states and responding to different events in each state. When a new interaction event is invoked then there first there is arbitration process: <code>CanProcessInteractionEvent</code> is called for each each displayable manager (that maps MRML nodes to rendering actors). Displayable managers ask all their widgets if they can process the event and if they can, then provide a “distance” value (usually physical distance from the mouse pointer in screen space). The displayable manager that can process the event and reported the shortest distance gets to process the event. If this displayable manager is not the same as the displayable manager that currently has the focus then the previous displayable manager is notified that it no longer has the focus, the new displayable manager gets the focus, and its <code>ProcessInteractionEvent</code> method is called.</p>
<p>You could add a low-level high-priority observation to the VTK interactor and hijack some mouse events. It would be simple, but because you would just ignore all the existing event arbitration and displayable manager and widget state mechanisms, you would cause many small, often not immediately noticeable errors in the viewer.</p>
<p>If you used an event that does not interfere with any other widget’s state then you may get away without any serious issues. However, a right-double-click causes many events: right button down, right button click, right button up, right button down, right button double-click, right button up. If you don’t consume all these events then widget states will be messed up. The double click may also have different side effects, depending on what widget your mouse pointer is hovered over.</p>
<p>What would you like to trigger by double-right-click?<br>
Would it be acceptable to use an event that is less likely to cause havoc (e.g., some keyboard combinations or right-click with Ctrl/Alt/Shift modifiers, …)?<br>
Would you double-click over a markup, slice intersection, or just over blank screen region?<br>
Would you need to interact in both slice and 3D views?<br>
Do you need 3D click position in 3D views?</p>

---

## Post #4 by @rhodesdante (2023-01-26 22:12 UTC)

<p>Thanks so much for the reply! To answer those questions:</p>
<ol>
<li>What would you like to trigger by double-right-click?<br>
I want to pause scrolling on the slice viewer similar to:<br>
interactorStyle = slicer.app.layoutManager().sliceWidget(“Red”)<br>
interactorStyle.SetActionEnabled(interactorStyle.BrowseSlice = False<br>
but stricter such that the user cannot move the slice viewer under any circumstances (unless they repeat the action)</li>
<li>Would it be acceptable to use an event that is less likely to cause havoc (e.g., some keyboard combinations or right-click with Ctrl/Alt/Shift modifiers, …)?<br>
Absolutely. Any reasonable combination of keys with any click will do.</li>
<li>Would you double-click over a markup, slice intersection, or just over blank screen region?<br>
Slice view.</li>
<li>Would you need to interact in both slice and 3D views?<br>
Just the slice view.</li>
<li>Do you need 3D click position in 3D views?<br>
N/A</li>
</ol>

---

## Post #5 by @lassoan (2023-01-26 22:52 UTC)

<p>Why would you like to activate the scroll lock using double-click? Mouse gestures are not discoverable and by repeatedly clicking too quickly may trigger double-click events, too.</p>
<p>If you can lock/unlock all slice views at once then adding a button to your module would be the simplest. A dedicated button would also make the feature easily discoverable and you would always see the current state of the views.<br>
If you must lock/unlock a single slice view then I would recommend adding a right-click menu item for toggling this, or maybe add a button to the slice view controller (next to the slice selector slider).</p>

---

## Post #6 by @rhodesdante (2023-01-27 03:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="27486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you must lock/unlock a single slice view then I would recommend adding a right-click menu item for toggling this, or maybe add a button to the slice view controller (next to the slice selector slider).</p>
</blockquote>
</aside>
<p>Unfortunately, it is necessary to lock single slice views. I appreciate the suggestion to use a right-click menu item; it seems to work well for my purpose. I am curious though–if I were to go with a checkbox/button option instead, is there a convenient way to add it to the slice viewer?</p>
<p>As for locking the slice, I am aware only of the interactorStyle.BrowseSlice option from above. Is there anything that won’t let the slice scroll even if it is linked to the other slices from that view group?</p>

---

## Post #7 by @rhodesdante (2023-01-27 16:49 UTC)

<p>To clarify the first question–I am able to add a checkbox to the slice viewer using:</p>
<p>checkbox = qt.QCheckBox()<br>
sc = slicer.app.layoutManager().sliceWidget(“Red”).sliceController()<br>
sc.layout().addWidget(checkBox)</p>
<p>But this places the checkbox underneath the slice controller widget. Is there any way to put it <em>next</em> to the slice selector slider like you had proposed? Thank you.</p>

---

## Post #8 by @lassoan (2023-01-28 17:20 UTC)

<p>You can add buttons anywhere in the widget. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-widgets-in-view-controller-bars">examples in the script repository</a>.</p>

---

## Post #9 by @rhodesdante (2023-01-31 16:39 UTC)

<p>Thanks that works great! As for the freezing slices question–is it possible to freeze a slice that is linked to another slice? interactorStyle.BrowseSlice alone is not sufficient to achieve this.</p>

---

## Post #10 by @lassoan (2023-01-31 19:17 UTC)

<p>You can change the group ID of the view node to unlink it from the other views.</p>

---

## Post #11 by @rhodesdante (2023-01-31 21:17 UTC)

<p>Thank you so much! These are all incredibly helpful suggestions.</p>

---
