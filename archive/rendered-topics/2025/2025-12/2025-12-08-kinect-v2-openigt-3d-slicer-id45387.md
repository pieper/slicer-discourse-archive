# Kinect v2 >OpenIGT> 3D Slicer

**Topic ID**: 45387
**Date**: 2025-12-08
**URL**: https://discourse.slicer.org/t/kinect-v2-openigt-3d-slicer/45387

---

## Post #1 by @HazemShereef (2025-12-08 03:19 UTC)

<p>Hello, pardon me if what i am asking is obvious, I am a student still learning.</p>
<p>So i have been trying to add a support for Kinect V2 device to the Plus toolkit however it seems very hard for me because of the layers and layers of dependencies Plus was built on, when i try building i always fail.</p>
<p>So, i thought about a new approach, I want to get the Coordinate matrix (4x4 matrix, rotation and translation) of the tracker and reference by my self and send this matrix continuously to openigt server to show it in 3D slicer.<br>
What i am asking is, is that possible? would that replace the need for Plus Toolkit? or am i missing something important it does?<br>
Thank you</p>

---

## Post #2 by @lassoan (2025-12-08 03:25 UTC)

<p>Yes, if you don’t need highly accurate synchronization of several data streams (e.g., live ultrasound images and transforms) or very high frame rate then it should be easy to put together a Python script that acquires data from a Kinect and sends data via OpenIGTLink (via <a href="https://pypi.org/project/pyigtl/">pyigtl</a>).</p>
<p>Since Microsoft discontinued the Kinect about 2 years ago, we don’t plan to invest into improving Kinect support in Plus.</p>

---

## Post #3 by @Mark_Ryan (2025-12-08 21:36 UTC)

<p>Any recommendations for a replacement? Have been using a Leap Motion 2 which was also discontinued.</p>

---

## Post #4 by @adeguet1 (2025-12-08 22:17 UTC)

<p>You might want to take a look at <a href="https://realsenseai.com/" rel="noopener nofollow ugc">https://realsenseai.com/</a></p>

---

## Post #5 by @lassoan (2025-12-09 15:12 UTC)

<p>I would recommend <a href="https://realsenseai.com/">RealSense</a> cameras, too. They are supported in PLUS. For a while their future was uncertain but then Intel spun off a separate company for this and they seem to be alive and well.</p>

---

## Post #6 by @kareem_abdelaziz (2026-01-25 13:38 UTC)

<p>I have Access to Intel RealSense D435 Depth Camera, is there a Step by Step Guide on using it for a simple ArUco marker tracking project?</p>

---
