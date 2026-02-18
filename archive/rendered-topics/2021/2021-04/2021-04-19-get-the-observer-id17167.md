# Get the observer

**Topic ID**: 17167
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/get-the-observer/17167

---

## Post #1 by @timeanddoctor (2021-04-19 12:07 UTC)

<p>How can I get the observer(vtkObserver ) from a interactor.<br>
such as the print(interactor):<br>
vtkWin32RenderWindowInteractor (0000021811DBF070)<br>
Debug: Off<br>
Modified Time: 376531<br>
Reference Count: 2<br>
Registered Events:<br>
Registered Observers:<br>
vtkObserver (0000021811E26D80)<br>
Event: 12<br>
EventName: LeftButtonPressEvent<br>
Command: 0000021812223760<br>
Priority: 0<br>
Tag: 90</p>

---

## Post #2 by @lassoan (2021-09-05 02:10 UTC)

<p>I don’t think there is an API to get observers to an object, because only that software component should remove the observation that added it. That component stores the observation tag when it creates the observation.</p>
<p>Why do you need the observer?</p>

---
