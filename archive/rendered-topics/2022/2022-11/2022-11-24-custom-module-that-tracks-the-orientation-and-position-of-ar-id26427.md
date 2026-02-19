---
topic_id: 26427
title: "Custom Module That Tracks The Orientation And Position Of Ar"
date: 2022-11-24
url: https://discourse.slicer.org/t/26427
---

# Custom module that tracks the orientation and position of arUco markers in real time

**Topic ID**: 26427
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/custom-module-that-tracks-the-orientation-and-position-of-aruco-markers-in-real-time/26427

---

## Post #1 by @GbekeAdesiyun (2022-11-24 18:49 UTC)

<p>Hi,</p>
<p>I’m currently writing a custom module that tracks the orientation and position of arUco markers in real-time, but I haven’t figured out how to track the markers in real-time. Could you give me some advice on what I can do to achieve this?</p>
<p>Thanks,<br>
Mogbekeloluwa Adesiyun</p>

---

## Post #2 by @ungi (2022-11-25 01:50 UTC)

<p>Hi, this is already implemented in PLUS: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Optical Marker Tracker</a><br>
There is a tutorial on how to use it in this repository: <a href="https://github.com/PerkLab/PerkLabBootcamp" class="inline-onebox" rel="noopener nofollow ugc">GitHub - PerkLab/PerkLabBootcamp: Materials for the yearly PerkLab bootcamp course</a><br>
Look at Doc/day2_Plus.pptx<br>
PLUS communicates with Slicer though the OpenIGTLinkIF module. Using PLUS instead of implementing a direct interface to hardware in Slicer keeps Slicer less dependent on hardware-specific libraries.</p>

---

## Post #3 by @GbekeAdesiyun (2022-11-25 17:45 UTC)

<p>Hi,</p>
<p>Thanks for your reply. The Optical Marker Tracker shown in the link you sent tracks the markers, but the Tracker doesn’t record the position of the markers at any given time. I’m trying to develop an automatic way of tracking the orientation and position of the markers in real-time; so, would you be able to point me in the right direction?</p>
<p>Thanks,<br>
Mogbekeloluwa Adesiyun</p>

---

## Post #4 by @ungi (2022-11-25 18:38 UTC)

<p>All PLUS optical tracker devices compute the positions of optical markers relative to the camera by default. PLUS can also compute their positions relative to each other, based on the transform name you specify in the config file. Using the OpenIGTLink server in PLUS, send to Slicer whatever makes most sense in your application. PLUS will compute the transformation between markers based on the transform name you specify in the server part of the PLUS config file. Tracking information will be sent to Slicer from PLUS in real time. You don’t need to code anything to use the marker positions in real time in Slicer.</p>
<p>You may add a CaptureDevice in the PLUS config file to record real time data into files without Slicer. But I recommend using the Sequences module in Slicer to record time-series data. Slicer Sequences gives you more options when you need to replay this data (pause, rewind, etc.).</p>
<p>The PerkLab bootcamp tutorials (link in my previous message) provide step-by-step instructions how to do these.</p>

---

## Post #5 by @GbekeAdesiyun (2022-11-25 18:47 UTC)

<p>Okay, I will look into that. Thanks</p>

---

## Post #6 by @GbekeAdesiyun (2022-12-01 19:01 UTC)

<p>I went through the webpage you sent, but I don’t think that effectively solves my problem. I’m trying to figure out the lines of code to add to a Slicer module that will ensure I have access to a live scene. I already know the algorithm that will extract the position of the arUco markers from the transform node, so I just need to find out how to use a live scene in the module. Any pointers on what I can do?</p>

---

## Post #7 by @GbekeAdesiyun (2022-12-05 17:50 UTC)

<p>Hey just following up to see if you have any more advice regarding this topic</p>

---
