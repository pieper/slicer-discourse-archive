# Issue with vtk.vtkCommand.HoverEvent on vtk.vtkHandleWidget

**Topic ID**: 41159
**Date**: 2025-01-20
**URL**: https://discourse.slicer.org/t/issue-with-vtk-vtkcommand-hoverevent-on-vtk-vtkhandlewidget/41159

---

## Post #1 by @jhan1245 (2025-01-20 07:53 UTC)

<p>I am currently working with the vtk.vtkHandleWidget and attempting to add the vtk.vtkCommand.HoverEvent using the AddObserver method. However, it seems that the hover event is not functioning as expected.</p>
<p>Could you provide guidance on the necessary code or steps required to enable the hover event for a custom handle widget created with vtk.vtkHandleWidget? Any assistance or advice would be greatly appreciated.</p>
<pre data-code-wrap="python"><code class="lang-python">
def createHandle(self):
    self.sphereRep, self.sphereHandle = self._createSphereHandle()

    # connect Hover Event
    self.sphereHandle.AddObserver(vtk.vtkCommand.HoverEvent, self.handleHoverEventCallback)

# Create Handle
def _createSphereHandle(self):
    handleSphereSource = vtk.vtkSphereSource()
    handleSphereSource.SetRadius(self.sphereRadius)
    handleSphereSource.SetThetaResolution(self.sphereResolution)
    handleSphereSource.SetPhiResolution(self.sphereResolution)
    handleSphereSource.Update()
    self.spherePoly = handleSphereSource.GetOutput()
   
    sphereRep = vtk.vtkPolygonalHandleRepresentation3D()
    sphereRep.SetHandle(self.spherePoly)
    sphereRep.GetProperty().SetColor(self.sphereColor)
    sphereRep.GetSelectedProperty().SetColor(self.sphereColor)
    sphereRep.GetProperty().SetAmbient(0.2)
    sphereRep.GetSelectedProperty().SetAmbient(0.2)

    sphereHandle = vtk.vtkHandleWidget()
    sphereHandle.SetInteractor(self.interactor)
    sphereHandle.SetRepresentation(sphereRep)
    sphereHandle.SetPriority(1.0)
    sphereHandle.SetAllowHandleResize(False)

    return sphereRep, sphereHandle

def handleHoverEventCallback(self, caller, event):
    print("mouse hover")

</code></pre>
<p>Thank you in advance for your time and support.</p>
<p>Best regards</p>

---
