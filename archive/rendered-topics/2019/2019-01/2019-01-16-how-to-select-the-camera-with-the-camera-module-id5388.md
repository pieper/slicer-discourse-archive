# How to select the camera with the camera module

**Topic ID**: 5388
**Date**: 2019-01-16
**URL**: https://discourse.slicer.org/t/how-to-select-the-camera-with-the-camera-module/5388

---

## Post #1 by @timeanddoctor (2019-01-16 16:29 UTC)

<p>I went display the camera1 in the view1 by script. I searched in the forum but found nothing.<br>
ID: vtkMRMLViewNode1<br>
Camera ID: vtkMRMLCameraNode2</p>

---

## Post #2 by @pieper (2019-01-16 21:29 UTC)

<p>It would be something like this.  If you go into the Dual 3D layout, rotate the views a bit, then go into the Developers-&gt;Cameras module you can play with it:</p>
<pre><code class="lang-auto">v = getNode('View1')
c = getNode('*Camera*')
c.SetActiveTag(v.GetID())
</code></pre>

---
