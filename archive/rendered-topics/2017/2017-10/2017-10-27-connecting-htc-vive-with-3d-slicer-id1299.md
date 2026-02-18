# Connecting HTC vive with 3D slicer

**Topic ID**: 1299
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/connecting-htc-vive-with-3d-slicer/1299

---

## Post #1 by @Huda1 (2017-10-27 06:59 UTC)

<p>Can I connect 3D Slicer with HTC viv via a module ?<br>
Where can I find this module ?</p>

---

## Post #2 by @jcfr (2017-10-27 07:03 UTC)

<p>Hi <span class="mention">@Huda_Al_Mubarak</span>,</p>
<p>We are finalizing a Slicer extension integrating the <code>vtkRenderingOpenVR</code> module. Once we are done, you will be to install the extension on windows.</p>
<p>This should allow you to:</p>
<ul>
<li>represent the Slicer scene in both the 3D View and the OpenVR</li>
<li>update fiducial, model, volume rendering in Slicer and have the OpenVR updated</li>
<li>move Slicer objects in OpenVR and have the Slicer scene updated</li>
</ul>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/2afd9df8cb63c856ca5133fc5a8e178d30b6f8baf8885014677a5f24bb99d53d/KitwareMedical/SlicerVirtualReality" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerVirtualReality" target="_blank" rel="noopener">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables...</a></h3>

  <p>A Slicer extension that enables user to interact with a Slicer scene using virtual reality. - GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a S...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Huda1 (2017-10-27 07:11 UTC)

<p>That’s great !<br>
but is there another one that I can use now?<br>
I need an available module for my Senior Design Project</p>

---

## Post #4 by @jcfr (2017-10-27 07:26 UTC)

<p>You could try to build the extension and report feedback, in its current state it should still allow you to load object in the OpenVR context.</p>
<p>But note that it is still work in progress, we expect to have a version of the extension available for download ideally in the next 2 weeks.</p>
<p>Cc: <a class="mention" href="/u/jbvimort">@jbvimort</a></p>

---

## Post #5 by @Huda1 (2017-10-27 07:45 UTC)

<p>This is good.<br>
From where can I try it ?</p>

---

## Post #6 by @amirjaber (2018-02-08 06:00 UTC)

<p>Thanks Christophe,<br>
I want to know if your module development is completed. I have some questions about the viewer:<br>
1- Does it support dashboard overlay for GUI inside VR.<br>
2- I heard Microsoft MR headsets support OpenVR, Can I use them with this module. (or Rift)<br>
3- Based on your experience, is it fair to say visualizing medical images is faster with VTK implementation vs Unity implementations?<br>
I appreciate your help,</p>

---

## Post #7 by @cpinter (2018-02-08 16:42 UTC)

<aside class="quote no-group" data-username="amirjaber" data-post="6" data-topic="1299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b9e5f3/48.png" class="avatar"> amirjaber:</div>
<blockquote>
<p>1- Does it support dashboard overlay for GUI inside VR.</p>
</blockquote>
</aside>
<p>Not yet. It will be added later.</p>
<aside class="quote no-group" data-username="amirjaber" data-post="6" data-topic="1299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b9e5f3/48.png" class="avatar"> amirjaber:</div>
<blockquote>
<p>I heard Microsoft MR headsets support OpenVR, Can I use them with this module. (or Rift)</p>
</blockquote>
</aside>
<p>I tried to make it work with Windows Mixed Reality, but I had very limited success. The problem was not with the hardware, but with how the WMR application “hijacks” the VR view, so maybe after a few updates it will work.<br>
Oculus Rift works, the only problem is that the controller cannot be used yet (it is different from the Vive controller, and the Oculus events are not handled in the VTK layer on OpenVR)</p>
<aside class="quote no-group" data-username="amirjaber" data-post="6" data-topic="1299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b9e5f3/48.png" class="avatar"> amirjaber:</div>
<blockquote>
<p>Based on your experience, is it fair to say visualizing medical images is faster with VTK implementation vs Unity implementations?</p>
</blockquote>
</aside>
<p>Probably similar performance. However the question is not this! The question is what do you want to do with the image? Because Unity is a game engine with zero medical image computing capabilities, so if you want to add “that one feature”, it will quickly turn into “just this other one”, and this process could take years while being completely redundant. At the same time, Slicer contains a wide range of processing and visualization features that you will need in your medical application.</p>

---

## Post #8 by @amirjaber (2018-02-08 18:39 UTC)

