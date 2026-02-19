---
topic_id: 12586
title: "Disable Interaction With Camera"
date: 2020-07-16
url: https://discourse.slicer.org/t/12586
---

# Disable interaction with camera

**Topic ID**: 12586
**Date**: 2020-07-16
**URL**: https://discourse.slicer.org/t/disable-interaction-with-camera/12586

---

## Post #1 by @Eloi_gbrt (2020-07-16 22:02 UTC)

<p>Hello everyone,<br>
So I’m developping a module in python and at some point i need to move the camera around. For that I need to disable all the interaction that moves the camera around in the 3D view.<br>
My solution for now is to reach the interactor and to delete it until the module does not need it anymore. I use those few lines to achieve it :</p>
<p><span class="hashtag">#Copy</span> original interactor<br>
self.interactorStyle = slicer.app.layoutManager().threeDWidget(0).threeDView().interactorStyle()<br>
self.interactor = self.interactorStyle.GetInteractor()<br>
<span class="hashtag">#Delete</span> the interactor<br>
self.interactorStyle.SetInteractor(None)<br>
<span class="hashtag">#Reset</span> the interactor<br>
self.interactorStyle.SetInteractor(self.interactor)</p>
<p>It works for now but i’m afraid that it could interfere with other modules or cause problem with slicer directly.<br>
I tried to find some other functions on vtkInteractorStyle but none seemed to work as i wanted.</p>
<p>Is there a way to achieve what i did directly in slicer or with a function i would have missed ?</p>
<p>Thank you.<br>
Eloi</p>

---

## Post #2 by @lassoan (2020-07-16 22:31 UTC)

<p>There is a proper interface to customize what mouse gestures you enable on every view. Here is an example in the script repository for slice views that works the same way for 3D views with small adjustments: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Disable_certain_user_interactions_in_slice_views</a></p>

---

## Post #3 by @Eloi_gbrt (2020-07-17 23:01 UTC)

<p>Yes, i saw this example and tried to adapt it but i did not find a documentation to use SetActionEnabled().</p>

---

## Post #4 by @lassoan (2020-07-17 23:26 UTC)

<p>If you search for “SetActionEnabled” in Slicer’s source code or API documentation to find the usable values:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82" target="_blank" rel="noopener">Slicer/Slicer/blob/47deb76d7556e40de4e25e585c4b24a63a153da5/Libs/MRML/DisplayableManager/vtkMRMLSliceViewInteractorStyle.h#L69-L82</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="69" style="counter-reset: li-counter 68 ;">
<li>Translate = 1,</li>
<li>Zoom = 2,</li>
<li>Rotate = 4, /* Rotate not currently used */</li>
<li>Blend = 8, /* fg to bg, labelmap to bg */</li>
<li>AdjustWindowLevelBackground = 16,</li>
<li>AdjustWindowLevelForeground = 32,</li>
<li>BrowseSlice = 64,</li>
<li>ShowSlice = 128,</li>
<li>AdjustLightbox = 256, /* not used */</li>
<li>SelectVolume = 512,</li>
<li>SetCursorPosition = 1024, /* adjust cursor position in crosshair node as mouse is moved */</li>
<li>SetCrosshairPosition = 2048,</li>
<li>TranslateSliceIntersection = 4096,</li>
<li>RotateSliceIntersection = 8192,</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @atracsys-sbt (2021-09-08 14:54 UTC)

<p>Sorry to re-open this topic, but I don’t undestand the proposed solution since <code>vtkMRMLThreeDViewInteractorStyle</code> has no <code>SetActionEnabled</code> function.<br>
Also, <code>vtkMRMLThreeDViewInteractorStyle::EnabledOff()</code> and <code>vtkMRMLThreeDViewInteractorStyle::Off()</code> do not deactivate interaction with the 3D scene.<br>
So, how does one disable interaction in a 3D view ?</p>

---

## Post #6 by @lassoan (2021-09-08 14:59 UTC)

<p><code>SetActionEnabled</code> was added at the time when keyboard&amp;mouse gestures were hardcoded and we needed a way to disable some. Now you can add/remove/edit all keyboard&amp;mouse gestures - see for example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers">here</a>. <code>SetActionEnabled</code> method is only kept for backward compatibility, but I would not recommend using them anymore.</p>

