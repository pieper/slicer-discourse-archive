---
topic_id: 12730
title: "Optitrack Duo And External Webcam Problem"
date: 2020-07-25
url: https://discourse.slicer.org/t/12730
---

# Optitrack Duo and external webcam problem

**Topic ID**: 12730
**Date**: 2020-07-25
**URL**: https://discourse.slicer.org/t/optitrack-duo-and-external-webcam-problem/12730

---

## Post #1 by @apparrilla (2020-07-25 11:31 UTC)

<p>Hi everyone.<br>
I’ve config Plus for sending both Duo and webcam data to Slicer. Duo is working properly but webcam have some trouble.<br>
It is configured as WMvideo device and Duo and webcam are connected to different usb3 ports.<br>
I saw webcam image in just low resolution config (172x144) and with some delay and stops. If I witch off Duo connector, webcam becomes working fine, even in 640*480 mode without delay. It looks like some problem with DirectShow or something similar.<br>
Thanks on advance.</p>

---

## Post #2 by @lassoan (2020-07-25 15:19 UTC)

<p>What computer is this? What webcam do you use?</p>
<p>Maybe you could try to connect one or both devices through an externally powered USB hub to make sure the issue is not due to too much power consumption.</p>
<p>You could also try lowering the webcam framerate to see if it helps.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> have we experienced similar issues before?</p>

---

## Post #3 by @Sunderlandkyl (2020-07-25 16:00 UTC)

<p>I don’t remember an issue like this coming up.</p>
<p><a class="mention" href="/u/apparrilla">@apparrilla</a> What versions of Plus and Motive are you using? Can you upload your config file somewhere?</p>

---

## Post #4 by @lassoan (2020-07-25 19:03 UTC)

<p>You may also try running the webcam and tracker data acquisition in two different PlusServer processes and see if it makes any difference.</p>

---

## Post #5 by @apparrilla (2020-07-25 19:24 UTC)

<p>Sorry.<br>
Win10<br>
Slicer 4.11.0-2020-07-04 r29204<br>
PlusApp-2.8.0.20191105-Win64<br>
Motive 2.2 Final (last)</p>
<p>Config file:<br>
<a href="https://drive.google.com/file/d/1afhJFWmfmYI3YtM4b33ND_pQeIiOvElu/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/1afhJFWmfmYI3YtM4b33ND_pQeIiOvElu/view?usp=sharing</a></p>

---

## Post #6 by @apparrilla (2020-07-25 19:28 UTC)

<p>They are connected to a different USB central port each other and it´s a desktop. I think it´s not a power or bandwidth problem.<br>
Webcam device is 30fps for reference but i´m going to low down for a try.<br>
Two different Plus processes was my first aproach to fit it but it didn´t work.<br>
It´s not really a webcam, it´s a USB endoscope but it works with Win Camera App properly.</p>

---

## Post #7 by @apparrilla (2020-07-28 09:13 UTC)

<p>Finally NaturalPoint Support Team has answare to me ant it looks like there is no way to fix it:</p>
<blockquote>
<p>HI Angel,<br>
Glad to help!<br>
This is a known issue that can’t be addressed, unfortunately. You’ll be unable to run both the web camera and the Duo on the same computer.<br>
Best,<br>
Ryan<br>
OptiTrack Support</p>
</blockquote>

---

## Post #8 by @lassoan (2020-07-29 02:28 UTC)

<p>Thank you, it is bad news, but useful to know.</p>

---

## Post #9 by @J.vd.Zee (2022-09-12 09:31 UTC)

<p>Hi!<br>
This post has been ‘solved’ two years ago with the message it is not possible.<br>
Is there any progress on this topic from then?</p>
<p>I would like to track with an OptiTrack system and capture ultrasound data via an Epiphan framegrabber. Anyone ideas for a workaround?</p>
<p>Regards!</p>

---

## Post #10 by @lassoan (2022-09-16 04:09 UTC)

<p>Please contact OptiTrack support and report back what they said.</p>
<p>As a workaround, you can connect the tracker and camera to two different computers and stream the images and transforms via OpenIGTLink.</p>

---
