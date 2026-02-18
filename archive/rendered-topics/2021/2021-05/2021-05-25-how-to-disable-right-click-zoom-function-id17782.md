# How to disable right click Zoom function

**Topic ID**: 17782
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/how-to-disable-right-click-zoom-function/17782

---

## Post #1 by @luxiaoyang9999 (2021-05-25 08:03 UTC)

<p>Hello everyone,<br>
I want to implement my right click function in slicer. however, when I use observer  to active my right click function, the default zoom function will also be activated and it cannot be closed.<br>
interactorStyle = slicer.app.layoutManager().sliceWidget(‘Red’).sliceView().sliceViewInteractorStyle()<br>
interactorStyle.SetActionEnabled(interactorStyle.Zoom, False)<br>
If I use above code to close zoom function, all relative functions will be closed, including ctrl+ mouse scrolling  zoom function, this is function I need. Could anyone tell my how to only close the  right click zoom function in slicer.</p>

---

## Post #2 by @lassoan (2021-05-26 04:28 UTC)

<p>You can fully reprogram all mouse and keyboard shortcuts in all the views, any way you want, just by using Python scripting. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers">script repository</a>.</p>
<p>Adding a VTK event observer is generally not the right way to implement custom mouse&amp;keyboard shortcuts (it would be too low level, so it would interfere with Slicer’s event routing). What would you like to achieve? Display a context menu if the user clicks in a view?</p>

---

## Post #3 by @luxiaoyang9999 (2021-06-08 02:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>K event observer is generally not the right way to implement custom mouse&amp;keyboard</p>
</blockquote>
</aside>
<p>I would like to create a right-click menu in a view. Moreover, when I use<br>
interactorStyle.SetActionEnabled(interactorStyle.Zoom, False)<br>
, I cannot get mouse position in view through crosshairNode like this</p>
<pre><code>    event2 = slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent
    crosshairNode = slicer.util.getNode("Crosshair")
    obs2 = crosshairNode.AddObserver(event2, self.updateAnnotation_One_call)
</code></pre>

---

## Post #4 by @lassoan (2021-06-09 21:42 UTC)

<p>FYI, we’ll enable right-click menu in views about 2 weeks. You’ll be able to register your own menu items via subject hierarchy (the same way as all other menu items are registered in the Subject hierarchy tree, in Data module).</p>

---

## Post #5 by @lassoan (2023-03-21 02:32 UTC)



---
