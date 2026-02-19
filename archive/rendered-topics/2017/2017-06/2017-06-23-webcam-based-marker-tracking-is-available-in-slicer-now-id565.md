---
topic_id: 565
title: "Webcam Based Marker Tracking Is Available In Slicer Now"
date: 2017-06-23
url: https://discourse.slicer.org/t/565
---

# Webcam-based marker tracking is available in Slicer now

**Topic ID**: 565
**Date**: 2017-06-23
**URL**: https://discourse.slicer.org/t/webcam-based-marker-tracking-is-available-in-slicer-now/565

---

## Post #1 by @lassoan (2017-06-23 20:35 UTC)

<p>While 3D Slicer - using SlicerIGT/Plus - have been supporting real-time position tracking using high-end devices (optical trackers, electromagnetic trackers, surgical navigation system, etc), there has been no ultra-low-cost tracking solution available - until now.</p>
<p>With latest version of Plus toolkit you can connect any webcam, print your own markers, and start tracking objects - and show them in real-time in 3D Slicer.</p>
<div class="lazyYT" data-youtube-id="MOqh6wgOOYs" data-youtube-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Many thanks to Mark Asselin at PerkLab for adding this feature!</p>
<p>While the tracking is already reasonable accurate to be suitable for certain applications, we are implementing further improvements during the next couple of months.</p>
<p>See more details of how to set it up in comments of the <a href="https://youtu.be/MOqh6wgOOYs">YouTube video</a>.</p>

---

## Post #2 by @cpinter (2017-06-28 09:50 UTC)

<p>Can you please upload the Slicer scene somewhere so that it can be easily tried without having to create each object with CreateModels? It would make it much easier for others to start. Thanks!</p>

---

## Post #3 by @lassoan (2017-06-28 13:17 UTC)

<p>Good idea. An example <a href="https://github.com/PlusToolkit/PlusLibData/raw/master/ConfigFiles/OpticalMarkerTracker/OpticalMarkerTracker_Scene.mrb">3D Slicer scene file is available here</a>.</p>
<p>It displays markers that are in this <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/OpticalMarkerTracker/marker_sheet_36h12.pdf">marker sheet (pdf file, ready for printing)</a>. You may need to zoom in-out 3D views after you place the markers in the field of view of your camera to make the markers show up.</p>

---

## Post #4 by @robmbar (2018-05-28 19:45 UTC)

<p>I am having a problem with the device set configuration file in Plus Server Launcher. After choosing the device set “PlusServer: Optical marker tracker using MMF video”, I have followed the example presented here <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html</a> to create the file but when launched, an error occurs and the connection fails.<br>
I am trying to use the built-in webcam of my laptop. Is it possible to upload a different example file for this application? I can’t figure out where is the error. Thanks!</p>

---

## Post #5 by @lassoan (2018-05-28 20:12 UTC)

<p>It seems that you need help with getting Plus set up right. To get help on this, please <a href="https://github.com/PlusToolkit/PlusLib/issues/new">submit an issue on Github page of Plus</a>.</p>

---

## Post #6 by @robmbar (2018-05-28 20:34 UTC)

<p>Thanks for your prompt reply!</p>

---

## Post #7 by @kamrul079 (2018-08-31 16:55 UTC)

<p>I’ve updated the links now (Plus repositories moved since the time of the original post).</p>

---

## Post #8 by @lassoan (2018-09-04 15:35 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-set-up-real-time-position-tracking-of-tools-using-2d-barcodes/3985">How to set up real-time position tracking of tools using 2D barcodes</a></p>

---

## Post #9 by @apparrilla (2019-11-02 09:54 UTC)

<p>I´m trying to make from scratch my own 3d Slicer scene and I´ve problems creating vector volume image_image. I´m following SlicerIGT tutorials but i can´t find solution. Thanks!</p>

---

## Post #10 by @lassoan (2019-11-03 02:07 UTC)

<p>Normally you would just let OpenIGTLinkIF module create image and transform nodes for you, but you can certainly create them from your own Python script, too. Here is an example of creating a scalar volume node: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume</a>. You can create a vector volume node very similarly.</p>

---

## Post #11 by @apparrilla (2019-11-03 11:07 UTC)

<p>Thanks Andras, really usefull info.</p>

---

## Post #12 by @apparrilla (2019-11-10 15:33 UTC)

<p>Little more complex. How can I add a second video source to the scene?<br>
I have 2 Plus connections with different ports for each device (18944/18945 and 18954/18955). Both successfully connected. I´ve added in OpenIGTLinkIF 2 connectors for the second camera and config properly ports but … i have no Image2-image2 (as I´ve called in Plus xml config file) vectorvolume. OpenIGTLinkIF has not create input volume nor transforms from camera and tracker.<br>
Is there any way to create them without code?<br>
Thanks on advance!</p>

---

## Post #13 by @lassoan (2019-11-14 13:56 UTC)

<p>This should be no problem, if you receive images with different names then the nodes should be created in the scene automatically. If this is still a problem then create a new topic and provide more details (the full Plus config file, etc.).</p>

---
