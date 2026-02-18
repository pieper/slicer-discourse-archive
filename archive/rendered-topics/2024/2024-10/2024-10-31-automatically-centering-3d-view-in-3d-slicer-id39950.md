# Automatically Centering 3D View in 3D Slicer

**Topic ID**: 39950
**Date**: 2024-10-31
**URL**: https://discourse.slicer.org/t/automatically-centering-3d-view-in-3d-slicer/39950

---

## Post #1 by @huwqchn (2024-10-31 08:57 UTC)

<p>Hi everyone,</p>
<p>I’m trying to make the 3D view automatically center whenever a new object is added. My current code mostly works but fails when I hide the 3D box and axis. Here’s what I have:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
renderer = threeDView.renderWindow().GetRenderers().GetFirstRenderer()

initialActorCount = renderer.GetActors().GetNumberOfItems()
print("Initial actor count:", initialActorCount)

def checkForNewObject(caller, event):
    global initialActorCount
    currentActorCount = renderer.GetActors().GetNumberOfItems()
    
    if currentActorCount &gt; initialActorCount:
        print("New object added to 3D view")
        print("Current actor count:", currentActorCount)

        slicer.app.processEvents() 
        threeDView.resetFocalPoint()
        
    initialActorCount = currentActorCount

renderer.AddObserver(vtk.vtkCommand.ModifiedEvent, checkForNewObject)
</code></pre>
<p>The issue arises when I hide the 3D box and axis using:</p>
<pre><code class="lang-auto">viewNode.SetBoxVisible(False)
viewNode.SetAxisLabelsVisible(False)
</code></pre>
<p>With these settings, the automatic centering doesn’t work as expected. Does anyone know why this happens or have suggestions for a solution?</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @cpinter (2024-10-31 09:55 UTC)

<p>I’d probably connect the callback to the event <code>slicer.vtkMRMLScene.NodeAddedEvent</code>.</p>
<p>Note that then the callback should look like this:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(self, caller, event, calldata):
</code></pre>
<p>(no <code>self</code> if not in a class of course)</p>

---
