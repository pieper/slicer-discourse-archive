---
topic_id: 44751
title: "Us Probe Tracking With Aruco Marker"
date: 2025-10-13
url: https://discourse.slicer.org/t/44751
---

# US probe tracking with ArUco marker 

**Topic ID**: 44751
**Date**: 2025-10-13
**URL**: https://discourse.slicer.org/t/us-probe-tracking-with-aruco-marker/44751

---

## Post #1 by @Hamza_Oran (2025-10-13 20:57 UTC)

<p>Hello,</p>
<p>We want to track an ultrasound probe using an ArUco marker because we need to determine the probe’s position and orientation to perform 3D reconstruction of ultrasound images.</p>
<p>More specifically, our goal is to perform image-to-probe calibration so that we can accurately align the ultrasound images with the tracked probe position. I’ve seen similar workflows implemented using PLUS and 3D Slicer, but even after reading articles and manuals, I’m still quite lost.</p>
<p>I’m not very experienced in this area, and the setup seems quite complex.</p>
<p>In short, we have a Telemed ultrasound probe and an MMF-compatible webcam, and we would like guidance on how to set up a working tracking and image-to-probe calibration pipeline using ArUco markers.</p>
<p>Any help, documentation, or step-by-step instructions would be greatly appreciated.</p>

---

## Post #2 by @lassoan (2025-10-14 03:54 UTC)

<p>You can find detailed description on how to set up this tracking <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html">here</a>. If you have any specific questions then let us know.</p>
<p>Note, however, that error of ArUco marker tracking using a single webcam is about a magnitude larger than all other tracking solutions that are commonly used for ultrasound probe tracking. You can use a webcam for tracking in demos or student homework projects, but if the goal is to rely on a position tracker for ultrasound volume reconstruction then I would recommend not to waste your time with a webcam but get an inexpensive tracker, such as an OptiTrack Duo (costs about $3000).</p>

---

## Post #3 by @Hamza_Oran (2025-10-14 09:07 UTC)

<p>Thank you. Is there any manual or source for using FCal application with only ArUco marker based tracking ?</p>

---

## Post #4 by @lassoan (2025-10-14 18:16 UTC)

<p>FCal application performs the calibration in two main steps: landmark registration and probe calibration. Since the error of landmark registration would be very high if you use a single webcam, the subsequent probe calibration step would most likely fail.</p>
<p>If you want to set up a demo using ArUco marker tracking with a webcam, I would not recommend to use FCal. Instead, you can get the scale factors by scanning an object of known size and then use the transform sliders in Slicer to get a reasonable translation and rotation.</p>

---
