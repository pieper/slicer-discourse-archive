---
topic_id: 7925
title: "Sending Transformed Ultrasound Data To Unity For Ar Overlay"
date: 2019-08-07
url: https://discourse.slicer.org/t/7925
---

# Sending Transformed Ultrasound Data to Unity for AR Overlay

**Topic ID**: 7925
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/sending-transformed-ultrasound-data-to-unity-for-ar-overlay/7925

---

## Post #1 by @David_Asgar-Deen (2019-08-07 17:39 UTC)

<p>Hello,</p>
<p>Thank you for taking the time to read this post. I am currently working on visualizing ultrasound slice data through a <a href="https://www.researchgate.net/profile/Ingela_Nystroem/publication/41616685/figure/fig3/AS:667871751462938@1536244442637/A-SenseGraphics-display-with-a-PHANToM-device-Stereo-graphics-is-rendered-onto-a_W640.jpg" rel="nofollow noopener">semi-transparent mirror AR display</a> and was hoping to get some help sending the data to Unity. I am currently using a SonixTouch Ultrasound machine with 2 6DOF NDI Aurora trackers. I have seen several resources showing me how to do the volume reconstruction of the US slices (haven’t completed this step yet), but I was wondering if there was any way to send the transformed data to Unity for further visualization (maybe through a Plus server?). Any help or assistance in this project would be greatly appreciated.</p>
<p>Thanks for taking the time to read this and I hope someone will be able to help me with my task!</p>

---

## Post #2 by @J.vd.Zee (2022-06-07 08:57 UTC)

<p>Did you made any progress? Really curious in this topic as I am looking for the same application!</p>

---

## Post #3 by @mau_igna_06 (2022-06-07 09:00 UTC)

<p>I think you may be able to do that on igtlink<br>
<a class="mention" href="/u/ungi">@ungi</a> may help</p>

---

## Post #4 by @J.vd.Zee (2022-06-07 09:19 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="7925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>igtlink</p>
</blockquote>
</aside>
<p>Thanks for your response!<br>
I am interested in using the Hololens as tracking device and sending it’s transformation into Slicer. Secondly, doing my registration procedure in Slicer and sending the resulting transformation to the Hololens/Unit for visualization thereafter. The user case is a tracked-US bone based registration using the Hololens.</p>
<p>To what extent is the work of <a class="mention" href="/u/franklinwk">@franklinwk</a> applicable for my usercase?</p>

---

## Post #5 by @ungi (2022-06-07 15:16 UTC)

<p>I haven’t used HoloLens yet. But Slicer certainly can import and export transformations, images, points, string messages, etc. through OpenIGTLink with minimal latency. OpenIGTLink is a very simple communication protocol that can be added to any project without dependencies.</p>

---

## Post #6 by @lassoan (2022-06-13 13:16 UTC)

<p>You can certainly build Unity applications that communicate with Slicer via OpenIGTLink. You can find code fragments in various projects for OpenIGTLink protocol implementation for Unity.</p>
<p>However, we would to move beyond Unity, because although it is very easy to get started with Unity, you need to reimplement lots of basic features. Instead, we are aiming for using OpenXR for rendering in Slicer directly to display in all kinds of compatible AR and VR headsets. The implementation is still experimental in VTK library and only some preliminary tests have been done in Slicer, but there is no readily usable solution yet. I would recommend to join the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">upcoming project week</a> to learn more and collaborate with others on this topic.</p>

---
