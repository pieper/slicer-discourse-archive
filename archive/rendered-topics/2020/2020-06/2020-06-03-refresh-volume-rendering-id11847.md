# Refresh volume rendering

**Topic ID**: 11847
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/refresh-volume-rendering/11847

---

## Post #1 by @ada (2020-06-03 15:28 UTC)

<p>Hi developpers,</p>
<p>I am writing a scripted module with python to hide the volume and only display slices into the 3d view using following functions :<br>
red = slicer.util.getNode(‘vtkMRMLSliceNodeRed’)<br>
red.SetSliceVisible(1)</p>
<p>volRenLogic = slicer.modules.volumerendering.logic()<br>
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)<br>
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())<br>
displayNode.SetVisibility(True)</p>
<p>ROI_node = displayNode.GetROINode()<br>
ROI_node.SetDisplayVisibility(True)<br>
displayNode.SetAndObserveROINodeID(ROI_node.GetID())<br>
ROI_node.SetROIAnnotationVisibility(1)</p>
<p>It is working but the result is not automatically updated. I need to change the zoom or translate the volume to update the view. Do you know how avoid that in python ?<br>
Thank you !</p>

---

## Post #2 by @lassoan (2020-06-03 16:03 UTC)

<p>Display is only updated when your python script execution is completed. If you want to enforce re-rendering of views while a script is running, call <code>slicer.util.forceRenderAllViews()</code>.</p>

---

## Post #3 by @ada (2020-06-03 16:25 UTC)

<p>Thank you for your answer.<br>
I have the following error :<br>
AttributeError: ‘module’ object has no attribute ‘forceRenderAllViews’</p>

---

## Post #4 by @ada (2020-06-04 09:47 UTC)

<p>I downloaded the last release version. The function is now avalaible.<br>
Nevertheless the problem is still here.<br>
If I first hide the 3D volume, then try to display it using the previous functions, only the ROI is displayed and I need to click on the 3D viewand move the mouse to update the volume display.</p>

---

## Post #5 by @lassoan (2020-06-04 13:52 UTC)

<p>Could you provide a code snippet that reproduces the issue from an empty scene? (downloads a sample data set, sets up visualization, etc. - you can find examples to start from in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>)</p>

---

## Post #6 by @ada (2020-06-04 15:09 UTC)

<p>Hello, I found a solution updating the display like that :</p>
<p>viewNode = slicer.util.getNode(‘View1’)<br>
viewNode.SetVisibility(False)<br>
viewNode.SetVisibility(True)</p>
<p>Thank you</p>

---

## Post #7 by @ada (2020-06-12 14:39 UTC)

<p>Hello all,<br>
I though my problem was solved but I have a quite similar problem :</p>
<p>I am changing the zoom and position of the camera using “camera.Dolly” and “camera.SetPosition” functions but the 3D view is not automatically updated (only the background is displayed).<br>
The volume is only displayed when I click and move the mouse on the “View1” screen</p>
<p>Do you know how can I avoid it ?</p>
<p>Best</p>

---

## Post #8 by @lassoan (2020-06-12 15:59 UTC)

<p>You can use MRML interface of the camera (get the camera node and adjust position, focal point, etc.), which works as you expect.</p>
<p>If you go one level lower and manipulate VTK rendering objects directly, then you need to do all the necessary steps at that level, including resetting camera clipping planes, when you change the camera position. For example, this works for me:</p>
<pre><code class="lang-python"># Load some sample data and show it using volume rendering
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
displayNode.SetVisibility(True)
displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName('MR-Default'))

# Get camera node
view = slicer.app.layoutManager().threeDWidget(0).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)

# Move camera using low-level VTK interface
cameraNode.GetCamera().Dolly(1.05);
cameraNode.ResetClippingRange()
</code></pre>

---

## Post #9 by @ada (2020-06-12 16:04 UTC)

<p>Thank you so much, the ResetClippingRange() function was missing.</p>

---
