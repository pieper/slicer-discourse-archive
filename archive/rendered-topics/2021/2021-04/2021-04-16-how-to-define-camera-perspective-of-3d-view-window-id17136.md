---
topic_id: 17136
title: "How To Define Camera Perspective Of 3D View Window"
date: 2021-04-16
url: https://discourse.slicer.org/t/17136
---

# How to define camera perspective of 3D view window

**Topic ID**: 17136
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/how-to-define-camera-perspective-of-3d-view-window/17136

---

## Post #1 by @deferd (2021-04-16 17:23 UTC)

<p>Hello</p>
<p>I am trying to control the perspective of an X-ray-like image generated from CT data. E.g., I would like to define the distance between the focal point and a specific anatomical feature and control the viewing angle so that the perspective (distortion) of the X-ray-like image is equal to an actual X-ray.</p>
<p>I am able to generate an image that looks quite similar to an x-ray (using volume rendering - CT-X-Ray properties) and I am able to zoom, rotate the viewing angle and change the focal axis with my mouse, however I am unable to quantify or define these values.</p>
<p>Is there a way to access this perspective information and to actively control them?</p>
<p>Thank you for your help</p>
<p>Best<br>
deferd</p>

---

## Post #2 by @mau_igna_06 (2021-04-16 18:56 UTC)

<p>Here is how I was able to do it:</p>
<pre><code class="lang-auto">viewNode = slicer.mrmlScene.GetSingletonNode("1", "vtkMRMLViewNode")
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode)
position = [0,0,0]
focalPoint = [20,20,20]
viewUpDirection = [0,1,0]
cameraNode.SetPosition(position)
cameraNode.SetFocalPoint(focalPoint)
cameraNode.SetViewUp(viewUpDirection)
</code></pre>

---

## Post #3 by @deferd (2021-04-19 07:14 UTC)

<p>Hello Mauro,</p>
<p>thank you for your fast response, your solution is extremely useful. I could further define the camera angle with:<br>
cameraNode.SetViewAngle().</p>
<p>Am I correct in assuming that the coordinates are global coordinates? And do you know if there is a simple way to transform these coordinates into metric measures?</p>
<p>Also, is there a way to access the coordinates of the camera position, focal point etc. after manual manipulation?</p>
<p>Best</p>

---

## Post #4 by @mau_igna_06 (2021-04-19 19:57 UTC)

<aside class="quote no-group" data-username="deferd" data-post="3" data-topic="17136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/aeb1de/48.png" class="avatar"> deferd:</div>
<blockquote>
<p>Am I correct in assuming that the coordinates are global coordinates? And do you know if there is a simple way to transform these coordinates into metric measures?</p>
</blockquote>
</aside>
<p>From what I know this coordinates are in RAS and longitudes are measured in mm.</p>
<aside class="quote no-group" data-username="deferd" data-post="3" data-topic="17136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/aeb1de/48.png" class="avatar"> deferd:</div>
<blockquote>
<p>Also, is there a way to access the coordinates of the camera position, focal point etc. after manual manipulation?</p>
</blockquote>
</aside>
<p>You can change “Set” by “Get” in the previous methods to get the information you want. I think you have to provide a list of lenght equal 3 as parameter of the function</p>

---