<p>Thanks Csaba for your response,</p>
<p>Is it possible to draw ROI with the controllers on the images.<br>
When the GUI feature will be added, is it possible to work with all extension user interfaces inside VR as in the desktop application?</p>

---

## Post #9 by @cpinter (2018-02-08 19:00 UTC)

<aside class="quote no-group" data-username="amirjaber" data-post="8" data-topic="1299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b9e5f3/48.png" class="avatar"> amirjaber:</div>
<blockquote>
<p>Is it possible to draw ROI with the controllers on the images.</p>
</blockquote>
</aside>
<p>Not right now but it’s also in the plans. The idea is that once we have implemented the Slicer VR interactions layer, it will be quite easy to do simple freehand segmentation, and after that if we can come up with a nice VR menu then we can use most Segment Editor effects within VR. Simple “sphere-brush” drawing may happen in a few weeks, but the full “SegmentEditorVR” will take a while.</p>
<aside class="quote no-group" data-username="amirjaber" data-post="8" data-topic="1299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b9e5f3/48.png" class="avatar"> amirjaber:</div>
<blockquote>
<p>When the GUI feature will be added, is it possible to work with all extension user interfaces inside VR as in the desktop application?</p>
</blockquote>
</aside>
<p>Still to be decided. If you have a stake in it, then I advise to keep pushing, and if you can contribute, then please check with us about which components you could help with.</p>

---

## Post #10 by @Lucas (2018-04-23 10:12 UTC)

<p>hi,<br>
where can i try the module and how to build it.  i want to use 3D slicer with oculus.</p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2018-04-23 13:10 UTC)

<p>SlicerVirtualReality module is available in the extension manager in recent nightly builds - and it is awesome! We’ll make an announcement soon.</p>

---

## Post #12 by @cpinter (2018-04-23 14:34 UTC)

<p>Please note that the oculus controller is not supported by VTKRenderingOpenVR. What this means for now is that you cannot use it to move in the scene. You’ll need to initialize the reference view (which you’ll see in the Virtual Reality module) and VR will match that when started. You can also synchronize it yourself anytime.</p>

---

## Post #13 by @timeanddoctor (2018-04-28 10:17 UTC)

<p>can I use googles’ Cardboard for a VR view. Or dose any software of android to apply…</p>

---

## Post #14 by @lassoan (2018-04-28 14:05 UTC)

<p>All OpenVR compatible headsets should work. There are several OpenVR/Google cardboard bridges out there that makes a cheap phone-based VR goggle appear as an OpenVR device, see for example this one: <a href="https://riftcat.com/vridge">https://riftcat.com/vridge</a></p>
<p>It would be great if you could give them a try and let us know if they work.</p>

---

## Post #15 by @fedorov (2018-05-07 18:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> this sounds interesting - did you guys confirm Slicer works with Google cardboard? I wanted to give a demo to kids in my son’s class, and if it works, I would actually just buy a cardboard device, but if it’s something that needs investigation, I will leave the VR part for better times.</p>

---

## Post #16 by @fedorov (2018-05-08 02:49 UTC)

<p>Ah, never mind - just discovered my phone is not “advanced enough” for the google “daydream”. In any case, if anyone tried using Slicer with Google cardboard/daydream, please share your experience!</p>

---

## Post #17 by @lassoan (2018-05-09 13:08 UTC)

<p>I’ve tested this with a Samsung S8 phone and RiftCat <a href="https://riftcat.com/vridge">VRidge VR viewer</a> worked perfectly with SlicerVirtualReality extension.</p>
<p>I’ve used Windows 10 and USB connection. Installation takes 5-10 minutes, as you need to install a companion app on the desktop computer, and on your phone the VRidge app and a VR sideload app. All the steps are very clearly described though. You also need to install Steam and SteamVR, if you haven’t installed those before.</p>

---

## Post #18 by @ssyip (2018-05-09 17:39 UTC)

<p>That’s great! I can’t seem to find SlicerVirtualReality in the Sicer 4.8.1 extension.</p>

---

## Post #19 by @lassoan (2018-05-09 17:40 UTC)

<p>SlicerVirtualReality extension requires VTK9 and therefore it is only available in nightly builds.</p>

---

## Post #20 by @ssyip (2018-05-09 18:08 UTC)

<p>I installed it. But Slicer crashes right away when I clicked on the VR button. Memory issue? Running on a latop w/ 16RAM.</p>

---

