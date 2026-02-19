---
topic_id: 6432
title: "Questions About Virtual Reality Implementation On Slicer"
date: 2019-04-08
url: https://discourse.slicer.org/t/6432
---

# Questions about Virtual Reality Implementation on Slicer

**Topic ID**: 6432
**Date**: 2019-04-08
**URL**: https://discourse.slicer.org/t/questions-about-virtual-reality-implementation-on-slicer/6432

---

## Post #1 by @triple_axel (2019-04-08 14:23 UTC)

<p>Hi, I have a few questions about Virtual Reality Implementation on Slicer</p>
<ol>
<li>I have a volume rendering that will not appear on Virtual Reality even though it appears on my 3D views. Why is this so and how do I fix it?<br>
Ex: Perspective from Slicer Desktop:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d96e08ba007e4b06dd4586898f2bf2754c5b1c31.jpeg" alt="image" data-base62-sha1="v1tmchxUn0YWzL8ZqDQjb5Cadq1" width="595" height="381"></li>
</ol>
<p>Perspective from Slicer Virtual Reality:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6c84ead167459145e316369b16d71da38afd2ea.png" alt="image" data-base62-sha1="zd8C4ZIoPTqoLeVDvGM5FqmaEYO" width="680" height="317"></p>
<ol start="2">
<li>
<p>Is there any way to implement segmentation via Virtual Reality (ex: using the remote to segment)?</p>
</li>
<li>
<p>I cannot see my Oculus touch controllers in Slicer, making it difficult to move around segmentations. Is there a setting I can change to make them visible?</p>
</li>
</ol>

---

## Post #2 by @cpinter (2019-04-08 14:42 UTC)

<ol>
<li>
<p>I had issues like this in past versions (4.9) when the display node of the volume rendering did not have the VR view included (VR view node ID was not in ViewNodeIDs). Try to create the scene from scratch in 4.10.1.</p>
</li>
<li>
<p>We want this a lot too. The main task that needs to be done first is to allow using Qt GUIs in VR in an easy way (see this <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/43" rel="nofollow noopener">ticket</a>). We’re planning to work on this over the summer. Contributions are welcome! Let us know if you’re considering participating in this effort.</p>
</li>
<li>
<p>The ControllerModelsVisible flag in vtkMRMLVirtualRealityViewNode controls the visibility. You can turn it on/off from the GUI using the “Controllers visible” checkbox in the Virtual Reality module. Again, please use 4.10.1.</p>
</li>
</ol>
<p>I hope this helps!</p>

---

## Post #3 by @triple_axel (2019-04-08 16:09 UTC)

<p>Thanks for the prompt reply.<br>
2) I will continue to follow the development of the VR segmentation tool. Sounds very cool and would be very helpful!</p>
<p>In regards to 1) and 3), I am currently working on slicer 4.10.1 but I still do not see any virtual reality view of the controller models (after checking off the “Controllers visible checkbox”) nor the volume rendering, even after restarting the app and recreating the scene. I have also downloaded the latest nightly version of Slicer 4.11.0 and still do not see the volume rendering nor controller models. Am I missing a step?</p>

---

## Post #4 by @lassoan (2019-04-08 18:11 UTC)

<p>Make sure you updated to the latest version of SlicerVirtualReality extension (you can check for updates and then install updates in the extension manager).</p>
<aside class="quote no-group" data-username="triple_axel" data-post="3" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>I still do not see any virtual reality view of the controller models</p>
</blockquote>
</aside>
<p>Controller display works fine for me for Windows Mixed Reality headsets and HTC Vive. I don’t have access to an Oculus Rift, but if for any reason you don’t see the controllers, you can always show where the controller is by enabling controller transforms and then applying the transforms to any models.</p>
<aside class="quote no-group" data-username="triple_axel" data-post="3" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>nor the volume rendering, even after restarting the app and recreating the scene</p>
</blockquote>
</aside>
<p>Volume rendering works fine for me for Windows Mixed Reality headsets and HTC Vive. Can you share an example scene that has volume rendering that does not show up in virtual reality?</p>

---

