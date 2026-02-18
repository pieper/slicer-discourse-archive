# Black screen on VR

**Topic ID**: 23076
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/black-screen-on-vr/23076

---

## Post #1 by @Eserval (2022-04-21 17:23 UTC)

<p>Hello friends,</p>
<p>I just bought a new notebook VR ready, however, when I try to open the VR module I have just a black screen. It<code>s weird because I</code>m using the same process on my desktop (inferior hardware configuration), the same glass, etc… It should be some specs on the laptop. Does anyone have any clues or has been through something like this?</p>

---

## Post #2 by @cpinter (2022-04-22 11:47 UTC)

<p>Do you use the same Slicer version as well? There have been updates in the VR module recently that broke certain things, so an older version (before 2022.02.24) may work better at the moment.</p>

---

## Post #3 by @Eserval (2022-04-23 22:12 UTC)

<p>It’s the same version. I belive that the Slicer is activating the integrated grafic card that could not support VR.</p>

---

## Post #4 by @cpinter (2022-04-25 09:12 UTC)

<p>In that case you can choose the card used for Slicer in the graphics card’s app. For NVidia card it’s in the NVidia Control Panel, and the application is SlicerApp-real.exe</p>

---

## Post #5 by @Eserval (2022-05-27 22:57 UTC)

<p>That works fine. Now I`m having truble with the controlers. I can see them, but the button does not work.</p>

---

## Post #6 by @pixellett (2022-07-21 04:33 UTC)

<p>Did you manage to sort the issue with controllers Eserval?  I am hitting the exact same issue, even with the .json files from vtk that someone suggested in another thread.</p>

---

## Post #7 by @Eserval (2022-07-25 11:37 UTC)

<p>Hello,</p>
<p>Still have the same problem. I did not try with the new version. The interesting is that using the Desktop, with the  4.13.0-2022-03-13 it works really fine.<br>
The desktop hardware has a lower configuration than the desktop.</p>
<p>Do you have any news?</p>
<p>bests</p>

---

## Post #8 by @cpinter (2022-07-26 10:49 UTC)

<aside class="quote no-group" data-username="Eserval" data-post="7" data-topic="23076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eserval/48/14650_2.png" class="avatar"> Eserval:</div>
<blockquote>
<p>Still have the same problem</p>
</blockquote>
</aside>
<p>Which one? The issue in the topic seems to have been resolved. Do you mean the controller buttons? Please elaborate.</p>

---

## Post #9 by @Eserval (2022-07-26 13:33 UTC)

<p>Hello !</p>
<p>I’m having trouble with the controls. I have the image in the VR envarioment however the control buttons doesn’t wortk. Do you think its better to create a new topic? I can send images or some other usefull information you need.</p>
<p>Best</p>

---

## Post #10 by @cpinter (2022-07-27 11:30 UTC)

<p>No need, this is a known issue. See a quick summary of the current state of SlicerVR here</p><aside class="quote quote-modified" data-post="11" data-topic="23028">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicervirtualreality-issues/23028/11">SlicerVirtualReality issues</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the update <a class="mention" href="/u/rbumm">@rbumm</a> , quite useful! 
We are currently in an “almost there” state with SlicerVR on many fronts. 

OpenXR support can be expected to be finalized soon in terms of the new Kitware-Robarts project (at least as far as I know using OpenXR is in the plans for this project - they want HoloLens2 support)
In-VR widget exposing many Slicer features is on the way. The widget works, the laser pointer basically works. We currently struggle with that the texture update that shows in th…
  </blockquote>
</aside>

<p>You can try it with a Slicer older than Feb 25, 2022 (before 7da00248941292c429ba11204d3a5a7d78210a46), or wait until OpenXR support is fully functional.</p>

---

## Post #11 by @Eserval (2022-07-27 12:00 UTC)

<p>Thanks for the reply. It may be a dumby question, but, how can I download older versions ?</p>
<p>bests</p>

---

## Post #12 by @Eserval (2022-07-27 12:08 UTC)

<p>Just found a topic about it.</p>
<aside class="quote quote-modified" data-post="1" data-topic="23378">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/naninano1/48/13621_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/older-versions-of-3d-slicer/23378">Older versions of 3D Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
Since my laptop does not support the Open GL, I receive this error: 
See more information and help at: 
<a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Slicer_does_not_start" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Slicer_does_not_start</a> 
Graphics capabilities of this computer: 
Renderer does not support required OpenGL capabilities. 
I am using Ver 4.11. 
To override this error I thought I may use older versions like v4.5. But I couldn’t find the older versions for download. 
I was wondering how it is possible to download older windows ve…
  </blockquote>
</aside>

<p>Best</p>

---
