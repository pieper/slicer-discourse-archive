---
topic_id: 38111
title: "Plus Server Support For Motion Capture Systems Optitrack Wit"
date: 2024-08-29
url: https://discourse.slicer.org/t/38111
---

# PLUS server support for motion capture systems (Optitrack with Motive 3.x and VICON)

**Topic ID**: 38111
**Date**: 2024-08-29
**URL**: https://discourse.slicer.org/t/plus-server-support-for-motion-capture-systems-optitrack-with-motive-3-x-and-vicon/38111

---

## Post #1 by @modenaxe (2024-08-29 10:14 UTC)

<p>Hello,<br>
I am looking into the PLUS toolkit documentation and tutorials with the aim of  building a 3D Ultrasound setup and I am writing with the hope of understanding if the support to the Optitrack motion capture system is still maintained or limited to Motive 2.1.2 as the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html" rel="noopener nofollow ugc">current documentation</a> suggests. Currently Motive 3.x is available and shipped with the new Optitrack systems.<br>
Also, I take the occasion of asking if there is any support or possibility of interfacing a VICON system with PLUS.<br>
Thank you for the great resources that you made available!<br>
Luca</p>

---

## Post #2 by @Sunderlandkyl (2024-08-29 13:54 UTC)

<p>The documentation is slightly out of date, the current version used in 64-bit Plus installers is 2.3.2, I don’t think there were any issues locking Plus to that version, so I will look into updating to 2.3.7.</p>
<p>Plus can be compiled with 3.x support (specifically 3.0.3), however it wasn’t included in the packages due to 3.0.x versions not supporting OptiTrack Duo/Trio cameras. It looks like support for USB cameras was re-introduced in Motive 3.1, so it would be worth trying again.</p>
<p>There is currently no support for VICON systems. This was first brought up in 2018, though no-one has contributed any implementation to Plus since then:<br>
<a href="https://discourse.slicer.org/t/real-time-tracking-with-vicon/2781/7" class="inline-onebox">Real-time tracking with Vicon - #7 by lassoan</a>.</p>

---

## Post #3 by @modenaxe (2024-09-06 05:00 UTC)

<p>Thank you Kyle, this is very helpful because Motive 2.x and 3.x have different licenses so it is not a trivial choice. Based on your reply I think I will look into Motive 2.x then!</p>

---

## Post #4 by @daimon2 (2025-08-04 08:27 UTC)

<p>Hello Sir, I am currently using Optitrack DUO with Motive 3.3.4. However, Motive 3.3.4 no longer allows exporting .xml configuration files or rigid bodies in .tra format. Instead, it exports .motive and rigid bodies in .motive/.csv format. Additionally, there have been some changes in the broadcasting method. It seems that PLUS is unable to recognize the data stream (in NatNet stream format), and the download link for the earlier version Motive 2.x is no longer available.</p>

---

## Post #5 by @modenaxe (2025-08-04 10:57 UTC)

<p>Hello, we are now using Motive 2.x (we don’t have a 3.x license), so I am afraid I cannot help you with this issue.</p>

---