---

## Post #7 by @atracsys-sbt (2021-09-08 15:20 UTC)

<p>I see, but if I were to follow this example, disabling all interaction would require to set all events of the camerawidget to <code>vtk.vtkWidgetEvent.NoEvent</code>, right ? Given the number of interactions possible in vtkCommand, this will be quite long (unless I could loop on it). Isn’t there a simpler way ?</p>

---

## Post #8 by @lassoan (2021-09-08 15:26 UTC)

<p>In general, it is not expected that a module disables all other modules. You are always expected to know what features you disable and why. You might be able to implement some simpler hacks, such as adding an observer to the interactor for all interaction events with very high priority that consumes all the events (as it is done in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L2625-L2727">Segment Editor</a>, which was implemented before the widget infrastructure was in place).</p>
<p>Why do you need to disable all interactions?</p>

---

## Post #9 by @atracsys-sbt (2021-09-08 15:31 UTC)

<p>I’m displaying a frustum in 3D from a very specific point of view, so I don’t want the user to be able to move the camera and change that point of view.<br>
Also, I’m using parallel projection for the camera and mouse-wheel zooming turns it off for some reason (if it’s a bug I’ll open a new separate ticket).</p>

---

## Post #10 by @lassoan (2021-09-08 15:43 UTC)

<blockquote>
<p>I’m displaying a frustum in 3D from a very specific point of view, so I don’t want the user to be able to move the camera and change that point of view.</p>
</blockquote>
<p>Then disabling camera translation &amp; rotation may make sense. You may still want to allow right-click menu, etc. so it makes sense not to disable all interactions.</p>
<aside class="quote no-group" data-username="atracsys-sbt" data-post="9" data-topic="12586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atracsys-sbt/48/11434_2.png" class="avatar"> atracsys-sbt:</div>
<blockquote>
<p>Also, I’m using parallel projection for the camera and mouse-wheel zooming turns it off for some reason (if it’s a bug I’ll open a new separate ticket).</p>
</blockquote>
</aside>
<p>Mouse wheel should not change camera projection, so it that happens then it is a bug. I tried this and for me the view is zoomed in/out with mouse wheel correctly (without changing projection mode).</p>

---

## Post #11 by @atracsys-sbt (2021-09-08 15:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Then disabling camera translation &amp; rotation may make sense. You may still want to allow right-click menu, etc. so it makes sense not to disable all interactions.</p>
</blockquote>
</aside>
<p>Ok, I’ll try to find a way to disable only the necessary.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Mouse wheel should not change camera projection, so it that happens then it is a bug. I tried this and for me the view is zoomed in/out with mouse wheel correctly (without changing projection mode).</p>
</blockquote>
</aside>
<p>I’m able to reproduce the bug with:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderer = renderWindow.GetRenderers().GetItemAsObject(0)
camera = renderer.GetActiveCamera()
camera.ParallelProjectionOn()
</code></pre>

---

## Post #12 by @lassoan (2021-09-08 16:15 UTC)

<aside class="quote no-group" data-username="atracsys-sbt" data-post="11" data-topic="12586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atracsys-sbt/48/11434_2.png" class="avatar"> atracsys-sbt:</div>
<blockquote>
<p>I’m able to reproduce the bug with:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderer = renderWindow.GetRenderers().GetItemAsObject(0)
camera = renderer.GetActiveCamera()
camera.ParallelProjectionOn()
</code></pre>
</blockquote>
</aside>
<p>I see, this is not a bug, but it is due to that camera projection mode is defined in vtkMRMLViewNode. If you change it in the camera VTK object then the view node will restore it to the stored value at the next update. I agree that this can be unexpected and it is probably like this due to historical reasons. You could <a href="https://issues.slicer.org/">file an enhancement request</a> to change this (i.e., only store projection mode in the camera node, not in the view node).</p>

---

## Post #13 by @atracsys-sbt (2021-09-09 07:35 UTC)

<p>The enhancement request has been posted <a href="https://github.com/Slicer/Slicer/issues/5841" rel="noopener nofollow ugc">here</a>.</p>

---
