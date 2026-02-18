# How to Activate Slice View on Mouse Hover

**Topic ID**: 39937
**Date**: 2024-10-30
**URL**: https://discourse.slicer.org/t/how-to-activate-slice-view-on-mouse-hover/39937

---

## Post #1 by @huwqchn (2024-10-30 13:54 UTC)

<p>Hi everyone,</p>
<p>I’ve set up multiple shortcuts for each view, but they only work if I click to activate the view first. I’d like to improve my workflow by activating views on mouse hover instead, so shortcuts are immediately available without extra clicks.</p>
<p>Is there a way to enable view activation on hover?</p>

---

## Post #2 by @pieper (2024-10-30 14:28 UTC)

<p>Generally the views act like other widgets, like text entry, with a click-to-focus model.  You can listen for window enter events and force the focus to change, but on some OSs in the past we found this also raised the application window if you moved the mouse through the view even if there was another application in front, which was annoying to users.  Maybe you can find a way to have focus follow the mouse only if the Slicer application is in the foreground.</p>
<p>If, for example I’m in paint mode, what I do is use the space bar to toggle to the arrow cursor, then click in the view, then space bar again so that keyboard and mouse events to to the view of choice.</p>

---

## Post #3 by @huwqchn (2024-10-30 14:32 UTC)

<p>Thanks for your response; this is very insightful!</p>

---

## Post #4 by @huwqchn (2024-10-30 15:29 UTC)

<p>I’ve created a <code>FocusOnHover</code> class to set focus when the mouse enters or leaves the view. The <code>print("enter")</code> and <code>print("leave")</code> statements work as expected, but <code>setFocus</code> doesn’t seem to activate the view, and vtk shortcuts still aren’t working.</p>
<p>Here’s the code I’m using:</p>
<pre><code class="lang-auto">import qt

class FocusOnHover(qt.QObject):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        # Install event filter
        self.widget.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Check event type
        if obj == self.widget:
            if event.type() == qt.QEvent.Enter:
                # Set focus when mouse enters
                print("enter")
                self.widget.setFocus(qt.Qt.MouseFocusReason)
            elif event.type() == qt.QEvent.Leave:
                # Clear focus when mouse leaves
                print("leave")
                self.widget.clearFocus()
        return False

layoutManager = slicer.app.layoutManager()
threeDView = layoutManager.threeDWidget(0).threeDView()  # Select specific 3D view
hover_focus = FocusOnHover(threeDView)
</code></pre>

---

## Post #5 by @pieper (2024-10-30 15:58 UTC)

<p>I don’t recall, but you may need to do something at the VTK render window or render window interactor level too.</p>

---

## Post #6 by @huwqchn (2024-10-30 17:21 UTC)

<pre data-code-wrap="import"><code class="lang-import">
class FocusOnHover(qt.QObject):
    def __init__(self, threeDWidget):
        super().__init__()
        self.threeDWidget = threeDWidget
        self.threeDWidget.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.threeDWidget:
            threeDView = self.threeDWidget.threeDView()
            renderWindow = threeDView.renderWindow()
            interactor = renderWindow.GetInteractor()

            if event.type() == qt.QEvent.Enter:
                print("enter")
                self.threeDWidget.setFocus(qt.Qt.MouseFocusReason)
                interactor.Enable()
                slicer.app.processEvents()
                
            elif event.type() == qt.QEvent.Leave:
                # 鼠标离开时禁用交互器
                print("leave")
                interactor.Disable()
                self.threeDWidget.clearFocus()
                
        return False

layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0) 
hover_focus = FocusOnHover(threeDWidget)``` the VTK interactor doesn’t seem to activate when I call `interactor.Enable()`. this make me confused, it's seems can't make it active programmatically</code></pre>

---

## Post #7 by @lassoan (2024-10-30 20:57 UTC)

<p>I agree that it would be nice if some keyboard shortcuts could be applied to views without requiring clicking.</p>
<p>However, changing the focus by mouse hover is an operating system/window manager level decision that should not be overridden at application level. On Windows, “Activate a window by hovering over it with the mouse” is an accessibility feature that can be enabled/disabled in the operating system (it works only at application window level though, so it does not set the focus to a particular widget).</p>
<p>For a custom application, activating a view widget on hover could be fine. If we want to improve Slicer core behavior, we could do something like installing an event filter and capture unprocessed keyboard events. If an unprocessed event occurs then the focus can be set to the last active view widget (we should probably hightlight this widget with a frame) and the event could be sent to that widget.</p>

---

## Post #8 by @huwqchn (2024-10-31 03:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="39937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we should probably hightlight this widget with a frame</p>
</blockquote>
</aside>
<p>That’s exactly what I’m trying to do, but there’s no way to activate <code>vtkRenderWindowInteractor</code>. <code>interactor.Enable()</code> not work anyway.</p>

---

## Post #9 by @lassoan (2024-10-31 13:52 UTC)

<p>Would you be able to spend a couple of weeks on this, developing mainly in C++? It would be great. We could help you along the way.</p>
<p>This could be done in 3 steps:</p>
<ul>
<li>Implement the concept of “active” view node. The user would change which view is active by clicking in it, and it would be indicated by some decoration (probably a colored border around the view). Node ID of the active view would be stored in the selection node in the scene.</li>
<li>Implement an event filter that can detect events that are not processed by the Qt widget that currently has the focus. For example, if you are in a textbox and press <code>r</code> then you want to add that letter to the textbox, but if a button or slider has the focus then the active view should get a chance to process the event.</li>
<li>Implement changing of widget focus to the active view and forward the event to the active view, when there is an event that the currently focused Qt widget cannot process but the currently active view can process.</li>
</ul>

---

## Post #10 by @huwqchn (2024-11-01 08:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="39937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you be able to spend a couple of weeks on this, developing mainly in C++? It would be great. We could help you along the way.</p>
</blockquote>
</aside>
<p>Yes, I’m primarily working with C++, and I’d be happy to spend a couple of weeks contributing to Slicer.</p>

---

## Post #12 by @huwqchn (2024-11-01 08:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="39937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>Implement the concept of “active” view node. The user would change which view is active by clicking in it, and it would be indicated by some decoration (probably a colored border around the view). Node ID of the active view would be stored in the selection node in the scene.</li>
<li>Implement an event filter that can detect events that are not processed by the Qt widget that currently has the focus. For example, if you are in a textbox and press <code>r</code> then you want to add that letter to the textbox, but if a button or slider has the focus then the active view should get a chance to process the event.</li>
<li>Implement changing of widget focus to the active view and forward the event to the active view, when there is an event that the currently focused Qt widget cannot process but the currently active view can process.</li>
</ul>
</blockquote>
</aside>
<p>I’m very interested in implementing this feature and would appreciate your help.</p>

---

## Post #13 by @lassoan (2024-11-01 16:59 UTC)

<p>The first step would be to implement drawing of focus frame around a view. I quite like how it looks in ParaView:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23bbbfec648265ae2daab0efc69a186b47ac2d21.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7167593ed870fef7076a90d813fc17b5381f7d79.jpeg">
  </div><p></p>
<p>Since ParaView uses the exact same libraries (Qt for GUI, VTK for rendering) and it is open-source software with permissive license, we can have a look how they implemented this frame and implement the same solution in Slicer. It seems that they simply have a <a href="https://github.com/Kitware/ParaView/blob/master/Qt/Components/pqViewFrame.h">Qt frame around the view</a> and change the border visibility.</p>
<p>In Slicer, <code>activeViewFrame()</code> method (that would return the frame widget that can be used to show a border around the active view) could be added to <code>qMRMLAbstractViewWidget.h</code> (similarly to <code>viewWidget()</code> method). <code>activeViewFrame()</code> would be implemented in <code>qMRMLSliceWidget</code>, <code>qMRMLThreeDWidget</code>, <code>qMRMLPlotWidget</code>, and <code>qMRMLTableWidget</code>. The frame widget has to be added in qMRMLSliceWidget.ui, qMRMLThreeDWidget.cxx, qMRMLPlotWidget.cxx, and qMRMLTableWidget.cxx.</p>
<p>Once each widget can display a border, the next step is to connect it to MRML. The selection node stores the currently active view node. Each <code>qMRMLAbstractViewWidget</code> could observe the selection node and update border visibility (show the border if the active view node in the selection node is the same as the widget’s view node). Whenever a view widget receives the focus then it would updates the active node in the selection node.</p>

---
