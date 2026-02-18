# Mouse click over slice

**Topic ID**: 24967
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/mouse-click-over-slice/24967

---

## Post #1 by @JBeninca (2022-08-28 21:33 UTC)

<p>Hi everyone.<br>
Just a question: how can I read the mouse event (right click) over a widget and then run a call back?<br>
Is there some function that do it?<br>
thanks</p>

---

## Post #2 by @lassoan (2022-08-29 02:59 UTC)

<p>By default, in markup widgets <code>RightButtonClickEvent</code> interaction event is translated to <code>WidgetEventMenu</code> widget event, which displays a context menu. You can remove the old mapping and add a new mapping to a custom event using <code>widget.SetEventTranslation</code> (see examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>).</p>
<p>For example, you can translate the right-click event to <code>slicer.vtkSlicerMarkupsWidget.WidgetEventCustomAction1</code> event, which invokes a <code>slicer.vtkMRMLMarkupsDisplayNode.CustomActionEvent1</code> on the markup’s display node. To get notified about the right-click event you just need to add an observer to this event.</p>
<p>Example:</p>
<pre><code class="lang-python">def someCustomAction(caller, eventId):
  markupsDisplayNode = caller
  print(f"Custom action activated in {markupsDisplayNode.GetName()}")

views = [
    slicer.app.layoutManager().threeDWidget(0).threeDView(),
    slicer.app.layoutManager().sliceWidget("Red").sliceView(),
    slicer.app.layoutManager().sliceWidget("Yellow").sliceView(),
    slicer.app.layoutManager().sliceWidget("Green").sliceView()
]

observations = []  # store the observations so that later can be removed
markupsDisplayNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsDisplayNode")
for markupsDisplayNode in markupsDisplayNodes:
    # Add observer to custom actions
    observations.append([markupsDisplayNode, markupsDisplayNode.AddObserver(markupsDisplayNode.CustomActionEvent1, someCustomAction)])
    for view in views:
        markupsDisplayableManager = view.displayableManagerByClassName('vtkMRMLMarkupsDisplayableManager')
        # Assign keyboard shortcut to trigger custom actions
        widget = markupsDisplayableManager.GetWidget(markupsDisplayNode)
        # Remove old event translation
        widget.SetEventTranslation(widget.WidgetStateOnWidget, slicer.vtkMRMLInteractionEventData.RightButtonClickEvent, vtk.vtkEvent.NoModifier, vtk.vtkWidgetEvent.NoEvent)
        # Add new event translation
        widget.SetEventTranslation(widget.WidgetStateOnWidget, slicer.vtkMRMLInteractionEventData.RightButtonClickEvent, vtk.vtkEvent.NoModifier, widget.WidgetEventCustomAction1)

## Remove observations when custom actions are not needed anymore by uncommenting these lines:
# for observedNode, observation in observations:
#     observedNode.RemoveObserver(observation)
</code></pre>

---

## Post #3 by @jay1987 (2022-08-31 02:24 UTC)

<p>which widget do you want to react the right click event?<br>
in slicer,it different to react and to hand right click event with different widgets</p>

---

## Post #4 by @JBeninca (2022-08-31 09:17 UTC)

<p>Hi. It’s the Red widget.<br>
Else, i want to tell you, that its ready a first version of a Leksell path stereotaxia.<br>
It does works fine, but it need some tests. If you hace 2 or 3 different heads-with-frame volumen, please send them to me.</p>

---

## Post #5 by @Grigoriy_Postolskiy (2023-05-26 09:38 UTC)

<p>This code started work for only when I added the decorator above the function:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_OBJECT)
def someCustomAction(caller, eventId, callData):
</code></pre>

---
