---
topic_id: 15468
title: "Move 3D Focal Point Using Mouse Or Keyboard"
date: 2021-01-12
url: https://discourse.slicer.org/t/15468
---

# Move 3D focal point using mouse or keyboard

**Topic ID**: 15468
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/move-3d-focal-point-using-mouse-or-keyboard/15468

---

## Post #1 by @torquil (2021-01-12 10:25 UTC)

<p>I would like to know how to use the mouse or keyboard in the 3D view to move the focal point of the camera away from me or closer to me. I know how to move it sideways by using the mouse middle-click + drag. I also know how to rotate around the focal point using the mouse left-click and drag.</p>
<p>But whenever I use the mouse wheel to “travel” through a structure (or mouse right-click + drag), the movement stops as I approach the focal point, so it is not possible to travel through a 3D structure if the focal point is in the structure’s interior (since I’m just zooming without actually moving the focal point).</p>
<p>So: how to I move the focal point away from me or towards me in a continuous manner, using the keyboard or mouse?</p>

---

## Post #2 by @lassoan (2021-01-12 18:30 UTC)

<p>Yes, zooming just moves the camera towards or away from the focal point, but not changes the focal point position, so this is not suitable for exploring a volume, but it is for inspecting what is in the camera’s focal point.</p>
<p>There are many options for exploring navigating in space, for example to move through vasculature, airways, or intestines.</p>
<ol>
<li>Virtual reality</li>
</ol>
<p>The most natural and effective way of navigating through a volume is via virtual reality, using SlicerVirtualReality extension (you will get inside the Slicer scene by a single click). You can use any OpenVR compatible headsets (Oculus Rift, HTC Vive, any Windows MR devices) and fly through the volume; or grab the scene with two hands and pull yourself through it; or grab any object in your hand and move/rotate to inspect it.</p>
<ol start="2">
<li>Use camera manouver</li>
</ol>
<p>You can change the focal point position by rotating the camera by approximately 90 degrees, and pan the camera (Shift+Left-click-and-drag into any direction), and rotate it back by 90 degrees.</p>
<ol start="3">
<li>Enable keyboard or mouse shortcuts to translate the focal point along with the camera</li>
</ol>
<p>For example, you can add a keyboard shortcut “Ctrl-Up” and “Ctrl-Down” and “Ctrl+Mousewheel” to move forward and backward by copy-pasting this code into the Python console:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
cameraDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLCameraDisplayableManager')
cameraWidget = cameraDisplayableManager.GetCameraWidget()

# Make Ctrl + Arrow Up/Down key translate forward/backward
cameraWidget.SetKeyboardEventTranslation(cameraWidget.WidgetStateIdle, vtk.vtkEvent.ControlModifier, '\0', 0, "Down", cameraWidget.WidgetEventCameraTranslateBackwardZ)
cameraWidget.SetKeyboardEventTranslation(cameraWidget.WidgetStateIdle, vtk.vtkEvent.ControlModifier, '\0', 0, "Up", cameraWidget.WidgetEventCameraTranslateForwardZ)

# Make Ctrl + Mousewheel translate forward/backward
cameraWidget.SetEventTranslation(cameraWidget.WidgetStateIdle, vtk.vtkCommand.MouseWheelForwardEvent, vtk.vtkEvent.ControlModifier, cameraWidget.WidgetEventCameraTranslateBackwardZ)
cameraWidget.SetEventTranslation(cameraWidget.WidgetStateIdle, vtk.vtkCommand.MouseWheelBackwardEvent, vtk.vtkEvent.ControlModifier, cameraWidget.WidgetEventCameraTranslateForwardZ)
</code></pre>
<ol start="4">
<li>Use Endoscopy module</li>
</ol>
<p>Endoscopy module can move the camera along a curve. You can generate the curve by manually dropping points, or automatically using VMTK extension’s Extract Centerline module. Centerline extraction works very well for vasculature, intestines, etc. This method can be used alone or in combination with the above described methods.</p>
<ol start="5">
<li>Focus on markup control point</li>
</ol>
<p>You can focus the camera on any control point of a markups node by going to Markups module / Control points, right-click on the control point, and choose “Refocus all cameras”.</p>
<p>Would these options work for you? What kind of data are you visualizing?</p>

---

## Post #3 by @torquil (2021-01-13 20:02 UTC)

<p>Thanks! At the moment, method 1 is out because it needs special hardware. Method 2 is what I was already doing as a workaround. But I am very pleased with method 3 with the mousewheel. I have put the code into ~/.slicerrc.py to load it automatically.</p>
<p>The data I’m looking at are CT images of human cochleas with surroundings.</p>

---
