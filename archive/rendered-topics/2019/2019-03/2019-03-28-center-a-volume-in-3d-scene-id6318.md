# Center a volume in 3D scene

**Topic ID**: 6318
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/center-a-volume-in-3d-scene/6318

---

## Post #1 by @Alex1 (2019-03-28 04:30 UTC)

<p>Hi, I want to center a certain volume in the 3D view. I tried<br>
layoutManager = slicer.app.layoutManager()<br>
threeDWidget = layoutManager.threeDWidget(0)<br>
threeDView = threeDWidget.threeDView()<br>
threeDView.resetFocalPoint()<br>
in the scripted repository, but I have more than one nodes in the scene and I don’t want to delete them, so it doesn’t work. Does anyone have any idea how to do this?</p>
<p>Thanks for your time!</p>

---

## Post #2 by @lassoan (2019-03-29 21:17 UTC)

<p>You don’t need to delete the nodes that you don’t want to include in the center computation, just temporarily hide them (<code>node.GetDisplayNode().SetVisibility(False)</code>).</p>

---

## Post #3 by @Alex1 (2019-03-31 02:14 UTC)

<p>Hi Andras,<br>
Thanks for your answer! I tried hiding them but it is still not at the center on the scene.<br>
If I have more than one volumes, even if I hide the others, the volume still won’t be at the center on the scene.<br>
What I want to know is how to center one specific volume while other volumes are still there.<br>
Thanks!</p>

---

## Post #4 by @lassoan (2019-03-31 04:17 UTC)

<p>You can center the camera on a node by basic VTK method calls. Something like this should work:</p>
<pre><code class="lang-auto">node = getNode('CTChest')
threedView = slicer.app.layoutManager().threeDWidget(0).threeDView()

# Get volume center
bounds=[0,0,0,0,0,0]
node.GetRASBounds(bounds)
nodeCenter = [(bounds[0]+bounds[1])/2, (bounds[2]+bounds[3])/2, (bounds[4]+bounds[5])/2]

# Shift camera to look at the new focal point
renderWindow = threedView.renderWindow()
renderer = renderWindow.GetRenderers().GetFirstRenderer()
camera = renderer.GetActiveCamera()
oldFocalPoint = camera.GetFocalPoint()
oldPosition = camera.GetPosition()
cameraOffset = [nodeCenter[0]-oldFocalPoint[0], nodeCenter[1]-oldFocalPoint[1], nodeCenter[2]-oldFocalPoint[2]]
camera.SetFocalPoint(nodeCenter)
camera.SetPosition(oldPosition[0]+cameraOffset[0], oldPosition[1]+cameraOffset[1], oldPosition[2]+cameraOffset[2])
</code></pre>

---
