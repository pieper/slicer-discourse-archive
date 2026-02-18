# vtkMRMLSliceNode observe events

**Topic ID**: 3480
**Date**: 2018-07-13
**URL**: https://discourse.slicer.org/t/vtkmrmlslicenode-observe-events/3480

---

## Post #1 by @priya.vada4 (2018-07-13 15:55 UTC)

<p>Hi</p>
<p>I would like to implement custom functionality based on user clicks/keypress in the slice views. I would like to observe the events separately for clicks/keypress in the red and yellow slices. For this, I was implementing the following code. However, the function does not seem to be called when I press the left mouse button or press a key. Could you please let me know the reason. Is there a better way to independently detect key press events on the red and yellow slices?</p>
<pre><code>def testMethod(caller, event):
  print("Event detected")

color = "Red"
sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNode%s" % color)
sliceNode.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, testMethod)
sliceNode.AddObserver(vtk.vtkCommand.KeyPressEvent, testMethod)
sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, testMethod)
</code></pre>
<p>Thanks<br>
Priya</p>

---

## Post #2 by @lassoan (2018-07-13 17:52 UTC)

<p>It is better to avoid this kind of low-level access and use widgets (markups, ROI, etc.), segment editor effects, etc. What would you like to achieve (define input points, move objects, …)?</p>
<p>If you want to process these internal events anyway then you need to observe events of the interactor:</p>
<pre><code>interactor = slicer.app.layoutManager().sliceWidget('Red').sliceView().interactor()

def processEvent(caller=None, event=None):
  print(event)
  if event == "KeyPressEvent":
    key = interactor.GetKeySym()
    if key.lower() == 'backslash':
      xy = interactor.GetEventPosition()
      print(xy)
  return False

interactorObserverTags = []
events = ( vtk.vtkCommand.LeftButtonPressEvent,
  vtk.vtkCommand.LeftButtonReleaseEvent,
  vtk.vtkCommand.MiddleButtonPressEvent,
  vtk.vtkCommand.MiddleButtonReleaseEvent,
  vtk.vtkCommand.RightButtonPressEvent,
  vtk.vtkCommand.RightButtonReleaseEvent,
  vtk.vtkCommand.MouseMoveEvent,
  vtk.vtkCommand.KeyPressEvent,
  vtk.vtkCommand.EnterEvent,
  vtk.vtkCommand.LeaveEvent )
for e in events:
  tag = interactor.AddObserver(e, processEvent, 1.0)
  interactorObserverTags.append(tag)</code></pre>

---

## Post #3 by @priya.vada4 (2018-07-13 18:10 UTC)

<p>Thanks very much, Andras. This works well.</p>
<p>Priya</p>

---
