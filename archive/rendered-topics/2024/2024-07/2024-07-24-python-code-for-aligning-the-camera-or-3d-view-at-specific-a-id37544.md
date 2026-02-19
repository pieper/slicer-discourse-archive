---
topic_id: 37544
title: "Python Code For Aligning The Camera Or 3D View At Specific A"
date: 2024-07-24
url: https://discourse.slicer.org/t/37544
---

# Python code for aligning the camera or 3D view at specific angle

**Topic ID**: 37544
**Date**: 2024-07-24
**URL**: https://discourse.slicer.org/t/python-code-for-aligning-the-camera-or-3d-view-at-specific-angle/37544

---

## Post #1 by @uday_15 (2024-07-24 12:33 UTC)

<p>Can I have code for aligning the camera node or 3D view at specific angle. More specific, I have three points and want to align the camera node or 3D view such that the plane created through those three points should be visible just as line in 3D view or those three points should be visible colinear.</p>

---

## Post #2 by @JASON (2024-07-24 22:00 UTC)

<p><a class="mention" href="/u/uday_15">@uday_15</a> You can access the camera and change it’s position like this:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
camera = threeDView.cameraNode()
camera.SetPosition( yourCamCoord  )
camera.SetFocalPoint( yourCamTargetCoord )
</code></pre>
<p>You could SetFocalPoint to one of your points and use the vector to a second point for the camera position, just modify the magnitude for your preferred camera distance.</p>
<p>More info on camera API:<br>
<a href="https://apidocs.slicer.org/v4.8/classvtkMRMLCameraNode.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/v4.8/classvtkMRMLCameraNode.html</a></p>

---
