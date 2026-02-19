---
topic_id: 18029
title: "How To Disable Right Click Zoom Function Individually"
date: 2021-06-09
url: https://discourse.slicer.org/t/18029
---

# How to disable right click zoom function individually?

**Topic ID**: 18029
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/how-to-disable-right-click-zoom-function-individually/18029

---

## Post #1 by @luxiaoyang9999 (2021-06-09 05:26 UTC)

<p>Hello everyone<br>
I tried to disable right click zoom function through</p>
<pre><code class="lang-auto">interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
interactorStyle.SetActionEnabled(interactorStyle.Zoom, False)
</code></pre>
<p>but it can also lead to that I cannot observe mouse position change event in CrosshairNode</p>
<pre><code class="lang-auto">   self.mycrosshairNode = slicer.util.getNode('Crosshair')
   self.observationId_rightclick = self.mycrosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.mouse_move_event)

def mouse_move_event(self, observer, eventid):
    ras = [0, 0, 0]
    pos = self.interactor_red.GetEventPosition()
    self.mycrosshairNode.GetCursorPositionRAS(ras)
    print(ras)
</code></pre>
<p>Could you tell me how to only disable right click zoom function?</p>

---

## Post #2 by @lassoan (2021-06-09 13:55 UTC)

<p>Due to a small bug, you need to re-enable cursor position setting after you disable any action:</p>
<pre><code class="lang-auto">interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
interactorStyle.SetActionEnabled(interactorStyle.Zoom, False)
interactorStyle.SetActionEnabled(interactorStyle.SetCursorPosition, True)
</code></pre>
<p>We’ll fix this soon in the Slicer Preview Release, se this re-enabling <code>SetCursorPosition</code> will no longer be necessary.</p>

---

## Post #3 by @luxiaoyang9999 (2021-06-09 14:37 UTC)

<p>Thank you for your help, this code works.</p>

---

## Post #4 by @ond12 (2021-07-07 13:34 UTC)

<p>Hello, Thank you for this usefull post.</p>
<p>How can i do the same things but for the 3D view ?</p>

---

## Post #5 by @cpinter (2021-07-07 14:00 UTC)

<p>I believe like this:</p>
<p><code>interactorStyle = slicer.app.layoutManager().threeDWidget(0).threeDView().interactorStyle()</code></p>

---
