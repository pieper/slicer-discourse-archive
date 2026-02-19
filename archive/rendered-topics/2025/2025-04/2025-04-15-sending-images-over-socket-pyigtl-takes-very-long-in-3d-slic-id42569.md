---
topic_id: 42569
title: "Sending Images Over Socket Pyigtl Takes Very Long In 3D Slic"
date: 2025-04-15
url: https://discourse.slicer.org/t/42569
---

# Sending images over socket/pyigtl takes very long in 3D Slicer

**Topic ID**: 42569
**Date**: 2025-04-15
**URL**: https://discourse.slicer.org/t/sending-images-over-socket-pyigtl-takes-very-long-in-3d-slicer/42569

---

## Post #1 by @Daniel_L (2025-04-15 07:48 UTC)

<p>Hello everyone!</p>
<p>I am using a Raspberry Pi with an Intel Realsense to send images to 3D Slicer over a socket connection to create a point cloud out of them. Now sometimes it takes a very long time until the image is received in Slicer, it is irregular in between 2 seconds and 20 seconds.<br>
The thing is that on the Pi’s case I mounted a tracking tool, that is additionally tracked by a NDI camera, because I want to have the real life position of the point cloud that is created afterwards. Now the problem is if I move the tracked camera in between transmission, the position of the camera is different than to the time I took the image. That is why I send beforehand just a single Triggerbyte to capture the transformation. But even just receiving the trigger byte takes sometimes up to 10 seconds.</p>
<p>I also tested the same receiving code outside of Slicer, just with a VSC code and the triggerbyte is received instantly.<br>
Also I tried using “my own” socket connection, as well as a pyigtl implementation, there was no difference in transmission speed.<br>
Another interesting thing I noticed was that I feel like if I click into the 3D Slicer scene the byte comes as I click. It feels like Slicer only updates when clicked into the scene (and also after an irregular amount of time)</p>
<p>Did anyone have a similar issue?<br>
I am glad for every help received.</p>

---

## Post #2 by @lassoan (2025-04-17 04:38 UTC)

<p>You can directly connect your computer to a RealSense camera and an NDI tracker and stream synchronized tracking and point cloud data via OpenIGTLink using Plus toolkit. You csn receive updates within a fraction of a second. The Slicer module that can receive the data is available here:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/PerkLab/DepthImageToPointCloud">
  <header class="source">

      <a href="https://github.com/PerkLab/DepthImageToPointCloud" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/23caf48fa205f8606dc95ab8427b386a/PerkLab/DepthImageToPointCloud" class="thumbnail">

  <h3><a href="https://github.com/PerkLab/DepthImageToPointCloud" target="_blank" rel="noopener">GitHub - PerkLab/DepthImageToPointCloud: This repo contains a slicer module for generating...</a></h3>

    <p><span class="github-repo-description">This repo contains a slicer module for generating point clouds from static or streamed depth images.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Daniel_L (2025-04-18 08:58 UTC)

<p>Hello Andras,</p>
<p>Thank you for your reply. I already know about this slicer module and in fact I have been adapting it to my use case for over a year now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> . So my first steps were obviously to connect it to the computer and test everything from there. With that setup everything worked smoothly and as you said withing a fraction of a second I get the data. But now I would like the setup to be wireless, so I build a device including a Raspberry Pi, which sends the depth image of the Realsense over a socket connection to Slicer every button press. And here comes the issue I described.</p>
<p>So I want it to be transmitted over Wifi, so it is cableless. Do you have any experience with such described delays?</p>

---
