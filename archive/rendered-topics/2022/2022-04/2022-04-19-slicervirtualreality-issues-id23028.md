---
topic_id: 23028
title: "Slicervirtualreality Issues"
date: 2022-04-19
url: https://discourse.slicer.org/t/23028
---

# SlicerVirtualReality issues

**Topic ID**: 23028
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/slicervirtualreality-issues/23028

---

## Post #1 by @jruben4 (2022-04-19 18:10 UTC)

<p>Trying to view a volume rendering in VR using SlicerVirtualReality plugin.   Using an occulus quest 2 using occulus link cable to a laptop.  I load the DICOM data set, and set up the volume rendering so I see it on the laptop.</p>
<ol>
<li>
<p>If I hit the VR icon in slicer 3D then put on my headset while it’s in SteamVR, I just get a blank empty space</p>
</li>
<li>
<p>If I hit the VR icon from inside the steam Vr space (by viewing desktop) I get this error:<br>
“the action manifest for slicerapp-real was not found”</p>
</li>
</ol>

---

## Post #2 by @cpinter (2022-04-20 12:38 UTC)

<p>I don’t think any of us has tried the Oculus Quest 2 with SlicerVR yet, as it is not supported by OpenVR, and SlicerVR is not yet updated to OpenXR.</p>
<aside class="quote no-group" data-username="jruben4" data-post="1" data-topic="23028">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jruben4/48/14989_2.png" class="avatar"> jruben4:</div>
<blockquote>
<p>“the action manifest for slicerapp-real was not found”</p>
</blockquote>
</aside>
<p>Please copy the json files from <a href="https://gitlab.kitware.com/vtk/vtk/-/tree/master/Rendering/OpenVR">here</a> to the folder from where you start Slicer.</p>

---

## Post #3 by @jruben4 (2022-04-20 18:08 UTC)

<p>Like this?  This didn’t have any effect.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1b8364f11d62f4767ba096067c49abbb1b33029.png" alt="image" data-base62-sha1="rDIP7mf2fCIPCRiJ7U9l10MYKmZ" width="687" height="358"></p>

---

## Post #4 by @jruben4 (2022-04-20 18:19 UTC)

<p>Also, can’t you run OpenVR applications on the quest 2 as long as you execute them in SteamVR and use the occuluslink?</p>

---

## Post #5 by @pieper (2022-04-20 18:21 UTC)

<p>I don’t know if occuluslink works (let us know if you get it working).  But <a href="https://developer.nvidia.com/nvidia-cloudxr-sdk">cloudxr</a> works with Slicer 4.11 and SlicerVR, either from a local machine or a cloud hosted machine over wifi.</p>

---

## Post #6 by @cpinter (2022-04-20 19:20 UTC)

<p>Are you positive you mean 4.11 and not 4.13? Just curious to know what did you use successfully CloudXR with (and 4.11 is pre-2021/02).</p>

---

## Post #7 by @cpinter (2022-04-20 19:21 UTC)

<p>I used it with build Slicer not installed, but yes as far as I know this should work for the manifest errors.</p>
<p>About oculus link I also cannot give you information. I personally haven’t used wiress headsets with SlicerVR yet.</p>

---

## Post #8 by @pieper (2022-04-21 00:21 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="23028" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Are you positive you mean 4.11 and not 4.13? Just curious to know what did you use successfully CloudXR with (and 4.11 is pre-2021/02).</p>
</blockquote>
</aside>
<p>Yes, definitely.  CloudXR works with OpenVR (not yet OpenXR).  The stock binary Slicer-4.11.20210226 with the corresponding SlicerVR extension just works (if everything else is set up right, like the network ports, steam account, occulus client, etc).</p>
<p>I also tested 4.13 with CloudXR and I got an error in the client about. controller manifest that maybe could be fixed but I didn’t look more closely since 4.11 suits my purposes for now.</p>

---

## Post #9 by @rbumm (2022-05-08 08:33 UTC)

