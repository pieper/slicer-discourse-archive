---
topic_id: 5309
title: "Can I Have Two Endoscope Fly Window With Dual 3D"
date: 2019-01-08
url: https://discourse.slicer.org/t/5309
---

# Can I have two endoscope fly-window with dual 3D

**Topic ID**: 5309
**Date**: 2019-01-08
**URL**: https://discourse.slicer.org/t/can-i-have-two-endoscope-fly-window-with-dual-3d/5309

---

## Post #1 by @timeanddoctor (2019-01-08 14:03 UTC)

<p>I am going to have two 3d fly-window just like right-left eye. Firstly, I am planing to create dual contacting endoscope windows.<br>
can I have two endoscope<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8430da977b86d3fc420e29fccf184ed907c94c64.jpeg" data-download-href="/uploads/short-url/iRpH5JQc5GW9NjxXjxImthWm9hi.jpeg?dl=1" title="2019-01-08_214751" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8430da977b86d3fc420e29fccf184ed907c94c64_2_690x302.jpeg" alt="2019-01-08_214751" data-base62-sha1="iRpH5JQc5GW9NjxXjxImthWm9hi" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8430da977b86d3fc420e29fccf184ed907c94c64_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8430da977b86d3fc420e29fccf184ed907c94c64_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8430da977b86d3fc420e29fccf184ed907c94c64_2_1380x604.jpeg 2x" data-dominant-color="BDB0CE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-01-08_214751</span><span class="informations">1917×840 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-01-08 19:38 UTC)

<p>Hi -</p>
<p>The Endoscopy module was one of the first (maybe even the very first) scripted module in Slicer 4, so it doesn’t have all the things we might want.  So unless it gets reworked, it only supports a single flythrough setup and the state is not saved with the mrml scene.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @wpgao (2019-01-09 10:39 UTC)

<p>You can create two parallel trajectories for two cameras respectively. The motion of two cameras should be synchronous. Modified scripted module is required to achieve this!</p>

---

## Post #4 by @timeanddoctor (2019-01-09 15:21 UTC)

<p>Thanks <a href="https://discourse.slicer.org/u/pieper">Steve Pieper</a>.<br>
can I change the self-detection code to achieve my aim</p>
<pre><code>#  Remove previous observer
if self.cameraNode and self.cameraNodeObserverTag:
  self.cameraNode.RemoveObserver(self.cameraNodeObserverTag)
if self.camera and self.cameraObserverTag:
  self.camera.RemoveObserver(self.cameraObserverTag)

newCamera = None
if newCameraNode:
  newCamera = newCameraNode.GetCamera()
  # Add CameraNode ModifiedEvent observer
  self.cameraNodeObserverTag = newCameraNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.onCameraNodeModified)
  # Add Camera ModifiedEvent observer
  self.cameraObserverTag = newCamera.AddObserver(vtk.vtkCommand.ModifiedEvent, self.onCameraNodeModified)

self.cameraNode = newCameraNode
self.camera = newCamera

# Update UI
self.updateWidgetFromMRML()
</code></pre>
<p>def updateWidgetFromMRML(self):<br>
if self.camera:<br>
self.viewAngleSlider.value = self.camera.GetViewAngle()<br>
if self.cameraNode:<br>
pass</p>

---

## Post #5 by @timeanddoctor (2019-01-09 15:22 UTC)

<p>Thank you very much!<br>
can you help me ?</p>

---

## Post #6 by @timeanddoctor (2019-01-09 15:29 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/3dprintingdoctor/endoscope">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/3dprintingdoctor/endoscope" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d5f0a6f66f01738cc04fc2c40fe89c226b642de4347bb8d3d8f4be98c5cdb602/3dprintingdoctor/endoscope" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/3dprintingdoctor/endoscope" target="_blank" rel="noopener nofollow ugc">GitHub - 3dprintingdoctor/endoscope</a></h3>

  <p>Contribute to 3dprintingdoctor/endoscope development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @pieper (2019-01-09 20:00 UTC)

