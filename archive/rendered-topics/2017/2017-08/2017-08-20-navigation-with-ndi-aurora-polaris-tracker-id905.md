---
topic_id: 905
title: "Navigation With Ndi Aurora Polaris Tracker"
date: 2017-08-20
url: https://discourse.slicer.org/t/905
---

# Navigation with NDI Aurora/Polaris tracker

**Topic ID**: 905
**Date**: 2017-08-20
**URL**: https://discourse.slicer.org/t/navigation-with-ndi-aurora-polaris-tracker/905

---

## Post #1 by @Hwang_YoungEun (2017-08-20 14:05 UTC)

<p>I want to build a surgical navigation system using NDI’s Aurora(Polaris) and Slicer program. But there were some problems in linking Aurora(Polaris) with the Slicer program.</p>
<p>First, I have used NDI OpenIGTLink to send Aurora(Polaris) coordinate information to the Slicer, and in Slicer’s 3D space, I have a Skull model redering CT images. But here, I am having difficulty in registering the coordinates of the Aurora(Polaris) needle and the coordinates of the CT model.</p>
<p>Although the tutorial on the SlicerIGT module is well documented, it doesn’t seem to be working properly(I think that many other users also have this problem.). If you know how to align the coordinate information of NDI Aurora(Polaris) with the 3D spatial coordinates of Slicer, or if you have a guide document or video, please help.</p>

---

## Post #2 by @lassoan (2017-08-20 14:17 UTC)

<p>We use NDI Polaris regularly, most of the time doing patient registration is performed with Fiducial registration wizard, so it should work well. Use latest version of 3D Slicer and Plus.</p>
<p>Which SlicerIGT tutorials did you complete?<br>
Which ones you had problem following?<br>
What was the specific issue?</p>

---

## Post #3 by @Hwang_YoungEun (2017-08-21 04:52 UTC)

<p>I refer to the tutorial on the SlicerIGT site(<a href="http://www.slicerigt.org/" rel="noopener nofollow ugc">http://www.slicerigt.org/</a><br>
wp/user-tutorial/).<br>
I am having difficulty in coordinate transformations and registration(I<br>
will attach some pictures.).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a707f7d81915741d5c27cbf24855185e423aff.png" alt="image" data-base62-sha1="gmgieMi00InWMvEbWkHY3udmyyr" width="566" height="401"><br>
Here is my source code.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/23da45dde13a7b705ee75452da841bff376da5f8.jpg" data-download-href="/uploads/short-url/57amg7HdRkkNsErFwYES7rLD6nS.jpg?dl=1" title="slicer1.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23da45dde13a7b705ee75452da841bff376da5f8_2_690x374.jpg" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23da45dde13a7b705ee75452da841bff376da5f8_2_690x374.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23da45dde13a7b705ee75452da841bff376da5f8_2_1035x561.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23da45dde13a7b705ee75452da841bff376da5f8_2_1380x748.jpg 2x" data-dominant-color="737379"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1.jpg</span><span class="informations">1909×1035 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e29d81123cb427e3568e04627efffb11bf3d0e9c.jpg" data-download-href="/uploads/short-url/wkJmhQh27OXUf1ObdlsYxAghjFG.jpg?dl=1" title="slicer2.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e29d81123cb427e3568e04627efffb11bf3d0e9c_2_690x359.jpg" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e29d81123cb427e3568e04627efffb11bf3d0e9c_2_690x359.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e29d81123cb427e3568e04627efffb11bf3d0e9c_2_1035x538.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e29d81123cb427e3568e04627efffb11bf3d0e9c_2_1380x718.jpg 2x" data-dominant-color="B6B7DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2.jpg</span><span class="informations">2988×1558 490 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-08-21 05:05 UTC)

<p>Polaris “connection failed” issue has to be investigated. Do you use the latest development snapshot of Plus? Could you please attach the Plus log file?</p>
<p>After tool tracking works, follow steps, described in U-12 tutorial to register the coordinate system of your CT scan with the coordinate system of the reference marker attached to the skull phantom.</p>

---

## Post #5 by @Hwang_YoungEun (2017-08-21 07:49 UTC)

<p>Yes, I use the latest Plus program.<br>
I’ll attach the log file, and please check it!</p>
<p>Thank you,<br>
Youngeun</p>

---

## Post #6 by @emetss (2018-01-26 12:23 UTC)

<p>Hello Hwang Young Eun,<br>
I have the same problem like you and want to ask if you have solved it. Also we can work on this together because I have a skull model and I tested it on MITK Program. But the MITK registration is still not developed yet to solve this issue, so I’ll try with slicer</p>
<p>thanks in advance for your help</p>

---

## Post #7 by @lassoan (2018-01-26 13:51 UTC)

<aside class="quote no-group" data-username="emetss" data-post="6" data-topic="905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/90db22/48.png" class="avatar"> emetss:</div>
<blockquote>
<p>I have the same problem like you</p>
</blockquote>
</aside>
<p>Can you describe what your problem is?</p>

---

## Post #8 by @emetss (2018-01-26 14:36 UTC)

<p>Thanks for your question. I want to make a connection (usb) between slicer and ndi polaris camera to have a surgical navigation system (skull and a pointer). At first I cannot connect to the camera. I read that I have to use “Plus Server” to make a connection between the both. I’'m using ubuntu 16.04 and I have the slicer 3d. I added the IGT extension but I tried to download the Plus Server and I still cannot. It seems the website is not working</p>

---

## Post #9 by @lassoan (2018-01-26 16:04 UTC)

<p>We don’t provide binaries packages of Plus for Linux but you have to build it yourself. See <a href="https://github.com/PlusToolkit/PlusBuild/blob/master/README.md">build instructions</a>. If you have any questions about how to build or set up Plus, please <a href="https://github.com/PlusToolkit/PlusLib/issues/new">submit as an issue on GitHub project page of Plus</a>.</p>

---

## Post #10 by @emetss (2018-01-29 22:30 UTC)

<p>Many Thanks for the advice. I downloaded and built the PlusServer. Now I’m trying to connect. So I open “Plus Server Launcher”. Then I have to choose: “Device set configuration directory:” and “Device set”. There’re many device sets. Our tracking system is “NDI Polaris Old” which uses usb connection which is installed in (/dev/ttyusb). I tried different kinds of “Device Sets” but when i try to click “Launch server” button then i get "connection failed! Please select another device set and try again!"<br>
Am I doing wright? Should I use my special xml configuration file and if so then how? Because I only know the model of my tracking system. And I have the calibration files, and stl files of my tool and my object.</p>

---

## Post #11 by @lassoan (2018-01-30 14:06 UTC)

<p>Plus developers can help you, just <a href="https://github.com/PlusToolkit/PlusLib/issues/new">submit your question as an issue on GitHub project page of Plus</a>.</p>

---
