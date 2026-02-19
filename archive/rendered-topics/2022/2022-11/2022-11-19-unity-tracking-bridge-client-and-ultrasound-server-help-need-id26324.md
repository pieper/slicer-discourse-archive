---
topic_id: 26324
title: "Unity Tracking Bridge Client And Ultrasound Server Help Need"
date: 2022-11-19
url: https://discourse.slicer.org/t/26324
---

# Unity tracking bridge client and ultrasound server... help needed

**Topic ID**: 26324
**Date**: 2022-11-19
**URL**: https://discourse.slicer.org/t/unity-tracking-bridge-client-and-ultrasound-server-help-needed/26324

---

## Post #1 by @Allan (2022-11-19 17:23 UTC)

<p>Hi all,</p>
<p>I am pretty new to slicer, actually I stumbled over it yesterday and I have a problem that could be easy to solve or it is just impossible <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I have some experience in spatial tracking using unity with all kinds of hardware and really like it. Recently I stumbled over a Telemed ultrasound device and the idea was born to use an object tracked in the unity coordinate frame and combine it with the tracked ultrasound surface reconstruction that is well implemented in Slicer.<br>
So far I managed it to get the outdated Unity OpenIGTLink scripts working and, with a Server started in Slicer I get the transforms and rotations of my trackables displayed in the 3D view as expected.<br>
On the other hand, if I start the Plus server and switch slicer in client mode, I get the ultrasound images of the Telemed device displayed in slicer.<br>
Unfortunately I am no networking specialist and so far not as experienced with slicer to find a simple solution to get both features combined. Because the Unity script only listens to a server and sends some transformations back I have a Client / Server paradoxon and would need Slicer to work as Server for the trackables and as client for the US images simultaniously.</p>
<p>Maybe it is only some xml magic in the Plus server configs so that the server catches the transformations send from unity and parses it to a Slicer client together with the US image…but so far I could not manage  it.<br>
At least Unity does not crash when the plus server is launched so they are communicating.</p>
<p>Any help is much appreciated!</p>
<p>Best regards</p>
<p>Allan</p>
<p>Operating system: Windows 10<br>
Slicer version: 5.0.3<br>
Expected behavior: Working<br>
Actual behavior: Not working</p>

---

## Post #2 by @slicer365 (2023-06-25 09:47 UTC)

<p>Do  you have connected the unity with 3D Slicer elements?</p>

---

## Post #3 by @lassoan (2023-06-27 02:48 UTC)

<p>There is  a more recent Unity/Slicer integration project by <a class="mention" href="/u/aliciapose">@AliciaPose</a>:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/1d0157a7a50a0c35b3956925b10394a13952db3dd75d7fe4dfb4a0d270d3a27b/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning: GitHub...</a></h3>

  <p>GitHub repository for the IJCARS paper: "Real-Time open-source integration between Microsoft HoloLens 2 and 3D Slicer" - GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlann...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It allows sending/receiving transforms and sending an image stream from Slicer to Unity.</p>

---

## Post #4 by @Allan (2023-08-08 16:47 UTC)

<p>That looks promising, I´ll give it a try. I also thought about using the already available Slicer VR-Pipeline to attach the ultrasound images to a vive tracker as a low-cost navigation solution which should also enable the ultrasound segmentation capability of slicer. I´ve done some experiments in the past to get rid of the headset requirement in steamVR so maybe I find the time to try both ideas. Thanks a lot for your response.</p>

---
