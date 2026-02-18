# How can I get camera position information?

**Topic ID**: 27067
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/how-can-i-get-camera-position-information/27067

---

## Post #1 by @dsa934 (2023-01-06 00:32 UTC)

<p>Operating system: window 11<br>
Slicer version: 4.13.0</p>
<p>Hi , everyone</p>
<p>I would like to know about camera coordinates, viewup vector, and focal point information based on the first time I ran 3d slicer.</p>
<p>so, I used follow code</p>
<p>viewNode = slicer.mrmlScene.GetSingletonNode(“1”, “vtkMRMLViewNode”)<br>
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode)<br>
print(cameraNode.GetPosition())</p>
<p>but result : 000001dd…_p_void</p>
<p>How can I get camera coordinates like [x,y,z] based on ras coordinates or view coordinates?</p>

---

## Post #2 by @lassoan (2023-01-06 04:19 UTC)

<p>It seems that a vector length hint was missing in the <code>GetPosition</code> call, therefore a raw pointer is returned. We’ll fix this. Until then you can use this syntax:</p>
<pre><code class="lang-python">p=[0,0,0]
cameraNode.GetPosition(p)
print(p)
</code></pre>
<p>Please use the current version of Slicer, especially for development.</p>

---

## Post #3 by @lassoan (2023-01-06 16:28 UTC)

<p>I’ve <a href="https://github.com/Slicer/Slicer/pull/6765">submitted a pull request</a> to add the missing size hints, which will make <code>GetPosition()</code> syntax work as expected. The fix will be available in the Slicer Preview Release within a few days.</p>

---