<p>Got the Oculus Quest 2 at least halfway working in Slicer 4.11, impressive …<br>
Prerequisites:</p>
<ul>
<li>Windows 10</li>
<li>install Steam</li>
<li>install SteamVR</li>
<li>install Oculus PC app</li>
<li>install Slicer 4.11</li>
<li>install Slicer VR extension</li>
</ul>
<p>Session:</p>
<ul>
<li>Put on the Quest 2 headset</li>
<li>Adjust Guardian to local Guardian (circle around you)</li>
<li>In Quest Home → touch settings</li>
<li>In Settings, touch Airlink and connect to your graphics workstation</li>
<li>(For airlink use a 5Ghz WLAN  access, connect the PC to router via LAN cable)</li>
<li>First run: In Airlink mode → touch the desktop symbol and start Steam VR</li>
<li>Subsequent runs: → Touch SteamVR</li>
<li>In SteamVR, you will see an empty giant space with ground and stars</li>
<li>Press left controller menu button → menu appears → touch desktop symbol low left in the menu → normal desktop screen opens</li>
<li>Start and adjust Slicer 4.11, load a volume and segmentation</li>
<li>Swich to Slicer VR extension</li>
<li>In Slicer top menu, press the headset symbol</li>
</ul>
<p>The segmentation appears floating in empty space, can be moved forwards and backwards (only) with the right controller’s thumb joystick back and forth, and can be rotated with gestures as soon as both trigger buttons are pressed.</p>
<p>Is this what to be expected or is there more in other headsets?</p>

---

## Post #10 by @pieper (2022-05-08 13:38 UTC)

<p>Thanks for the report <a class="mention" href="/u/rbumm">@rbumm</a>.  It sounds like Airlink behaves basically the same as CloudXR.  I’m not sure if CloudXR offers better performance but Airlink sounds a bit easier.  Regarding other headsets, I think they offer similar features.</p>
<p>There should be better features in the Slicer 5 version using OpenXR, but that seems to be taking a while to sort out so it’s not available yet.  Maybe someone can comment on any progress recently.</p>

---

## Post #11 by @cpinter (2022-05-09 09:28 UTC)

<p>Thanks for the update <a class="mention" href="/u/rbumm">@rbumm</a> , quite useful!</p>
<p>We are currently in an “almost there” state with SlicerVR on many fronts.</p>
<ul>
<li>OpenXR support can be expected to be finalized soon in terms of the new Kitware-Robarts project (at least as far as I know using OpenXR is in the plans for this project - they want HoloLens2 support)</li>
<li>In-VR widget exposing many Slicer features is on the way. The widget works, the laser pointer basically works. We currently struggle with that the texture update that shows in the normal 3D view doesn’t show up in VR. Anyway, it’s very close now.</li>
<li>A VR “training course” as far as I know is also on the way. There will be some kind of OR with objects and little goals that walk you through the basics of how to use the controller, how to navigate in the scene, etc</li>
<li>I’m personally planning many small additional features, but these will come slowly after we successfully add the in-VR widget with the laser</li>
<li>Unfortunately there are several small but important issues with the latest SlicerVR after the recent VTK update, and maybe due to other updates. For example, volume rendering does not show up in VR at all. Or there are errors in the log that even slow down rendering. Some button events are not caught. Maybe these are the most important ones.</li>
</ul>
<p>I hope this answers your question!</p>
<p>Can you please describe your use case in VR? Also what is it that you would ideally do in VR. Thanks!</p>

---

## Post #12 by @rbumm (2022-05-09 13:11 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>.</p>
<p>I’m thrilled to see 3D Slicer supporting VR at all, in fact, it would be great to have that volume rendering available as well as a “laser”, which I do not yet find in the Oculus Quest 2.</p>
<p>My personal use cases would be to plan thoracoscopic access with a shrunk lung/tumor segmentation, provide anatomical teaching to students or use it for patient education. Possibilities seem to be endless as soon as one could overlay 3D Slicer segmentations and human bodies in mixed reality.<br>
Saw a <a href="https://www.brainlab.com/press-releases/brainlab-releases-immersive-interactive-anatomy-viewer-based-on-magic-leap-one/">similar project</a> at Brainlab’s headquarters using → <a href="https://www.magicleap.com/magic-leap-1">Magic Leap One</a>.</p>
<p>Driving and manipulating simulated “fibreoptics” and “instruments”  into a (maybe bloated) body segmentation, being able to manipulate them in VR, and seeing the result on a virtual screen in VR space is something that immediately came into my mind when using Slicer VR the first time.</p>
<p>Please let me know if I can support this project or if you need further tests.</p>

