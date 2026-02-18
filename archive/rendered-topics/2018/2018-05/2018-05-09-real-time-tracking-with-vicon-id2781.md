# Real-time tracking with Vicon

**Topic ID**: 2781
**Date**: 2018-05-09
**URL**: https://discourse.slicer.org/t/real-time-tracking-with-vicon/2781

---

## Post #1 by @val.dil (2018-05-09 03:14 UTC)

<p>Hello!<br>
I want to develop an extension that aim to acquire in real time the position of some markers and visualize them on a MRI, this is in order to track the position of an electrode inside the brain during a brain surgery.<br>
Actually I used the Vicon system to acquire the positions of the markers and saved them in a .txt file.<br>
My question is, how can i read in real time the .txt file and visualize the updated position on the MRI?<br>
Thanks for your helping.</p>

---

## Post #2 by @lassoan (2018-05-09 03:23 UTC)

<p>Most of these features (and many more) are readily available in <a href="http://www.slicerigt.org">SlicerIGT extension</a> and <a href="http://www.plustoolkit.org">Plus toolkit</a>. You can track sensors, reconstruct paths real-time and show it in Slicer.</p>
<p>You can use a wide range of electromagnetic and optical trackers (NDI, OptiTrack, Claron, NDI, Ascension, etc.). We currently don’t support Vicon systems, as they are very expensive and for surgical tool tracking there are much better alternatives. For example, OptiTrack Duo cameras provide very good tracking (comparable to NDI Polaris medical device grade trackers), good software, great flexibility of markers (you can use not just spheres but reflective disks on 3D-printable frames) for $3000. If you must use Vicon then you could implement a VRPN interface in Plus toolkit - if you choose to do this, then let us know and we’ll help you to get started.</p>
<p>Let us know if you have more specific questions. Slicer has large navigation and image-guided therapy community with lots of experience in these topics.</p>

---

## Post #3 by @wpgao (2018-05-09 03:34 UTC)

<p>Maybe you can use openigtlink in c/s mode or develop a module to read the file and update the transformation node!</p>

---

## Post #5 by @val.dil (2018-05-09 12:48 UTC)

<p>Thanks for the reply.<br>
I don’t aim to implement a virtual reality interface, because i don’t have the equipment and the Vicon system is only what the lab offers to me. However thanks for the support.<br>
Do you think that it’s possible to directly aquire in real time, by SlicerIGT or Plus toolkit, the data from the Vicon system using the client/server mode?</p>

---

## Post #6 by @val.dil (2018-05-09 12:51 UTC)

<p>Thanks for the reply.<br>
Do you think that is possibile to read the file while it is updated by the vicon in real time?</p>

---

## Post #7 by @lassoan (2018-05-09 13:19 UTC)

<aside class="quote no-group" data-username="val.dil" data-post="5" data-topic="2781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/6bbea6/48.png" class="avatar"> val.dil:</div>
<blockquote>
<p>Do you think that it’s possible to directly aquire in real time, by SlicerIGT or Plus toolkit, the data from the Vicon system using the client/server mode?</p>
</blockquote>
</aside>
<p>As far as I know, for real-time tracking data transfer Vicon supports VRPN protocol and maybe has its own proprietary communication protocol, too. Slicer understands OpenIGTLink protocol. So you need to convert between these two protocols. PlusServer application in Plus toolkit can do protocol conversion for many devices, so it would not be too difficult to add conversion from VRPN or Vicon’s own protocol. Or you can develop a converter on your own, which receives messages from Vicon and sends them to Slicer using OpenIGTLink.</p>

---

## Post #8 by @AurelieS (2024-03-05 09:13 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
We are two engineers that want to develop the integration of Vicon into Slicer 3D. Our objective is to combine motion capture and 3D ultrasound using the same device, for example to integrate personalized muscle insertions and muscle paths into musculoskeletal models.<br>
I saw this discussion and I think we will start by trying to convert the VRPN protocol into a OpenIGTLink protocol.<br>
I just wanted to know if you had any new information, if someone already tried this ? or also do you have any advices for us ?<br>
Best,<br>
Aurélie</p>

---

## Post #9 by @lassoan (2024-03-05 11:35 UTC)

<p>I am not aware of any VRPN implementations for PLUS. It would be great if you could work on it.</p>

---
