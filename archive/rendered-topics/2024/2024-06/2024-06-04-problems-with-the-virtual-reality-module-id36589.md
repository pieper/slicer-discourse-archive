# Problems with the Virtual Reality Module

**Topic ID**: 36589
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/problems-with-the-virtual-reality-module/36589

---

## Post #1 by @karl (2024-06-04 13:46 UTC)

<p>Hello dear community,</p>
<p>I am trying to get the VR Module to run since a couple of hours now.</p>
<p>I tried with Quest 3 + Quest Controller.</p>
<p>I tried with Varjo VR3 and Vive Controllers.</p>
<p>I run into serious interaction problems.</p>
<p>Especially if I open the menu and try to select the cutting/probe tool. Using Quest 3 (in both OpenVR/OpenXR) it is not possible to select anything even though I manage to at least toggle thorugh the options.</p>
<p>With the Varjo XR I can select the tools with quite some hustle, but the way the interaction works (cutting plane) it is almost useless as I am forced to cut in a way that is perpendicular to my perspective.</p>
<p>Slicer 3D often shuts down without any error code and it is not clear why. (I reinstalled etc.)</p>
<p>I really like the looks of the module and to have VR integrated in Slicer 3D and being able to use all the modules and render the results in VR is really nice.</p>
<p>Did someone here manage to use it effectively? I have other software to render medical images and it works way better. I very much like the idea of open source however…</p>

---

## Post #2 by @cpinter (2024-06-04 14:36 UTC)

<p>What Slicer version do you use?</p>

---

## Post #3 by @karl (2024-06-04 15:07 UTC)

<p>Hi, thanks for the fast answer.</p>
<p>So I use the (latest) 5.6.2 Version.</p>
<p>Should I use an older one?</p>

---

## Post #4 by @karl (2024-06-05 08:33 UTC)

<p>In the readme: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerVirtualReality/README.md at master · KitwareMedical/SlicerVirtualReality · GitHub</a> it does not directly recommend any version, therefore I used the newest.</p>
<p>Is there an alternative set-up hardware and/or software wise that I should try?</p>

---

## Post #5 by @cpinter (2024-06-05 10:05 UTC)

<p>The problem is that SlicerVR is undergoing a complete backend reimplementation, and I think 5.6.2 contains a VTK that does not fully support the new one (I haven’t tested VR for a while as I am waiting for the announcement that the OpenXR backend fully works, and I intend to try it then - my interest is development and not usage so I can afford such wait).</p>
<p>I suggest the following two options:</p>
<ul>
<li>5.4.0: It was a month after the last summer project week, when I remember that everything seemed to work again after a long period when they didn’t. Use OpenVR (install Steam and SteamVR first)</li>
<li>The latest 5.7.0: Yesterday at the Slicer Project Week meeting the Kitware developers said that other than the complex gestures (e.g. two-handed world manipulation - a feature that I consider essential but others may not) and certain minor things the OpenXR backend works well.</li>
</ul>

---

## Post #6 by @karl (2024-06-10 13:39 UTC)

<p>Hello Csaba Pinter,</p>
<p>thank you for the ideas, I will try them both!</p>
<p>Best,<br>
Karl</p>

---

## Post #8 by @kantmedha (2024-07-21 10:10 UTC)

<p>Hi Karl,<br>
Were you able to make the VR plugin work for Quest 3?</p>

---

## Post #9 by @karl (2024-07-23 08:18 UTC)

<p>Hello Medha,</p>
<p>Sometimes it worked a little bit - but nowhere where it needs to be to be anything more than a “party trick”. So moving myself/my camera consistently works. Choosing tools from the menu was -at best- iffy. Using the tools on the rendered medical image was close to impossible. In the current state the plug in is more frustrating than anything else. For sure you will not want to use it. Especially if you have alternatives at hand.</p>
<p>I tried different versions of slicer (5.4.0, 5.6.2 (?!), 5.7.0).</p>
<p>I think the UI is not thought out and is not implemented correctly. I tried for hours to use it…</p>
<p>This is sad as Slicer offers a lot of nice plug ins and would be awesome as a medical image VR viewer.</p>
<p>Another thing I noticed is that if you combine for example a CT with a segmented organ/pathology and volumetrically render it in Slicer it will show on the desktop but in VR will only show the CT.</p>

---

## Post #10 by @ssingh (2024-07-23 10:42 UTC)

<p>Dear <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Looking at the commit history of the SlicerVR plugin, I can see you have most of the commits.<br>
Your input on the future work of this plugin and device support (Meta Quest 3 or others) will be useful.</p>

---

## Post #11 by @ssingh (2024-07-24 09:43 UTC)

<p>By plugin, I meant extension.</p>

---

## Post #12 by @cpinter (2024-08-02 12:46 UTC)