## Post #21 by @lassoan (2018-05-09 19:03 UTC)

<p>Do you have Steam and SteamVR installed? Do other SteamVR applications work well on your computer? What operating system and GPU do you have? Do you see any error in the logs (menu: Help / Report a bug; choose the previous session where the crash occurred)?</p>

---

## Post #22 by @ssyip (2018-05-09 20:14 UTC)

<p>Thanks for your help. I got my HTC+Vive controller work like a mouse to interact w/ Slicer. Pretty fun.</p>
<p>Next. How do I make 3D rendering so I can walk around the room w/ my headset+controller to hover over the images?</p>

---

## Post #23 by @lassoan (2018-05-09 22:14 UTC)

<p>Just do everything as usual. Whatever you see in the scene in the 3D viewers will show up in your VR headset as soon as you click the VR headset button on the toolbar (after installing SlicerVirtualReality extension). For example, to see images, you can show slices, enable volume rendering, segment it and show the segments, etc. You can fly around and grab objects and we plan to further improve interactions and control throughout the coming months.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74060357035c88a4bb09724b431b4f25bed72813.png" data-download-href="/uploads/short-url/gyogHOZkGGjmmLAnKANCZohXdGX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74060357035c88a4bb09724b431b4f25bed72813_2_690x117.png" alt="image" data-base62-sha1="gyogHOZkGGjmmLAnKANCZohXdGX" width="690" height="117" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74060357035c88a4bb09724b431b4f25bed72813_2_690x117.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74060357035c88a4bb09724b431b4f25bed72813_2_1035x175.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74060357035c88a4bb09724b431b4f25bed72813_2_1380x234.png 2x" data-dominant-color="EDDEE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1852×315 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @kaushikdasroy (2018-06-23 05:07 UTC)

<p>I am using Oculus HMD. When i am trying to use slicervirtualreality extension, I am getting “connection failed” error appearing next to “connect to hardware” checkbox. Any reason why. Thanks !</p>

---

## Post #25 by @lassoan (2018-06-23 05:11 UTC)

<p>Have you set up your Oculus headset to work with SteamVR? I use HTC Vive and Windows Mixed Reality headsets, so I cannot give you instructions, but you should be able to find it on the internet. As far as I know, Oculus controllers are not supported in VTK’s virtual reality interface, so you’ll only be able to move around by moving around physically.</p>

---

## Post #26 by @kaushikdasroy (2018-06-23 08:14 UTC)

<p>Thanks Andras. I got the Oculas working with SteamVR. I am not able to see in VR yet, getting SlicerApp-real.exe unresponsive. My laptop is a gaming laptop with good gpu/ram etc.</p>

---

## Post #27 by @kaushikdasroy (2018-06-23 08:18 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e6ee5e991dd13f826129b1a5ec7085ab0d55a5b.png" alt="image" data-base62-sha1="6CLyPe9E0s0SDyx0FA946UG6NzJ" width="594" height="415"> - while closing slicer</p>

---

## Post #28 by @cpinter (2018-06-23 11:12 UTC)

<p>Yes there’s this last leak I haven’t been able to figure out yet. Don’t worry about this, it doesn’t influence usage at all, just destruction of the objects at exit.</p>
<p>If you have Steam and SteamVR, and you have SlicerVirtualReality extension, then after the Oculus app is started (put on the headset for a moment and it will start it), then Slicer should be able to connect to Oculus no problem.</p>

---

## Post #29 by @kaushikdasroy (2018-06-23 16:49 UTC)

<p>slicer is connecting ok, i think. I am able to see a 3d space. But it is empty. I am attaching my slicer screen</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5090c59797f7905b473b0f4130c6cc570972bfb0.jpeg" data-download-href="/uploads/short-url/buImVPf0HM31TGUoTJU27eMFL0Y.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5090c59797f7905b473b0f4130c6cc570972bfb0_2_690x388.jpg" alt="image" data-base62-sha1="buImVPf0HM31TGUoTJU27eMFL0Y" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5090c59797f7905b473b0f4130c6cc570972bfb0_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5090c59797f7905b473b0f4130c6cc570972bfb0_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5090c59797f7905b473b0f4130c6cc570972bfb0_2_1380x776.jpg 2x" data-dominant-color="BAB7B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 420 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @lassoan (2018-06-23 17:16 UTC)

<p>Look around. Also, if you click the crosshair icon (to the right from the connection icon) then the virtual reality view will be set up to show the same as the 3D view on the screen (when your head is in the default position/orientation that you’ve set up in SteamVR).</p>