---

## Post #13 by @Eserval (2022-05-09 14:34 UTC)

<p>That’s an awesome topic.<br>
<a class="mention" href="/u/rbumm">@rbumm</a> I think you can move completely however you need to grab the model and sometimes it’s difficult.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc84a90e78775c3121892e4edc243d165459ff9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc84a90e78775c3121892e4edc243d165459ff9.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc84a90e78775c3121892e4edc243d165459ff9.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #14 by @rbumm (2022-05-09 14:47 UTC)

<p>Very nice <a class="mention" href="/u/eserval">@Eserval</a>!</p>
<p>Could you share briefly how you segmented the vessels and how you recorded the VR screen?</p>

---

## Post #15 by @Eserval (2022-05-09 16:01 UTC)

<p>For vessels segmentation I use a workflow that creates masks and new masks inside then:</p>
<p>1- Create a lung mask including the mediastinal part of vessels (I use the Lung segment module)</p>
<p>2- Create a new mask using the threshold tool for the vessels</p>
<p>3- I perform some fine work on 3D to exclude some “trash” points</p>
<p>4- Use grow from seeds to separate the artery and vein.</p>
<p>To record the VR screen I use the OBS Studio. I just enable the screen playback in Steam VR options and recording with OBS.</p>
<p>I’m a thoracic surgeon and we are using routinely the 3D slicer in our lung resection cases and research:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e654263d024157c7e91534555b0d0e309530919f.jpeg" data-download-href="/uploads/short-url/wRA6EOUu3ZJu0fszAgBLNchFvS7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e654263d024157c7e91534555b0d0e309530919f_2_690x207.jpeg" alt="image" data-base62-sha1="wRA6EOUu3ZJu0fszAgBLNchFvS7" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e654263d024157c7e91534555b0d0e309530919f_2_690x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e654263d024157c7e91534555b0d0e309530919f_2_1035x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e654263d024157c7e91534555b0d0e309530919f_2_1380x414.jpeg 2x" data-dominant-color="C2B0B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1510×454 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>Our dream is to develop a more autonomous process for lung vessel segmentation. I think that it’s not a very hard job for a developer, however for us, surgeons, It’s quite impossible.</li>
</ul>
<p>Here at our University (University of Sao Paulo - Brazil), we are developing many projects involving thoracic surgery and 3D reconstruction (including VR, preoperative planning, and robotic surgery…). We are completely open to the exchange of experiences and collaborations.</p>

---

## Post #16 by @rbumm (2022-05-09 16:41 UTC)

<p>I do not want to push that topic up too often, but are you referring to the Lung CT Segmenter as part of the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" rel="noopener nofollow ugc">Lung CT Analyzer extension</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69e4848c11fbd20801b1630ff4b0f45a6f309a46.png" alt="image" data-base62-sha1="f6LJlFNoU7Ba30Gd2rynFF4l2gC" width="124" height="60"></p>
<p>of which I am one of the principal authors? If yes this could be the start of direct cooperation because your goal is exactly my goal and I am a thoracic surgeon with a bit of programming knowledge. We could probably take the vessel segmentation workflow ideas to another topic then …</p>
<p>BTW impressive segmentation</p>

---

## Post #17 by @rbumm (2022-05-09 16:52 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>I found the scissor effect in the free SteamVR application → “The Lab” → “Human body scan”  very impressive and helpful to analyze an obvious volume rendering.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="-PVAcLlYUpg" data-video-title="The Lab [Human Body Scan]" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=-PVAcLlYUpg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/-PVAcLlYUpg/hqdefault.jpg" title="The Lab [Human Body Scan]" width="" height="">
  </a>
</div>


---

## Post #18 by @mau_igna_06 (2022-05-09 20:26 UTC)

<p>Hi Rudolf.</p>
<p>I think the functionality you show on the video is already on Slicer by PRISM Volume Rendering extension…</p>
<p>Please look at this:<br>
<a href="https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io/en/latest/tutorials.html#plane-intersecting" class="onebox" target="_blank" rel="noopener">https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io/en/latest/tutorials.html#plane-intersecting</a></p>
<p>You would just need to code a good VR handles interface to control the intersection planes I think</p>
<p>Mauro</p>

