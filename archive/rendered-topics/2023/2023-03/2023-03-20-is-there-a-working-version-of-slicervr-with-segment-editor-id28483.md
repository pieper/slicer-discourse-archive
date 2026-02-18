# Is there a working version of SlicerVR with Segment Editor?

**Topic ID**: 28483
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/is-there-a-working-version-of-slicervr-with-segment-editor/28483

---

## Post #1 by @Taci (2023-03-20 18:59 UTC)

<p>Hi, I followed SlicerVR development updates through previous GitHub issues and NA-MIC project weeks. The in-VR widget seems to have had problems for a long time. Is there any specific previous version/commit/branch of SlicerVR that can access the Segment Editor in Slicer3D, and modify the segment in VR with controllers? We specifically want to use the Paint functionality in VR for manual correction.</p>
<p>If not, what would be the complexity of fixing this feature if we want to try it ourselves?</p>
<p>I confirmed that flying and grabbing the object functions work with Oculus Quest 2 using the commit <a href="https://github.com/KitwareMedical/SlicerVirtualReality/commit/a5468fc3eb674cdbd2c724654e3e30d99f9ca360" rel="noopener nofollow ugc">“Rename VR interactor style callback functions”</a>.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-03-20 21:07 UTC)

<p>Infrastructure for displaying Qt widgets in immersive views is now in place, but I don’t think any modules have taken advantage of it yet.</p>
<aside class="quote no-group" data-username="Taci" data-post="1" data-topic="28483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/73ab20/48.png" class="avatar"> Taci:</div>
<blockquote>
<p>We specifically want to use the Paint functionality in VR for manual correction.</p>
</blockquote>
</aside>
<p>I know that <a class="mention" href="/u/cpinter">@cpinter</a> and others have been planning to work on this, but I don’t think there is dedicated funding for it, so the progress may be very slow.</p>
<aside class="quote no-group" data-username="Taci" data-post="1" data-topic="28483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/73ab20/48.png" class="avatar"> Taci:</div>
<blockquote>
<p>If not, what would be the complexity of fixing this feature if we want to try it ourselves?</p>
</blockquote>
</aside>
<p>It would be great if you could work on it. To get started, you can build Slicer and the SlicerVirtualReality extension and try to display a vtkQWidgetWidget in Slicer.</p>
<aside class="quote no-group" data-username="Taci" data-post="1" data-topic="28483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/73ab20/48.png" class="avatar"> Taci:</div>
<blockquote>
<p>I confirmed that flying and grabbing the object functions work with Oculus Quest 2 using the commit</p>
</blockquote>
</aside>
<p>How did you set up the Oculus/Meta Quest 2 headset to be accessible from Slicer?</p>

---

## Post #3 by @Taci (2023-03-21 01:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How did you set up the Oculus/Meta Quest 2 headset to be accessible from Slicer?</p>
</blockquote>
</aside>
<p>I have built the Slicer version 5.3.0-2023-02-27 from the source code. Then, built the SlicerVR using this commit: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/commit/a5468fc3eb674cdbd2c724654e3e30d99f9ca360" rel="noopener nofollow ugc">“Rename VR interactor style callback functions”</a>.</p>
<ul>
<li>Copied the json files as discussed in <a href="https://discourse.slicer.org/t/slicervirtualreality-issues/23028">this topic</a> to make controllers work.</li>
<li>Connected the Quest 2 headset to the PC using a cable and Oculus PC app.</li>
<li>In the Quest 2, opened the Oculus Link from the menu and went to the Virtual Desktop.</li>
<li>In the PC, launched the SteamVR.</li>
<li>In the PC, opened the Slicer, loaded my volume and segmentation data, and clicked the headset icon on the top left.</li>
<li>Finally, it started the application through the SteamVR.</li>
</ul>
<p>I can see my controllers, fly around, grab and transform my segmentation (could not grab the volume). I can also see the volumes, but they disappear if I get close. Seems like volumes might have some clipping issues.</p>

---

## Post #4 by @cpinter (2023-03-21 10:04 UTC)

<p>I can confirm there is (at least was not long ago) a clipping issue with volume rendering in VR. There is no direct issue about this in the repository (although really falls under this one but not mentioned there either <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/91" class="inline-onebox">Address issues related to integration with VTK 9.1 · Issue #91 · KitwareMedical/SlicerVirtualReality · GitHub</a>). Feel free to open a new issue for this. The Kitware team is working on related things as their capacity allows.</p>
<p>FYI I personally am most interested in the two-handed interaction and the in-VR widget. I will try to revive the two-handed interactions but my free time is very limited.</p>

---

## Post #5 by @cpwadell (2025-01-15 23:32 UTC)

<p>I noticed that there’s was an R01 that was recently awarded to Kitware (congratulations! <a href="https://reporter.nih.gov/project-details/11050527" class="inline-onebox" rel="noopener nofollow ugc">RePORT ⟩ RePORTER</a>).  Does this mean that we can look forward to further development of the SlicerVR module in 2025?  My research involves a lot of segmentation in Slicer and ideally, I’d really like to be able to do this work in VR, similar to commercial applications like Elucis? <a href="https://www.realizemed.com/" rel="noopener nofollow ugc">Realize Medical</a></p>

---