<aside class="quote no-group" data-username="karl" data-post="9" data-topic="36589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/34f0e0/48.png" class="avatar"> karl:</div>
<blockquote>
<p>Choosing tools from the menu was -at best- iffy</p>
</blockquote>
</aside>
<p>As I said this extension is not yet finished. The tools that you talk about are probably from the original VTK tech demo. We’ll need to add a configurable in-VR widget. I did some experiments a while ago</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerVRInteraction/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerVRInteraction/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerVRInteraction/" target="_blank" rel="noopener">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
But since the extension has been undergoing profound changes, such DIY solutions are not worth maintaining, as everything they are based on is constantly changing. Unfortunately these efforts are quite slow (as I understand the OpenXR rework started several years ago and has not been finalized still).</p>
<aside class="quote no-group" data-username="karl" data-post="9" data-topic="36589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/34f0e0/48.png" class="avatar"> karl:</div>
<blockquote>
<p>Especially if you have alternatives at hand</p>
</blockquote>
</aside>
<p>Well this is why I think that this extension is what we need to improve, because the “alternatives” are Unity or Unreal Engine based solutions, which are fine for static scenes (great for education, you can see many examples published), but not really for patient-specific use cases where you need to work on various new patients every day.</p>
<aside class="quote no-group" data-username="karl" data-post="9" data-topic="36589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/34f0e0/48.png" class="avatar"> karl:</div>
<blockquote>
<p>Another thing I noticed is that if you combine for example a CT with a segmented organ/pathology and volumetrically render it in Slicer it will show on the desktop but in VR will only show the CT.</p>
</blockquote>
</aside>
<p>I think this is inaccurate. Maybe you configure the volume rendering before activating VR, and the new VR view is not added to the volume rendering display node? Try setting up rendering first and then show it in VR.</p>
<p>I understand your frustration, but please keep in mind that you are talking about an open-source, entirely free piece of software, that can be maintained and developed either by funded projects (which are almost never about infrastructure like this extension but about driving use cases, and most of the time larger infrastructural work cannot be included), or in the free time of developers. If you can provide either of the two, the community will welcome your contribution.</p>

---

## Post #13 by @Mark_Ryan (2024-08-03 10:50 UTC)

<p>I have been using MedicalHolodeck, which allows for pretty seamless display of volume rendering and segmentation data. Also able to view 4D/motion CT and MRI. The manual segmentation tools need work (Elucis is good for this), but AI segmentation with Totalsegmentator is integrated. This is a paid application though, and an open-source alternative would be great. I’ve tried SlicerVR on Quest 2,  3, and Index but it’s really difficult to navigate and manipulate images. Haven’t had issues showing volume renderings but the lighting can be strange, even with various combinations of dual/back lighting turned on and off.</p>

---

## Post #14 by @lassoan (2024-08-03 22:24 UTC)

<p>Thanks for the feedback. We have an amazingly powerful and versatile foundation in Slicer for augmented and virtual reality that can easily overtake all existing commercial solutions.</p>
<p>However, right now there are no end-user workflows built on this foundation. Maybe because AI took almost all attention and funding away from AR/VR? Even Apple’s headset failed to generate any lasting excitement in the field. Or maybe the main challenge is to find a widely usable impactful clinical application of AR/VR.</p>
<p>Anyway, AR/VR applications in Slicer are evolving at a slow pace. If you can contribute with developer time or funding then a lot of progress could be achieved quite quickly.</p>

---

## Post #15 by @Mark_Ryan (2024-08-04 02:41 UTC)

<p>I really appreciate all the work you and the other contributors have put into 3D Slicer and all of the extensions. I would love to contribute, but unfortunately I don’t know all that much about programming. I’m learning as I go, so hopefully I can help at some point.</p>

---

## Post #16 by @karl (2024-08-06 09:30 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I am aware that slicer is an opensource project. When I describe the state of the vr plugin / addon I am not bashing it. It is just barely useable at the moment. I will think about contributing to the project as I see a lot of potential.</p>
<p>There are opensource alternatives that are dynamic such as the project by mlavik1 - <a href="https://github.com/mlavik1/UnityVolumeRendering" class="inline-onebox" rel="noopener nofollow ugc">GitHub - mlavik1/UnityVolumeRendering: Volume rendering, implemented in Unity3D. Want to support the project? Donate a small sum to Save The Children(https://www.savethechildren.net/) or another charity, and send me a message, and I will be greatly motivated!</a>   Generally the user interfaces in VR and volume rendering settings are still evolving.</p>
<p>Regarding the rendering: I first rendered everything in the 3D view and then toggled VR on and it didnt show the segmentations.</p>

---

## Post #17 by @cpinter (2024-08-06 11:08 UTC)

<aside class="quote no-group" data-username="karl" data-post="16" data-topic="36589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/34f0e0/48.png" class="avatar"> karl:</div>
<blockquote>
<p>Regarding the rendering: I first rendered everything in the 3D view and then toggled VR on and it didnt show the segmentations.</p>
</blockquote>
</aside>
<p>Even so, please make sure the view node is enabled for the segmentation in the VR view. At least then we’ll know if the problem is there or not.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3c26f55fb82709d51e22f71bcf7c76caadf9d02.png" data-download-href="/uploads/short-url/rVLGg4OuOpV8xrWY4VY8Q07yB4m.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3c26f55fb82709d51e22f71bcf7c76caadf9d02_2_377x500.png" alt="image" data-base62-sha1="rVLGg4OuOpV8xrWY4VY8Q07yB4m" width="377" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3c26f55fb82709d51e22f71bcf7c76caadf9d02_2_377x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3c26f55fb82709d51e22f71bcf7c76caadf9d02.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3c26f55fb82709d51e22f71bcf7c76caadf9d02.png 2x" data-dominant-color="F1F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">516×684 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the VR view is included, then I guess I or some other developer will need to try it and see why it does not show up. The best probably would be adding a new issue in the SlicerVR GitHub repository.</p>

---