---

## Post #19 by @Eserval (2022-05-10 01:41 UTC)

<p>Thats right Rudolf! By the way thanks for your excelent job.<br>
I think we can work together!</p>

---

## Post #20 by @cpinter (2022-05-10 08:44 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thanks for pointing it out! We have ROI cropping in Slicer that is more or less the same except that instead of a plane you need to define a box, but this plane cutting seems quite easy to use for sure.</p>

---

## Post #21 by @cpinter (2022-05-10 08:46 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="18" data-topic="23028">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>You would just need to code a good VR handles interface to control the intersection planes I think</p>
</blockquote>
</aside>
<p>Yes, and these “good VR handles” are the critical part <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Because we have everything we need in Slicer, but exposing it in a UI-less environment is the challenge. This is why we have eben trying to make time (and find funding) for such developments in the last three years. Hopefully soon at least the basics will be available!</p>
<p>FYI you don’t need Prism to do box cropping. What you need Prism for are the custom GPU shaders that for example allow sphere cropping, and a lot more things too.</p>

---

## Post #22 by @jruben4 (2022-05-10 18:37 UTC)

<p>I’m doing the same thing, except using occulus link (via cable) instead of airlink.  I assume that has identical functionality other than how the link is physically created.</p>
<p>When I get to your last step, I am floating in the empty space, except my segmentation is nowhere to be found. I’ve pressed the joysticks back and forth but I never see anything except empty black space.</p>

---

## Post #23 by @rbumm (2022-05-10 20:58 UTC)

<p>Ran into a similar problem when I tried to open a volume rendering - they seem not to be functional in VR  at the moment. After doing a thresholded bone segmentation you need to activate it in 3D view (segment editor), then switch to Slicer VR and press the VR headset symbol - this should work in Slicer 4.11 as of May 10th 22.</p>

---

## Post #24 by @cpinter (2022-05-11 08:46 UTC)

<p>Volume rendering not working: Please see my <a href="https://discourse.slicer.org/t/slicervirtualreality-issues/23028/11">comment above</a> for the current state of SlicerVR.</p>
<p>If you use a Slicer Preview version older than mid-February then volume rendering will work. It was broken with the update of VTK under Slicer on February 24 (if I remember the day correctly).</p>

---

## Post #25 by @jruben4 (2022-05-11 15:02 UTC)

<p>I just tried the 2-2-22 version of 4.13.0 and I still can’t visualize a volume render in slicerVR.</p>

---

## Post #26 by @cpinter (2022-05-11 18:16 UTC)

<p>Two ideas:</p>
<ol>
<li>Try an even older version, maybe I remembered wrong.2. In Volume Rendering module, in the Inputs section, make sure that in the Views combobox not just the 3D view but the VirtualReality view is checked as well</li>
</ol>

---

## Post #27 by @jruben4 (2022-05-11 18:39 UTC)

<p>This is what I see for views box:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73dc25829cce50c83d31e2c004e686e2f890333.png" alt="image" data-base62-sha1="q91H7pKmIjORmlSYT4T4B8pHYfF" width="434" height="122"></p>
<p>Edit - after I turn on slicerVR, I do see a view1 option AND a virtualrealityview.  They are both checked.</p>

---

## Post #28 by @cpinter (2022-05-12 07:49 UTC)

<p>When you start VR, then a second option for the new VR view will show up, which needs to be checked in order for the volume rendering to show up. Note that this step should not be done every time, but sometimes it occurred to me that it was unchecked and had to be checked manually.</p>

---

## Post #29 by @jruben4 (2022-06-03 12:28 UTC)

<p>Finally got to test this using Airlink instead of OcculusLink.  Same issue, empty VR space.</p>

---

## Post #30 by @jruben4 (2022-06-24 14:49 UTC)

<p>Anyone get VR to work yet with occulus?  Just tried 5.1.0 same issues.</p>

---

## Post #31 by @TiniNant (2022-08-04 14:24 UTC)

<p>Same issues for me, it does not work</p>

---
