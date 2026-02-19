---
topic_id: 1874
title: "Camera Calibration"
date: 2018-01-19
url: https://discourse.slicer.org/t/1874
---

# Camera calibration

**Topic ID**: 1874
**Date**: 2018-01-19
**URL**: https://discourse.slicer.org/t/camera-calibration/1874

---

## Post #1 by @adamrankin (2018-01-19 19:27 UTC)

<p>Hello,</p>
<p>Are there any current extensions for camera calibration and registration?</p>
<p>Adam</p>

---

## Post #2 by @timeanddoctor (2018-01-19 23:39 UTC)

<p>I am interesting too</p>

---

## Post #3 by @lassoan (2018-01-22 19:41 UTC)

<p>I think <a class="mention" href="/u/drouin-simon">@drouin-simon</a> plans to implement a Slicer module for it, and collaborators of <a class="mention" href="/u/tokjun">@tokjun</a> worked on releated topics in the past. They may be able to give you more information.</p>

---

## Post #4 by @adamrankin (2018-01-23 14:18 UTC)

<p>Starting work here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/VASST/SlicerPinholeCameras">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/VASST/SlicerPinholeCameras" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/f113c88073970f5c539974a12502f58562578e413a00d857ab3a97318f1d32d6/VASST/SlicerPinholeCameras" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/VASST/SlicerPinholeCameras" target="_blank" rel="noopener nofollow ugc">GitHub - VASST/SlicerPinholeCameras: An extension for interacting,...</a></h3>

  <p>An extension for interacting, calibrating, and using cameras in Slicer - GitHub - VASST/SlicerPinholeCameras: An extension for interacting, calibrating, and using cameras in Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @OTI (2018-12-04 06:41 UTC)

<p>I want to use SlicerVideoCameras extension, but I cant find it. How can I use this?</p>

---

## Post #6 by @OTI (2018-12-04 07:13 UTC)

<p>I use Slicer4.10.0 on win64.</p>

---

## Post #7 by @adamrankin (2018-12-04 14:52 UTC)

<p>I will see if it’s being built on the build machines.</p>
<p>Edit: Tests are failing on precursor extension, making a build now to fix tests.</p>

---

## Post #8 by @adamrankin (2018-12-05 15:35 UTC)

<p>Sorry, build took a long time, I am still investigating.</p>

---

## Post #9 by @adamrankin (2018-12-12 15:17 UTC)

<p>Sorry for the massive delay, tonight’s (tomorrow morning’s) build should show us whether my fixes worked.</p>

---

## Post #10 by @adamrankin (2018-12-14 14:15 UTC)

<p>Ok, it’s in the extension manager!</p>

---

## Post #11 by @OTI (2018-12-14 17:21 UTC)

<p>I can get it.<br>
I’m very grateful for your work.</p>

---

## Post #12 by @cvic (2024-02-22 15:27 UTC)

<p>Hi Adam,</p>
<p>I can’t get the extension to work on 3D Slicer 5.6.1. Has the extension been discontinued?<br>
In addition, I was also wondering: would it be possible to implement the kalibr toolbox (<a href="https://github.com/ethz-asl/kalibr" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ethz-asl/kalibr: The Kalibr visual-inertial calibration toolbox</a>) as a Slicer extension? I am quite new to Slicer, so before delving into it I would like to hear some feedback.</p>
<p>Thank you</p>

---

## Post #13 by @adamrankin (2024-02-22 15:41 UTC)

<p>Hi,</p>
<p>Yes, I have discontinued support. I will remove it from the extension index. It wouldn’t take much work to renew, but there wasn’t enough of a need to keep maintaining it.</p>
<p>Adam</p>

---
