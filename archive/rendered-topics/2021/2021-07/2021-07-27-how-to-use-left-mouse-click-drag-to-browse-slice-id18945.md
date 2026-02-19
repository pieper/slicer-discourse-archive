---
topic_id: 18945
title: "How To Use Left Mouse Click Drag To Browse Slice"
date: 2021-07-27
url: https://discourse.slicer.org/t/18945
---

# how to use left mouse click & drag to browse slice

**Topic ID**: 18945
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/how-to-use-left-mouse-click-drag-to-browse-slice/18945

---

## Post #1 by @wycstar (2021-07-27 13:39 UTC)

<p>NOT use shift, only use left mouse click &amp;&amp; drag to browse the slice in each sliceWidge(Red ,green etc) separately</p>

---

## Post #2 by @lassoan (2021-07-27 16:06 UTC)

<p>You can make left-click-and-drag set the slice intersection position by mapping the left-click-and-drag GUI event to “slice translate” widget event:</p>
<pre><code class="lang-python">for viewName in slicer.app.layoutManager().sliceViewNames():
    widget = slicer.app.layoutManager().sliceWidget(viewName).sliceView().displayableManagerByClassName("vtkMRMLCrosshairDisplayableManager").GetSliceIntersectionWidget()
    widget.SetEventTranslationClickAndDrag(widget.WidgetStateIdle, vtk.vtkCommand.LeftButtonPressEvent, vtk.vtkEvent.NoModifier, widget.WidgetStateTranslate, widget.WidgetEventTranslateStart, widget.WidgetEventTranslateEnd)

</code></pre>
<p>If you want this behavior to be persistent then you can put this code snippet into your startup <code>.slicerrc.py</code> file.</p>

---

## Post #3 by @wycstar (2021-07-28 03:03 UTC)

<p>thx nice lassoan <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:"> , but i want to browse the slice in current widge, for example, in red widget i want to browse the slice in it by mouse click and drag</p>

---

## Post #4 by @jamesobutler (2021-07-28 03:47 UTC)

<p>So you want to browse (change slice offset) for the current widget with left mouse click and drag over the image data? Is there a reason you do not want to left mouse click and drag the slider at the top of the slice widget to change slice offset?</p>
<p>There are other ways to change slice offset of the current widget including:</p>
<ul>
<li>mouse scroll wheel while over the slice</li>
<li>left/right arrow keys</li>
<li>“f” and “b” keys</li>
</ul>
<p>Are these inconvenient methods for you?</p>

---

## Post #5 by @wycstar (2021-07-28 03:54 UTC)

<p>hi james <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:">, this is a habbit of some users, i want to keep it as it is before</p>

---

## Post #6 by @lassoan (2021-07-28 16:17 UTC)

<p>Yes, there are so many other ways to browse slices that although it would not be hard adding one more method, it would be quite low on the priority list of Slicer core developers.</p>
<p>If you can work in C++ then you can implement a proper solution by adding a new state in the crosshair widget (we’ll be happy to review and merge it in the Slicer core if you send a pull request). Alternatively, you can implement a somewhat hacky solution in Python, by observing low-level view interaction events.</p>

---

## Post #7 by @koeglfryderyk (2024-12-08 10:16 UTC)

<p>here is a solution that worked fo rme (you just have to change the view names)</p>
<pre data-code-wrap="python"><code class="lang-python">def enable_scrolling_through_dragging(sensitivity: float = 0.1):
    # Global dictionary to track dragging state for each view
    global dragging
    dragging = {}

    sliceViewNames = ['Red1', 'Yellow1', 'Green1', 'Red2',
                      'Yellow2', 'Green2', 'Red3', 'Yellow3', 'Green3']

    def createDragHandlers(sliceViewName):
        # Create a separate dragging state for each view
        dragging[sliceViewName] = {"isDragging": False, "lastY": None}

        def startDrag(caller, event):
            dragging[sliceViewName]["isDragging"] = True
            dragging[sliceViewName]["lastY"] = caller.GetEventPosition()[1]

        def drag(caller, event):
            if dragging[sliceViewName]["isDragging"]:
                currentY = caller.GetEventPosition()[1]
                deltaY = currentY - dragging[sliceViewName]["lastY"]
                dragging[sliceViewName]["lastY"] = currentY

                if abs(deltaY) &gt; 0:
                    position = slicer.util.getNode(
                        "*Crosshair*").GetCursorPositionXYZ([0]*3)
                    if position is not None:
                        current_view = position.GetName()
                        sliceLogic = slicer.app.layoutManager().sliceWidget(current_view).sliceLogic()
                        sliceOffset = sliceLogic.GetSliceOffset()
                        newSliceOffset = sliceOffset - deltaY * sensitivity
                        sliceLogic.SetSliceOffset(newSliceOffset)

        def endDrag(caller, event):
            dragging[sliceViewName]["isDragging"] = False
            dragging[sliceViewName]["lastY"] = None

        return startDrag, drag, endDrag

    # Loop through slice views and add event observers
    for sliceViewName in sliceViewNames:
        # Get the interactor for this slice view
        interactor = slicer.app.layoutManager().sliceWidget(
            sliceViewName).sliceView().interactor()

        # Create handlers specific to this view
        startDrag, drag, endDrag = createDragHandlers(sliceViewName)

        # Add observers
        interactor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, startDrag)
        interactor.AddObserver(vtk.vtkCommand.LeftButtonReleaseEvent, endDrag)
        interactor.AddObserver(vtk.vtkCommand.MouseMoveEvent, drag, 1.0)


def disable_scrolling_through_dragging():
    """
    Disable scrolling through dragging by removing observers from slice views.

    This function should be called after enable_scrolling_through_dragging() 
    to remove the drag event observers.
    """
    sliceViewNames = ['Red1', 'Yellow1', 'Green1', 'Red2',
                      'Yellow2', 'Green2', 'Red3', 'Yellow3', 'Green3']

    for sliceViewName in sliceViewNames:
        # Get the slice view from the layout manager
        sliceWidget = slicer.app.layoutManager().sliceWidget(sliceViewName)

        if sliceWidget:
            # Get the interactor from the slice view
            interactor = sliceWidget.sliceView().interactor()

            # Remove the observers if they exist
            if hasattr(interactor, 'startDragObserver'):
                interactor.RemoveObserver(interactor.startDragObserver)
                del interactor.startDragObserver

            if hasattr(interactor, 'dragObserver'):
                interactor.RemoveObserver(interactor.dragObserver)
                del interactor.dragObserver

            if hasattr(interactor, 'endDragObserver'):
                interactor.RemoveObserver(interactor.endDragObserver)
                del interactor.endDragObserver

    # Clear the global dragging dictionary
    global dragging
    dragging.clear()
</code></pre>

---
