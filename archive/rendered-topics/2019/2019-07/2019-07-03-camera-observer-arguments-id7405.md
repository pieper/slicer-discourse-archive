---
topic_id: 7405
title: "Camera Observer Arguments"
date: 2019-07-03
url: https://discourse.slicer.org/t/7405
---

# Camera Observer Arguments

**Topic ID**: 7405
**Date**: 2019-07-03
**URL**: https://discourse.slicer.org/t/camera-observer-arguments/7405

---

## Post #1 by @Amine (2019-07-03 22:33 UTC)

<p>I’m trying to add an observer to the camera (and call a function to set a slice plane normal to camera), the function itself works fine but the observer of the camera either states “TypeError: ‘NoneType’ object is not callable”  or wrong arguments if i input anything else than vtk.vtkCommand.ModifiedEvent,</p>
<p>Here is the code i’ve tried :</p>
<pre><code>#grab reformat widget and green slice
layoutManager = slicer.app.layoutManager()
reformatWidget = slicer.modules.reformat.widgetRepresentation()
targetslice = slicer.app.layoutManager().sliceWidget('Green')
sliceNode = targetslice.mrmlSliceNode()
reformatWidget.setEditedNode(sliceNode,"","")
reformatWidget.setNormalToCamera ()

# Grab camera and cameranode
view = layoutManager.threeDWidget(0).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)  ##grabs camera NODE
camera = cameraNode.GetCamera()
# function to call
def refresh():
    reformatWidget.setNormalToCamera ()

#set observer  &lt;-------problematic part
cameraobserver = camera.AddObserver(vtk.vtkCommand.ModifiedEvent, refresh())
#also tried   cameraobserver = camera.AddObserver("ModifiedEvent", refresh())
</code></pre>
<p>Any suggestions? thanks.</p>

---

## Post #2 by @lassoan (2019-07-03 23:06 UTC)

<p>I see two syntax errors:</p>
<ul>
<li>second argument for Add Observer must be <code>refresh</code> or <code>lambda: refresh()</code> (and not <code>refresh()</code>)</li>
<li>refresh method must have two arguments (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" rel="nofollow noopener">this example</a>)</li>
</ul>

---

## Post #3 by @Amine (2019-07-03 23:55 UTC)

<p>Thanks a lot! i could fix it by doing these modifications:</p>
<pre><code>def refresh(param1, param2):
    reformatWidget.setNormalToCamera()
#set observer
cameraobserver = camera.AddObserver(vtk.vtkCommand.ModifiedEvent, refresh, 2)
</code></pre>
<p>I dont understand why the refresh method needs two arguments though, even if it doesent use them,<br>
also in this example there is no “,2” at the end (i couldnt make it work without it)</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified</a></p>

---

## Post #4 by @lassoan (2019-07-04 00:06 UTC)

<p><code>AddObserver</code> requires a callback function that can receive event id and caller parameters (and optionally an additional eventdata), regardless if you use this information in the callback function or not.</p>
<p>The third parameter of <code>AddObserver</code> is the event priority. It is optional, default value is 0.0.</p>

---

## Post #5 by @Amine (2019-07-04 00:42 UTC)

<p>Understood, thanks for your help!</p>

---