<p>Hi <a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> -</p>
<p>It’s great if you want to try this out - I see you already have a fork of Slicer in your github account.  If you start developing from there it will be easy to create “diff” links that show what edits you have made and people here can comment.</p>
<p>Best,<br>
Steve</p>

---

## Post #8 by @timeanddoctor (2019-01-14 03:25 UTC)

<p>I add “second cameranode” and “eyesAngleSlider” widget. And I have some troubles now.</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/3dprintingdoctor/Slicer/commit/e2f845bd4b019076a62e345095562cb4147cfe11">
  <header class="source">

      <a href="https://github.com/3dprintingdoctor/Slicer/commit/e2f845bd4b019076a62e345095562cb4147cfe11" target="_blank" rel="noopener nofollow ugc">github.com/3dprintingdoctor/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/3dprintingdoctor/Slicer/commit/e2f845bd4b019076a62e345095562cb4147cfe11" target="_blank" rel="noopener nofollow ugc">add "second cameranode" and "eyesAngleSlider"</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-01-12" data-time="04:25:33" data-timezone="UTC">04:25AM - 12 Jan 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/3dprintingdoctor" target="_blank" rel="noopener nofollow ugc">
          <img alt="3dprintingdoctor" src="https://avatars.githubusercontent.com/u/46531341?v=4" class="onebox-avatar-inline" width="20" height="20">
          3dprintingdoctor
        </a>
      </div>

      <div class="lines" title="changed 1 files with 26 additions and 4 deletions">
        <a href="https://github.com/3dprintingdoctor/Slicer/commit/e2f845bd4b019076a62e345095562cb4147cfe11" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+26</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">add "second cameranode" and "eyesAngleSlider", While I donnot know how to do it <span class="show-more-container"><a href="https://github.com/3dprintingdoctor/Slicer/commit/e2f845bd4b019076a62e345095562cb4147cfe11" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">next..discribled here:
https://discourse.slicer.org/t/can-i-have-two-endoscope-fly-window-with-dual-3d/5309/7</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
First, did I should change the variable name from “cameraNodeSelector” to “cameraNodeSelector1” for Camera1.<br>
# Camera node second selector<br>
cameraNodeSelector = slicer.qMRMLNodeComboBox()<br>
cameraNodeSelector.objectName = ‘cameraNodeSelector’<br>
cameraNodeSelector.toolTip = “Select a camera that will fly along this path.”<br>
cameraNodeSelector.nodeTypes = [‘vtkMRMLCameraNode’]<br>
cameraNodeSelector.noneEnabled = False<br>
cameraNodeSelector.addEnabled = False<br>
cameraNodeSelector.removeEnabled = False<br>
cameraNodeSelector.connect(‘currentNodeChanged(bool)’, self.enableOrDisableCreateButton)<br>
cameraNodeSelector.connect(‘currentNodeChanged(vtkMRMLNode*)’, self.setCameraNode)<br>
pathFormLayout.addRow(“Camera:”, cameraNodeSelector)<br>
self.parent.connect(‘mrmlSceneChanged(vtkMRMLScene*)’,<br>
cameraNodeSelector, ‘setMRMLScene(vtkMRMLScene*)’)</p>
<p>Second, the eyesAngleSlider seems wrong.</p>
<pre><code>	# View angle of left-right eyes slider 
    eyesAngleSlider = ctk.ctkSliderWidget()
    eyesAngleSlider.connect('valueChanged(double)', self.eyesAngleSliderValueChanged)
    eyesAngleSlider.decimals = 0
    eyesAngleSlider.minimum = 1
    eyesAngleSlider.maximum = 60
    flythroughFormLayout.addRow("eyes Angle:", eyesAngleSlider)
</code></pre>

---

## Post #9 by @timeanddoctor (2019-01-14 03:28 UTC)

<p>Can I create a “Transform” between the “Camera” and “Camera1” to have a Synchronize-Fly-window.</p>

---

## Post #10 by @lassoan (2019-01-14 04:18 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> worked on synchronizing camera views. I think there is a solution for setting relative transforms between cameras but I don’t remember how it can be configured.</p>

---
