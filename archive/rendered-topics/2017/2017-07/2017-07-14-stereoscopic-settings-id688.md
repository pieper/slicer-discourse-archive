---
topic_id: 688
title: "Stereoscopic Settings"
date: 2017-07-14
url: https://discourse.slicer.org/t/688
---

# Stereoscopic settings

**Topic ID**: 688
**Date**: 2017-07-14
**URL**: https://discourse.slicer.org/t/stereoscopic-settings/688

---

## Post #1 by @phil.dunn (2017-07-14 13:03 UTC)

<p>Hi, is there a way of changing the stereoscopic settings when viewing a 3D render in openGL mode? This would probably include changing the effective eye separation (or convergance angle), possibly setting the screen size and width. changing is the model zooms in Z or just scales in size at the same Z position.</p>
<p>Many thanks<br>
Phil</p>

---

## Post #2 by @lassoan (2017-07-14 14:02 UTC)

<p>You can modify the VTK camera parameters directly.</p>
<pre><code>view = layoutManager.threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
camera = cameraNode.GetCamera()
camera.SetEyeAngle(15)
</code></pre>
<p>See more examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras">Slicer script repository</a>.</p>

---
