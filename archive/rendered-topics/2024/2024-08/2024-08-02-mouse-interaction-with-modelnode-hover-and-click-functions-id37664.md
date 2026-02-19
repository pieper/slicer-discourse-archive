---
topic_id: 37664
title: "Mouse Interaction With Modelnode Hover And Click Functions"
date: 2024-08-02
url: https://discourse.slicer.org/t/37664
---

# Mouse Interaction with ModelNode: Hover and Click Functions

**Topic ID**: 37664
**Date**: 2024-08-02
**URL**: https://discourse.slicer.org/t/mouse-interaction-with-modelnode-hover-and-click-functions/37664

---

## Post #1 by @park (2024-08-02 08:48 UTC)

<p>Hello,</p>
<p>I want to create a feature that interacts with a <code>modelNode</code> through the mouse. Specifically, when the mouse hovers over a model, I want its color to change, and when clicked, I want the camera to center on that model.</p>
<p>I have come across several similar questions, but I couldn’t find a solution, and some of the example links were invalid.</p>
<p>I thought knowing the mouse (cursor) position would be the starting point, so I found the following code that allows me to get the mouse coordinates:</p>
<blockquote>
<p>crosshairNode=slicer.util.getNode(“Crosshair”)</p>
<p>def onMouseMoved(ViewName):<br>
ras=[0,0,0]<br>
crosshairNode.GetCursorPositionRAS(ras)<br>
print(ras)</p>
<p>for viewName in [“View1”]:<br>
threeDView = slicer.app.layoutManager().threeDWidget(viewName).threeDView()<br>
tag = threeDView.interactor().AddObserver(vtk.vtkCommand.MouseMoveEvent , lambda caller, event, viewName=viewName: onMouseMoved(viewName))</p>
</blockquote>
<p>However, I am having difficulty determining if the mouse is over a specific model with these coordinates (do I need to write code to compare the coordinates with all points of the model? This seems to take too long).</p>
<p>I believe that the features I mentioned are already implemented in the <code>markups</code> module. Therefore, I would appreciate it if you could provide a code snippet or some tips.</p>

---

## Post #2 by @lassoan (2024-08-03 22:36 UTC)

<p>Check out focus implementation  <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>. It seems to be what you would like to achieve. You can find more information <a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/NodeFocus/">here</a>.</p>

---

## Post #3 by @park (2024-08-06 08:18 UTC)

<p>I solved this using <code>vtk.vtkCellPicker()</code>.<br>
This is the code snippet of my implementation.</p>
<pre><code class="lang-auto">def setThreeDViewInteraction(self):
    self.picker = vtk.vtkCellPicker()
    self.picker.SetTolerance(0.005)    

    modelDisplayableManager = slicer.app.layoutManager().threeDWidget('View1').threeDView().displayableManagerByClassName("vtkMRMLModelDisplayableManager")
    self.actorModels = []
    for modelNode in self.modelNodes:
        self.actorModels.append(modelDisplayableManager.GetActorByID(modelNode.GetDisplayNode().GetID()))

    self.interactor3D = slicer.app.layoutManager().threeDWidget('View1').threeDView().interactor()
    self.threeDViewMouseHoverTag = self.interactor3D.AddObserver(vtk.vtkCommand.MouseMoveEvent, self.threeDViewMouseHover)
    self.threeDViewMouseClickTag = self.interactor3D.AddObserver(vtk.vtkCommand.LeftButtonDoubleClickEvent, self.threeDViewMouseClick)
    
def threeDViewMouseHover(self, caller, event):
    x, y = caller.GetEventPosition()
    self.picker.Pick(x, y, 0, caller.GetRenderWindow().GetRenderers().GetFirstRenderer())
    actorMouse = self.picker.GetActor()

    if actorMouse in self.actorModels:
        for modelNode in self.modelNodes:
            modelNode.GetDisplayNode().SetAmbient(0.95)
    else:
        for modelNode in self.modelNodes:
            modelNode.GetDisplayNode().SetAmbient(0.5)
</code></pre>

---
