---
topic_id: 47552
title: "Stereo Off-Axis Projection and Mouse Interactions"
date: 2026-07-06
url: https://discourse.slicer.org/t/47552
last_bumped: 2026-07-14T18:22:48.277Z
---

# Stereo Off-Axis Projection and Mouse Interactions

**Topic ID**: 47552
**Date**: 2026-07-06
**URL**: https://discourse.slicer.org/t/stereo-off-axis-projection-and-mouse-interactions/47552

---

## Post #1 by @LucasP (2026-07-06 18:31 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance. But I’m still human</p>
</blockquote>
<p>Hi,</p>
<p>I’m new to 3D Slicer and VTK. I am trying to build a “virtual window” effect using a custom stereo display that gives me real-time <code>viewDistance</code> and <code>eyeSeparation</code>.</p>
<p>My goal is to let the user interact normally with the 3D volume using standard mouse controls (rotate, pan, zoom). From my understanding, to achieve this “virtual window” effect while preserving standard mouse interactions, the physical screen coordinates must dynamically track the camera: the screen center should sit exactly at the camera position, and the <code>EyePosition</code> should be placed behind it (<code>camera.GetPosition() - viewDist * dop</code>).</p>
<p>However, as soon as <code>camera.SetUseOffAxisProjection(True)</code> is invoked, it feels like <code>ViewUp</code> is locked, and the user can no longer rotate the camera, only translate it. This leads to broken math on my side during mouse movements.</p>
<p>Here is how I’m updating the frustrum :</p>
<pre><code class="lang-auto">  layoutManager = slicer.app.layoutManager()
  threeDWidget = layoutManager.threeDWidget(0)
  renderWindow = threeDWidget.threeDView().renderWindow()
  renderer = renderWindow.GetRenderers().GetFirstRenderer()
  camera = renderer.GetActiveCamera()
  p = self.stereoParams
  pixelPitch = p['pixelPitch'] # unit : meter
  viewDist = p['viewDistance'] # Distance User to screen (m)
  eyeSeparation = p['eyeSeparation'] # IPD (m)

  viewportSizePx = renderWindow.GetSize()
  if viewportSizePx[0] &lt;= 0 or viewportSizePx[1] &lt;= 0:
      return # Window minimized or invalid
  
  viewportWidth = viewportSizePx[0] * pixelPitch # viewport width (m)
  viewportHeight = viewportSizePx[1] * pixelPitch # viewport height (m)
  halfW = viewportWidth / 2.0
  halfH = viewportHeight / 2.0

  up = np.array(camera.GetViewUp())
  dop = np.array(camera.GetDirectionOfProjection())
  cam = np.array(camera.GetPosition())

  right = np.cross(dop, up)
  rMag = np.linalg.norm(right)
  right /= rMag

  bl = cam - halfW * right - halfH * up
  br = cam + halfW * right - halfH * up
  tr = cam + halfW * right + halfH * up

  camera.SetUseOffAxisProjection(True)
  camera.SetScreenBottomLeft(bl)
  camera.SetScreenBottomRight(br)
  camera.SetScreenTopRight(tr)
  camera.SetEyePosition(camera.GetPosition()- viewDist * dop)
  camera.SetEyeSeparation(eyeSeparation)
</code></pre>
<p>It seems that I’m not doing things right.<br>
Is there any documentation or existing examples on implementing off-axis projection with dynamic screen coordinates within Slicer?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @mau_igna_06 (2026-07-07 14:21 UTC)

<p>From a quick read to the code I think you forgot to use the set methods for the camera (e.g. <code>SetViewUp</code>, <code>SetDirectionOfProjection</code>, <code>SetPosition</code>)</p>

---

## Post #3 by @LucasP (2026-07-07 14:57 UTC)

<p>Hi Mauro,</p>
<p>Thanks for the reply!</p>
<p>From my undestanding Slicer’s mouse interactor is dynamically updating the camera’s <code>Position</code>, <code>ViewUp</code>, and <code>DirectionOfProjection</code> as the user interacts, and my code reads those updates to dynamically recalculate the screen coordinates.</p>
<p>The core issue is that as soon as <code>SetUseOffAxisProjection(True)</code> is enabled, the mouse interactor loses the ability to rotate the camera and the <code>ViewUp</code> vector becomes completely locked. Only translation continues to work.</p>
<p>It feels like VTK’s internal off-axis calculations are fighting or overriding the interactor’s ability to modify the camera orientation. Is there a specific way to configure the interactor style or the camera so that rotation updates are still processed properly in off-axis mode?</p>

---

## Post #4 by @lassoan (2026-07-13 11:18 UTC)

<p>If you just want to do since quick testing in python then you can add an observer with high priority that captures and consumes mouse move and button events. If you want to have a proper solution then you probably need to investigate what happens exactly in the mouse event handler in C++.</p>

---

## Post #5 by @Tomas_Gomes (2026-07-14 18:22 UTC)

<p>Hello Mr.Andras Lasso!</p>
<p>My name is Tomás. I´m a Medical Student from Portugal and I´m currently exploring the 3D Slicer app and it´s extensions for CT scan images of the spine. I am new on this 3D Slicer forum, so I wasn´t able to send you a message. Is it possible to ask you some questions via e-mail or even in this forum through direct messaging if feasible? Thank you for your time in advance!</p>

---
