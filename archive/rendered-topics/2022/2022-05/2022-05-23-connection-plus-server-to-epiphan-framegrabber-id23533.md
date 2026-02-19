---
topic_id: 23533
title: "Connection Plus Server To Epiphan Framegrabber"
date: 2022-05-23
url: https://discourse.slicer.org/t/23533
---

# Connection Plus Server to Epiphan Framegrabber

**Topic ID**: 23533
**Date**: 2022-05-23
**URL**: https://discourse.slicer.org/t/connection-plus-server-to-epiphan-framegrabber/23533

---

## Post #1 by @J.vd.Zee (2022-05-23 12:19 UTC)

<p>Dear all!</p>
<p>I am trying to stream US data to 3D Slicer (4.13) via Plus Server (2.8, latest version) and OpenIGT. Therefore, I bought the Epiphan <a href="http://AV.io" rel="noopener nofollow ugc">AV.io</a> framegrabber and connected it to my computer.<br>
However, I am not able to connect the device successfully and I must make obvious mistakes in the .xml file. Could you please help me?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61219f9562e6d3a09883ce7c8cd7e95124a4c990.png" data-download-href="/uploads/short-url/dRglQxDQIN7Ss6GWFzUBMDKbIIg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61219f9562e6d3a09883ce7c8cd7e95124a4c990.png" alt="image" data-base62-sha1="dRglQxDQIN7Ss6GWFzUBMDKbIIg" width="690" height="37" data-dominant-color="ECE4E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1650×89 9.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/098e113789ba0dfc43e7e0d0a87d3b9f5c03af4a.png" data-download-href="/uploads/short-url/1mwFQoDWDSza9BeEFsFreBHPSwW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/098e113789ba0dfc43e7e0d0a87d3b9f5c03af4a.png" alt="image" data-base62-sha1="1mwFQoDWDSza9BeEFsFreBHPSwW" width="364" height="500" data-dominant-color="F9F6FC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">634×869 19.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-05-24 03:31 UTC)

<p><code>Av.io</code> series framegrabbers <a href="https://www.epiphan.com/compare-usb-video-grabbers/">do not support the Epiphan software toolkit</a>. You can probably use <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html">Microsoft Media Foundation</a> or <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpenCVVideo.html">OpenCV</a> Plus devices.</p>

---

## Post #3 by @J.vd.Zee (2022-05-30 19:29 UTC)

<p>Thanks a lot! It worked to set the device via Microsoft Media Foundation into PlusServer.</p>

---

## Post #4 by @lassoan (2022-05-30 20:44 UTC)

<p><a class="mention" href="/u/j.vd.zee">@J.vd.Zee</a> Thank you for confirming.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you add a note about this to the Plus User’s Guide? Thanks!</p>

---

## Post #5 by @J.vd.Zee (2025-04-24 15:22 UTC)

<p>Hi,</p>
<p>Regarding our previous topic, I noticed a too high temporal resolution for tracked ultrasound (+/-130 ms) while streaming my <a href="https://www.epiphan.com/products/avio-hd/" rel="noopener nofollow ugc">Epiphan Av.io</a> videostream via the Microsfot Media Foundation protocol. The Epiphan streaming protocol is working for the DVI2USB 3.0 grabbers, but those are discontinued. Which current available Epiphan framegrabber should I buy? I think that the latency will be better if I can use the dedicated Plus Server streaming protocol for the Epiphan framegrabber instead of current streaming protocol.</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2025-04-26 12:51 UTC)

<p>We still have those high-performance DVI2USB framegrabbers and I don’t know if there good replacements. It would be great if you could ask around on the Epiphan forum if this increased latency is expected and let us know what you learned. Maybe we need to configure the If it turns out that we need tune the video capture in the Microsoft Media Foundation video source in PLUS then we can certainly do it.</p>

---

## Post #7 by @J.vd.Zee (2025-04-28 14:09 UTC)

<p>I wrote a post on the Epiphan forum, will let you know if I got any reactions.<br>
If we can’t improve the current setup with Epiphan, what other framegrabber do you recommend? I prefer an external device.</p>

---