---

## Post #31 by @kaushikdasroy (2018-06-24 05:38 UTC)

<p>Good new is I can see the model now. I had to force my laptop to use GPU. Resolved that.<br>
But I am not getting stereoscopic vision. Images are not getting combined properly. Model is showing continuous minor up and down move as well.</p>

---

## Post #32 by @lassoan (2018-06-24 12:34 UTC)

<p>This looks like a hardware/configuration problem. What laptop model and GPU do you have? Do other SteamVR applications work well?</p>
<p>Volume rndering is demanding operation, you may try simple slice display first (click eye icon in the slice view controller, above the slice view).</p>
<p>For volume rendering, make sure to choose GPU volume rendering in Volume rendering module, and try adaptive technique first.</p>

---

## Post #33 by @kaushikdasroy (2018-06-24 17:12 UTC)

<p>Andras, you last suggestion did it. I was not selecting GPU rendering. It looks great now! very well done. I will try some more.<br>
I am using Oculus rift so not able to walk around using the controllers. Any idea when rift and touch controllers might be supported.</p>

---

## Post #34 by @timeanddoctor (2018-06-25 12:08 UTC)

<p>I can connect slicer with my phone by vridge success, but it fail to pull or push(Magnify or Zoom out)</p>

---

## Post #35 by @lassoan (2018-06-25 12:15 UTC)

<p>With vridge, you cannot interact with the scene, only view it. To change your viewpoint, click the crosshair icon on the toolbar (on the right side of virtual reality headset icon).</p>

---

## Post #36 by @Frank (2018-11-07 08:38 UTC)

<p>Hey Buddy, I have encountered the same problem of SteamVR window “ready” with “[unresponsive] SlicerApp-real.exe”. The difference is that it reads “connection failed” next to the Connect to hardware. May I know how did you solve this problem. Thank you!</p>

---

## Post #37 by @lassoan (2018-11-07 19:56 UTC)

<p>Since we’ve improved SlicerVirtualReality extension so that you can do much more than just viewing (fly, scale/rotate/move the scene, move around objects, etc.) and you can buy Windows Mixed Reality headsets for $300 (that come with two 6-dof controllers), it does not make much sense anymore to use vridge. I would recommend to get a Windows Mixed Reality device instead.</p>

---

## Post #38 by @kopachini (2018-12-16 19:43 UTC)

<p>Hello everybody,<br>
today I tried to view model in VR using Samsung S8 edge… I have installed all needed softwares and same message pops up in Steam VR as mentioned before (unresponsive SlicerApp-real.exe another one about graphic card and vr set as seen on the pic.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2d7b48b82eef0b634f3c0c910019be49d69c75e.jpeg" data-download-href="/uploads/short-url/rNEM5zbQtSRI5n2o6k3RWCQe9BQ.jpeg?dl=1" title="error%203d%20slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2d7b48b82eef0b634f3c0c910019be49d69c75e_2_690x388.jpeg" alt="error%203d%20slicer" data-base62-sha1="rNEM5zbQtSRI5n2o6k3RWCQe9BQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2d7b48b82eef0b634f3c0c910019be49d69c75e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2d7b48b82eef0b634f3c0c910019be49d69c75e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2d7b48b82eef0b634f3c0c910019be49d69c75e_2_1380x776.jpeg 2x" data-dominant-color="D3D2E0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error%203d%20slicer</span><span class="informations">1920×1080 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>is there any help? I won’t be able to buy HTC Vive or Windows Mixer Reality anytime soon.</p>

---

## Post #39 by @lassoan (2018-12-16 20:00 UTC)

<p>I’ve used this before with a Samsung S8 edge when the Slicer module was still quite limited and it made sense. However, now the experience with a phone (with 3-DOF tracking and a single 3-DOF controller) is so much worse than when using a proper virtual reality headset (with 6-DOF tracking and two 6-DOF controllers) that I would not recommend anyone to do this. You might end up making the false conclusion that medical virtual reality is useless, while the fact is that it is just so much worse using a phone-based system.</p>
<p>A Windows mixed reality headset costs $300 (including two controllers). If you can afford a virtual reality capable computer then this 10-20% extra cost should be tolerable. Windows mixed reality headsets have comparable or better specs than the original HTC Vive and their huge advantage is that they use inside-out-tracking, so you don’t to set up external trackers, with all the hassles of extra wires, necessary space, etc.</p>

---