## Post #5 by @triple_axel (2019-04-08 18:50 UTC)

<p>I have attached an example scene in gdocs:<br>
<a href="https://drive.google.com/file/d/16FwaOCQseLVeWhtq9ytA9ofcI-g331ej/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/16FwaOCQseLVeWhtq9ytA9ofcI-g331ej/view?usp=sharing</a></p>
<p>How do I enable the controller transforms? They are visible on slicer as seen below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c646a681382fb1976cf86581d3801d8115c1d356.png" alt="image" data-base62-sha1="si1UekcflPJMXkziB8VTzHRwSSW" width="493" height="449"><br>
, however turning on and off the view does nothing. If I apply the controller transform to the models I am still unable to see the controllers.</p>
<p>Thanks for the help.</p>

---

## Post #6 by @lassoan (2019-04-09 04:06 UTC)

<aside class="quote no-group" data-username="triple_axel" data-post="3" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>I have also downloaded the latest nightly version of Slicer 4.11.0 and still do not see the volume rendering</p>
</blockquote>
</aside>
<p>In your scene, Volume Rendering is hidden in the virtual reality view. You can enable it in Volume rendering module / Inputs section / View:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5d2158b35c079f1f5ec48af0c97fb5ad35d83d.png" alt="image" data-base62-sha1="mapxoiT5pjgwRKmsHq7hN2yiyvz" width="524" height="358"></p>
<aside class="quote no-group" data-username="triple_axel" data-post="3" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>I still do not see any virtual reality view of the controller models</p>
</blockquote>
</aside>
<p>As I wrote above, enable controller transforms (they appear in the scene, so you’ve done this correctly), but then don’t click on the eye icon of the transform (that would visualize the transform if you specify a region of interest), instead load any model (STL, OBJ, … file) that you would like to use as controller model and apply the controller transform to that.</p>
<p>By the way, is there a particular reason you chose an Oculus Rift headset? If you need high quality (absolute tracking, additional controllers, high resolution, etc.) then HTC Vive headsets are better, if you need something inexpensive or easily portable (no need for external trackers) then Windows Mixed Reality headsets are better.</p>

---

## Post #7 by @triple_axel (2019-04-09 13:28 UTC)

<p>Thank you so much for all the help! The reason I’m using Oculus is because I’m borrowing it temporarily from someone else to explore the virtual reality feature on slicer.</p>

---

## Post #8 by @triple_axel (2019-04-10 14:25 UTC)

<p>Hi, sorry I had another question about the views. Is there a way through Python to automatically set views to include the “virtual reality view”? I’ve attempted to do it with getting the volume rendering node:<br>
volumeRendering = slicer.mrmlScene.GetNodesByName(‘GPURayCastVolumeRendering’).GetItemAsObject(0)</p>
<p>and setting the view of the volume rendering node like so:<br>
volumeRendering.SetViewNodeIDs(vrViewNodeID)</p>
<p>however, doing so does nothing. I’ve also noticed the vrViewNodeID is different from a regular view node ID (vtkMRMLVirtualRealityViewNode vs. vtkMRMLViewNode). Is there anyway to do this?</p>

---

## Post #9 by @cpinter (2019-04-10 15:07 UTC)

<aside class="quote no-group" data-username="triple_axel" data-post="8" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e56c9b/48.png" class="avatar"> triple_axel:</div>
<blockquote>
<p>and setting the view of the volume rendering node like so:<br>
volumeRendering.SetViewNodeIDs(vrViewNodeID)</p>
</blockquote>
</aside>
<p>This should not work, and you probably got an error as well. Instead, call AddViewNodeID</p>

---

## Post #10 by @triple_axel (2019-04-17 18:33 UTC)

<p>Thanks for the help,</p>
<p>Just wanted to write an update for this that I wrote a small work around for the “eraser effect” in Virtual Reality (in the meantime before you integrate the Qt GUIs in VR).  Through this code, a  sphere segmentation is created in VR that gets transformed to the right hand controller. Then, when I move the sphere  around and it intersects with a part of a segmentation that needs to be erased (ie the spine) , I press a button on the keyboard that erases it (by using “subtract” in the “logical operators” effect). What I am wondering is that every time I press this button on the keyboard the Virtual Reality screen goes black for 1-3 seconds before an altered scene is shown. Is there anyway to fix this or is this inevitable as Slicer is running background processes?</p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2019-04-17 19:03 UTC)

