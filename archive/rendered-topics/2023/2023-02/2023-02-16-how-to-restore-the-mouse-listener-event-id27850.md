---
topic_id: 27850
title: "How To Restore The Mouse Listener Event"
date: 2023-02-16
url: https://discourse.slicer.org/t/27850
---

# How to restore the mouse listener event

**Topic ID**: 27850
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/how-to-restore-the-mouse-listener-event/27850

---

## Post #1 by @user_ghost (2023-02-16 06:47 UTC)

<p>Hello:<br>
every teachers, i uesd the code to define a new event about left mouse press event<br>
<a href="/uploads/short-url/xlgLIx2FVa3PMC0RP5I73aVOv8h.png">image|690x282</a><br>
but how can i restore the default action<br>
this is my code<br>
def onStartMark(self):<br>
layoutManager = slicer.app.layoutManager()<br>
threeDWidget = layoutManager.threeDWidget(0)<br>
threeDView = threeDWidget.threeDView()<br>
self.interactor = threeDView.interactorStyle().GetInteractor()<br>
import copy<br>
self.interactor1 = self.interactor<br>
# self.defaultObserver = interactor.GetObserverMediator()<br>
self.interactor.RemoveObservers(‘LeftButtonPressEvent’)<br>
self.interactor.AddObserver(‘LeftButtonPressEvent’, self.onRightButtonPressed)<br>
pointPicker = vtk.vtkPointPicker()<br>
self.interactor.SetPicker(pointPicker)</p>

---
