# Entry and exit events from MRML slice views

**Topic ID**: 1060
**Date**: 2017-09-15
**URL**: https://discourse.slicer.org/t/entry-and-exit-events-from-mrml-slice-views/1060

---

## Post #1 by @mschumaker (2017-09-15 15:34 UTC)

<p>I’m hoping to perform actions in my scripted module when the user’s mouse enters or exits the Red and Yellow MRML slice views. I know this involves observing events, but I’m not sure what event to observe, and where to use AddObserver. How can I accomplish this?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2017-09-15 16:00 UTC)

<p>These are standard VTK interaction events that you can get by observing low-level VTK objects (probably the interactor; see examples of accessing these low-level objects in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras">script repository</a>).</p>
<p>However, I would recommend to use higher-level API, such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view">observing the crosshair node</a>. You can get the current slice node using <a href="http://apidocs.slicer.org/master/classvtkMRMLCrosshairNode.html#adab412c60e3be57eb5f6612d96667e96">vtkMRMLCrosshairNode::GetCursorPositionXYZ</a> method.</p>

---

## Post #3 by @mschumaker (2017-09-15 17:28 UTC)

<p>Excellent, thank you. I’m able to get the slice node and its name that way.<br>
I am using a ctkWorkflow, and I’ve also set it up to add the observer when advancing to the relevant step, and remove the observer afterwards:</p>
<pre><code>def onEntry(self):
    ...
    self.crosshairNode=slicer.util.getNode('Crosshair')
    self.crosshairNodeObserverTag = self.crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)
#end onEntry

def onExit(self):
    if(self.crosshairNodeObserverTag is not None):
        self.crosshairNode.RemoveObserver(self.crosshairNodeObserverTag)
#end onExit</code></pre>

---

## Post #4 by @Saima (2019-07-26 04:25 UTC)

<p>I am creating a crosshairnode but still the program shows erroe crosshairnode not defined</p>
<pre><code class="lang-python">self.crosshairNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCrosshairNode")
self.observeid = self.crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)
</code></pre>

---

## Post #5 by @lassoan (2019-07-26 12:33 UTC)

<p>There is a singleton crosshair node, which is used by the application. You need to retrieve and use that node, as shown in the examples (do not create a new crosshair node).</p>

---