<p>The problem should go away if the segmentation is updated more quickly. For example, you can disable smoothing (checkbox in “Show 3D” button’s drop-down menu) to make 3D view updates magnitudes faster.</p>

---

## Post #12 by @lassoan (2019-09-12 01:42 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-operation-takes-too-long-for-virtual-reality/8394">Segmentation operation takes too long for virtual reality</a></p>

---

## Post #13 by @Nicholas.jacobson (2020-01-09 04:19 UTC)

<p>We are looking to be able to control the ROI in VR with controllers. Has anyone been able to figure out visualizing and controlling the ROI in VR space?</p>

---

## Post #14 by @lassoan (2020-01-09 04:42 UTC)

<p>You can move the ROI without any programming, by adding a model that the user can grab and set the same parent transform for the model and the ROI.</p>
<p>If you also need to change the ROI size with the controllers then one option is to add a few models to the scene (each serve as handles that can be grabbed and moved using the controllers) and implement a small python script that adjust the ROI position/size based on parent transforms of these handles.</p>

---

## Post #15 by @Biomodelos_3D (2021-01-09 03:22 UTC)

<p>Hi, this is for <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a>:<br>
Are you familiar with Tom Goddard’s ChimeraX software? It’s an Open Source software designed for chemical purposes, but it can handle DICOM images (including some limited Volume Rendering and Surface features) and has the best virtual reality module I’ve seen so far. ChimeraX can somehow display floating standard menus in the VR environment, so you can access any command you want, and interact with them in real time inside VR (including configuration of Volume Render histograms, etc.). Is it possible to reach this kind of staff in 3D Slicer in the near future?<br>
ChimeraX has very limited Volume Render and Surface Segmentation capabilities, I imagine a sort of mutual collaboration to improve both developments… what you think?</p>

---

## Post #16 by @lassoan (2021-01-09 04:09 UTC)

<p>These features are already available in VTK’s virtual reality interface and we are ready to take advantage of it. We just need to update to latest VTK version, which is taking longer than anticipated (it is a work in progress, see the list of open issues <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+label%3Adomain%3Avtk9">here</a>). I would expect that the update will be completed in a couple of weeks. After that it should not take more than a few weeks of work to make the menus available in virtual reality, but I’m not sure when the work will start. <a class="mention" href="/u/cpinter">@cpinter</a> and I have always several projects to work on, but may still find time. Things can go much faster if you can join the efforts or anyone else show up who would be interested to contribute.</p>
<p>Slicer’s virtual reality support is actually very powerful and flexible (all Slicer features are available and there are additional features that are only available in the immersive view), it is just not possible to activate things from the immersive view yet. So, the missing piece is really just a convenient immersive GUI.</p>

---

## Post #17 by @Biomodelos_3D (2021-01-09 14:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="6432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Things can go much faster if you can join the efforts or anyone else show up who would be interested to contribute</p>
</blockquote>
</aside>
<p>Andras, off course I want to contribute, unfortunately I don´t know anything about programming, but will be glad to help on any other matter at my reach. I’m using a standard Oculus Rift with two sensors. Eventually I can have access to an HTC Vive, but Oculus is much more practical.</p>

---

## Post #18 by @cpinter (2021-01-11 10:29 UTC)

<p>Just to confirm what <a class="mention" href="/u/lassoan">@lassoan</a> has already said: after some technical hurdles the very next thing in SlicerVR will be the floating menus (see <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/43">here</a>). We wanted to do this for almost two years now, but now that VTK9 is integrated with Slicer, we need to hammer out a few details and then we can work on the in-VR UI. Please note that there is no dedicated funding for this, so it will be done in our free time, so you may need to be patient even though this is a project I’d really love to work on. As an alternative you can help get funding in which case please contact me.</p>

---
