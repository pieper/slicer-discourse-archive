---
topic_id: 19862
title: "How To Make The Stylus More Smooth And Stable"
date: 2021-09-26
url: https://discourse.slicer.org/t/19862
---

# How to make the stylus more smooth and stable

**Topic ID**: 19862
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/how-to-make-the-stylus-more-smooth-and-stable/19862

---

## Post #1 by @slicer365 (2021-09-26 09:26 UTC)

<p>Dear friends,</p>
<p>when I use IGT and camera-based navigation simulation,</p>
<p>as this video shows, the movement of the stylus is always stuck and not smooth.</p>
<p>how to solve this problem？<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f5dca1f40fdc037779716ef6502fdb4323c740a.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f5dca1f40fdc037779716ef6502fdb4323c740a.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f5dca1f40fdc037779716ef6502fdb4323c740a.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @lassoan (2021-09-27 03:00 UTC)

<p>Do you use the aruco marker tracker? Unstable tracking is usually due to uncalibrated camera or markers printed in incorrect size, but may be due to using too small markers, low camera resolution, inadequate lighting, etc.</p>

---

## Post #3 by @lassoan (2021-09-27 14:33 UTC)

<p>5 posts were split to a new topic: <a href="/t/how-to-improve-optitrack-duo-tool-tracking-stability/19882">How to improve OptiTrack Duo tool tracking stability</a></p>

---

## Post #8 by @slicer365 (2021-09-27 12:26 UTC)

<p>Trhank you !</p>
<p>Yes,it is aruco marker tracker.How to calibrated camera?</p>

---

## Post #9 by @lassoan (2021-09-27 15:18 UTC)

<p>Camera calibration procedure is described in <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html">Plus Toolkit’s User manual</a>. See Calibration section.</p>

---

## Post #10 by @J.vd.Zee (2022-06-14 12:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I am new to Cmake, C++, OpenCV etc. and i am not able to do the calibration procedure.<br>
Could you explain how the calibration needs to be performed?<br>
The aruco_calibration.exe is not working.</p>
<p>Thanks in advance!</p>

---

## Post #11 by @lassoan (2022-06-15 03:17 UTC)

<p>Setup instructions are available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html">here</a>. If you run into any issues then please provide details.</p>
<aside class="quote no-group" data-username="J.vd.Zee" data-post="10" data-topic="19862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/j.vd.zee/48/15064_2.png" class="avatar"> J.vd.Zee:</div>
<blockquote>
<p>The aruco_calibration.exe is not working.</p>
</blockquote>
</aside>
<p>What did you do? How did you run it exactly? What camera do you use? What are the available image resolutions of the camera?</p>
<p>What did you expect to happen?<br>
What happened instead?</p>

---

## Post #12 by @J.vd.Zee (2022-06-17 14:37 UTC)

<p>I managed!</p>
<p>I downloaded the CMake-gui software and was able to right click on the folder to start ‘git Bash Here’. With the CMake I was able to start the calibration procedure.</p>
<p>Thanks again for you help!</p>

---

## Post #13 by @ChristophG123 (2022-07-19 18:42 UTC)

<p>Hi, how did you get this working? I am able to enter Git Bash and run the following command line without errors:<br>
<code>start aruco_calibration.exe live:0 camera_calibration.yml -size 0.03556</code></p>
<p>But it doesn’t show any GUI and I can’t find any new files from it. How did you use CMake-gui to get this working? Thanks.</p>
<p>Update: I was able to get it working by installing a Qt5Test DLL file. When I tried running the executable, it said this was missing. Now the program works perfectly.</p>

---

## Post #14 by @adamrankin (2022-07-19 19:05 UTC)

<p>Dependency Walker showed missing dependency: Qt5Test.dll</p>
<p>Copied from another Qt5.15 SDK installation and it ran as expected.</p>
<p>Missing from packaging in Plus?</p>

---
