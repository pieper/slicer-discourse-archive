---
topic_id: 18469
title: "Connecting Widget Callback With Custom Logic Signal Event In"
date: 2021-07-01
url: https://discourse.slicer.org/t/18469
---

# Connecting widget callback with custom logic signal/event in a scripted module

**Topic ID**: 18469
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/connecting-widget-callback-with-custom-logic-signal-event-in-a-scripted-module/18469

---

## Post #1 by @atracsys-sbt (2021-07-01 21:54 UTC)

<p>Hi,<br>
I’m trying to connect a callback in the widget class of my scripted module with a custom event of the logic class. My first attempt has been with the Qt signal/slot system, much like in <a href="https://discourse.slicer.org/t/how-to-use-signals-and-slots-in-slicer-3d/14013/5">this post</a>.</p>
<p>My code looks like so:</p>
<pre><code class="lang-auto">class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
  def setup(self):
    ...
    self.logic.moved.connect(self.onPtrMoved)

  def onPtrMoved(self):
    # do something

class MyModuleLogic(ScriptedLoadableModuleLogic):
  def __init__(self):
    ...
    self.moved = qt.Signal()
  
  @vtk.calldata_type(vtk.VTK_OBJECT)
  def someOtherCallback(self, caller, event=None, calldata=None):
    self.moved.emit()
</code></pre>
<p>When someOtherCallback is called, the signal is allegedly emitted and then Slicer crashes.</p>
<p>I would like to know why it’s not working given that the signal is emitted from its own class (which is better as pointed out <a href="https://discourse.slicer.org/t/use-of-qt-signal-leads-to-a-crash-on-exit/8321/4">here</a>) and how to fix it. Also, I’m not restricted to using Qt for this and apparently resorting to a vtk custom event and an observer would be a better way (as suggested <a href="https://discourse.slicer.org/t/custom-signal-slots-with-pythonqt/3278/8">here</a>) but I couldn’t find any example in Python.</p>
<p>Any help would be appreciated</p>

---

## Post #2 by @lassoan (2021-07-01 22:52 UTC)

<p>MRML classes (such as the module logic classes) do not depend on Qt, to minimize unnecessary dependencies. Therefore, you cannot emit Qt signals from logic classes. Instead, you can use VTK events and callbacks.</p>
<p>Widgets normally do not observe logic classes, because logic classes are generally stateless. State is stored in MRML nodes instead, the logic classes may modifies MRML nodes (such as the scripted module’s parameter node; or any other nodes), and widgets observe MRML node changes. You can define your own event IDs (just choose numbers that are not used already on that object) and invoke them on any MRML node.</p>

---
